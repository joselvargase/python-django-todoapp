from rest_framework.reverse import reverse_lazy
from rest_framework import serializers
from Experimento_1.models import Todos
from pprint import pprint


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.SerializerMethodField('get_self')

    def get_self(self, obj):

        request = self.context.get('request')
        return reverse_lazy('Experimento_1:details', kwargs={'pk': obj.id}, request=request)

    class Meta:
        model = Todos
        fields = ('id', 'title', 'completed', 'order', 'url')
