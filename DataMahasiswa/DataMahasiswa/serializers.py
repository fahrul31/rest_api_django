from rest_framework import serializers
from DataMahasiswa.models import Data

class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data
        fields = ['name', 'nim', 'jurusan']
