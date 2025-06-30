from django.urls import path, include

from sneakers_project.sneakers import views

urlpatterns = [
    path("latest-sneakers/", views.LatestSneakersList.as_view()),
    path(
        "sneakers/<slug:category_slug>/<slug:sneaker_slug>/",
        views.SneakerDetail.as_view(),
    ),
]
