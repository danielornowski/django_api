from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import ProjectModelSerializer, CommentModelSerializer
from .models import Project, Comment
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

# Projects and Comment section

@api_view(['GET'])
def getRoutes(request):
    routes = [

    ]
    return Response(routes)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProjects(request):

    projects = Project.objects.all()
    serializer = ProjectModelSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProject(request, pk):
    projects = Project.objects.get(id=pk)
    serializer = ProjectModelSerializer(projects, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createProject(request):
    data = request.data
    if 'end_date' in data:
        project = Project.objects.create(
            name=data['name'],
            created=data['created'],
            end_date=data['end_date'],
            status=data['status']
        )
    else:
        project = Project.objects.create(
            name=data['name'],
            created=data['created'],
            status=data['status']
        )
    serializer = ProjectModelSerializer(project, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateProject(request, pk):
    data = request.data
    project = Project.objects.get(id=pk)
    # serializer = ProjectModelSerializer(instance=projects, data=data)

    # if serializer.is_valid():
    #    serializer.save()

    project.name = data['name']
    project.status = data['status']
    project.created = data['created']
    project.end_date = data['end_date']

    project.save()

    return Response(data)


@api_view(['DELETE'])
def deleteProject(request, pk):
    projects = Project.objects.get(id=pk)
    projects.delete()
    return Response('Project DELETE')


@api_view(['GET'])
def getComments(request, pk):
    try:
        comment = Comment.objects.all().filter(project_id=pk)
        serializer = CommentModelSerializer(comment, many=True)
        return Response(serializer.data)
    except Comment.DoesNotExist:
        return Response()


@api_view(['POST'])
def createComment(request, pk):
    data = request.data
    comment = Comment.objects.create(
        project_id=Project.objects.get(id=pk),
        author='admin',
        body=data['comment']
    )
    serializer = CommentModelSerializer(comment, many=False)
    return Response(serializer.data)
