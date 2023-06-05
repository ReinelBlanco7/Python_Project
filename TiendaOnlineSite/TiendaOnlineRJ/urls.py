from django.urls import path
from . import views

urlpatterns = [

    # Login
    path('', views.indexLogin),
    path('ingresar/', views.ingresar),

    # Usuarios
    path('usuarios/', views.index),
    path('usuarios/registrarUsuario/', views.registrarUsuario),
    path('usuarios/editarUsuario/<id>', views.editarUsuario),
    path('usuarios/editarUsuario/edicionUsuario/', views.edicionUsuario),
    path('usuarios/eliminarUsuario/<id>', views.eliminarUsuario),

    # Productos
    path('productos/', views.indexProductos),
    path('productos/registrarProducto/', views.registrarProducto),
    path('productos/editarProducto/<id>', views.editarProducto),
    path('productos/editarProducto/edicionProducto/', views.edicionProducto),
    path('productos/eliminarProducto/<id>', views.eliminarProducto),

    # Pedidos
    path('pedidos/', views.indexPedidos),
    path('pedidos/registrarPedido/', views.registrarPedido),
    path('pedidos/buscarPedido/', views.buscarPedido),
    path('pedidos/editarPedido/<id>', views.editarPedido),
    path('pedidos/editarPedido/edicionPedido/', views.edicionPedido),
    path('pedidos/eliminarPedido/<id>', views.eliminarPedido),

]
