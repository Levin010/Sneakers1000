from django.urls import path, include

from sneakers_project.sneakers import views

urlpatterns = [
    path("latest-sneakers/", views.LatestSneakersList.as_view()),
]
