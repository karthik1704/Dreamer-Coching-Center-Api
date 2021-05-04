from django.contrib import admin


from materials.models import Material
# Register your models here.
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'tuition_class', 'file', 'created')

admin.site.register(Material, MaterialAdmin)