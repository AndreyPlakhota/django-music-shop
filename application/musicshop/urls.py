from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import (
    BaseView,
    ArtistDetailView,
    AlbumDetailView,
    LoginView,
    RegistrationView,
    AccountView,
    CartView,
    AddToCartView,
    DeleteFromCartView,
    ChangeQTYView,
    AddToWishList,
    ClearNotificationsView,
    RemoveFromWishListView,
    CheckOutView,
    MakeOrderView
)

urlpatterns = [
    # endpoint-ы для корзины
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<str:ct_model>/<str:slug>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<str:ct_model>/<str:slug>/', DeleteFromCartView.as_view(), name='delete_from_cart'),
    path('change-qty/<str:ct_model>/<str:slug>/', ChangeQTYView.as_view(), name='change_qty'),
    # Основные endpoint-ы
    path('', BaseView.as_view(), name='base'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('account/', AccountView.as_view(), name='account'),
    path('checkout/', CheckOutView.as_view(), name='checkout'),
    path('make-order/', MakeOrderView.as_view(), name='make_order'),
    path('clear-notifications/', ClearNotificationsView.as_view(), name='clear_notifications'),
    path('add-to-wishlist/<int:album_id>/', AddToWishList.as_view(), name='add_to_wishlist'),
    path('remove-from-wishlist/<int:album_id>/', RemoveFromWishListView.as_view(), name='remove_from_wishlist'),
    path('<str:artist_slug>/', ArtistDetailView.as_view(), name='artist_detail'),
    path('<str:artist_slug>/<str:album_slug>/', AlbumDetailView.as_view(), name='album_detail')
]
