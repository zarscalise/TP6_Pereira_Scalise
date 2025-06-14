from service_request import create_service_request_resource
from observation import create_observation_resource
from base import send_resource_to_hapi_fhir, get_resource_from_hapi_fhir
from fhir.resources.reference import Reference

if __name__ == "__main__":
    patient_id = "47891960"

    # Crear y subir una observación (por ejemplo, fiebre alta)
    observation = create_observation_resource(
        patient_id=patient_id,
        obs_text="Temperatura corporal",
        value="38.7 °C",
        date="2024-11-20"
    )
    observation_id = send_resource_to_hapi_fhir(observation, "Observation")

    if observation_id:
        print(f"Observation subida con ID: {observation_id}")

        # Crear la solicitud de servicio relacionada con esa observación
        service_request = create_service_request_resource(
            patient_id=patient_id,
            service_text="Estudio de laboratorio por fiebre",
            status="active",
            intent="order",
            authored_on="2024-11-20",
            identifier_value="SR123456"
        )

        # RELACIÓN: agregar la observación como supportingInfo
        service_request.supportingInfo = [
            Reference(reference=f"Observation/{observation_id}")
        ]

        # Enviar la solicitud
        service_id = send_resource_to_hapi_fhir(service_request, "ServiceRequest")

        if service_id:
            print(f"ServiceRequest creada con ID: {service_id}")
            get_resource_from_hapi_fhir(service_id, "ServiceRequest")
