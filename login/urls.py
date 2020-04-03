from django.urls import path
from . import views

urlpatterns = [
	path('', views.render_home),
	path('success', views.render_success),
	path('register', views.register_user),
	path('login', views.authenticate_user),
	path('logout', views.logout),
	path('ajax/email_uniqueness', views.email_uniqueness)
]
