# from django.conf.urls import url
from students import views
# from .views import CRUD
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[

    path('CRUD',views.studentApi),
    # path('CRUD',CRUD.as_view()),
    # url(r'^student/([0-9]+)$',views.studentApi),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


