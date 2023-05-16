from django.contrib import admin
from django.urls import path
from myapp import views  
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('announcements/', views.announcements, name='announcements'),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  
    path('addnew/',views.addnew, name='addnew'),  
    path('edit/<int:id>', views.edit, name='edit'),  
    path('update/<int:id>', views.update, name='update'),  
    path('delete/<int:id>', views.destroy, name='destroy'),  
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)