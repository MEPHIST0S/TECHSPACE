from django.utils import translation
from django.http import HttpResponseForbidden
from django.conf import settings

class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        lang = request.GET.get('lang') or request.headers.get('Accept-Language')
        if lang:
            translation.activate(lang)
        response = self.get_response(request)
        translation.deactivate()
        return response

class BlockIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.blocked_ips = getattr(settings, 'BLOCKED_IPS', [])

    def __call__(self, request):
        # GETTING IP ADRESS
        ip_addr = request.META.get('REMOTE_ADDR')
        # CHECKING IS IP IS BLOCKED
        if ip_addr in self.blocked_ips:
            return HttpResponseForbidden("YOUR IP IS BLOCKED!")
        # CONTINUE IF IP IS NOT BLOCKED
        response = self.get_response(request)
        return response