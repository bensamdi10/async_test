"""
ASGI config for test_async project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import sys

from django.core.asgi import get_asgi_application




app_path = os.path.abspath(
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)), os.pardir
    )
)
sys.path.append(os.path.join(app_path, "test_async"))
# We defer to a DJANGO_SETTINGS_MODULE already in the environment. This breaks
# if running multiple sites in the same mod_wsgi process. To fix this, use
# mod_wsgi daemon mode with each site in its own daemon process, or use
# os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.production"


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_async.settings')

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

application = get_asgi_application()
