from typing import Optional

from django.db import models
from django.forms import ModelMultipleChoiceField
from django.utils.translation import ugettext_lazy as _

# ISO 3166-1 country names and codes adapted from http://opencountrycodes.appspot.com/python/

CURRENCY_CHOICES = [
    ("AED", "UAE Dirham"),
    ("AFN", "Afghani"),
    ("ALL", "Lek"),
    ("AMD", "Armenian Dram"),
    ("ANG", "Netherlands Antillean Guilder"),
    ("AOA", "Kwanza"),
    ("ARS", "Argentine Peso"),
    ("AUD", "Australian Dollar"),
    ("AWG", "Aruban Florin"),
    ("AZN", "Azerbaijan Manat"),
    ("BAM", "Convertible Mark"),
    ("BBD", "Barbados Dollar"),
    ("BDT", "Taka"),
    ("BGN", "Bulgarian Lev"),
    ("BHD", "Bahraini Dinar"),
    ("BIF", "Burundi Franc"),
    ("BMD", "Bermudian Dollar"),
    ("BND", "Brunei Dollar"),
    ("BOB", "Boliviano"),
    ("BOV", "Mvdol"),
    ("BRL", "Brazilian Real"),
    ("BSD", "Bahamian Dollar"),
    ("BTN", "Ngultrum"),
    ("BWP", "Pula"),
    ("BYN", "Belarusian Ruble"),
    ("BZD", "Belize Dollar"),
    ("CAD", "Canadian Dollar"),
    ("CDF", "Congolese Franc"),
    ("CHE", "WIR Euro"),
    ("CHF", "Swiss Franc"),
    ("CHW", "WIR Franc"),
    ("CLF", "Unidad de Fomento"),
    ("CLP", "Chilean Peso"),
    ("CNY", "Yuan Renminbi"),
    ("COP", "Colombian Peso"),
    ("COU", "Unidad de Valor Real"),
    ("CRC", "Costa Rican Colon"),
    ("CUC", "Peso Convertible"),
    ("CUP", "Cuban Peso"),
    ("CVE", "Cabo Verde Escudo"),
    ("CZK", "Czech Koruna"),
    ("DJF", "Djibouti Franc"),
    ("DKK", "Danish Krone"),
    ("DOP", "Dominican Peso"),
    ("DZD", "Algerian Dinar"),
    ("EGP", "Egyptian Pound"),
    ("ERN", "Nakfa"),
    ("ETB", "Ethiopian Birr"),
    ("EUR", "Euro"),
    ("FJD", "Fiji Dollar"),
    ("FKP", "Falkland Islands Pound"),
    ("GBP", "Pound Sterling"),
    ("GEL", "Lari"),
    ("GHS", "Ghana Cedi"),
    ("GIP", "Gibraltar Pound"),
    ("GMD", "Dalasi"),
    ("GNF", "Guinean Franc"),
    ("GTQ", "Quetzal"),
    ("GYD", "Guyana Dollar"),
    ("HKD", "Hong Kong Dollar"),
    ("HNL", "Lempira"),
    ("HRK", "Kuna"),
    ("HTG", "Gourde"),
    ("HUF", "Forint"),
    ("IDR", "Rupiah"),
    ("ILS", "New Israeli Sheqel"),
    ("INR", "Indian Rupee"),
    ("IQD", "Iraqi Dinar"),
    ("IRR", "Iranian Rial"),
    ("ISK", "Iceland Krona"),
    ("JMD", "Jamaican Dollar"),
    ("JOD", "Jordanian Dinar"),
    ("JPY", "Yen"),
    ("KES", "Kenyan Shilling"),
    ("KGS", "Som"),
    ("KHR", "Riel"),
    ("KMF", "Comorian Franc"),
    ("KPW", "North Korean Won"),
    ("KRW", "Won"),
    ("KWD", "Kuwaiti Dinar"),
    ("KYD", "Cayman Islands Dollar"),
    ("KZT", "Tenge"),
    ("LAK", "Lao Kip"),
    ("LBP", "Lebanese Pound"),
    ("LKR", "Sri Lanka Rupee"),
    ("LRD", "Liberian Dollar"),
    ("LSL", "Loti"),
    ("LYD", "Libyan Dinar"),
    ("MAD", "Moroccan Dirham"),
    ("MDL", "Moldovan Leu"),
    ("MGA", "Malagasy Ariary"),
    ("MKD", "Denar"),
    ("MMK", "Kyat"),
    ("MNT", "Tugrik"),
    ("MOP", "Pataca"),
    ("MRU", "Ouguiya"),
    ("MUR", "Mauritius Rupee"),
    ("MVR", "Rufiyaa"),
    ("MWK", "Malawi Kwacha"),
    ("MXN", "Mexican Peso"),
    ("MXV", "Mexican Unidad de Inversion (UDI)"),
    ("MYR", "Malaysian Ringgit"),
    ("MZN", "Mozambique Metical"),
    ("NAD", "Namibia Dollar"),
    ("NGN", "Naira"),
    ("NIO", "Cordoba Oro"),
    ("NOK", "Norwegian Krone"),
    ("NPR", "Nepalese Rupee"),
    ("NZD", "New Zealand Dollar"),
    ("OMR", "Rial Omani"),
    ("PAB", "Balboa"),
    ("PEN", "Sol"),
    ("PGK", "Kina"),
    ("PHP", "Philippine Peso"),
    ("PKR", "Pakistan Rupee"),
    ("PLN", "Zloty"),
    ("PYG", "Guarani"),
    ("QAR", "Qatari Rial"),
    ("RON", "Romanian Leu"),
    ("RSD", "Serbian Dinar"),
    ("RUB", "Russian Ruble"),
    ("RWF", "Rwanda Franc"),
    ("SAR", "Saudi Riyal"),
    ("SBD", "Solomon Islands Dollar"),
    ("SCR", "Seychelles Rupee"),
    ("SDG", "Sudanese Pound"),
    ("SEK", "Swedish Krona"),
    ("SGD", "Singapore Dollar"),
    ("SHP", "Saint Helena Pound"),
    ("SLE", "Leone"),
    ("SLL", "Leone"),
    ("SOS", "Somali Shilling"),
    ("SRD", "Surinam Dollar"),
    ("SSP", "South Sudanese Pound"),
    ("STN", "Dobra"),
    ("SVC", "El Salvador Colon"),
    ("SYP", "Syrian Pound"),
    ("SZL", "Lilangeni"),
    ("THB", "Baht"),
    ("TJS", "Somoni"),
    ("TMT", "Turkmenistan New Manat"),
    ("TND", "Tunisian Dinar"),
    ("TOP", "Pa’anga"),
    ("TRY", "Turkish Lira"),
    ("TTD", "Trinidad and Tobago Dollar"),
    ("TWD", "New Taiwan Dollar"),
    ("TZS", "Tanzanian Shilling"),
    ("UAH", "Hryvnia"),
    ("UGX", "Uganda Shilling"),
    ("USD", "US Dollar"),
    ("USN", "US Dollar (Next day)"),
    ("UYI", "Uruguay Peso en Unidades Indexadas (UI)"),
    ("UYU", "Peso Uruguayo"),
    ("UYW", "Unidad Previsional"),
    ("UZS", "Uzbekistan Sum"),
    ("VED", "Bolívar Soberano"),
    ("VES", "Bolívar Soberano"),
    ("VND", "Dong"),
    ("VUV", "Vatu"),
    ("WST", "Tala"),
    ("XAF", "CFA Franc BEAC"),
    ("XAG", "Silver"),
    ("XAU", "Gold"),
    ("XBA", "Bond Markets Unit European Composite Unit (EURCO)"),
    ("XBB", "Bond Markets Unit European Monetary Unit (E.M.U.-6)"),
    ("XBC", "Bond Markets Unit European Unit of Account 9 (E.U.A.-9)"),
    ("XBD", "Bond Markets Unit European Unit of Account 17 (E.U.A.-17)"),
    ("XCD", "East Caribbean Dollar"),
    ("XDR", "SDR (Special Drawing Right)"),
    ("XOF", "CFA Franc BCEAO"),
    ("XPD", "Palladium"),
    ("XPF", "CFP Franc"),
    ("XPT", "Platinum"),
    ("XSU", "Sucre"),
    ("XTS", "Codes specifically reserved for testing purposes"),
    ("XUA", "ADB Unit of Account"),
    ("XXX", "The codes assigned for transactions where no currency is involved"),
    ("YER", "Yemeni Rial"),
    ("ZAR", "Rand"),
    ("ZMW", "Zambian Kwacha"),
    ("ZWL", "Zimbabwe Dollar"),
]

COUNTRIES = (
    ('', '---------'),
    ('GB', _('United Kingdom')),
    ('AF', _('Afghanistan')),
    ('AX', _('Aland Islands')),
    ('AL', _('Albania')),
    ('DZ', _('Algeria')),
    ('AS', _('American Samoa')),
    ('AD', _('Andorra')),
    ('AO', _('Angola')),
    ('AI', _('Anguilla')),
    ('AQ', _('Antarctica')),
    ('AG', _('Antigua and Barbuda')),
    ('AR', _('Argentina')),
    ('AM', _('Armenia')),
    ('AW', _('Aruba')),
    ('AU', _('Australia')),
    ('AT', _('Austria')),
    ('AZ', _('Azerbaijan')),
    ('BS', _('Bahamas')),
    ('BH', _('Bahrain')),
    ('BD', _('Bangladesh')),
    ('BB', _('Barbados')),
    ('BY', _('Belarus')),
    ('BE', _('Belgium')),
    ('BZ', _('Belize')),
    ('BJ', _('Benin')),
    ('BM', _('Bermuda')),
    ('BT', _('Bhutan')),
    ('BO', _('Bolivia')),
    ('BA', _('Bosnia and Herzegovina')),
    ('BW', _('Botswana')),
    ('BV', _('Bouvet Island')),
    ('BR', _('Brazil')),
    ('IO', _('British Indian Ocean Territory')),
    ('BN', _('Brunei Darussalam')),
    ('BG', _('Bulgaria')),
    ('BF', _('Burkina Faso')),
    ('BI', _('Burundi')),
    ('KH', _('Cambodia')),
    ('CM', _('Cameroon')),
    ('CA', _('Canada')),
    ('CV', _('Cape Verde')),
    ('KY', _('Cayman Islands')),
    ('CF', _('Central African Republic')),
    ('TD', _('Chad')),
    ('CL', _('Chile')),
    ('CN', _('China')),
    ('CX', _('Christmas Island')),
    ('CC', _('Cocos (Keeling) Islands')),
    ('CO', _('Colombia')),
    ('KM', _('Comoros')),
    ('CG', _('Congo')),
    ('CD', _('Congo, The Democratic Republic of the')),
    ('CK', _('Cook Islands')),
    ('CR', _('Costa Rica')),
    ('CI', _('Cote d\'Ivoire')),
    ('HR', _('Croatia')),
    ('CU', _('Cuba')),
    ('CY', _('Cyprus')),
    ('CZ', _('Czech Republic')),
    ('DK', _('Denmark')),
    ('DJ', _('Djibouti')),
    ('DM', _('Dominica')),
    ('DO', _('Dominican Republic')),
    ('EC', _('Ecuador')),
    ('EG', _('Egypt')),
    ('SV', _('El Salvador')),
    ('GQ', _('Equatorial Guinea')),
    ('ER', _('Eritrea')),
    ('EE', _('Estonia')),
    ('ET', _('Ethiopia')),
    ('FK', _('Falkland Islands (Malvinas)')),
    ('FO', _('Faroe Islands')),
    ('FJ', _('Fiji')),
    ('FI', _('Finland')),
    ('FR', _('France')),
    ('GF', _('French Guiana')),
    ('PF', _('French Polynesia')),
    ('TF', _('French Southern Territories')),
    ('GA', _('Gabon')),
    ('GM', _('Gambia')),
    ('GE', _('Georgia')),
    ('DE', _('Germany')),
    ('GH', _('Ghana')),
    ('GI', _('Gibraltar')),
    ('GR', _('Greece')),
    ('GL', _('Greenland')),
    ('GD', _('Grenada')),
    ('GP', _('Guadeloupe')),
    ('GU', _('Guam')),
    ('GT', _('Guatemala')),
    ('GG', _('Guernsey')),
    ('GN', _('Guinea')),
    ('GW', _('Guinea-Bissau')),
    ('GY', _('Guyana')),
    ('HT', _('Haiti')),
    ('HM', _('Heard Island and McDonald Islands')),
    ('VA', _('Holy See (Vatican City State)')),
    ('HN', _('Honduras')),
    ('HK', _('Hong Kong')),
    ('HU', _('Hungary')),
    ('IS', _('Iceland')),
    ('IN', _('India')),
    ('ID', _('Indonesia')),
    ('IR', _('Iran, Islamic Republic of')),
    ('IQ', _('Iraq')),
    ('IE', _('Ireland')),
    ('IM', _('Isle of Man')),
    ('IL', _('Israel')),
    ('IT', _('Italy')),
    ('JM', _('Jamaica')),
    ('JP', _('Japan')),
    ('JE', _('Jersey')),
    ('JO', _('Jordan')),
    ('KZ', _('Kazakhstan')),
    ('KE', _('Kenya')),
    ('KI', _('Kiribati')),
    ('KP', _('Korea, Democratic People\'s Republic of')),
    ('KR', _('Korea, Republic of')),
    ('KW', _('Kuwait')),
    ('KG', _('Kyrgyzstan')),
    ('LA', _('Lao People\'s Democratic Republic')),
    ('LV', _('Latvia')),
    ('LB', _('Lebanon')),
    ('LS', _('Lesotho')),
    ('LR', _('Liberia')),
    ('LY', _('Libyan Arab Jamahiriya')),
    ('LI', _('Liechtenstein')),
    ('LT', _('Lithuania')),
    ('LU', _('Luxembourg')),
    ('MO', _('Macao')),
    ('MK', _('Macedonia, The Former Yugoslav Republic of')),
    ('MG', _('Madagascar')),
    ('MW', _('Malawi')),
    ('MY', _('Malaysia')),
    ('MV', _('Maldives')),
    ('ML', _('Mali')),
    ('MT', _('Malta')),
    ('MH', _('Marshall Islands')),
    ('MQ', _('Martinique')),
    ('MR', _('Mauritania')),
    ('MU', _('Mauritius')),
    ('YT', _('Mayotte')),
    ('MX', _('Mexico')),
    ('FM', _('Micronesia, Federated States of')),
    ('MD', _('Moldova')),
    ('MC', _('Monaco')),
    ('MN', _('Mongolia')),
    ('ME', _('Montenegro')),
    ('MS', _('Montserrat')),
    ('MA', _('Morocco')),
    ('MZ', _('Mozambique')),
    ('MM', _('Myanmar')),
    ('NA', _('Namibia')),
    ('NR', _('Nauru')),
    ('NP', _('Nepal')),
    ('NL', _('Netherlands')),
    ('AN', _('Netherlands Antilles')),
    ('NC', _('New Caledonia')),
    ('NZ', _('New Zealand')),
    ('NI', _('Nicaragua')),
    ('NE', _('Niger')),
    ('NG', _('Nigeria')),
    ('NU', _('Niue')),
    ('NF', _('Norfolk Island')),
    ('MP', _('Northern Mariana Islands')),
    ('NO', _('Norway')),
    ('OM', _('Oman')),
    ('PK', _('Pakistan')),
    ('PW', _('Palau')),
    ('PS', _('Palestinian Territory, Occupied')),
    ('PA', _('Panama')),
    ('PG', _('Papua New Guinea')),
    ('PY', _('Paraguay')),
    ('PE', _('Peru')),
    ('PH', _('Philippines')),
    ('PN', _('Pitcairn')),
    ('PL', _('Poland')),
    ('PT', _('Portugal')),
    ('PR', _('Puerto Rico')),
    ('QA', _('Qatar')),
    ('RE', _('Reunion')),
    ('RO', _('Romania')),
    ('RU', _('Russian Federation')),
    ('RW', _('Rwanda')),
    ('BL', _('Saint Barthelemy')),
    ('SH', _('Saint Helena')),
    ('KN', _('Saint Kitts and Nevis')),
    ('LC', _('Saint Lucia')),
    ('MF', _('Saint Martin')),
    ('PM', _('Saint Pierre and Miquelon')),
    ('VC', _('Saint Vincent and the Grenadines')),
    ('WS', _('Samoa')),
    ('SM', _('San Marino')),
    ('ST', _('Sao Tome and Principe')),
    ('SA', _('Saudi Arabia')),
    ('SN', _('Senegal')),
    ('RS', _('Serbia')),
    ('SC', _('Seychelles')),
    ('SL', _('Sierra Leone')),
    ('SG', _('Singapore')),
    ('SK', _('Slovakia')),
    ('SI', _('Slovenia')),
    ('SB', _('Solomon Islands')),
    ('SO', _('Somalia')),
    ('ZA', _('South Africa')),
    ('GS', _('South Georgia and the South Sandwich Islands')),
    ('ES', _('Spain')),
    ('LK', _('Sri Lanka')),
    ('SD', _('Sudan')),
    ('SR', _('Suriname')),
    ('SJ', _('Svalbard and Jan Mayen')),
    ('SZ', _('Swaziland')),
    ('SE', _('Sweden')),
    ('CH', _('Switzerland')),
    ('SY', _('Syrian Arab Republic')),
    ('TW', _('Taiwan')),
    ('TJ', _('Tajikistan')),
    ('TZ', _('Tanzania, United Republic of')),
    ('TH', _('Thailand')),
    ('TL', _('Timor-Leste')),
    ('TG', _('Togo')),
    ('TK', _('Tokelau')),
    ('TO', _('Tonga')),
    ('TT', _('Trinidad and Tobago')),
    ('TN', _('Tunisia')),
    ('TR', _('Turkey')),
    ('TM', _('Turkmenistan')),
    ('TC', _('Turks and Caicos Islands')),
    ('TV', _('Tuvalu')),
    ('UG', _('Uganda')),
    ('UA', _('Ukraine')),
    ('AE', _('United Arab Emirates')),
    ('US', _('United States')),
    ('UM', _('United States Minor Outlying Islands')),
    ('UY', _('Uruguay')),
    ('UZ', _('Uzbekistan')),
    ('VU', _('Vanuatu')),
    ('VE', _('Venezuela')),
    ('VN', _('Viet Nam')),
    ('VG', _('Virgin Islands, British')),
    ('VI', _('Virgin Islands, U.S.')),
    ('WF', _('Wallis and Futuna')),
    ('EH', _('Western Sahara')),
    ('YE', _('Yemen')),
    ('ZM', _('Zambia')),
    ('ZW', _('Zimbabwe')),
)

COUNTRY_TO_CONTINENT = {
    'AD': 'Europe',
    'AE': 'Asia',
    'AF': 'Asia',
    'AG': 'Americas',
    'AI': 'Americas',
    'AL': 'Europe',
    'AM': 'Asia',
    'AN': 'Americas',
    'AO': 'Africa',
    'AQ': 'Antarctica',
    'AR': 'Americas',
    'AS': 'Oceania',
    'AT': 'Europe',
    'AU': 'Oceania',
    'AW': 'Americas',
    'AX': 'Europe',
    'AZ': 'Asia',
    'BA': 'Europe',
    'BB': 'Americas',
    'BD': 'Asia',
    'BE': 'Europe',
    'BF': 'Africa',
    'BG': 'Europe',
    'BH': 'Asia',
    'BI': 'Africa',
    'BJ': 'Africa',
    'BL': 'Americas',
    'BM': 'Americas',
    'BN': 'Asia',
    'BO': 'Americas',
    'BR': 'Americas',
    'BS': 'Americas',
    'BT': 'Asia',
    'BV': 'Antarctica',
    'BW': 'Africa',
    'BY': 'Europe',
    'BZ': 'Americas',
    'CA': 'Americas',
    'CC': 'Asia',
    'CD': 'Africa',
    'CF': 'Africa',
    'CG': 'Africa',
    'CH': 'Europe',
    'CI': 'Africa',
    'CK': 'Oceania',
    'CL': 'Americas',
    'CM': 'Africa',
    'CN': 'Asia',
    'CO': 'Americas',
    'CR': 'Americas',
    'CU': 'Americas',
    'CV': 'Africa',
    'CX': 'Asia',
    'CY': 'Asia',
    'CZ': 'Europe',
    'DE': 'Europe',
    'DJ': 'Africa',
    'DK': 'Europe',
    'DM': 'Americas',
    'DO': 'Americas',
    'DZ': 'Africa',
    'EC': 'Americas',
    'EE': 'Europe',
    'EG': 'Africa',
    'EH': 'Africa',
    'ER': 'Africa',
    'ES': 'Europe',
    'ET': 'Africa',
    'FI': 'Europe',
    'FJ': 'Oceania',
    'FK': 'Americas',
    'FM': 'Oceania',
    'FO': 'Europe',
    'FR': 'Europe',
    'GA': 'Africa',
    'GB': 'Europe',
    'GD': 'Americas',
    'GE': 'Asia',
    'GF': 'Americas',
    'GG': 'Europe',
    'GH': 'Africa',
    'GI': 'Europe',
    'GL': 'Americas',
    'GM': 'Africa',
    'GN': 'Africa',
    'GP': 'Americas',
    'GQ': 'Africa',
    'GR': 'Europe',
    'GS': 'Antarctica',
    'GT': 'Americas',
    'GU': 'Oceania',
    'GW': 'Africa',
    'GY': 'Americas',
    'HK': 'Asia',
    'HM': 'Antarctica',
    'HN': 'Americas',
    'HR': 'Europe',
    'HT': 'Americas',
    'HU': 'Europe',
    'ID': 'Asia',
    'IE': 'Europe',
    'IL': 'Asia',
    'IM': 'Europe',
    'IN': 'Asia',
    'IO': 'Asia',
    'IQ': 'Asia',
    'IR': 'Asia',
    'IS': 'Europe',
    'IT': 'Europe',
    'JE': 'Europe',
    'JM': 'Americas',
    'JO': 'Asia',
    'JP': 'Asia',
    'KE': 'Africa',
    'KG': 'Asia',
    'KH': 'Asia',
    'KI': 'Oceania',
    'KM': 'Africa',
    'KN': 'Americas',
    'KP': 'Asia',
    'KR': 'Asia',
    'KW': 'Asia',
    'KY': 'Americas',
    'KZ': 'Asia',
    'LA': 'Asia',
    'LB': 'Asia',
    'LC': 'Americas',
    'LI': 'Europe',
    'LK': 'Asia',
    'LR': 'Africa',
    'LS': 'Africa',
    'LT': 'Europe',
    'LU': 'Europe',
    'LV': 'Europe',
    'LY': 'Africa',
    'MA': 'Africa',
    'MC': 'Europe',
    'MD': 'Europe',
    'ME': 'Europe',
    'MF': 'Americas',
    'MG': 'Africa',
    'MH': 'Oceania',
    'MK': 'Europe',
    'ML': 'Africa',
    'MM': 'Asia',
    'MN': 'Asia',
    'MO': 'Asia',
    'MP': 'Oceania',
    'MQ': 'Americas',
    'MR': 'Africa',
    'MS': 'Americas',
    'MT': 'Europe',
    'MU': 'Africa',
    'MV': 'Asia',
    'MW': 'Africa',
    'MX': 'Americas',
    'MY': 'Asia',
    'MZ': 'Africa',
    'NA': 'Africa',
    'NC': 'Oceania',
    'NE': 'Africa',
    'NF': 'Oceania',
    'NG': 'Africa',
    'NI': 'Americas',
    'NL': 'Europe',
    'NO': 'Europe',
    'NP': 'Asia',
    'NR': 'Oceania',
    'NU': 'Oceania',
    'NZ': 'Oceania',
    'OM': 'Asia',
    'PA': 'Americas',
    'PE': 'Americas',
    'PF': 'Oceania',
    'PG': 'Oceania',
    'PH': 'Asia',
    'PK': 'Asia',
    'PL': 'Europe',
    'PM': 'Americas',
    'PN': 'Oceania',
    'PR': 'Americas',
    'PS': 'Asia',
    'PT': 'Europe',
    'PW': 'Oceania',
    'PY': 'Americas',
    'QA': 'Asia',
    'RE': 'Africa',
    'RO': 'Europe',
    'RS': 'Europe',
    'RU': 'Europe',
    'RW': 'Africa',
    'SA': 'Asia',
    'SB': 'Oceania',
    'SC': 'Africa',
    'SD': 'Africa',
    'SE': 'Europe',
    'SG': 'Asia',
    'SH': 'Africa',
    'SI': 'Europe',
    'SJ': 'Europe',
    'SK': 'Europe',
    'SL': 'Africa',
    'SM': 'Europe',
    'SN': 'Africa',
    'SO': 'Africa',
    'SR': 'Americas',
    'ST': 'Africa',
    'SV': 'Americas',
    'SY': 'Asia',
    'SZ': 'Africa',
    'TC': 'Americas',
    'TD': 'Africa',
    'TF': 'Antarctica',
    'TG': 'Africa',
    'TH': 'Asia',
    'TJ': 'Asia',
    'TK': 'Oceania',
    'TL': 'Asia',
    'TM': 'Asia',
    'TN': 'Africa',
    'TO': 'Oceania',
    'TR': 'Asia',
    'TT': 'Americas',
    'TV': 'Oceania',
    'TW': 'Asia',
    'TZ': 'Africa',
    'UA': 'Europe',
    'UG': 'Africa',
    'UM': 'Oceania',
    'US': 'Americas',
    'UY': 'Americas',
    'UZ': 'Asia',
    'VA': 'Europe',
    'VC': 'Americas',
    'VE': 'Americas',
    'VG': 'Americas',
    'VI': 'Americas',
    'VN': 'Asia',
    'VU': 'Oceania',
    'WF': 'Oceania',
    'WS': 'Oceania',
    'YE': 'Asia',
    'YT': 'Africa',
    'ZA': 'Africa',
    'ZM': 'Africa',
    'ZW': 'Africa'
}


def get_country_name(code: str) -> Optional[str]:
    if not code:
        return None

    for country in COUNTRIES:
        if country[0] == code.upper():
            return country[1]
    return None


def get_country_continent(code: str) -> Optional[str]:
    return COUNTRY_TO_CONTINENT.get(code.upper(), None)


class CountryField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 2)
        kwargs.setdefault('choices', COUNTRIES)

        super(CountryField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return "CharField"


class GearItemChoiceField(ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        from astrobin.services.gear_service import GearService
        return GearService(obj).display_name(self.user)
