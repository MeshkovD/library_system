from django.contrib import admin
from django.urls import path

from books.views import BookAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/bookslist', BookAPIView.as_view()),
]
