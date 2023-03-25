# from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .models import Ticket
from .serializer import TicketSerializer,TicketCreateSerializer
from rest_framework.response import Response




class CreateTicket(APIView):
    def post(self, request):
        serializer = TicketCreateSerializer(data=request.data)
        print(serializer.is_valid)
        if serializer.is_valid():
            return Response(serializer.data, status=400)


        return Response("Invalid request", status=400)


    
class TicketList(ListAPIView):
    serializer_class=TicketSerializer
    queryset = Ticket.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        serializer = TicketSerializer(queryset, many=True)
        return Response(serializer.data)