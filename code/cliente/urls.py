from django.urls import path
from . import views


app_name = 'cliente'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.cliente, name='cliente'),
    path('query/<str:email>/', views.cliente_query, name='cliente_query'),
    path('novo', views.cliente, name='cliente_novo'),
    path('<int:pk>/deletar_email', views.deletar_email, name='deletar_email'),
    path('<int:pk>/deletar_telephone', views.deletar_telephone, name='deletar_telephone'),
    path('<int:pk>/deletar_cliente', views.deletar_cliente, name='deletar_cliente')

]