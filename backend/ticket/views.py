# from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .models import Ticket
from contact.models import Contact,Status
from .serializer import TicketSerializer,TicketCreateSerializer
from rest_framework.response import Response
from email_configure.models import OutgoingEmailServer
import smtplib
from email.message import EmailMessage
from django.db import IntegrityError
import datetime
import pytz


def creation_email_ticket(EMAIL_TO):
    email_configure = OutgoingEmailServer.objects.all().first()
    EMAIL_ADDRESS = email_configure.email_address
    EMAIL_PASS =  email_configure.email_password
    msg = EmailMessage()
    print()
    msg['Subject'] = 'Grab Dinner this weekend'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] =EMAIL_TO
    html_msg = "<br> <b><u> This is the Text .... </u></b><br>"
    msg.add_alternative(html_msg, subtype="html")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASS)
        smtp.send_message(msg)


class CreateTicket(APIView):
    def post(self, request):
        serializer = TicketCreateSerializer(data=request.data)

        if serializer.is_valid():
            try :
                state_id = Status.objects.get(name="New")
                contact,var =Contact.objects.get_or_create(name=serializer.data['name'],email=serializer.data['email'],
                                                           phone =serializer.data['phone']

                                                           )
                Ticket.objects.create(contact_id=contact,query=serializer.data['query'],state_id=state_id)
                creation_email_ticket(contact.email)
                return Response(serializer.data, status=400)

            except IntegrityError as e:
                contacts = Contact.objects.get(email=serializer.data['email'])
                creation_email_ticket(contacts.email)
                return Response(serializer.data, status=400)


            return Response(serializer.data, status=400)


        return Response("Invalid request", status=404)
    def put(self, request):

         id =request.data['id']
         message = request.data['message']
         ticket = Ticket.objects.get(id=id)
         if ticket.closed:
             return Response("Ticket is closed", status=400)

         else:
             message_id = ticket.message_ids.create(
                 name=request.user.username if request.user.id else ticket.contact_id.name,
                 message=message)
             ticket.message_ids.add(message_id)
             ticket.save()
             return Response("Created Successfull", status=400)





    
class TicketList(ListAPIView):
    serializer_class=TicketSerializer
    queryset = Ticket.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        serializer = TicketSerializer(queryset, many=True)
        return Response(serializer.data)

class TicketClientList(ListAPIView):
    serializer_class=TicketSerializer
    queryset = Ticket.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        queryset=queryset.filter(id=request.GET.get('id'))
        serializer = TicketSerializer(queryset, many=True)
        return Response(serializer.data)
class CloseTicket(APIView):
    def put(self, request):

        id = request.data['id']
        ticket = Ticket.objects.get(id=id)
        ticket.created_rating = datetime.datetime.now()
        if  not ticket.closed:
            message_id = ticket.message_ids.create(
                name=request.user.username if request.user.id else ticket.contact_id.name,
                message="Closed the Ticket")
            ticket.message_ids.add(message_id)
            ticket.closed = True

            ticket.save()
        return Response("Created Successfull", status=400)

class RatingTicket(APIView):
    def put(self, request):
        id = request.data['id']
        rating = request.data['rating']

        ticket = Ticket.objects.get(id=id)
        if ticket.is_expired:
            return Response("The Link Expired", status=400)
        else:
            message_id = ticket.message_ids.create(
                    name=request.user.username if request.user.id else ticket.contact_id.name,
                    message="Rated the Ticket as "+rating)
            ticket.message_ids.add(message_id)
            ticket.is_expired = True
            ticket.custom_rate = rating

            ticket.save()
            return Response("Created Successfull", status=400)

    def get(self, request):
        id = request.GET.get('id')
        ticket = Ticket.objects.get(id=id)
        max = ticket.created_rating+datetime.timedelta(minutes=30)


        ticket.last_visited = datetime.datetime.now()
        ticket.save()
        ticket = Ticket.objects.get(id=id)

        if max>ticket.last_visited:
            ticket.is_expired = False
        else:
            ticket.is_expired = True
        return Response(not ticket.is_expired)





