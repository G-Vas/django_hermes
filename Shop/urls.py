from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name="home"),
    path('catalog/', views.PostView.as_view(), name='post'),
    path('search/', views.Search.as_view(), name='search'),
    path('call/', views.call, name='call'),
    path('about/', views.About.as_view(), name='about'),
    path('delivery/', views.Delivery.as_view(), name='delivery'),
    # path('payment/', views.Payment.as_view(), name='payment'),
    path('guarantee/', views.Guarantee.as_view(), name='guarantee'),
    path('catalog/<slug:slug>/', views.PostListView.as_view(), name='post_list'),
    path('catalog/<slug:slug>/<slug:post_slag>/', views.PostDetail.as_view(), name='detail'),


]
