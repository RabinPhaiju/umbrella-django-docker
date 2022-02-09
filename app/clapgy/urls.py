from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("upload/", include('upload.urls')),
    path("admin/", admin.site.urls),
    path("user/",include('contrib.user.urls')),
    path("partner/",include('contrib.partner.urls')),
    path("company/",include('contrib.company.urls')),
    path("role/",include('contrib.role.urls')),
    path("daybook/",include('contrib.daybook.urls')),
    path("product/",include('contrib.product.urls')),
    path("daybook_line/",include('contrib.daybook_line.urls')),
    path("daybook_type/",include('contrib.daybook_type.urls')),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
