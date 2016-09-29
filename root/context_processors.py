from django.conf import settings  # import the settings file


def url_context_processor(request):
    return {
        'API_URL': settings.API_URL,
        'WEB_URL': settings.WEB_URL
    }
