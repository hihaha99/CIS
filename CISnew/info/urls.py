from django.urls import path

from . import views

urlpatterns = [
    path('', views.info, name='info'),
    path('add-store/',views.add_store,name='add-store'),
    path('add-dish/',views.add_dish,name='add-dish'),
    path('current/',views.current_store,name='current-store'),
    path('custom/',views.custom_store,name='custom-store'),
    path('dish/<str:store_name>/custom',views.render_items_custom, name='dish_custom'),
    path('dish/<str:store_name>/',views.render_items, name='dish')
]