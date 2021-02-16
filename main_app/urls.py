from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('petrocks/', views.petrocks_index, name='petrocks_index'),
    path('petrocks/<int:petrock_id>/', views.petrocks_detail, name='petrocks_detail'),
    path('petrocks/create/', views.PetrockCreate.as_view(), name='petrocks_create'),
    path('petrocks/<int:pk>/update', views.PetrockUpdate.as_view(), name='petrocks_update'),
    path('petrocks/<int:pk>/delete', views.PetrockDelete.as_view(), name='petrocks_delete'),
]