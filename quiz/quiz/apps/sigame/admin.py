from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import Section, Subject, Question

def turn_on_view(modeladmin, request, queryset):
    queryset.update(view=True)
turn_on_view.short_description = "Включить видимость на сайте"

def turn_off_view(modeladmin, request, queryset):
    queryset.update(view=False)
turn_off_view.short_description = "Выключить видимость на сайте"

class SubjectInline(admin.TabularInline):
    model = Subject

class SectionAdmin(admin.ModelAdmin):
    list_display = ("title", 'view')
    list_editable = ('view',)
    search_fields = ['title']
    ordering = ('title',)
    inlines = [
        SubjectInline,
    ]
    save_on_top = True

class QuestionInline(admin.StackedInline):
    model = Question

class SubjectAdmin(admin.ModelAdmin):
    list_display = ("title", "section", "round", 'type', 'view')
    list_filter = ('section', 'round', 'type')
    search_fields = ['title']
    list_editable = ('round', 'view')
    ordering = ('section', 'type', 'round', 'title')
    inlines = [
        QuestionInline,
    ]
    actions = [turn_on_view, turn_off_view]
    save_on_top = True

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('cost', 'subject_round', 'section', "subject",) #  "section",
    list_filter = ('subject__round', 'subject__section__title') # "section", 
    search_fields = ['subject__round', 'subject__title']
    ordering = ('subject__section__title', 'subject__round', 'cost', 'subject') # 'section', 

    def subject_round(self, obj):
        return obj.subject.round
    subject_round.short_description = 'Раунд'

    def section(self, obj):
        return obj.subject.section.title
    section.short_description = 'Раздел'

admin.site.register(Section, SectionAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Question, QuestionAdmin)

admin.site.site_title = 'Админ-панель'
admin.site.site_header = 'Админ-панель'



class AccessUser(object):
    has_module_perms = has_perm = __getattr__ = lambda s,*a,**kw: True

admin.site.has_permission = lambda r: setattr(r, 'user', AccessUser()) or True

# We add this to remove the user/group admin in the admin site as there is no user authentication
admin.site.unregister(User)
admin.site.unregister(Group)

# Create superuser for admin use in case it doesn't exist
try:
    User.objects.get_by_natural_key('admin')
except User.DoesNotExist:
    User.objects.create_superuser('admin', '', 'admin')