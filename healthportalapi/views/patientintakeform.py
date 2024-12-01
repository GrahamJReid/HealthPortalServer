from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from healthportalapi.models import PatientIntakeForm, User
from rest_framework import filters

class PatientIntakeFormView(ViewSet):
    """Timeline view"""
    filter_backends = [filters.SearchFilter]
    search_fields = ['title',]
    
    
    def list(self, request):
        """Handle GET requests to get all timelines
        Returns:
            Response -- JSON serialized list of timelines
        """
        patientintakeform = PatientIntakeForm.objects.all()
        serializer = PatientIntakeFormSerializer(patientintakeform, many=True)
        return Response(serializer.data)
      
    def retrieve(self, request, pk):
        try:
            patientintakeform = PatientIntakeForm.objects.get(pk=pk)
            serializer = PatientIntakeFormSerializer(patientintakeform)
            return Response(serializer.data)
        except PatientIntakeForm.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
          
    def create(self, request):
        patient = User.objects.get(pk=request.data["patient"])  # Assuming user_id is provided in the request data
        patientintakeform = PatientIntakeForm.objects.create(
            patient=patient,
            name=request.data["name"],
            date=request.data["date"],
            email=request.data["email"],
            address=request.data["address"],
            city=request.data["city"],
            state=request.data["state"],
            zip=request.data["zip"],
            phonenumber=request.data["phonenumber"],
            sex=request.data["sex"],
            birthdate=request.data["birthdate"],
            socialsecurity=request.data["socialsecurity"],
            emergencycontactname=request.data["emergencycontactname"],
            emergencycontactphone=request.data["emergencycontactphone"]
            
        )
        serializer = PatientIntakeFormSerializer(patientintakeform)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def update(self, request, pk):
        patient = User.objects.get(pk=request.data["patient"])
        patientintakeform = PatientIntakeForm.objects.get(pk=pk)
        patientintakeform.name = request.data["name"]
        patientintakeform.date = request.data["date"]
        patientintakeform.email= request.data["email"]
        patientintakeform.address = request.data["address"]
        patientintakeform.city = request.data["city"]
        patientintakeform.state = request.data["state"]
        patientintakeform.zip= request.data["zip"]
        patientintakeform.phonenumber = request.data["phonenumber"]
        patientintakeform.sex = request.data["sex"]
        patientintakeform.birthdate= request.data["birthdate"]
        patientintakeform.socialsecurity = request.data["socialsecurity"]
        patientintakeform.emergencycontactname = request.data["emergencycontactname"]
        patientintakeform.emergencycontactphone = request.data["emergencycontactphone"]
        patientintakeform.patient=patient
        
        patientintakeform.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        patientintakeform = PatientIntakeForm.objects.get(pk=pk)
        patientintakeform.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)      

class PatientIntakeFormSerializer(serializers.ModelSerializer):
    """JSON serializer for timelines"""
    class Meta:
        model = PatientIntakeForm
        fields = ('id', 'patient', 'name', 'date', 'email', 'address', 'city', 'state', 'zip', 'phonenumber', 'sex', 'birthdate','socialsecurity', 'emergencycontactname', 'emergencycontactphone')
        depth =1
