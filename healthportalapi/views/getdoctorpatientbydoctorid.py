from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from healthportalapi.models import DoctorPatient

@csrf_exempt
def get_doctor_patient_by_doctor_id(request, doctor_id):
    if request.method == "GET":
        try:
            # Filter DoctorPatient records by doctor_id
            doctor_patients = DoctorPatient.objects.filter(doctor__id=doctor_id)
            
            # If no records are found, return 404
            if not doctor_patients.exists():
                return JsonResponse({"message": "No doctor-patient assignments found for this doctor"}, status=404)

            # Serialize the data
            response = [
                {
                    "id": doctor_patient.id,
                    "doctor": {
                        "id": doctor_patient.doctor.id,
                        "username": doctor_patient.doctor.username,
                    },
                    "patient": {
                        "id": doctor_patient.patient.id,
                        "username": doctor_patient.patient.username,
                        "email": doctor_patient.patient.email,
                        "role": doctor_patient.patient.role,
                    },
                }
                for doctor_patient in doctor_patients
            ]

            return JsonResponse(response, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request method"}, status=405)
