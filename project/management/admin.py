from ast import Pass
from django.db.models import Sum
from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Assign)
class AdminAssign(admin.ModelAdmin):
    list_display=[
        'sandogh_khayerieh',
        'khayer_full_name',
        'tahvilgirandeh',
        'date'
    ]
    def khayer_full_name(self,assign:models.Assign):
        return assign.sandogh_khayerieh.khayer.last_name+' '+assign.sandogh_khayerieh.khayer.first_name
    
    list_select_related=[
        'sandogh_khayerieh',
        'tahvilgirandeh',
        ]
    list_filter=[
        'sandogh_khayerieh',
        'tahvilgirandeh',
        'date'
    
        
    ]
    search_fields=[
        'sandogh_khayerieh__khayer__first_name',
        'sandogh_khayerieh__khayer__last_name',
        'sandogh_khayerieh__code',
        'tahvilgirandeh__first_name',
        'tahvilgirandeh__last_name',
    ]
    
@admin.register(models.Payment)
class AdminPayment(admin.ModelAdmin):
    list_display=['pk',
                  'khayer',
                  'sandogh_khayerieh',
                  'tahvilgirandeh_sandogh',
                  'amount',
                  'date'
                  ]
    search_fields=['pk',
                  'khayer__first_name',
                  'khayer__last_name',
                  'sandogh_khayerieh__code',
                  'tahvilgirandeh_sandogh__first_name',
                  'tahvilgirandeh_sandogh__last_name',
                  'amount',
                  ]
    #list_editable=['date']
    list_filter=[
        'id',
        'date',
        'khayer',
        'sandogh_khayerieh',
        'tahvilgirandeh_sandogh',
                ]
    ordering=['date']
    list_per_page=15

@admin.register(models.Khayer)
class AdminKhayer(admin.ModelAdmin):
    list_display=['pk',
                  'last_name',
                  'first_name',
                  'phone_number',
                  'sum_of_helps',
                  'creating_date'
                  ]
    search_fields=[
        'pk',
                  'last_name',
                  'first_name',
                  'phone_number',
    ]
    #list_editable=['first_name']
    #ordering=['']
    list_per_page=15

    def sum_of_helps(self,khayer):
        return khayer.sum_of_helps2
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            sum_of_helps2=Sum('payment__amount')
        )
    
@admin.register(models.HesabMoaseseh)
class AdminHesabMoaseseh(admin.ModelAdmin):
    list_display=['name',
                  'account_number',
                  'cart_number',
                  'sum_of_balance'
                  ]
    search_fields=['name']
    def sum_of_balance(self,hesab_moaseseh):
        if hesab_moaseseh.Pay != None and hesab_moaseseh.Recive !=None:
            return hesab_moaseseh.Recive -hesab_moaseseh.Pay
        if hesab_moaseseh.Pay == None:
            return (-1)*hesab_moaseseh.Recive
        return hesab_moaseseh.Pay
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            
            Recive=Sum('payment__amount'),
            Pay=Sum('helping__amount')
            
        )
        
    #list_editable=['']
    #ordering=['']
    list_per_page=15
    

@admin.register(models.Madadjo)
class AdminMadadjo(admin.ModelAdmin):
    list_display=['first_name',
                  'last_name',
                  'status',
                  'sum_of_helped_recived',
                  'creating_date'
                  ]
    search_fields=[
                'pk',
                'last_name',
                'first_name',
                'phone_number',
                'status',
    ]
    #list_editable=['']
    #ordering=['']
    list_per_page=15
    def sum_of_helped_recived(self,madadjo):
        return madadjo.sum
    def get_queryset(self, request):# set fillter for save or pay

        return super().get_queryset(request).annotate(
            sum=Sum('helping__amount')
        )
        
    #list_editable=['']
    #ordering=['']
    list_per_page=15
       

@admin.register(models.TahvilgirandehSandogh)
class AdminTahvilgirandehSandogh(admin.ModelAdmin):
    list_display=['first_name',
                  'last_name',
                  'phone_number'
                  ]
    search_fields=['first_name',
                  'last_name',
                  'phone_number'
                  ]
    #list_editable=['']
    #ordering=['']
    list_per_page=15

@admin.register(models.SandoghKhayerieh)
class AdminSandoghKhayerieh(admin.ModelAdmin):
    list_display=['pk',
                  'khayer'
                  ]
    search_fields=[
        'pk',
        'khayer__first_name',
        'khayer__last_name',
        ]
    #list_editable=['']
    #ordering=['']
    list_per_page=15

@admin.register(models.Helping)
class AdminHelping(admin.ModelAdmin):
    list_display=['madadjo',
                  'hesab_moaseseh',
                  'amount',
                  'date'
                  ]
    
    search_fields=['madadjo__first_name',
                   'madadjo__last_name',
                  'hesab_moaseseh__name',
                  'amount',
                  'date'
                  ]
    #list_editable=['']
    
    ordering=['date']
    list_per_page=15

