from django.urls import path
from .views import products_page, order_page, register_page, userlist, aboutUs_page, logout_page, accound_settings, \
    activate
from django.contrib.auth import views as a_views
urlpatterns = [
    path('',products_page, name='products'),
    path('order/<int:product_id>/',order_page,name='order'),
    path('register/',register_page),
    path('user/',userlist),
    path('description/', aboutUs_page),
    path('logout/',logout_page, name='logout'),
    path('profile/',accound_settings,name='profile'),
    path('reset_password/',a_views.PasswordResetView.as_view(template_name='dir'),name='password_reset'),
    path('reset_password_done/',a_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',a_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete/',a_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
]