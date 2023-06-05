from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Usuario
from .models import Producto
from .models import Pedido
from django.urls import reverse

# Create your views here.
from django.http import HttpResponse


def indexLogin(request):
    return render(request, 'index.html')


def ingresar(request):
    nombre = request.GET.get('txtNombre')
    contrasena = request.GET.get('txtContraseña')

    print(nombre)
    print(contrasena)

    cantidadUsuarios = Usuario.objects.filter(nombre=nombre, contrasena=contrasena).count()

    if cantidadUsuarios > 0:
        # El usuario existe, realizar las acciones necesarias
        return redirect('/productos')
    else:
        mensaje_error = "El usuario o contraseña son incorrectos"
        return render(request, 'index.html', {'error': mensaje_error})


def index(request):
    listaUsuarios = list(Usuario.objects.values())
    return render(request, 'usuarios.html', {"usuarios": listaUsuarios})


def registrarUsuario(request):
    nombre = request.POST['txtNombre']
    correo = request.POST['txtCorreo']
    contrasena = request.POST['txtContraseña']

    usuario = Usuario.objects.create(nombre=nombre, correo_electronico=correo, contrasena=contrasena)
    return redirect("/usuarios")


def editarUsuario(request, id):
    usuario = Usuario.objects.get(id=id)
    return render(request, "edicionUsuario.html", {"usuario": usuario})


def edicionUsuario(request):
    id = request.POST['txtId']
    nombre = request.POST['txtNombre']
    correo = request.POST['txtCorreo']
    contrasena = request.POST['txtContraseña']

    usuario = Usuario.objects.get(id=id)
    usuario.nombre = nombre
    usuario.correo_electronico = correo
    usuario.contrasena = contrasena
    usuario.save()

    return redirect("/usuarios")


def eliminarUsuario(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()

    return redirect("/usuarios")


# Productos

def indexProductos(request):
    listaProductos = list(Producto.objects.values())
    return render(request, 'productos.html', {"productos": listaProductos})


def registrarProducto(request):
    nombre = request.POST['txtNombre']
    descripcion = request.POST['txtDescripcion']
    precio = request.POST['txtPrecio']

    producto = Producto.objects.create(nombre=nombre, descripcion=descripcion, precio=precio)
    return redirect("/productos")


def editarProducto(request, id):
    producto = Producto.objects.get(id=id)
    return render(request, "edicionProducto.html", {"producto": producto})


def edicionProducto(request):
    id = request.POST['txtId']
    nombre = request.POST['txtNombre']
    descripcion = request.POST['txtDescripcion']
    precio = request.POST['txtPrecio']

    producto = Producto.objects.get(id=id)
    producto.nombre = nombre
    producto.descripcion = descripcion
    producto.precio = precio
    producto.save()

    return redirect("/productos")


def eliminarProducto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()

    return redirect("/productos")


# Pedidos

def indexPedidos(request):
    listaPedidos = list(Pedido.objects.values())
    listaProductos = list(Producto.objects.values())
    listaUsuarios = list(Usuario.objects.values())
    return render(request, 'pedidos.html',
                  {"pedidos": listaPedidos, "productos": listaProductos, "usuarios": listaUsuarios})


def registrarPedido(request):
    fecha = request.POST['txtFecha']
    cantidad = request.POST['txtCantidad']
    productoId = request.POST.get('selectProductoId')
    usuarioId = request.POST.get('selectUsuarioId')

    pedido = Pedido.objects.create(fecha=fecha, cantidad=cantidad, producto_id=productoId, usuario_id=usuarioId)
    return redirect("/pedidos")


def editarPedido(request, id):
    pedido = Pedido.objects.get(id=id)
    listaProductos = list(Producto.objects.values())
    listaUsuarios = list(Usuario.objects.values())
    return render(request, "edicionPedido.html",
                  {"pedido": pedido, "productos": listaProductos, "usuarios": listaUsuarios})


def edicionPedido(request):
    id = request.POST['txtId']
    fecha = request.POST['txtFecha']
    cantidad = request.POST['txtCantidad']
    productoId = request.POST.get('selectProductoId')
    usuarioId = request.POST.get('selectUsuarioId')

    pedido = Pedido.objects.get(id=id)
    pedido.fecha = fecha
    pedido.cantidad = cantidad
    pedido.producto_id = productoId
    pedido.usuario_id = usuarioId
    pedido.save()

    return redirect("/pedidos")


def eliminarPedido(request, id):
    pedido = Pedido.objects.get(id=id)
    pedido.delete()

    return redirect("/pedidos")


# Pedidos por usuarios

def buscarPedido(request):
    idUsuario = request.GET.get('txtBuscarUsuario')
    listaPedidos = Pedido.objects.filter(usuario_id=idUsuario)
    return render(request, 'pedidos.html', {"pedidos": listaPedidos})
