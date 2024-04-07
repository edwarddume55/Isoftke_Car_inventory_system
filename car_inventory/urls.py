from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from. import views


urlpatterns = [
    path('car/list/', views.car_list, name='car_list'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('car/add/', views.add_car, name='add_car'),
    path('car/<int:car_id>/edit/', views.edit_car, name='edit_car'),
    path('car/<int:car_id>/delete/', views.delete_car, name='delete_car'),

    # path('register/', views.register, name='register'),
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('car/<int:car_id>/add_expense/', views.add_expense, name='add_expense'),
    path('car/<int:car_id>/add_document/', views.add_document, name='add_document'),

    path('admin/', views.admin_panel, name='admin_panel'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('users/', views.user_list, name='user_list'),
    path('add_user/', views.add_user, name='add_user'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('car/list/admin', views.car_list_admin, name='car_list_admin'),
    path('car/gallery/', views.car_gallery, name='car_gallery'),
    path('car/<int:car_id>/', views.car_detail_admin, name='car_detail_admin'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)