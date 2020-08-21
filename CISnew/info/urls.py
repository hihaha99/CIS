from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.info, name='info'),
    path('add-store/',views.add_store,name='add-store'),
    path('add-dish/',views.add_dish,name='add-dish'),
    path('current/',views.current_store,name='current-store'),
    path('custom/',views.custom_store,name='custom-store'),
    path('dish/<str:store_name>/custom',views.render_items_custom, name='dish_custom'),
    path('dish/<str:store_name>/',views.render_items, name='dish'),
    path('register/',views.register, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name="users/login.html"),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name="users/logout.html"),name='logout')

    # path('dish/<str:store_name>/',views.IndexView.as_view(), name='dish')
]