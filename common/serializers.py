from avatar.templatetags.avatar_tags import avatar_url
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from rest_framework.fields import BooleanField, IntegerField, FloatField, CharField
from rest_framework.relations import PrimaryKeyRelatedField
from subscription.models import UserSubscription, Subscription, Transaction

from astrobin.api2.serializers.location_serializer import LocationSerializer
from astrobin.models import UserProfile, Location
from astrobin_apps_users.services import UserService
from toggleproperties.models import ToggleProperty


class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = (
            'id',
            'app_label',
            'model',
        )


class AvatarField(serializers.Field):
    def to_representation(self, user):
        return avatar_url(user, 40)


class LargeAvatarField(serializers.Field):
    def to_representation(self, user):
        return avatar_url(user, 200)


class UserSerializer(serializers.ModelSerializer):
    avatar = AvatarField(source='*')
    large_avatar = LargeAvatarField(source='*')
    userprofile = PrimaryKeyRelatedField(read_only=True)
    display_name = serializers.SerializerMethodField(read_only=True)

    def get_display_name(self, user: User) -> str:
        return user.userprofile.get_display_name()

    class Meta:
        model = User
        exclude = ('password', 'email', 'last_name')
        depth = 1


class TogglePropertySerializer(serializers.ModelSerializer):
    def validate(self, data):
        if data['property_type'] == 'like':
            obj = data['content_type'].get_object_for_this_type(pk=data['object_id'])
            if not UserService(data['user']).can_like(obj):
                raise serializers.ValidationError('User does not have the required permissions to like this object')
        elif data['property_type'] == 'follow':
            pass
        else:
            raise serializers.ValidationError('This property_type is not allowed via the API at the moment')

        return data

    class Meta:
        model = ToggleProperty
        fields = (
            'pk',
            'property_type',
            'user',
            'content_type',
            'object_id',
            'created_on',
        )


class UserProfileSerializer(serializers.ModelSerializer):
    username = CharField(read_only=True, source="user.username")

    def update(self, instance, validated_data):
        return super(serializers.ModelSerializer, self).update(instance, validated_data)

    class Meta:
        model = UserProfile
        exclude = (
            'premium_counter',
            'exclude_from_competitions',
            'shadow_bans',
        )


class UserProfileSerializerPrivate(UserProfileSerializer):
    astrobin_index = serializers.SerializerMethodField()
    contribution_index = serializers.SerializerMethodField()
    followers = IntegerField(read_only=True, source='followers_count')
    locations = LocationSerializer(many=True, source='location_set')
    email = CharField(read_only=True, source='user.email')

    def get_astrobin_index(self, obj: UserProfile) -> float:
        return float(obj.image_index) if obj.image_index is not None else None

    def get_contribution_index(self, obj: UserProfile) -> float:
        return float(obj.contribution_index) if obj.contribution_index is not None else None

    def update(self, instance, validated_data):
        locations = validated_data.pop('location_set', [])
        instance = super(UserProfileSerializer, self).update(instance, validated_data)
        instance.location_set.clear()

        for location_data in locations:
            try:
                location = Location.objects.get(pk=location_data.get('id'))
                instance.location_set.add(location)
            except Location.DoesNotExist:
                pass

        return instance

    class Meta(UserProfileSerializer.Meta):
        exclude = ()


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
        depth = 1


class UserSubscriptionSerializer(serializers.ModelSerializer):
    valid = BooleanField()

    class Meta:
        model = UserSubscription
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    subscription_name = CharField(read_only=True, source='subscription.name')

    class Meta:
        model = Transaction
        fields = '__all__'
