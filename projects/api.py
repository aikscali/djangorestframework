from .models import Projects
from rest_framework import viewsets, permissions
from .serializers import ProjectsSerializer

class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    permission_classes = [permissions.AllowAny] # Permitir acceso público, se puede ajustar según necesidades
    serializer_class = ProjectsSerializer