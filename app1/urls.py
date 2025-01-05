from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home,name='home'),
    path('first/',first,name='first'),
    path('store/',store,name='store'),
    path('catstore/',catstore,name='catstore'),
    path('reg/',register,name='register'),
    path('login/',login,name='login'),
    path('',index,name='index'),
    path('logout/',logout,name='logout'),
    path('profile/',profile,name='profile'),
    path('update/',update,name='update'),
    path('changepass/',changepass,name='changepass'),
    path('catpro/<int:id>',catpro,name='catpro'),
    path('prodetails/<int:id>',prodetails,name='prodetails'),
    path('cartdata/',cartdata,name='cartdata'),
    path('plusitem/<int:cartid>',plusitem,name='plusitem'),
    path('minusitem/<int:cartid>',minusitem,name='minusitem'),
    path('removeitem/<int:cartid>',removeone,name='removeone'),
    path('removeall/',removeall,name='removeall'),
    path('addproduct/',addproduct,name='addproduct'),
    path('selection/',selection,name='selection'),
    path('checkout/',checkout,name='checkout'),
    path('vend_product/',vend_product,name='vend_product'),
    # path('razorpay/',razorpayment,name='razorpayment'),
    # path('paymenthandler/',payemthandler,name='paymenthandler'),
    path('orderhistory/',orderhistory,name='orderhistory'),
    path('send_mail/',email_send,name='send_mail'),
    path('otp/',send_otp,name='otp'),
    path('check_otp/',check_otp,name = 'check_otp'),
    path('registernew/',newregisterparctice,name = 'register'),
    path('search/',search,name = 'search'),
    path('api_data/',api_data,name = 'api_data'),
    path('blogformview/',blogformview,name = 'blogformview'),
    





    
]
        