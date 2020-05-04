
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import State, Township
from .serializers import StateSerializer, TownSerializer

# Create your views here.


class StateView(APIView):

    def post(self, request):
        data = request.data
        serializer = StateSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        state = State.objects.all()
        serializer = StateSerializer(state, many=True)
        return Response(serializer.data)


class TownshipView(APIView):
    def post(self, request, state_id):
        state_id = State.objects.get(pk=state_id)
        data = request.data
        serializer = TownSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, state_id):
        # state_id = State.objects.get(pk=state_id)
        town = Township.objects.filter(state=state_id)
        serializer = TownSerializer(town, many=True)
        return Response(serializer.data)




























































































# if request.POST['file-format']:
#     state_resource = StateResource()
#     dataset = state_resource.export()
#     response = HttpResponse(dataset.json, content_type='application/json')
