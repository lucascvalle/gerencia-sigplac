import os
import sys

from django.core.wsgi import get_wsgi_application

# Add your project to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gerencia.settings')

# Run Django management commands for static files and migrations
# This will run on every cold start of the serverless function
# which is not ideal for migrations, but necessary for Vercel's serverless model.
# A better approach would be to run migrations as a separate build step,
# but Vercel's current Python runtime doesn't easily support that for WSGI.

# Only run these commands if not in a local development environment
if os.environ.get('VERCEL') == '1':
    try:
        from django.core.management import call_command
        call_command('collectstatic', '--no-input')
        call_command('migrate', '--no-input')
    except Exception as e:
        print(f"Error running management commands: {e}")


# Expose the WSGI application
handler = get_wsgi_application()
