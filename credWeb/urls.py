from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('record/<int:pk>', views.customerRecord, name='record'),
    path('deleteRecord/<int:pk>', views.deleteRecord, name='delete'),
    path('addRecord/', views.addRecord, name='add'),
    path('updateRecord/<int:pk>', views.updateRecord, name='update'),
]
