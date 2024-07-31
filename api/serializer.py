from rest_framework import serializers
from .models import File, Folder

class FileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = File
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        if 'http://localhost:8000/' in representation['file_c']:
            representation['file_c'] = representation['file_c'].replace('http://localhost:8000/', '', 1)
        
        return representation


class FileUpdateSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField()
    date = serializers.ReadOnlyField()

    class Meta:
        model = File
        fields = ['file_c', 'description', 'owner', 'date', 'folder']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        if 'http://localhost:8000/' in representation['file_c']:
            representation['file_c'] = representation['file_c'].replace('http://localhost:8000/', '', 1)

        return representation
    
    
class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = '__all__'


class MultipleFileUploadSerializer(serializers.Serializer):
    files = serializers.ListField(
        child=serializers.FileField(),
        allow_empty=False
    )
    owner = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=100)
    date = serializers.DateTimeField()
    folder = serializers.PrimaryKeyRelatedField(queryset=Folder.objects.all())

    