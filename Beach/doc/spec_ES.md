<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: Playa  
==============<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.PointOfInterest/blob/master/Beach/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Esta entidad contiene una descripción geográfica armonizada de una playa.**  
versión: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>  
- `accessType[array]`: Enum:'vehículo privado, barco, a pie, transporte público'. Describe cómo llegar a esta playa.  . Model: [https://schema.org/Text](https://schema.org/Text)- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `beachType[array]`: Tipo de playa según diferentes criterios. Enum:'whiteSand, urban, isolated, calmWaters, blueFlag, Q-Quality, strongWaves, windy, blackSand'. O cualquier otro valor que necesite una aplicación.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated[string]`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified[string]`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description[string]`: Una descripción de este artículo  - `facilities[array]`: Describe las diferentes instalaciones que ofrece esta playa. Enum:'paseo marítimo, duchas, servicios de limpieza, salvavidas, alquiler de sombrillas, alquiler de tumbonas, alquiler de embarcaciones, aseos, oficina de turismo, papeleras, teléfono, zona de práctica de surf, acceso para discapacitados'  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: Identificador único de la entidad  - `length[number]`: Longitud de esta playa  . Model: [https://schema.org/length](https://schema.org/length)- `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name[string]`: El nombre de este artículo.  - `occupationRate[string]`: Tasa de ocupación típica de esta playa. Enum:'bajo, medio, alto, ninguno'  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `peopleOccupancy[number]`: Cantidad de personas en el lugar  . Model: [https://schema.org/Number](https://schema.org/Number)- `refSeeAlso[array]`: Lista de referencias a una o más entidades relacionadas.  . Model: [https://schema.org/URL](https://schema.org/URL)- `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `type[string]`: Tipo de entidad NGSI. Tiene que ser Beach  - `width[number]`: Anchura de esta playa  . Model: [https://schema.org/width](https://schema.org/width)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `id`  - `location`  - `name`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Se usa en aplicaciones que utilizan datos espaciales y es aplicable a los segmentos verticales de Turismo, Medio Ambiente y Ciudades Inteligentes y a las aplicaciones IoT relacionadas. Un agradecimiento especial a [TURESPAÑA](https://www.tourspain.es/en-us) que proporcionó algunos ejemplos que inspiraron el desarrollo de este modelo de datos.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
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
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
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
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    length:    
      description: 'Length of this beach'    
      type: number    
      x-ngsi:    
        model: https://schema.org/length    
        type: Property    
        units: meter    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'GeoProperty. Geojson reference to the item. Point'    
          properties:    
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
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
          properties:    
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
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
          properties:    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
          properties:    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
          properties:    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
          properties:    
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
      x-ngsi:    
        type: GeoProperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    occupationRate:    
      description: 'Typical occupation rate of this beach. Enum:''low, medium, high, none'''    
      enum:    
        - high    
        - medium    
        - low    
        - none    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *beach_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    peopleOccupancy:    
      description: 'Amount of people at the location'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    refSeeAlso:    
      description: 'List of references to one or more related entities.'    
      items:    
        anyOf: *beach_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be Beach'    
      enum:    
        - Beach    
      type: string    
      x-ngsi:    
        type: Property    
    width:    
      description: 'Width of this beach'    
      type: number    
      x-ngsi:    
        model: https://schema.org/width    
        type: Property    
        units: meter.    
  required:    
    - id    
    - type    
    - location    
    - name    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/Beach/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.PointOfInterest/Beach/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
Este tipo de entidad ha sido diseñado como una extensión de [https://schema.org/Beach](https://schema.org/Beach) para que cualquier propiedad especificada por schema.org y cuyo dominio sea `https://schema.org/Beach` pueda ser utilizada por las aplicaciones.  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
#### Ejemplo de valores clave NGSI-v2 de la playa  
Aquí hay un ejemplo de una playa en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### Playa NGSI-v2 normalizada Ejemplo  
Este es un ejemplo de una playa en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### Ejemplo de valores clave NGSI-LD de la playa  
Aquí hay un ejemplo de una playa en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Beach:Beach-A-Concha-123456",  
    "type": "Beach",  
    "accessType": {  
        "type": "Property",  
        "value": [  
            "privateVehicle",  
            "onFoot",  
            "publicTransport"  
        ]  
    },  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressCountry": "ES",  
            "addressLocality": "Vilagarc\u00eda de Arousa",  
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
    "description": {  
        "type": "Property",  
        "value": "La Playa de A Concha se presenta ....."  
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
    "name": {  
        "type": "Property",  
        "value": "Playa de a Concha"  
    },  
    "occupationRate": {  
        "type": "Property",  
        "value": "high"  
    },  
    "source": {  
        "type": "Property",  
        "value": "http://www.tourspain.es"  
    },  
    "width": {  
        "type": "Property",  
        "value": 51  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.PointOfInterest/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### Playa NGSI-LD normalizada Ejemplo  
Este es un ejemplo de una playa en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Beach:Beach-A-Concha-123456",  
    "type": "Beach",  
    "accessType": [  
        "privateVehicle",  
        "onFoot",  
        "publicTransport"  
    ],  
    "address": {  
        "addressCountry": "ES",  
        "addressLocality": "Vilagarc\u00eda de Arousa",  
        "type": "PostalAddress"  
    },  
    "beachType": [  
        "whiteSand",  
        "urban",  
        "calmWaters"  
    ],  
    "description": "La Playa de A Concha se presenta .....",  
    "facilities": [  
        "promenade",  
        "showers",  
        "cleaningServices",  
        "lifeGuard"  
    ],  
    "length": 450,  
    "location": {  
        "coordinates": [  
            -8.768460000000001,  
            42.60214472222222  
        ],  
        "type": "Point"  
    },  
    "name": "Playa de a Concha",  
    "occupationRate": "high",  
    "source": "http://www.tourspain.es",  
    "width": 51,  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.PointOfInterest/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
