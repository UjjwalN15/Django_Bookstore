from django.urls import path
from .views import *

urlpatterns = [
    path('book_genre/', BookGenreApiView.as_view({'get':'list','post':'create'}), name='book_genre'),
    path('book_genre/<int:pk>/', BookGenreApiView.as_view({'get':'retrieve','put':'update','delete':'destroy'}), name='book_genre'),
    path('author/', AuthorApiView.as_view({'get':'list','post':'create'}), name='author'),
    path('author/<int:pk>/', AuthorApiView.as_view({'get':'retrieve','put':'update','delete':'destroy'}), name='author'),
    path('books/', BooksApiView.as_view({'get':'list','post':'create'}), name='books'),
    path('books/<int:pk>/', BooksApiView.as_view({'get':'retrieve','put':'update','delete':'destroy'}), name='books'),
    path('order/', OrderApiView.as_view({'get':'list','post':'create'}), name='order'),
    path('order/<int:pk>/', OrderApiView.as_view({'get':'retrieve','put':'update','delete':'destroy'}), name='order'),
    path('login/',Login),
    path('register/',register),
    path('role/',group),
]