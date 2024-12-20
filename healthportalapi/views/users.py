"""View module for handling requests about categories"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from healthportalapi.models import User
from rest_framework import filters

class UserView(ViewSet):
    """Rare Users view"""
    filter_backends = [filters.SearchFilter]
    search_fields = ['username','role']
    
    def list(self, request):
        """Handle GET requests to get all users
        Returns:
            Response -- JSON serialized list of users
        """
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
      
    def retrieve(self, request, pk):
      try:
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
      except User.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
          
    def update(self, request, pk):
        user = User.objects.get(pk=pk)
        user.username = request.data["username"]
        user.email=request.data["email"]
        user.image_url=request.data["image_url"]
        user.uid = request.data["uid"]
        user.role = request.data["role"]
        user.admin = request.data["admin"]
        
        user.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    def destroy(self, request, pk):
        order = User.objects.get(pk=pk)
        order.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)      
    
class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for categories
    """
    class Meta:
        model = User
        fields = ('id', 'username','email', 'image_url', 'uid','role','admin')
        depth = 1