from django.db.utils import OperationalError
from django.shortcuts import render

class DatabaseUnavailableMiddleware:
    """Show a friendly fail page instead of 500 when the database can't be reached."""
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        return self.get_response(request)
    def process_exception(self, request, exception):
        if isinstance(exception, OperationalError):
            return render(request, "db_unavailable.html", status=503)
        return None #if any other error,let Django handle it

