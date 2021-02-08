from django.urls import path 
from . import views 
app_name = 'esearch1' 
urlpatterns = [ 
path('', views.search_index, name='search_view'), 
]