from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from healthportalapi.models import PatientIntakeForm

@csrf_exempt
def get_patient_intake_form(request, patient_id):
    if request.method == "GET":
        try:
            # Filter the form by patient ID
            intake_form = PatientIntakeForm.objects.filter(patient__id=patient_id).first()
            if intake_form:
                # Serialize the data to return JSON
                response = {
                    "id": intake_form.id,
                    "name": intake_form.name,
                    "date": intake_form.date,
                    "email": intake_form.email,
                    "address": intake_form.address,
                    "city": intake_form.city,
                    "state": intake_form.state,
                    "zip": intake_form.zip,
                    "phonenumber": intake_form.phonenumber,
                    "sex": intake_form.sex,
                    "birthdate": intake_form.birthdate,
                    "socialsecurity": intake_form.socialsecurity,
                    "emergencycontactname": intake_form.emergencycontactname,
                    "emergencycontactphone": intake_form.emergencycontactphone,
                    "patient": {
                        "id": intake_form.patient.id,
                        "username": intake_form.patient.username,  # Replace name with username
                    },
                }
                return JsonResponse(response, safe=False)
            else:
                return JsonResponse({"message": "No intake form found for the patient"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request method"}, status=405)
