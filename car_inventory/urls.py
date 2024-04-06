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
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)