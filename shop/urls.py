from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('outer', views.outer, name='outer'),
    path('top', views.top, name='top'),
    path('dress', views.dress, name='dress'),
    path('pants', views.pants, name='pants'),
    path('<int:products_id>', views.product, name='product'),
    path('search/', views.search, name='search')
]