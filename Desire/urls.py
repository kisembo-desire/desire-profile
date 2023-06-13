from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Desire.views import homepage

app_name = "Desire"
urlpatterns = [
    path("", homepage, name="homepage")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
