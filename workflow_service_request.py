from service_request import create_service_request_resource
from base import send_resource_to_hapi_fhir, get_resource_from_hapi_fhir

if __name__ == "__main__":
    # Usar un patient_id válido previamente creado (p. ej. el de Olivia Casas)
    service_request = create_service_request_resource(
        patient_id="2594463",
        service_text="Hemograma completo",
        status="active",
        intent="order",
        authored_on="2024-11-20",
        identifier_value="SR123456"
    )

    service_id = send_resource_to_hapi_fhir(service_request, "ServiceRequest")

    if service_id:
        print(f"ServiceRequest creado con ID: {service_id}")
        get_resource_from_hapi_fhir(service_id, "ServiceRequest")
