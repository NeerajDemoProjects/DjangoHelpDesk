from rest_framework import serializers
from .models import Ticket
from  email_configure.models import Message
from contact.models import Status,Contact
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    contact_id = ContactSerializer()
    state_id = StateSerializer()
    message_ids = MessageSerializer()
    class Meta:
        model = Ticket
        fields = "__all__"


class TicketCreateSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=30)
        phone = serializers.CharField(max_length=30)
        email = serializers.EmailField(max_length=30)
        query = serializers.CharField(max_length=30)
