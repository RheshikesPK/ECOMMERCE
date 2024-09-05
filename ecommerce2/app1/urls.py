from django.urls import path
from django.shortcuts import render
from .views import IndexView, StoreView, ProductView,SignOutView,CartView, LaptopView, MobileView,CameraView, AccessoriesView,RegisterView,LoginView,CheckoutView,AddToCartView,GetCartItemsView,WishlistView, SaveReviewView, SearchProductsView, AddToWishlistView,UpdateCartView,CartRemove,SaveAddressView, GetWishlistItemsView,PaymentSuccessView
from .views import process_payment

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('store/', StoreView.as_view(), name='store'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('product/<int:id>/', ProductView.as_view(), name='product'),
    path('laptop/<int:id>/', LaptopView.as_view(), name='laptop'),
    path('mobile/<int:id>/', MobileView.as_view(), name='mobile'),
    path('camera/<int:id>/', CameraView.as_view(), name='camera'),
    path('accessories/<int:id>/', AccessoriesView.as_view(), name='accessories'),
    path('register/', RegisterView.as_view(), name='register'),
    path('signin/', LoginView.as_view(), name='signin'),    
    path('signout/', SignOutView.as_view(), name='signout'),
    path('add-to-cart/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', CartView.as_view(), name='cart_view'),
    path('get_cart_items/', GetCartItemsView.as_view(), name='get_cart_items'),
    path('save/', SaveReviewView.as_view(), name='save'),
    path('search_products/', SearchProductsView.as_view(), name='search_products'),
    path('add-to-wishlist/<int:product_id>/', AddToWishlistView.as_view(), name='add_to_wishlist'),
    path('update-cart/<int:cart_item_id>/', UpdateCartView.as_view(), name='update_cart'),
    path('remove/<int:cart_item_id>/', CartRemove.as_view(), name='remove_from_cart'),
    path('save_address/', SaveAddressView.as_view(), name='save_address'),
    path('get_wishlist_items/', GetWishlistItemsView.as_view(), name='get_wishlist_items'),
    path('process_payment/', process_payment, name='process_payment'),
    path('payment-success/', PaymentSuccessView.as_view(), name='payment_success'),


    # Other URL patterns

]