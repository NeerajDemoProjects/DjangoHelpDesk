from rest_framework import serializers
from .models import Ticket
from contact.models import Status,Contact
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    contact_id = ContactSerializer()
    state_id = StateSerializer()
    class Meta:
        model = Ticket
        fields = "__all__"

class TicketCreateSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=30)
        