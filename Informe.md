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
- resourceType: Especifica que se trata de un recurso de tipo Patient.
- id: Identificador único del recurso (47884498).
- name: Contiene el nombre del paciente, con nombre "Zarina" y apellido "Scalise".
- gender: Género declarado como female.
- birthDate: Fecha de nacimiento 2000-01-01.

Se adjuntas capturas de pantalla del procedimiento realizado:
FOTOS ACA


# Actividad 2
Postman
Se usó la herramienta Postman que sirve para probar cómo se conectan los sistemas. Ahí se envió manualmente el mismo formulario JSON con los datos del paciente al mismo servidor que la actividad anterior. Después de hacer el POST, se recibió una respuesta con un "201 Created", que sería una verificación del guardado.
FOTO DEL POST
Luego se verificó la existencia mediante un GET, al cual el sistem responde con un 200 OK, confirmando lo realizado.

# Actividad 3
En esta actividad se trabajó con el estandar FHIR utilizando Python, implementando recursos clinicos, enviandolos al servidor HAPI FHIR y estableciendo relaciones entre ellos. La actividad se dividio en tres partes:

## 3a. Crear un recurso patient y enviarlos al servidor
Se implemento en Python una función utilizando la libreria fhir.resources para crear el recurso patient, que incluye nombre, apellido, genero, fecha de nacimiento y numero de documento como identificador.
El recurso fue enviado exitosamente al servidor público HAPI FHIR (https://hapi.fhir.org/baseR4/Patient) utilizando una solicitud HTTP POST. El servidor devolvió un código 201 Created y un ID asignado, confirmando que el recurso fue almacenado correctamente.

## 3b. Buscar un recurso Patient por número de documento

(FOTOS)

## 3c. Crear un recurso ServiceRequest relacionado con un recurso Observation

(FOTOS)



