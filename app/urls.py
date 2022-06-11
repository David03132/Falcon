from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


app_name='tienda'

urlpatterns = [
    # paths menú
    path('', views.index, name='index'),
    path('categorias/', views.listCategorias, name='categorias'),
    path('marcas/', views.listMarcas, name='marcas'),
    path('usuarios/', views.listUsuarios, name='usuarios'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    
    
    path('nosotros/', views.nosotros, name='nosotros'),
    path('devoluciones/', views.devoluciones, name='devoluciones'),

    path('producto/', views.detalleProducto, name='producto'),
    path('addproducto/', views.addProducto, name='addproducto'),
    
    path('detalleproducto/<id>/', views.detalleProducto, name='detalleproducto'),
    path('busquedaproducto', views.busquedaProducto, name='busquedaproducto'),
    
    path('productocategoria/<id>/', views.productoxCategoria, name='productocategoria'),
    path('editproducto/<id>/', views.editarProducto, name='editproducto'),
    path('deleteProducto/<id>/', views.deleteProducto, name='deleteProducto'),
    path('listarproductos/', views.listarProductos, name='listarproductos'),
    
    
    path('addcategoria/', views.addCategoria, name='addcategoria'),
    path('editcategoria/<id>/', views.modificarCategoria, name='editcategoria'),
    path('deleteCategoria/<id>/', views.deleteCategoria, name='deleteCategoria'),
    
    path('addmarca/', views.addMarca, name='addmarca'),
    path('editmarca/<id>/', views.modificarMarca, name='editmarca'),
    path('deleteMarca/<id>/', views.deleteMarca, name='deleteMarca'),
    
    path('addusuario/', views.addUsuario, name='addusuario'),
    path('editusuario/<id>/', views.modificarUsuario, name='editusuario'),
    path('deleteUsuario/<id>/', views.deleteUsuario, name='deleteUsuario'),

    path('editproveedor/<id>/', views.modificarProveedor, name='editproveedor'),
    path('addproveedor/', views.addProveedor, name='addproveedor'),
    path('deleteProveedor/<id>/', views.deleteProveedor, name='deleteProveedor'),
    path('listarproveedores/', views.listarProveedores, name='listarproveedores'),
    
    path('addespecificaciones/', views.addEspecificaciones, name='addespecificaciones'),
    path('listarespecificaciones/', views.listarEspecificaciones, name='listarespecificaciones'),
    path('deleteEspecificacion/<id>/', views.deleteEspecificacion, name='deleteEspecificacion'),
    
    path('editperfilusuario/<id>/', views.modificarPerfilUsuario, name='editperfilusuario'),
        
    # paths de autenticacion
    path('registrar/', views.registrar, name='registrar'),
    path('login/', LoginView.as_view(template_name='auth/login.html'), name='login'),
    
    #Paths del carrito
    path('viewcart/', views.viewcart, name="viewcart"),

    path('addcart/<producto_id>/', views.agregar_producto, name="addcart"),

    path('delcart/<producto_id>/', views.eliminar_producto, name="delcart"),

    path('restarcart/<producto_id>/', views.restar_producto, name="restarcart"),

    path('cleancart/', views.cleancart, name="cleancart"),

    path('procesar_compra/', views.procesar_compra, name="procesar_compra"),
    
]
