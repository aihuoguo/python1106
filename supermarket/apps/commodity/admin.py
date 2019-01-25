from django.contrib import admin

# Register your models here.
from commodity.models import GoodsType, GoodsSPU, Unit, GoodsSKU, GoodsPhoto, Carousel, Activity, Activity_Area


# 商品类型管理

#
# admin.site.register(GoodsSPU)
# admin.site.register(Unit)
#
# admin.site.register(GoodsSKU)
#
#
#
#
# admin.site.register(GoodsPhoto)
# admin.site.register(Carousel)
# admin.site.register(Activity)
admin.site.register(Activity_Area)


# 商品类型表
@admin.register(GoodsType)
class GoodsTypeAdmin(admin.ModelAdmin):
    # 自定义后台
    list_display = ['id', 'type_name', 'sort_detail', 'order', 'update_time']
    list_display_links = ['id', 'type_name', 'sort_detail']

#单位表
@admin.register(Unit)
class UnitSKUAdmin(admin.ModelAdmin):
    list_display = ['id','unit_name']

#商品SPU表
@admin.register(GoodsSPU)
class GoodsSPUSKUAdmin(admin.ModelAdmin):
    list_display = ['id','spu_name','spu_detail']


class GoodsPhotoInline(admin.TabularInline):
    model = GoodsPhoto
    extra = 2


# 商品SKU表
@admin.register(GoodsSKU)
class GoodsSKUAdmin(admin.ModelAdmin):
    list_display = ["id", 'sku_name', 'price', 'unit', 'stock', 'sales_val', 'is_on_sale', 'goods_type']
    list_display_links = ["id", 'sku_name', 'price']

    search_fields = ['sku_name', 'price', 'sales_val']
    inlines = [
        GoodsPhotoInline,
    ]


#商品图片轮播表
@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ['id','name','img_url','order','goods_sku']

# 商品相册表
@admin.register(GoodsPhoto)
class GoodsPhotoAdmin(admin.ModelAdmin):
    list_display = ['id','img_url','goods_sku']


#首页活动表
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['id','act_name','img_url','url_address']

# #活动专区表
# @admin.register(Activity_Area)
# class Activity_AreaAdmin(admin.ModelAdmin):
#     list_display = ['id','name','describe','is_on_sale','goods_sku']