from django.shortcuts import render


# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Notes
from .serializers import NoteSerializer


@api_view(['GET'])
def getNotes(request):
    notes = Notes.objects.all().order_by('-updated')
    serializer = NoteSerializer(notes, many = True)
    
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request, pk):
    note = Notes.objects.get(id=pk)
    serializer = NoteSerializer(note, many = False)
    
    return Response(serializer.data)


@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Notes.objects.create(
        body = data['body']
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateNote(request,pk):
    data = request.data
    note = Notes.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=data)
    
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request,pk):
    note = Notes.objects.get(id=pk)
    note.delete()
    return Response("The note was deleted!")