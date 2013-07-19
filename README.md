# Fundus
Base django project.

## Quickstart
Create virtualenv and install requirements

    mkvirtualenv fundus
    pip install -r reqs.txt

Install requirements to settings.INSTALLED_APPS

    INSTALLED_APPS += (
        'crispy_forms',
        'contact_form',
        'flatpages_x',
    )
    $ python manage.py syncdb

Set settings.ALLOWED_HOSTS to deployment domain(s)
Add recaptcha keys, set typekit_id in settings.py

    ALLOWED_HOSTS = ['example.com', 'example.net']
    TYPEKIT_SITE_ID = 'xxxxxxx'
    RECAPTCHA_PUBLIC_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    RECAPTCHA_PRIVATE_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

