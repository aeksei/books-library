from django.urls import path

from books_api import views

app_name = "books_api"

urlpatterns = [
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
