from fhir.resources.servicerequest import ServiceRequest
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.reference import Reference
from fhir.resources.identifier import Identifier


def create_service_request_resource(
    patient_id: str,
    service_text: str,
    status: str = "active",
    intent: str = "order",
    authored_on: str = None,
    identifier_value: str = None
) -> ServiceRequest:

    kwargs = {
        "status": status,
        "intent": intent,
        "subject": Reference(reference=f"Patient/{patient_id}"),
        "code": CodeableConcept(text=service_text)
    }

    if authored_on:
        kwargs["authoredOn"] = authored_on

    if identifier_value:
        kwargs["identifier"] = [Identifier(use="official", value=identifier_value)]

    service_request = ServiceRequest(**kwargs)
    return service_request
