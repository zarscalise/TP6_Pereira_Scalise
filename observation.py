from fhir.resources.observation import Observation
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.reference import Reference
from fhir.resources.fhirdate import FHIRDate

def create_observation_resource(patient_id: str, obs_text: str, value: str, date: str) -> Observation:
    observation = Observation()
    observation.status = "final"
    observation.code = CodeableConcept(text=obs_text)
    observation.subject = Reference(reference=f"Patient/{patient_id}")
    observation.valueString = value
    observation.effectiveDateTime = FHIRDate(date)
    return observation
