from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from healthportalapi.models import DoctorPatient, User

class DoctorPatientView(ViewSet):
    """TimelineEvent view"""
    
    def list(self, request):
        """Handle GET requests to get all timeline events
        Returns:
            Response -- JSON serialized list of timeline events
        """
        doctor_patient = DoctorPatient.objects.all()
        serializer = DoctorPatientSerializer(doctor_patient, many=True)
        return Response(serializer.data)
      
    def retrieve(self, request, pk):
        try:
            timeline_event = DoctorPatient.objects.get(pk=pk)
            serializer = DoctorPatientSerializer(timeline_event)
            return Response(serializer.data)
        except DoctorPatient.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
          
    def create(self, request):
        doctor = User.objects.get(pk=request.data["doctor"])
        patient = User.objects.get(pk=request.data["patient"])
        doctorpatient = DoctorPatient.objects.create(
            doctor=doctor,
            patient=patient
        )
        serializer = DoctorPatientSerializer(doctorpatient)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def destroy(self, request, pk):
        doctorpatient = DoctorPatient.objects.get(pk=pk)
        doctorpatient.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)      

class DoctorPatientSerializer(serializers.ModelSerializer):
    """JSON serializer for timeline events"""
    class Meta:
        model = DoctorPatient
        fields = ('id', 'doctor', 'patient')
        depth = 1