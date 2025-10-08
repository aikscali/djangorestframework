from rest_framework import routers
from .api import ProjectsViewSet

routers = routers.DefaultRouter()
routers.register('api/projects', ProjectsViewSet, 'projects')

urlpatterns = routers.urls # Exportar las URLs del router, se generan automáticamente las rutas del crud