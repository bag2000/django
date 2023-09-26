from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Measurement, Sensor
from django.forms import model_to_dict
from .serializers import SensorSerializer, MeasurementSerializer


class Sens(APIView):
    def get(self, request, pk=''):
        """получение датчиков"""
        if pk == '':
            sensors = Sensor.objects.all()
            ser = SensorSerializer(sensors, many=True)
            return Response(ser.data)
        else:
            sensor_found = Sensor.objects.get(id__exact=pk)
            measures = Measurement.objects.filter(sensor=sensor_found)
            response = model_to_dict(sensor_found)
            response['measurements'] = [model_to_dict(measure) for measure in measures]
            return Response(response)

    def post(self, request):
        """создание датчика"""
        post_new = Sensor.objects.create(
            name=request.data['name'],
            description=request.data['description'],
        )

    def patch(self, request, pk):
        """обновление датчика"""
        patch_update = Sensor.objects.get(id__exact=pk)
        if 'name' in request.data:
            patch_update.name = request.data['name']

        if 'description' in request.data:
            patch_update.description = request.data['description']
        patch_update.save()


class Measur(APIView):
    def post(self, request):
        '''добавление измерения'''
        post_new = Measurement.objects.create(
            sensor=Sensor.objects.get(id__exact=request.data['sensor']),
            temperature=request.data['temperature'],
        )
