import os
import sys

from django.core.wsgi import get_wsgi_application

# Add your project to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gerencia.settings')


# Expose the WSGI application
application = get_wsgi_application()
