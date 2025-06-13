from fhir.resources.servicerequest import ServiceRequest
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.reference import Reference
from fhir.resources.identifier import Identifier
from fhir.resources.fhirdate import FHIRDate

def create_service_request_resource(
    patient_id: str,
    service_text: str,
    status: str = "active",
    intent: str = "order",
    authored_on: str = None,
    identifier_value: str = None
) -> ServiceRequest:
    
    # Crear la instancia del recurso
    service_request = ServiceRequest()

    # Relacionar con el paciente
    service_request.subject = Reference(reference=f"Patient/{patient_id}")

    # Código del servicio solicitado
    service_request.code = CodeableConcept(text=service_text)

    # Estado e intención
    service_request.status = status
    service_request.intent = intent

    # Fecha de creación (si se provee)
    if authored_on:
        service_request.authoredOn = FHIRDate(authored_on)

    # Identificador único (opcional)
    if identifier_value:
        service_request.identifier = [
            Identifier(use="official", value=identifier_value)
        ]

    return service_request
