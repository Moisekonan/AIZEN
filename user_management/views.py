from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class MeViewSet(viewsets.ViewSet):
    
    permission_classes = (IsAuthenticated,)
    
    @swagger_auto_schema(
        operation_description="Obtenir le profil de l'utilisateur actuel",
        responses={
            200: UserSerializer
            # 400: "Mauvaise requête"
        }    
    )
    
    def list(self, request):
        user = User.objects.get(username=request.user)
        user_data = UserSerializer(user).data
        return Response(user_data)