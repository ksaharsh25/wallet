from django.urls import path
from .views import *
urlpatterns=[
    path('register',create,name="create"),
    path('login',login,name="login"),
    path('verify',verify,name="verify"),
    path('wallet/<str:pk>',wallet,name="wallet"),
    path('add/<str:pk>',add,name="add"),
    # path('create',create,name="create"),
    path('edit/<str:pk>', edit, name='edit'),
    path('list',list,name="list")
    # path('delete/', views.delete_employee, name='delete-employee'),

]