from nturl2path import url2pathname
from django.http.response import HttpResponse
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .carro import Carro
from django.core.paginator import Paginator
from django.http import Http404, HttpRequest
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import ListView, CreateView
from django.db.models import Q
from .forms import CustomUserCreationFormAdd, ProductoForm, CategoriaForm, CustomUserCreationForm, MarcaForm, CustomUserCreationFormListado


# Create your views here.
def index(request):
    productos=Productos.objects.all()
    busqueda = request.POST.get("buscador")
    product_list = Productos.objects.order_by('nombre')
    page = request.GET.get('page', 1)

    if busqueda:
        product_list = Productos.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(descripcion__icontains = busqueda)
        ).distinct()
    
    try:
        paginator = Paginator(product_list, 12)
        product_list = paginator.page(page)
    except:
        raise Http404
    
    
    data = {'entity': product_list,
            'paginator': paginator,
            'productos': productos
    }
    return render(request, 'index.html', data)

def busquedaProducto(request):
    productos=Productos.objects.all()
    busqueda = request.POST.get("buscador")
    product_list = Productos.objects.order_by('id')
    page = request.GET.get('page', 1)

    if busqueda:
        product_list = Productos.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(descripcion__icontains = busqueda)
        ).distinct()
    
    try:
        paginator = Paginator(product_list, 12)
        product_list = paginator.page(page)
    except:
        raise Http404
    
    
    data = {'entity': product_list,
            'paginator': paginator,
            'productos': productos
    }
    return render(request, 'busquedaproducto.html', data)    

# Listar productos por categoria
def productoxCategoria(request, id):
    busqueda = request.POST.get("buscador")
    lista_productos = Productos.objects.filter(categoria = id)
    
    if busqueda:
        lista_productos = Productos.objects.filter(
            Q(nombre__icontains=busqueda) |
            Q(descripcion__icontains=busqueda)
        ).distinct()

    data = {'entity': lista_productos}
    return render(request, 'categorias.html', data)


# views productos
def detalleProducto(request, id):
    product = get_object_or_404(Productos, id=id)
    otrosProductos = Productos.objects.filter(categoria=product.categoria)
    data = {
        'producto': product,
        'productosRelacionados': otrosProductos
    }
    return render(request, 'producto/detalle.html', data)


@login_required(login_url='/login')
@permission_required('app.add_producto', login_url='/login')
def addProducto(request):
    data = {
        'form' : ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro agregado correctamente")
            return redirect(to="/listarproductos")
        else:
            data["form"] = formulario   
    return render(request, 'producto/agregar.html', data)



@permission_required('view_Producto', login_url='/login')
def listarProductos(request):
    busqueda = request.POST.get("buscador")
    lista_productos = Productos.objects.order_by('id')
    page = request.GET.get('page', 1)
    if busqueda:
        lista_productos = Productos.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(descripcion__icontains = busqueda)
        ).distinct()

    try:
        paginator = Paginator(lista_productos, 6)
        lista_productos = paginator.page(page)
    except:
        raise Http404

    data = {'entity': lista_productos,
            'title': 'LISTADO DE PRODUCTOS',
            'paginator': paginator
            }
    return render(request, 'listados/listadoproductos.html', data)


@login_required(login_url='/login')
@permission_required('change_Producto', login_url='/login')
def editarProducto(request, id):
    producto = get_object_or_404(Productos, id=id)
    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro modificado correctamente")
            return redirect(to="/listarproductos")
        data["form"] = formulario
    return render(request, 'producto/modificar.html', data)


@login_required(login_url='/login')
@permission_required('delete_Producto', login_url='/login')
def deleteProducto(request, id):
    producto = get_object_or_404(Productos, id=id)
    producto.delete()
    messages.success(request, "Registro eliminado correctamente")
    return redirect(to="/listarproductos")

def nosotros(request):
    return render(request, 'InfoFlacon/nosotros.html')

def garantia(request):
    return render(request, 'garantia.html')

def devoluciones(request):
    return render(request, 'InfoFlacon/devoluciones.html')

@login_required(login_url='/login')
@permission_required('user.is_staff', login_url='/')
def dashboard(request):
    return render(request, 'admin/dashboard.html')


# Views categorias
@login_required(login_url='/login')
@permission_required('view_Categoria', login_url='/login')
def listCategorias(request):
    lista_categorias = Categorias.objects.all().order_by('id')
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(lista_categorias, 10)
        lista_categorias = paginator.page(page)
    except:
        raise Http404

    data = {'entity': lista_categorias,
            'title': 'LISTADO DE CATEGORIAS',
            'paginator': paginator
            }

    return render(request,'listados/listadocategorias.html', data)


@login_required(login_url='/login')
@permission_required('add_Categoria', login_url='/login')
def addCategoria(request):
    data = {
        'form': CategoriaForm()
    }
    if request.method == 'POST':
        formulario = CategoriaForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro agregado correctamente")
            return redirect(to="/categorias")
        else:
            data["form"] = formulario
    return render(request, 'categoria/agregar.html', data)


@login_required(login_url='/login')
@permission_required('change_Categoria', login_url='/login')
def modificarCategoria(request, id):
    categoria = get_object_or_404(Categorias, id=id)

    data = {
        'form': CategoriaForm(instance=categoria)
    }
    if request.method == 'POST':
        formulario = CategoriaForm(data=request.POST, instance=categoria)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro modificado correctamente")
            return redirect(to="/categorias")
        else:
            data["form"] = formulario

    return render(request, 'categoria/modificar.html', data)


@login_required(login_url='/login')
@permission_required('delete_Categoria', login_url='/login')
def deleteCategoria(request, id):
    categoria = get_object_or_404(Categorias, id=id)
    categoria.delete()
    messages.success(request, "Registro eliminado correctamente")
    return redirect(to="/categorias")


#Views Marcas
@login_required(login_url='/login')
@permission_required('app.view_marca', login_url='/login')
def listMarcas(request):
    lista_marcas = Marcas.objects.all().order_by('id')
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(lista_marcas, 10)
        lista_marcas = paginator.page(page)
    except:
        raise Http404

    data = {'entity': lista_marcas,
            'title': 'LISTADO DE MARCAS',
            'paginator': paginator
            }

    return render(request,'listados/listadomarcas.html', data)


@login_required(login_url='/login')
@permission_required('add_marca', login_url='/')
def addMarca(request):
    data = {
        'form': MarcaForm()
    }
    if request.method == 'POST':
        formulario = MarcaForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro agregado correctamente")
            return redirect(to="/marcas")
        else:
            data["form"] = formulario
    return render(request, 'marca/agregar.html', data)


@login_required(login_url='/login')
@permission_required('change_marca', login_url='/login')
def modificarMarca(request, id):
    marca = get_object_or_404(Marcas, id=id)

    data = {
        'form': MarcaForm(instance=marca)
    }
    if request.method == 'POST':
        formulario = MarcaForm(data=request.POST, instance=marca)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro modificado correctamente")
            return redirect(to="/marcas")
        else:
            data["form"] = formulario

    return render(request, 'marca/modificar.html', data)


@login_required(login_url='/login')
@permission_required('delete_marca', login_url='/login')
def deleteMarca(request, id):
    marca = get_object_or_404(Marcas, id=id)
    marca.delete()
    messages.success(request, "Registro eliminado correctamente")
    return redirect(to="/marcas")


# Views usuarios
@login_required(login_url='/login')
@permission_required('view_user', login_url='/login')
def listUsuarios(request):
    lista_usuarios = Cliente.objects.all().order_by('id')
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(lista_usuarios, 10)
        lista_usuarios = paginator.page(page)
    except:
        raise Http404

    data = {'entity': lista_usuarios,
            'title': 'LISTADO DE USUARIOS',
            'paginator': paginator
            }

    return render(request,'listados/listadousuarios.html', data)


@login_required(login_url='/login')
@permission_required('add_user', login_url='/login')
def addUsuario(request):
    data = {
        'form': CustomUserCreationFormAdd()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationFormAdd(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro agregado correctamente")
            return redirect(to="/usuarios")
        else:
            data["form"] = formulario
    return render(request, 'usuarios/agregar.html', data)


@login_required(login_url='/login')
@permission_required('change_cliente', login_url='/login')
def modificarUsuario(request, id):
    usuario = get_object_or_404(Cliente, id=id)

    
     
    data = {
        'form': CustomUserCreationFormListado(instance=usuario)
    }
    if request.method == 'POST':
        formulario = CustomUserCreationFormListado(data=request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro modificado correctamente")
            return redirect(to="/usuarios")
        else:
            data["form"] = formulario

    return render(request, 'usuarios/modificar.html', data)

@login_required(login_url='/login')
def modificarPerfilUsuario(request, id):
    usuario = get_object_or_404(Cliente, id=id)
    
    if request.user.id != usuario.id:
           raise Http404() 
     
    data = {
        'form': CustomUserCreationFormListado(instance=usuario)
    }
    if request.method == 'POST':
        formulario = CustomUserCreationFormListado(data=request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro modificado correctamente")
            return redirect(to="/")
        else:
            data["form"] = formulario

    return render(request, 'usuarios/modificar.html', data)


@login_required(login_url='/login')
@permission_required('delete_user')

def deleteUsuario(request, id):

    usuario = get_object_or_404(Cliente, id=id)
    
    if request.user.id == usuario.id:
        raise Http404() 
        
             
    usuario.delete()
    messages.success(request, "Registro eliminado correctamente")
    return redirect(to="/usuarios")





def registrar(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, 'Usuario registrado correctamente')
            return redirect('/')
        else:
            data['form'] = formulario
    
    return render(request, 'auth/registrar.html', data)

# Acciones carrito
def viewcart(request):
    return render(request, 'carrito/cart.html', {'carro': request.session['carro']})

def agregar_producto(request, producto_id):
    carro=Carro(request)
    producto=Productos.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect(to="/viewcart")

def eliminar_producto(request, producto_id):
    carro=Carro(request)
    producto=Productos.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect(to="/viewcart")


def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Productos.objects.get(id=producto_id)
    carro.restar(producto=producto)
    return redirect(to="/viewcart")

def cleancart(request):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect(to="/viewcart")


def procesar_compra(request):
    messages.success(request, 'Gracias por su Compra!!')
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect('/')
