from django.urls import path
from .views import HomeView, AboutView, TermsAndConditios

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("terminos/", TermsAndConditios.as_view(), name="terminos")
]
