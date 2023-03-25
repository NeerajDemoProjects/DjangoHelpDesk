# from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Ticket
from .serializer import TicketSerializer
from rest_framework.response import Response



class TicketList(ListAPIView):
    serializer_class=TicketSerializer
    queryset = Ticket.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        serializer = TicketSerializer(queryset, many=True)
        return Response(serializer.data)