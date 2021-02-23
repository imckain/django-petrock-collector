from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('petrocks/', views.petrocks_index, name='index'),
    path('petrocks/<int:petrock_id>/', views.petrocks_detail, name='petrocks_detail'),
    path('petrocks/create/', views.PetrockCreate.as_view(), name='petrocks_create'),
    path('petrocks/<int:pk>/update', views.PetrockUpdate.as_view(), name='petrocks_update'),
    path('petrocks/<int:pk>/delete', views.PetrockDelete.as_view(), name='petrocks_delete'),
    path('petrocks/<int:petrock_id>/add_feeding', views.add_feeding, name='add_feeding'),
    path('petrocks/<int:petrock_id>/add_photo', views.add_photo, name='add_photo'),
    path('petrocks/<int:petrock_id>/associate_hat/<int:hat_id>/', views.associate_hat, name='associate_hat'),
    path('petrocks/<int:petrock_id>/unassociate_hat/<int:hat_id>/', views.unassociate_hat, name='unassociate_hat'),
    path('hats/', views.HatList.as_view(), name='hats_index'),
    path('hats/<int:pk>/', views.HatDetailView.as_view(), name='hats_detail'),
    path('hats/create/', views.HatCreateView.as_view(), name='hats_create'),
    path('hats/<int:pk>/update/', views.HatUpdateView.as_view(), name='hats_update'),
    path('hats/<int:pk>/delete/', views.HatDeleteView.as_view(), name='hats_delete'),
    path('accounts/signup', views.signup, name='signup'),
]