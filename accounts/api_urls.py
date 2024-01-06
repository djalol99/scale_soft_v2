from django.urls import path

from knox import views as knox_views

from .api_views import CreateUserView, LoginView, ManageUserView

app_name = 'accounts'

urlpatterns = [
    path('create/', CreateUserView.as_view(), name="create"),
    path('profile/', ManageUserView.as_view(), name='profile'),
    path('login/', LoginView.as_view(), name='knox_login'),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]