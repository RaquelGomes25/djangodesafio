from django.contrib import admin
from .models import Usuario, Livro
from django.contrib.admin.filters import SimpleListFilter

# Register your models here.

class CustomFilter(SimpleListFilter):  # filtro do django
    title = "Filtro customizado" #titulo do filtro do django
    parameter_name = "custom" # vai aparecer na url
    def lookups(self, request, model_admin):
        return(
            ("value_01", "value 01"), #filtro passado e filtro que aparece
            ("value_02", "value 02"), #filtro passado e filtro que aparece
            ("value_03", "value 03"), #filtro passado e filtro que aparece
        )
    def queryset(self, request, queryset): #classe obrigatoria para filtros customizados
        if self.value() == "value_01":
            queryset = queryset.order_by("titulo") #criar a ordenação
        elif self.value() == "value_02":
            queryset = queryset.order_by("autor")
        return queryset
    
class LivroAdmin(admin.ModelAdmin):
    list_filter = ["titulo", CustomFilter]
    search_fields = ['titulo', 'autor']


admin.site.register(Usuario)
admin.site.register(Livro, LivroAdmin) #acrescenta a classe pra chamar 


