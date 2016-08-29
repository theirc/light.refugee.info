from django.template.defaulttags import register


@register.simple_tag()
def get_direction(lang='en'):
    if lang == 'en':
        return 'ltr'
    else:
        return 'rtl'
