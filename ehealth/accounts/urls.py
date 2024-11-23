from django.urls import path
from .  import views
app_name='accounts'

urlpatterns = [
    path('login/',views.login_user, name="login"),
    path('logout/',views.logout_user, name="logout"),
    path('register/',views.register, name="register"),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('test-register/', views.test_template),

]
