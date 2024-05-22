from django.urls import path
from .views import *

urlpatterns = [
    path('register/',register , name='register'),
    path('login/', login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('', home, name='home'),
    path('add-to-portfolio/', add_to_portfolio, name='add-to-portfolio'),
    path('logout/', custom_logout_view, name='logout'),
    
    # ... other URL patterns
]
