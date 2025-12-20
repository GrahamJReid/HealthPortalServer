from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework import filters
from healthportalapi.models import PatientAllergyForm, User


class PatientAllergyFormView(ViewSet):
    """Patient Allergy Form view"""
    filter_backends = [filters.SearchFilter]

    def list(self, request):
        """Handle GET requests to get all allergy forms"""
        allergy_forms = PatientAllergyForm.objects.all()
        serializer = PatientAllergyFormSerializer(allergy_forms, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        """
        Retrieve a single allergy form by patient ID (instead of form PK)
        """
        try:
            allergy_form = PatientAllergyForm.objects.get(patient__id=pk)
            serializer = PatientAllergyFormSerializer(allergy_form)
            return Response(serializer.data)
        except PatientAllergyForm.DoesNotExist:
            return Response(
                {'message': 'Allergy form not found for this patient'},
                status=status.HTTP_404_NOT_FOUND
            )

    def create(self, request):
        patient = User.objects.get(pk=request.data["patient"])

        allergy_form = PatientAllergyForm.objects.create(
            patient=patient,
            pollen=request.data.get("pollen", False),
            pet=request.data.get("pet", False),
            mold=request.data.get("mold", False),
            milk=request.data.get("milk", False),
            eggs=request.data.get("eggs", False),
            nuts=request.data.get("nuts", False),
            shellfish=request.data.get("shellfish", False),
            insect=request.data.get("insect", False),
            medications=request.data.get("medications", False),
            latex=request.data.get("latex", False),
            other=request.data.get("other", "")
        )

        serializer = PatientAllergyFormSerializer(allergy_form)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        patient = User.objects.get(pk=request.data["patient"])
        allergy_form = PatientAllergyForm.objects.get(patient__id=pk)

        allergy_form.pollen = request.data.get("pollen", False)
        allergy_form.pet = request.data.get("pet", False)
        allergy_form.mold = request.data.get("mold", False)
        allergy_form.milk = request.data.get("milk", False)
        allergy_form.eggs = request.data.get("eggs", False)
        allergy_form.nuts = request.data.get("nuts", False)
        allergy_form.shellfish = request.data.get("shellfish", False)
        allergy_form.insect = request.data.get("insect", False)
        allergy_form.medications = request.data.get("medications", False)
        allergy_form.latex = request.data.get("latex", False)
        allergy_form.other = request.data.get("other", "")
        allergy_form.patient = patient

        allergy_form.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        allergy_form = PatientAllergyForm.objects.get(patient__id=pk)
        allergy_form.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class PatientAllergyFormSerializer(serializers.ModelSerializer):
    """JSON serializer for patient allergy forms"""
    class Meta:
        model = PatientAllergyForm
        fields = (
            'id',
            'patient',
            'pollen',
            'pet',
            'mold',
            'milk',
            'eggs',
            'nuts',
            'shellfish',
            'insect',
            'medications',
            'latex',
            'other'
        )
        depth = 1
