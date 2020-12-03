Entidad: Playa  
==============  
Esta especificación es una **versión temporal**. Se genera automáticamente a partir de las propiedades documentadas descritas en el schema.json condensadas en el archivo `model.yaml`. Se ha creado un archivo temporal `nuevo_modelo.yaml` en cada modelo de datos para evitar el impacto en los scripts existentes. Por lo tanto, la especificación estará incompleta mientras el schema.json no se actualice al nuevo formato (documentando las propiedades). Una vez actualizado el `modelo.yaml` (`nuevo_modelo.yaml`) necesita ser actualizado también (automáticamente) . Más información en este [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Mientras sea un formato provisional cualquier [feedback es bienvenido en este formulario](https://smartdatamodels.org/index.php/submit-an-issue-2/) eligiendo la opción `Feedback on the new specification`.  
Descripción global: **Esta entidad contiene una descripción geográfica armonizada de una playa.  

## Lista de propiedades  

- `accessType`: Enum:'vehículo privado, barco, a pie, transporte público'. Describe cómo llegar a esta playa.  - `address`: La dirección postal.  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica donde se presta un servicio o se ofrece un artículo.  - `beachType`: Tipo de playa según diferentes criterios. Enum:'arena blanca, urbana, aislada, aguas tranquilas, bandera azul, Q-Quality, olas fuertes, ventosa, arena negra'. O cualquier otro valor que necesite una aplicación.  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `dateModified`: Sello de tiempo de la última modificación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `facilities`: Describe las diferentes facilidades que ofrece esta playa. Enum:'paseo, duchas, limpiezaServicios, salvavidas, sombrillaAlquiler, tumbonaAlquiler, embarcacionesAlquiler, baños, oficina de turismo, papeleras, teléfono, área de práctica de surf, acceso para discapacitados'.  - `id`:   - `length`: La longitud de esta playa  - `location`:   - `name`: El nombre de este artículo.  - `occupationRate`: Típica tasa de ocupación de esta playa. Enum:'bajo, medio, alto'.  - `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  - `refSeeAlso`: Lista de referencias a una o más entidades conexas.  - `seeAlso`: lista de uri que apunta a recursos adicionales sobre el tema  - `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  - `type`: Tipo de entidad NGSI. Tiene que ser Playa  - `width`: El ancho de esta playa    
Propiedades requeridas  
- `id`  - `location`  - `name`  - `type`    
Se utiliza en aplicaciones que utilizan datos espaciales y es aplicable a los segmentos verticales de Turismo, Medio Ambiente y Ciudades Inteligentes y a las aplicaciones de IO relacionadas. Agradecimientos especiales a [TURESPAÑA](https://www.tourspain.es/en-us) que proporcionó algunos ejemplos que inspiraron el desarrollo de este modelo de datos.  
## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Beach:    
  description: 'This entity contains a harmonised geographic description of a beach.'    
  properties:    
    accessType:    
      description: 'Enum:''privateVehicle, boat, onFoot, publicTransport''. Describes how to get to this beach.'    
      items:    
        enum:    
          - privateVehicle    
          - boat    
          - onFoot    
          - publicTransport    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: https://schema.org/Text    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          type: string    
        addressLocality:    
          type: string    
        addressRegion:    
          type: string    
        areaServed:    
          type: string    
        postOfficeBoxNumber:    
          type: string    
        postalCode:    
          type: string    
        streetAddress:    
          type: string    
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided.'    
      type: Property    
    beachType:    
      description: 'Type of beach according to different criteria. Enum:''whiteSand, urban, isolated, calmWaters, blueFlag, Q-Quality, strongWaves, windy, blackSand''. Or any other value needed by an application.'    
      items:    
        enum:    
          - whiteSand    
          - urban    
          - isolated    
          - calmWaters    
          - blueFlag    
          - Q-Quality    
          - strongWaves    
          - windy    
          - blackSand    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: https://schema.org/Text    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    facilities:    
      description: 'Describes different facilities offered by this beach. Enum:''promenade, showers, cleaningServices, lifeGuard, sunshadeRental, sunLoungerRental, waterCraftRental, toilets, touristOffice, litterBins, telephone,surfPracticeArea, accessforDisabled'''    
      items:    
        enum:    
          - promenade    
          - showers    
          - cleaningServices    
          - lifeGuard    
          - sunshadeRental    
          - sunLoungerRental    
          - waterCraftRental    
          - toilets    
          - touristOffice    
          - litterBins    
          - telephone    
          - surfPracticeArea    
          - accessforDisabled    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: https://schema.org/Text    
    id:    
      anyOf: &beach_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
    length:    
      description: 'Length of this beach'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/length    
        units: meter    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      title: 'GeoJSON Geometry'    
    name:    
      description: 'The name of this item.'    
      type: Property    
    occupationRate:    
      description: 'Typical occupation rate of this beach. Enum:''low, medium, high'''    
      enum:    
        - high    
        - medium    
        - low    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *beach_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    refSeeAlso:    
      description: 'List of references to one or more related entities.'    
      items:    
        anyOf: *beach_-_properties_-_owner_-_items_-_anyof    
      type: Property    
      x-ngsi:    
        model: https://schema.org/URL    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity type. It has to be Beach'    
      enum:    
        - Beach    
      type: Property    
    width:    
      description: 'Width of this beach'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/width    
        units: meter    
  required:    
    - id    
    - type    
    - location    
    - name    
  type: object    
```  
</details>    
Este tipo de entidad ha sido diseñado como una extensión de [https://schema.org/Beach](https://schema.org/Beach) para que cualquier propiedad especificada por schema.org y cuyo dominio sea `https://schema.org/Beach` pueda ser utilizada por las aplicaciones.  
## Ejemplo de cargas útiles  
#### Playa NGSI V2 valores clave Ejemplo  
Aquí hay un ejemplo de una playa en formato JSON como valores clave. Esto es compatible con NGSI V2 cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "Beach-A-Concha-123456",  
  "type": "Beach",  
  "name": "Playa de a Concha",  
  "description": "La Playa de A Concha se presenta .....",  
  "address": {  
    "addressCountry": "ES",  
    "addressLocality": "Vilagarcía de Arousa"  
  },  
  "beachType": ["whiteSand", "urban", "calmWaters"],  
  "occupationRate": "high",  
  "facilities": ["promenade", "showers", "cleaningServices", "lifeGuard"],  
  "accessType": ["privateVehicle", "onFoot", "publicTransport"],  
  "location": {  
    "type": "Point",  
    "coordinates": [-8.768460000000001, 42.60214472222222]  
  },  
  "width": 51,  
  "length": 450,  
  "source": "http://www.tourspain.es"  
}  
```  
#### Playa NGSI V2 normalizada Ejemplo  
Aquí hay un ejemplo de una playa en formato JSON como normalizada. Esto es compatible con NGSI V2 cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "Beach-A-Concha-123456",  
  "type": "Beach",  
  "description": {  
    "value": "La Playa de A Concha se presenta ....."  
  },  
  "width": {  
    "value": 51  
  },  
  "accessType": {  
    "value": ["privateVehicle", "onFoot", "publicTransport"]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [-8.768460000000001, 42.60214472222222]  
    }  
  },  
  "facilities": {  
    "value": ["promenade", "showers", "cleaningServices", "lifeGuard"]  
  },  
  "length": {  
    "value": 450  
  },  
  "source": {  
    "value": "http://www.tourspain.es"  
  },  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "addressCountry": "ES",  
      "addressLocality": "Vilagarc\u00eda de Arousa"  
    }  
  },  
  "beachType": {  
    "value": ["whiteSand", "urban", "calmWaters"]  
  },  
  "occupationRate": {  
    "value": "high"  
  },  
  "name": {  
    "value": "Playa de a Concha"  
  }  
}  
```  
#### Playa NGSI-LD valores clave Ejemplo  
Aquí hay un ejemplo de una playa en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "accessType": ["privateVehicle", "onFoot", "publicTransport"],  
 "address": {"addressCountry": "ES",  
             "addressLocality": "VilagarcÃ­a de Arousa",  
             "type": "PostalAddress"},  
 "beachType": ["whiteSand", "urban", "calmWaters"],  
 "description": "La Playa de A Concha se presenta .....",  
 "facilities": ["promenade", "showers", "cleaningServices", "lifeGuard"],  
 "id": "urn:ngsi-ld:Beach:Beach-A-Concha-123456",  
 "length": 450,  
 "location": {"coordinates": [-8.768460000000001, 42.60214472222222],  
              "type": "Point"},  
 "name": "Playa de a Concha",  
 "occupationRate": "high",  
 "source": "http://www.tourspain.es",  
 "type": "Beach",  
 "width": 51}  
```  
#### Playa NGSI-LD normalizada Ejemplo  
Aquí hay un ejemplo de una playa en formato JSON-LD como normalizada. Esto es compatible con NGSI-LD cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "urn:ngsi-ld:Beach:Beach-A-Concha-123456",  
    "type": "Beach",  
    "description": {  
        "type": "Property",  
        "value": "La Playa de A Concha se presenta ....."  
    },  
    "width": {  
        "type": "Property",  
        "value": 51  
    },  
    "accessType": {  
        "type": "Property",  
        "value": [  
            "privateVehicle",  
            "onFoot",  
            "publicTransport"  
        ]  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -8.768460000000001,  
                42.60214472222222  
            ]  
        }  
    },  
    "facilities": {  
        "type": "Property",  
        "value": [  
            "promenade",  
            "showers",  
            "cleaningServices",  
            "lifeGuard"  
        ]  
    },  
    "length": {  
        "type": "Property",  
        "value": 450  
    },  
    "source": {  
        "type": "Property",  
        "value": "http://www.tourspain.es"  
    },  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressCountry": "ES",  
            "addressLocality": "VilagarcÃ­a de Arousa",  
            "type": "PostalAddress"  
        }  
    },  
    "beachType": {  
        "type": "Property",  
        "value": [  
            "whiteSand",  
            "urban",  
            "calmWaters"  
        ]  
    },  
    "occupationRate": {  
        "type": "Property",  
        "value": "high"  
    },  
    "name": {  
        "type": "Property",  
        "value": "Playa de a Concha"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
