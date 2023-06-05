from django.urls import path
from . import views

urlpatterns = [

    # Usuarios
    path('', views.index),
    path('registrarUsuario/', views.registrarUsuario),
    path('editarUsuario/<id>', views.editarUsuario),
    path('editarUsuario/edicionUsuario/', views.edicionUsuario),
    path('eliminarUsuario/<id>', views.eliminarUsuario),

    # Productos
    path('productos/', views.indexProductos),
    path('productos/registrarProducto/', views.registrarProducto),
    path('productos/editarProducto/<id>', views.editarProducto),
    path('productos/editarProducto/edicionProducto/', views.edicionProducto),
    path('productos/eliminarProducto/<id>', views.eliminarProducto),

    # Pedidos
    path('pedidos/', views.indexPedidos),
    path('pedidos/registrarPedido/', views.registrarPedido),
    path('pedidos/editarPedido/<id>', views.editarPedido),
    path('pedidos/editarPedido/edicionPedido/', views.edicionPedido),
    path('pedidos/eliminarPedido/<id>', views.eliminarPedido),

]

