from django.urls import path

from .views import *

urlpatterns = [
    path('', SettingsAPIView.as_view(), name="settings list api"),
    path('create/', SettingsCreateAPI.as_view(), name="settings create api"),
    path('retrive/<int:pk>/', SettingsRetrieveAPI.as_view(), name="settings retrive api"),
    path('update/<int:pk>/', SettingsUpdateAPI.as_view(), name="settings update api"),
    path('delete/<int:pk>/', SettingsDestroyAPI.as_view(), name="settings delete api"),
]
