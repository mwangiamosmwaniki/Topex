from django.urls import path
from topex_school import settings
from . import views
from django.conf.urls.static import static

app_name = 'academics'

urlpatterns = [
    path('departments/', views.department_list, name='department_list'),
    path('program/<int:program_id>/', views.program_detail, name='program_detail'),
    path('unit/<int:unit_id>/', views.unit_detail, name='unit_detail'),
    path('my-units/', views.enrolled_units, name='enrolled_units'),
    path('search-units/', views.unit_search, name='unit_search'),
    path('units/<int:unit_id>/unenroll/', views.unenroll_from_unit, name='unenroll_from_unit'),
    path('unit/enroll/<int:unit_id>/', views.enroll_in_unit, name='enroll_in_unit'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)