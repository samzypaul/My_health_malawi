from django.urls import path
from . import views

app_name = 'subscriptions'

urlpatterns = [
    path('generate-code/', views.generate_subscription_code, name='generate_code'),
    path('redeem-code/', views.redeem_subscription_code, name='redeem_code'),
    path('details/', views.subscription_details, name='subscription_details'),
]
