# from django.contrib import admin
#系统包
from xadmin import views
import xadmin #第三方模块
from art.models import Tag, Art ,Category,RollSet,Chapter # 自定义的模块
# Register your models here.
#设置admin站点样式
class BaseSettings:
    enable_themes = True
    use_bootswatch = True

class GlobalSettings:
    site_title = '创意小说'
    site_footer = '西安大将军府<h5>联系方式：15051332561</h5>'
    menu_style = 'accordion'
    apps_label_title = {
        'art':'文章管理'
    }
    apps_icons = {
        'art':'glyphicon glyphicon-book'
    }
    global_models_icon = {
        Tag:'fa fa-cloud'
    }
    #global_search_models = [Tag]

xadmin.site.register(views.BaseAdminView,BaseSettings)
xadmin.site.register(views.CommAdminView,GlobalSettings)
class TagAdmin:
    list_display = ['name', 'describe', 'add_time']
    search_fields = ['name', 'describe']
    list_per_page = 10
class ArtAdmin:
    list_display = ['title', 'content', 'author','publish_date']
    search_fields = ['title', 'author']
    list_per_page = 10
class CategoryAdmin:
    list_display = ['title','add_time']
    search_fields = ['title', 'add_time']
    list_per_page = 10
class RollSetAdmin:
    list_display = ['name', 'free', 'art']
    search_fields = ['name', 'free']
    list_per_page = 10
class ChapterAdmin:
    list_display = ['name','content','publish_date','rool']
    search_fields = ['name', 'publish_date']
    style_fields = {'content':'ueditor'}
    list_per_page = 10
xadmin.site.register(Tag,TagAdmin)
xadmin.site.register(Art,ArtAdmin)
xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(RollSet,RollSetAdmin)
xadmin.site.register(Chapter,ChapterAdmin)