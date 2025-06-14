from fhir.resources.observation import Observation
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.reference import Reference

def create_observation_resource(patient_id: str, obs_text: str, value: str, date: str) -> Observation:
    observation = Observation.construct()   
    observation.status = "final"  
    observation.code = CodeableConcept.construct()
    observation.code.text = obs_text
    observation.subject = Reference.construct()
    observation.subject.reference = f"Patient/{patient_id}"
    observation.valueString = value
    observation.effectiveDateTime = date
    return observation
