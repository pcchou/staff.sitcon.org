# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

ALLOWED_HOSTS = ['staff.sitcon.camp']
SITE_URL = 'http://staff.sitcon.camp'

DEFAULT_FROM_EMAIL = '"SITCON 夏令營行政系統" <admin@staff.sitcon.camp>'
SERVER_EMAIL = DEFAULT_FROM_EMAIL

DEFAULT_NOTIFICATION_SENDER = 'SITCON 夏令營行政系統:notifications@staff.sitcon.camp'
DEFAULT_ACCOUNTS_SENDER =  'SITCON 夏令營行政系統:accounts@staff.sitcon.camp'
DEFAULT_ISSUE_SENDER = 'SITCON 夏令營行政系統:issues@staff.sitcon.camp'

USER_ISSUE_SENDER = '{0} (SITCON):issues@staff.sitcon.camp'
DEFAULT_SMS_SENDER = 'SITCON'

ISSUE_EXPIRE_TIMEDELTA = datetime.timedelta(hours=12)

# Non-enforcing options

RESIDENCE_OPTIONS = (
    '基隆市', '臺北市', '新北市', '桃園市',
    '新竹市', '新竹縣', '苗栗縣', '臺中市',
    '彰化縣', '南投縣', '雲林縣', '嘉義市',
    '嘉義縣', '臺南市', '高雄市', '屏東縣',
    '臺東縣', '花蓮縣', '宜蘭縣', '澎湖縣',
    '金門縣', '連江縣', '國外',
)

SHIRT_SIZE_OPTIONS = (
    'XS', 'S', 'M', 'L', 'XL', '2XL',
)

DIET_OPTIONS = (
    '葷',
    '忌牛肉', '忌豬肉', '忌海鮮',
    '方便素', '蛋奶素', '全素',
)
