from django.conf import settings


def docs_base_url(request):
    return {
        'css_js_version': '?v=1.0.8',
        'docs_base_url': settings.DOCS_BASE_URL
    }
