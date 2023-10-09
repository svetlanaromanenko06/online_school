import re
from rest_framework.serializers import ValidationError

class UrlValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        url_value = dict(value).get(self.field)
        if 'youtube.com' not in url_value:
            raise ValidationError('Ссылка на запрещенный ресурс')

