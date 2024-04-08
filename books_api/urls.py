from django.urls import path

from books_api import views

urlpatterns = [
    path(
        "books/",
        views.ListCreateAPIView.as_view(),
        name="book-list"
    ),
    path(
        "books/<int:pk>/",
        views.RetriveUpdateDeleteBookAPIView.as_view(),
        name="book-detail",
    ),
    path("categories/", views.ListCreateCategoryAPIView.as_view(), name="category-list"),
]
