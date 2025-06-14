from fhir.resources.patient import Patient
from fhir.resources.humanname import HumanName
from fhir.resources.contactpoint import ContactPoint
from fhir.resources.identifier import Identifier  

#Crear el recurso FHIR de paciente con parámetros opcionales
def create_patient_resource(family_name=None, given_name=None, birth_date=None, gender=None, phone=None, document_id=None):
    patient = Patient()
    
    #Agregar el nombre del paciente
    if family_name or given_name:
        name = HumanName()
        if family_name:
            name.family = family_name
        if given_name:
            name.given = [given_name]
        patient.name = [name]
    
    #Fecha de nacimiento
    if birth_date:
        patient.birthDate = birth_date

    #Género
    if gender:
        patient.gender = gender

    #Teléfono
    if phone:
        contact = ContactPoint()
        contact.system = "phone"
        contact.value = phone
        contact.use = "mobile"
        patient.telecom = [contact]

    #Documento como identifier
    if document_id:
        identifier = Identifier()
        identifier.system = "http://www.argentina.gob.ar/dni"
        identifier.value = document_id
        patient.identifier = [identifier]

    return patient
