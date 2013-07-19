from django.conf import settings

def fundi(request):
    """
    Adds site specific settings: ALLOWED_HOSTS, TYPEKIT_ID
    """ 

    return {
            'TYPEKIT_ID': settings.TYPEKIT_SITE_ID,
            'ALLOWED_HOSTS': settings.ALLOWED_HOSTS,
           }
