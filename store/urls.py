from django.urls import path

from store import views
from store.controller import auth_view ,cart,wishlist,checkout,orders

urlpatterns = [
#  genaral
    path('',views.store,name='home'),
    path('collections/',views.collection,name='collections'),
    path('collectionsview/<str:slug>',views.collectionview,name='collectionsview'),
    path('collections/<str:cat_slug>/<str:prod_slug>',views.productview,name='productview'),

    path('product-list',views.productlistajax),
    path('searchproduct',views.searchproduct,name='searchproduct'),
# auth
    path('register/',auth_view.register,name='register'),
    path('login/',auth_view.Login,name='loginpage'),
    path('logout/',auth_view.Logout,name='logoutpage'),
# cart
    path('add-to-cart',cart.addtocart,name ='add-to-cart'),
    path('cart/',cart.viewcart,name = 'cart'),
    path('update-to-cart',cart.updatecart,name ='add-to-cart'),
    path('delete-to-cart',cart.DeleteCart,name='deletecart'),
# wish-list
    path('wishlist',wishlist.wishlist,name='wishlist'),
    path('add-to-wish',wishlist.addtowish,name='addwish'),
    path('delete-to-wishlist',wishlist.deletetowish,name='deletewish'),
    # Chceck out
    path('checkout',checkout.checkout, name='checkout'),
    path('placeorder',checkout.placeorder,name='placeorder'),

    path("procced-to-pay",checkout.RozarpayCheck, name='razorpay'),


    path('my-orders',orders.index,name='order'),
    path('vieworders/<str:t_no>',orders.vieworder,name='orderview'),
    # path('my-orders',checkout.Order),




    

]
