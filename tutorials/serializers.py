from rest_framework import serializers 
from . import models
 
 
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = models.Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published')