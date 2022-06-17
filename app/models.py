from datetime import timezone
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Create your models here.
class Categorias(models.Model):
    nombre = models.CharField('Nombre',max_length=100)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = "CATEGORIA"
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']
        
class Marcas(models.Model):
    nombre = models.CharField('Nombre',max_length=100)
    
    
    def __str__(self):
        return str(self.nombre)
    
    class Meta:
        db_table = "MARCA"
        verbose_name = 'marca'
        verbose_name_plural = 'marcas'
        ordering = ['id']


#modelo Productos
class Productos(models.Model):
    nombre = models.CharField('Nombre',max_length=100)
    imagen = models.ImageField('Imagen',upload_to='productos', null=True)
    descripcion = models.CharField('Descripcion',max_length=500)
    precio = models.IntegerField('Precio',validators=[MinValueValidator(0.0)])
    stock = models.IntegerField('Stock',null=True, default=0, validators=[MaxValueValidator(100),
            MinValueValidator(1)])     
    videoid = models.CharField('Enlace del video',max_length=100, null=True)
    destacado= models.BooleanField('¿Es destacado?')
    categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT)
    marca = models.ForeignKey(Marcas, on_delete=models.PROTECT)
    descuento = models.IntegerField('Descuento',null=True, default=0, validators=[MaxValueValidator(100)])
    
    @property
    def precio_descuento(self):
        return round(self.precio - (self.precio * self.descuento / 100))

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'PRODUCTOS'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']
        



class Metodo_Pago(models.Model):
    nombre_metodo= models.CharField('Metodo de pago',max_length=50)

    def __str__(self):
        return self.nombre_metodo
    class Meta:
        db_table = 'METODO_PAGO'
        verbose_name = 'Metodo pago'
        verbose_name_plural = 'METODO_PAGOS'
        ordering = ['id']


class Region (models.Model):
    nombre_region= models.CharField('Nombre region',max_length=50)
    abreviatura = models.CharField('Abreviatura',max_length=4)
    capital = models.CharField('Capital',max_length=64)
    
    def __str__(self):
        return self.nombre_region
    class Meta:
        db_table = 'REGION'
        verbose_name = 'Region'
        verbose_name_plural = 'REGIONES'
        ordering = ['id']



class Provincia (models.Model):
    nombre_provincia= models.CharField('Nombre provincia',max_length=50)
    region= models.ForeignKey(Region, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre_provincia
    class Meta:
        db_table = 'PROVINCIA'
        verbose_name = 'Provincia'
        verbose_name_plural = 'PROVINCIA'
        ordering = ['id']


class Comuna(models.Model):
    nombre_comuna= models.CharField('Nombre comuna',max_length=50)
    provincia= models.ForeignKey(Provincia, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre_comuna
    class Meta:
        db_table = 'COMUNA'
        verbose_name = 'Comuna'
        verbose_name_plural = 'COMUNAS'
        ordering = ['id']



class Envio(models.Model):
    comuna_envio= models.ForeignKey(Comuna, on_delete=models.PROTECT)

    def __str__(self):
        return self.comuna_envio
    class Meta:
        db_table = 'ENVIO'
        verbose_name = 'Envio'
        verbose_name_plural = 'ENVIOS'
        ordering = ['id']
        

            
class Cliente(AbstractUser):
    username  = models.CharField('Nombre de usuario',max_length=50, unique=True) 
    email = models.EmailField('Email',max_length=50, unique=True)
    first_name = models.CharField('Primer nombre',max_length=50, null=False)
    last_name = models.CharField('Apellido paterno',max_length=50, null=False)
    ape_materno = models.CharField('Apellido materno',max_length=50, null=False)
    calle = models.CharField("Calle", max_length=50)
    numero = models.IntegerField("Número",default=0, validators=[MaxValueValidator(99999),
            MinValueValidator(1)])
    depto = models.CharField("N° depto / oficina / otro dato (si aplica)", max_length=100, blank=True)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT)
    comuna = models.ForeignKey(Comuna, on_delete=models.PROTECT)
    is_superuser = models.BooleanField('Administrador', null=True)
    
    def __str__(self):
        return self.test
    class Meta:
        db_table = 'CLIENTE'
        verbose_name = 'Cliente'
        verbose_name_plural = 'CLIENTES'
        ordering = ['id']
    
class Venta (models.Model):
    monto = models.IntegerField('Monto')
    fecha_venta= models.DateField('Fecha de la venta')
    estado_venta= models.CharField('Estado de la venta',max_length=50)
    usuario= models.ForeignKey(Cliente, on_delete=models.PROTECT)
    


    def __str__(self):
        return self.monto
    class Meta:
        db_table = 'VENTA'
        verbose_name = 'Venta'
        verbose_name_plural = 'VENTAS'
        ordering = ['id']
        
class Trabajador (models.Model):
    nombre= models.CharField('Nombre',max_length=20)
    apellido_paterno= models.CharField('Apellido paterno',max_length=30) 
    apellido_materno= models.CharField('Apellido materno',max_length=30)
    fecha_nacimiento= models.DateField('Fecha de nacimiento')
    telefono= models.IntegerField('Telefono')
    email= models.EmailField('Email',max_length=50)
    usuario= models.CharField('Usuario',max_length=20)
    password= models.BinaryField('Contraseña')
    venta= models.ForeignKey(Venta, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'TRABAJADOR'
        verbose_name = 'Trabajador'
        verbose_name_plural = 'Trabajadores'
        ordering = ['nombre']
    
class Proveedor (models.Model):
    nombre= models.CharField('Nombre',max_length=50)
    razon_social= models.CharField('Razon social',max_length=150)
    sector_comercial= models.CharField('Sector comercial',max_length=50)
    tipo_documento= models.CharField('Tipo de documento',max_length=50)
    num_documento= models.IntegerField('Numero de documento')
    telefono= models.IntegerField('Telefono')
    email= models.EmailField('Email',max_length=50)
    url= models.URLField('Enlace sitio web', max_length=200)
    comuna= models.ForeignKey(Comuna, on_delete=models.PROTECT)
    

    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'PROVEEDOR'
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['nombre']

class Ingreso(models.Model):
    fecha= models.DateField('Fecha de ingreso')
    tipo_comprobante= models.CharField('Tipo de comprobante',max_length=50)
    proveedor= models.ForeignKey(Proveedor, on_delete=models.PROTECT)

    def __str__(self):
        return self.proveedor.nombre
    class Meta:
        db_table = 'INGRESO'
        verbose_name = 'Ingreso'
        verbose_name_plural = 'Ingresos'
        ordering = ['fecha']
        
class Detalle_Ingreso(models.Model):
    precio_compra= models.IntegerField('Precio de compra') 
    precio_venta= models.IntegerField('Precio de venta',) 
    stock_inicial= models.IntegerField('Stock inicial',validators=[MaxValueValidator(100),
            MinValueValidator(1)]) 
    stock_actual= models.IntegerField('Stock actual',validators=[MaxValueValidator(100),
            MinValueValidator(1)])
    ingreso= models.ForeignKey(Ingreso, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.ingreso.proveedor.nombre
    
    class Meta:
        db_table = 'DETALLE_INGRESO'
        verbose_name = 'Detalle_Ingreso'
        verbose_name_plural = 'Detalle_Ingresos'
        ordering = ['precio_compra'] 


        
class Carrito_Compras(models.Model):
    cantidad= models.IntegerField('Cantidad')
    subtotal= models.IntegerField('Subtotal')
    cod_producto= models.IntegerField('Codigo del producto')
    
    def __str__(self):
        return self.cantidad

    class Meta:
        db_table = 'CARRITO_COMPRAS'
        verbose_name = 'Carrito_Compras'
        verbose_name_plural = 'Carrito_Compras'
        ordering = ['id']
