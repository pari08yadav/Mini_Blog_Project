from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('logout/', views.user_logout, name="logout"),
    path('login/', views.user_login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('addpost/', views.add_post, name="addpost"),
    path('updatepost/<int:id>', views.update_post, name="updatepost"),
    path('deletepost/ <int:id>', views.delete_post, name="deletepost"),
    # path('forgotpass/', views.forgot_pass, name="forgotpass"),
]