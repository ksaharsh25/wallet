from django.urls import path
from .views import *
urlpatterns=[
    path('register',register,name="register"),
    path('login',login,name="login"),
    path('verify',verify,name="verify"),
    path('wallet/<str:mobile>',Wallet,name="wallet"),
    path('add/<str:mobile>',add,name="add"),
    path('withdraw/<str:mobile>',withdraw,name="withdraw"),
    path('bank_transfer',bank_transfer,name="bank_transfer"),
    path('transaction_done/<str:account_number>',transaction_done,name="transaction_done"),
    path('marks/<str:mobile>',marks,name="marks"),
    path('points1/<str:mobile>',points1,name="points1"),
    path('points2/<str:mobile>',points2,name="points2"),
    # path('list',list,name="list"),


]