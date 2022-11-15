from django.urls import path
from .views import *
urlpatterns=[
    path('register',register,name="register"),
    path('login',login,name="login"),
    path('verify',verify,name="verify"),
    path('wallet/<str:mobile>',Wallet,name="wallet"),
    path('add/<str:mobile>',add,name="add"),
    path('withdraw/<str:mobile>',withdraw,name="withdraw"),
    # path('create',create,name="create"),
    # path('edit/<str:pk>', edit, name='edit'),
    # path('list',list,name="list"),
    
    # path('delete/', views.delete_employee, name='delete-employee'),

]