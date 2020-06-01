from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include, re_path
from django.views.generic import TemplateView

admin.site.site_header = 'Agro weather admin'
admin.site.site_title = 'Agro weather admin'
admin.site.site_url = 'http://Agro_admin.com/'
admin.site.index_title = 'Agro weather Admin'

urlpatterns = [
    path('admin', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('users/', include('users.urls')),
    path('', include('Faq.urls')),
    path('', include('Farmer.urls')),
    path('', include('Feedback.urls')),
    re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]
