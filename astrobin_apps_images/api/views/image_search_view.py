import base64
import json
from urllib.parse import parse_qs, unquote
import zlib
import msgpack

from djangorestframework_camel_case.render import CamelCaseJSONRenderer
from drf_haystack.filters import HaystackFilter, HaystackOrderingFilter
from drf_haystack.viewsets import HaystackViewSet
from rest_framework.exceptions import ParseError
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.throttling import ScopedRateThrottle

from astrobin.models import Image
from astrobin_apps_images.api.serializers import ImageSearchSerializer
from common.api_page_size_pagination import PageSizePagination
from common.permissions import ReadOnly
from common.services.search_service import SearchService


class ImageSearchView(HaystackViewSet):
    index_models = [Image]
    serializer_class = ImageSearchSerializer
    renderer_classes = [BrowsableAPIRenderer, CamelCaseJSONRenderer]
    permission_classes = [ReadOnly]
    filter_backends = (HaystackFilter, HaystackOrderingFilter)
    ordering_fields = ('published', 'title', 'w', 'h', 'likes')
    ordering = ('-published',)
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'search'
    pagination_class = PageSizePagination

    decoded_query_params = {}

    def decode_base64_padding(self, base64_string: str) -> str:
        # Add padding if necessary
        missing_padding = len(base64_string) % 4
        if missing_padding:
            base64_string += '=' * (4 - missing_padding)
        return base64_string

    def initialize_request(self, request, *args, **kwargs):
        def is_json(value):
            try:
                json_obj = json.loads(value)
                if isinstance(json_obj, (dict, list, bool, type(None))):
                    return True
                return False
            except json.JSONDecodeError:
                return False

        # Decode and decompress params before handling the request
        request = super().initialize_request(request, *args, **kwargs)
        params = request.query_params.get('params')
        if params:
            try:
                # Ensure correct Base64 padding
                padded_params = self.decode_base64_padding(unquote(params))
                # Base64 decode to get compressed data
                compressed_data = base64.b64decode(padded_params)
                # Decompress the data
                decompressed_data = zlib.decompress(compressed_data)
                # Decode the binary data back to a string
                query_string = msgpack.unpackb(decompressed_data, raw=False)
                # Parse the query string
                parsed_params = parse_qs(query_string)

                # Convert lists to single values if necessary
                decoded_params = {key: value[0] if len(value) == 1 else value for key, value in parsed_params.items()}

                # Convert JSON strings back to objects where applicable
                for key, value in decoded_params.items():
                    if isinstance(value, str) and is_json(value):
                        try:
                            decoded_params[key] = json.loads(value)
                        except json.JSONDecodeError:
                            continue

                # Replace request.query_params with decoded_params
                request._request.GET = request._request.GET.copy()
                for key, value in decoded_params.items():
                    request._request.GET[key] = value

            except (ValueError, TypeError, base64.binascii.Error, zlib.error) as e:
                raise ParseError(f"Error decoding parameters: {str(e)}")
        return request

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)

        queryset = SearchService.filter_by_subject(self.request.query_params, queryset)
        queryset = SearchService.filter_by_telescope(self.request.query_params, queryset)
        queryset = SearchService.filter_by_camera(self.request.query_params, queryset)

        return queryset
