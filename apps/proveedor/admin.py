from django.contrib import admin
from djangoql.admin import DjangoQLSearchMixin
from import_export.admin import ExportActionMixin

from apps.proveedor.models import Proveedor, Responsable, Placa, \
	Material, Compania


@admin.register(Proveedor)
class ProveedorAdmin(DjangoQLSearchMixin, ExportActionMixin, admin.ModelAdmin):
	djangoql_completion_enabled_by_default = False
	# Sección de años de registros mostrados arriba de la tabla:
	date_hierarchy = 'entrada'
	ordering = ['-entrada']
	empty_value_display = ' - Vacío - '
	list_display = (
		'entrada',
		'operador',
		'compania',
		'material',
		'placa',
		'hora_inicio_descarga',
		'hora_salida',
		'observaciones',
		'programado',
		'recibido',
		# 'colored_name'
		'tiempo_estancia'
	)
	search_fields = (
		# 'entrada',
		'operador__icontains',
		'compania__nombre__icontains',
		'material__nombre__icontains',
		'placa__placa__icontains',
		# 'hora_inicio_descarga',
		# 'hora_salida',
		# tiempo_estancia
		'observaciones__icontains',
		'responsable__nombre__icontains',
		'programado__icontains',
		'recibido__nombre__icontains',
	)
	autocomplete_fields = [
		'material',
		'compania',
		'placa',
		'responsable',
		'recibido'
		]
	list_per_page = 150

	def get_search_results(self, request, queryset, search_term):
		# print("In get search results")
		results = super().get_search_results(request, queryset, search_term)
		return results

	"""def time_seconds(self, obj):
		return obj.entrada.time().strftime("%H:%M:%S %p")
	time_seconds.short_description = 'Precise Time'"""

@admin.register(Compania)
class CompaniaAdmin(admin.ModelAdmin):
	empty_value_display = ' - Vacío - '
	list_display = ('nombre',)
	search_fields = ('nombre',)

@admin.register(Responsable)
class ResponsableAdmin(admin.ModelAdmin):
	empty_value_display = ' - Vacío - '
	list_display = ('nombre',)
	search_fields = ('nombre',)

@admin.register(Placa)
class PlacaAdmin(admin.ModelAdmin):

	empty_value_display = ' - Vacío - '
	list_display = ('placa',)
	search_fields = ('placa',)

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):

	empty_value_display = ' - Vacío - '
	list_display = ('nombre',)
	search_fields = ('nombre',)
