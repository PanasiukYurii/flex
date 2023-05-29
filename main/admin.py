from django.contrib import admin
from main.models import Flex


# Register your models here.
class FlexAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Flex._meta.fields]
    fields = ["message"]

    class Meta:
        model = Flex


admin.site.register(Flex, FlexAdmin)
