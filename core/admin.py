from django.contrib import admin
from . import models

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['job', 'customer', 'courier', 'amount', 'status', 'created_at']
    list_filter = ['status',]

    def customer(self, obj):
        return obj.job.customer

    def courier(self, obj):
        return obj.job.courier



admin.site.register(models.Customer)
admin.site.register(models.Courier)
admin.site.register(models.Category)
admin.site.register(models.Job)
admin.site.register(models.Transaction, TransactionAdmin)