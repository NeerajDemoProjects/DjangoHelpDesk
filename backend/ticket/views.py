# from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .models import Ticket
from contact.models import Contact,Status
from .serializer import TicketSerializer,TicketCreateSerializer
from rest_framework.response import Response




class CreateTicket(APIView):
    def post(self, request):
        serializer = TicketCreateSerializer(data=request.data)
        print(serializer.is_valid)

        if serializer.is_valid():
            state_id = Status.objects.get(name="New")
            contact,var =Contact.objects.get_or_create(name=serializer.data['name'])
            Ticket.objects.create(contact_id=contact,query=serializer.data['query'],state_id=state_id)
            return Response(serializer.data, status=400)


        return Response("Invalid request", status=404)


    
class TicketList(ListAPIView):
    serializer_class=TicketSerializer
    queryset = Ticket.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        serializer = TicketSerializer(queryset, many=True)
        return Response(serializer.data)