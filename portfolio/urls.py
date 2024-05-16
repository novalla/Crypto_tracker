from django.urls import path
from .views import *

urlpatterns = [
    path('register/',register , name='register'),
    path('login/', login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('', home, name='home'),
    # path('cryptocurrency-assets/', display_cryptocurrency_assets, name='cryptocurrency_assets'),
    # path('add-to-portfolio/<int:cryptocurrency_id>/', add_to_portfolio, name='add_to_portfolio'),
    # path('view-portfolio/', view_portfolio, name='view_portfolio'),
]
