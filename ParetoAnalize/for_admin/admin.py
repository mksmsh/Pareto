from django.contrib import admin
from .models import MarketPlace, ModelWork, MethodofExport, TariffTranslate, Category, CategoryYM, CategoryOZ, CategorySBR


class MethodofExportAdmin(admin.ModelAdmin):
    list_display = ('nameME', 'mp', 'mw', 'cost')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'mp':
            # Ограничиваем выбор маркетплейсов только теми, которые существуют
            kwargs['queryset'] = MarketPlace.objects.all()
        elif db_field.name == 'mw':
            print('Зашли в условие')
            # Ограничиваем выбор моделей работ только теми, которые привязаны к выбранному маркетплейсу
            mp_id = request.POST.get('mp')  # Получаем ID выбранного маркетплейса из POST-запроса
            if mp_id:
                kwargs['queryset'] = ModelWork.objects.filter(mp_id=mp_id)
            else:
                kwargs['queryset'] = ModelWork.objects.none()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(MarketPlace)
admin.site.register(ModelWork)
admin.site.register(MethodofExport, MethodofExportAdmin)
admin.site.register(TariffTranslate)
admin.site.register(Category)
admin.site.register(CategoryYM)
admin.site.register(CategoryOZ)
admin.site.register(CategorySBR)