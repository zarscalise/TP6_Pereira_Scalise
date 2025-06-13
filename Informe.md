El objetivo de este trabajo es comprender cómo se aplican los estándares de interoperabilidad (en particular, FHIR) en sistemas de salud, con foco en la Red Nacional de Salud Digital de Argentina.

# Actividad 1
Creación de un recurso Patient con HAPI FHIR
Ingresamos al servidor de prueba HAPI FHIR (versión R4) a través del sitio oficial:
https://hapi.fhir.org/baseR4.

Luego, seleccionamos el recurso Patient y utilizamos la opción POST para crear un nuevo paciente. Enviamos el siguiente JSON:
    {
    "resourceType": "Patient",
    "name": [
      {
        "use": "official",
        "family": "Scalise",
        "given": ["Zarina"]
      }
    ],
    "gender": "female",
    "birthDate": "2000-01-01"
  }

El servidor respondió con HTTP 201 Created, lo que indica que el recurso fue creado correctamente. La URL generada fue:
https://hapi.fhir.org/baseR4/Patient/47884498/_history/1

El recurso creado incluye los siguientes atributos:
- resourceType: especifica que se trata de un recurso de tipo Patient.
- id: identificador único del recurso (47884498).
- name: contiene el nombre del paciente, con nombre "Zarina" y apellido "Scalise".
- gender: género declarado como female.
- birthDate: fecha de nacimiento 2000-01-01.

Se adjuntas capturas de pantalla del procedimiento realizado:
FOTOS ACA


# Actividad 2
Postman
Se usó la herramienta Postman que sirve para probar cómo se conectan los sistemas. Ahí se envió manualmente el mismo formulario JSON con los datos del paciente al mismo servidor que la actividad anterior. Después de hacer el POST, se recibió una respuesta con un "201 Created", que sería una verificación del guardado.
FOTO DEL POST
Luego se verificó la existencia mediante un GET, al cual el sistem responde con un 200 OK, confirmando lo realizado.



