from datetime import timezone
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Create your models here.
class Categorias(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = "CATEGORIA"
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']
        
class Marcas(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='marcas', null=True)
    
    def __str__(self):
        return str(self.nombre)
    
    class Meta:
        db_table = "MARCA"
        verbose_name = 'marca'
        verbose_name_plural = 'marcas'
        ordering = ['id']


#modelo Productos
class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='productos', null=True)
    descripcion = models.CharField(max_length=500)
    precio = models.PositiveIntegerField()
    stock = models.IntegerField(null=True, default=0, validators=[MaxValueValidator(100),
            MinValueValidator(1)])     
    videoid = models.CharField(max_length=100, null=True)
    destacado= models.BooleanField()
    categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT)
    marca = models.ForeignKey(Marcas, on_delete=models.PROTECT) 
    

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'PRODUCTOS'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']
        



class Metodo_Pago(models.Model):
    nombre_metodo= models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_metodo
    class Meta:
        db_table = 'METODO_PAGO'
        verbose_name = 'Metodo pago'
        verbose_name_plural = 'METODO_PAGOS'
        ordering = ['id']


class Region (models.Model):
    nombre_region= models.CharField(max_length=50)
    abreviatura = models.CharField(max_length=4)
    capital = models.CharField(max_length=64)
    
    def __str__(self):
        return self.nombre_region
    class Meta:
        db_table = 'REGION'
        verbose_name = 'Region'
        verbose_name_plural = 'REGIONES'
        ordering = ['id']



class Provincia (models.Model):
    nombre_provincia= models.CharField(max_length=50)
    region= models.ForeignKey(Region, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre_provincia
    class Meta:
        db_table = 'PROVINCIA'
        verbose_name = 'Provincia'
        verbose_name_plural = 'PROVINCIA'
        ordering = ['id']


class Comuna(models.Model):
    nombre_comuna= models.CharField(max_length=50)
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
    email = models.CharField(max_length=50, unique=True)
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
    
    def __str__(self):
        return self.test
    class Meta:
        db_table = 'CLIENTE'
        verbose_name = 'Cliente'
        verbose_name_plural = 'CLIENTES'
        ordering = ['id']
    
class Venta (models.Model):
    monto = models.IntegerField()
    fecha_venta= models.DateField()
    estado_venta= models.CharField(max_length=50)
    usuario= models.ForeignKey(Cliente, on_delete=models.PROTECT)
    


    def __str__(self):
        return self.monto
    class Meta:
        db_table = 'VENTA'
        verbose_name = 'Venta'
        verbose_name_plural = 'VENTAS'
        ordering = ['id']
        
class Trabajador (models.Model):
    nombre= models.CharField(max_length=20)
    apellido_paterno= models.CharField(max_length=30) 
    apellido_materno= models.CharField(max_length=30)
    fecha_nacimiento= models.DateField()
    telefono= models.IntegerField()
    email= models.EmailField(max_length=50)
    usuario= models.CharField(max_length=20)
    password= models.BinaryField()
    venta= models.ForeignKey(Venta, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'TRABAJADOR'
        verbose_name = 'Trabajador'
        verbose_name_plural = 'Trabajadores'
        ordering = ['nombre']
    
class Proveedor (models.Model):
    nombre= models.CharField(max_length=50)
    razon_social= models.CharField(max_length=150)
    sector_comercial= models.CharField(max_length=50)
    tipo_documento= models.CharField(max_length=50)
    num_documento= models.IntegerField()
    telefono= models.IntegerField()
    email= models.EmailField(max_length=50)
    url= models.CharField(max_length=100)
    comuna= models.ForeignKey(Comuna, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'PROVEEDOR'
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['nombre']

class Ingreso(models.Model):
    fecha= models.DateField()
    tipo_comprobante= models.CharField(max_length=50)
    proveedor= models.ForeignKey(Proveedor, on_delete=models.PROTECT)

    def __str__(self):
        return self.proveedor.nombre
    class Meta:
        db_table = 'INGRESO'
        verbose_name = 'Ingreso'
        verbose_name_plural = 'Ingresos'
        ordering = ['fecha']
        
class Detalle_Ingreso(models.Model):
    precio_compra= models.IntegerField() 
    precio_venta= models.IntegerField() 
    stock_inicial= models.IntegerField(validators=[MaxValueValidator(100),
            MinValueValidator(1)]) 
    stock_actual= models.IntegerField(validators=[MaxValueValidator(100),
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
    cantidad= models.IntegerField()
    subtotal= models.IntegerField()
    cod_producto= models.IntegerField()
    
    def __str__(self):
        return self.cantidad

    class Meta:
        db_table = 'CARRITO_COMPRAS'
        verbose_name = 'Carrito_Compras'
        verbose_name_plural = 'Carrito_Compras'
        ordering = ['id']
