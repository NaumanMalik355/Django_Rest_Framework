from .models import Consumo
from rest_framework import serializers
class consumoSerializers(serializers.ModelSerializer):
    class Meta:
        model=Consumo
        #fields=('x','consumo_r','consumo_s')
        fields='__all__'