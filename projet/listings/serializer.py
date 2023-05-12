from rest_framework.serializers import ModelSerializer
from listings.models import Domain

class DomainSerializer(ModelSerializer):
    class Meta:
        model= Domain
        fields=['permutation']