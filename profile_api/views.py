from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profile_api import serializer


class HelloApiView(APIView):
    serializer_class = serializer.HelloSerializer

    def get(self, request, format=None):
        return Response({'message': 'Hello!', 'api_apiview': []})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
