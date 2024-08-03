from django.contrib import admin
from .models import Product

# para administrar mejor los modelos
#@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # para que salga todo esto en el panel
    list_display = ('name', 'short_description', 'stock')
    # para agregar un buscador
    search_fields = ('name', 'short_description')
    # para añadir filtros
    list_filter = ('name', 'stock')
    # gerarquia de fechas
    date_hierarchy = 'discount_until'
    


# para registrar el modelo y salga en el panel de admin
admin.site.register(Product, ProductAdmin)

    
