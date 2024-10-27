from django.urls import path
from . import views


urlpatterns = [
    path('logout/',views.loggout,name='logout'),
    path('home/',views.home,name='home'),
    path('products/',views.products,name='products'),
    path('account/',views.account,name='account'),
    path('cart/',views.cart,name='cart'),
    path('pdt_detail/<pk>/',views.pdt_detail,name='product_details'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('add_to_cart/',views.add_to_cart,name='add_to_cart'),
    path('remove_item_cart/<pk>',views.remove_item_cart,name='remove_item_cart'),
    path('checkout/',views.checkout,name='checkoutpage')
] 