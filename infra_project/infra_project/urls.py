from django.urls import include, path

from infra_project.infra_app import admin

urlpatterns = [
    path('', include('infra_app.urls', namespace='infra_app')),
    path('admin/', admin.site.urls),
]
