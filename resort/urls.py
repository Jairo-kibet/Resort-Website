from django.urls import path,include
from . import views as v


urlpatterns = [
    path("", v.index, name="home"),
    path("about/", v.about, name="about"),
    path("dining/", v.dining, name="dining"),
    path("conference/", v.conference, name="conference"),
    path("accommodation/", v.accommodation, name="accommodation"),
    path("reservation/", v.reservation, name="reservation"),
    path("contact/", v.contact, name="contact"),
    path("gallery/", v.gallery, name="gallery"),
]