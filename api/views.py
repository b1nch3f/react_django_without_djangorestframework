from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status

class IndexView(APIView):  
  
    def get(self, request, *args, **kwargs):  
        result = {"name": "max"} 
        return Response({'status': 'success', "data":result}, status=200) 
