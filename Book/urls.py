from django.urls import path
from .views import get_Bookstore,create_Bookstore,update_Bookstore,delete_Bookstore,filter_Bookstore


urlpatterns=[

      path('get/',get_Bookstore,name='get_Bookstore'), 
      path('create/',create_Bookstore,name='create_Bookstore'),
      path('update/<int:pk>',update_Bookstore,name='update_Bookstore'),
      path('delete/<int:pk>',delete_Bookstore,name='delete_Bookstore'),
      path('filter/',filter_Bookstore,name='filter'),
]

