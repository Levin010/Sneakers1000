from django.urls import path, include

from sneakers_project.order import views

urlpatterns = [
    path("checkout/", views.checkout),
    path("orders/", views.OrdersList.as_view()),
]
