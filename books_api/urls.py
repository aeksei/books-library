from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from books_api import views

app_name = "books_api"

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path(
        "books/",
        views.ListCreateBookAPIView.as_view(),
        name="book-list"
    ),
    path(
        "books/<int:pk>/",
        views.RetriveUpdateDeleteBookAPIView.as_view(),
        name="book-detail",
    ),
    path("categories/", views.ListCreateCategoryAPIView.as_view(), name="category-list"),
]
