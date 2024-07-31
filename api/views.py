from rest_framework import viewsets, status
from .serializer import FileUpdateSerializer, FileSerializer, FolderSerializer, MultipleFileUploadSerializer
from .models import File, Folder
from rest_framework.parsers import MultiPartParser, FormParser
from .handle.response import custom_response  
from rest_framework.response import Response
from rest_framework.views import APIView
import os


class FileUploadView(APIView):
    def post(self, request, *args, **kwargs):
        folder_id = request.data.get('folder')
        try:
            folder = Folder.objects.get(id=folder_id)
        except Folder.DoesNotExist:
            return Response(f'Folder with id {folder_id} does not exist', status=status.HTTP_400_BAD_REQUEST)
        
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UploadFolderView(APIView):
    def post(self, request, *args, **kwargs):
        folder = request.FILES.get('folder')

        new_folder = Folder.objects.create(name=folder.name)

        for file_item in os.listdir(folder.temporary_file_path()):
            with open(os.path.join(folder.temporary_file_path(), file_item), 'rb') as file:
                new_file = File(file_c=file, owner=request.user.username, description="Descripción del archivo")
                new_file.folder = new_folder
                new_file.save()

        return Response({'message': 'Carpeta y archivos guardados correctamente'})



class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    parser_classes = (MultiPartParser, FormParser)

    def get_serializer_class(self):
        if self.action == 'update':
            return FileUpdateSerializer
        return FileSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        
        if serializer.is_valid():
            serializer.save()
            return custom_response(data=serializer.data, message="Archivo actualizado correctamente.")

        return custom_response(message="Error al actualizar el archivo.", status_code=status.HTTP_400_BAD_REQUEST)
    

    def upload_multiple_files(self, request):
        serializer = MultipleFileUploadSerializer(data=request.data)
        if serializer.is_valid():
            files = serializer.validated_data['files']
            for file in files:
                File.objects.create(
                    file_c=file,
                    owner=serializer.validated_data['owner'],
                    description=serializer.validated_data['description'],
                    date=serializer.validated_data['date'],
                    folder=serializer.validated_data['folder']
                )
            return Response({"message": "Files uploaded successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class FolderViewSet(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

    def list(self, request, *args, **kwargs):
        parent_id = request.query_params.get('parent', None)
        if parent_id is not None:
            folders = Folder.objects.filter(parent_id=parent_id)
        else:
            folders = Folder.objects.filter(parent__isnull=True)
        serializer = self.get_serializer(folders, many=True)
        return Response(serializer.data)
    



