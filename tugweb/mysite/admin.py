from django.contrib import admin
from mysite.models import Weight,Loss,ImageModel  

#admin.site.register(Loss)
#admin.site.register(Weight)
admin.site.register(ImageModel)
admin.site.register(Loss)

class LossInline(admin.StackedInline):
    model = Loss
    extra = 2

class WeightAdmin(admin.ModelAdmin):
    fieldsets = [
        ('權重',    {'fields': ['weights']}),
    ]
    inlines = [LossInline]
    
admin.site.register(Weight,WeightAdmin)

# class LossAdmin(admin.ModelAdmin):
#     list_display=("id","weight","box_train_loss","box_value_loss",)
#      #fields = ("",) # 能讓人家填寫的格子(內容)

# admin.site.register(Loss, LossAdmin)
