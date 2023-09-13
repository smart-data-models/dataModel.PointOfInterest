<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: PuntoDeInterés  
=======================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.PointOfInterest/blob/master/PointOfInterest/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Esta entidad contiene una descripción geográfica armonizada de un Punto de Interés**.  
versión: 0.3.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.  
- `additionalInfoURL[*]`: URL desde la que se puede obtener información adicional del asunto  - `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: El país. Por ejemplo, España  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La localidad en la que se encuentra la dirección postal, y que está en la región  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La región en la que se encuentra la localidad, y que está en el país  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distrito es un tipo de división administrativa que, en algunos países, gestiona el gobierno local    
	- `postOfficeBoxNumber[string]`: El número del apartado de correos para las direcciones de apartados postales. Por ejemplo, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: El código postal. Por ejemplo, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: La dirección  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[array]`: Categoría de este punto de interés  . Model: [https://schema.org/Text](https://schema.org/Text)- `contactPoint[object]`: Los datos de contacto del artículo  . Model: [https://schema.org/ContactPoint](https://schema.org/ContactPoint)	- `areaServed[string]`: Área geográfica en la que se presta un servicio o se ofrece un artículo. Sustituye a serviceArea    
	- `availabilityRestriction[*]`: Esta propiedad vincula un punto de contacto con información sobre cuándo el punto de contacto no está disponible. Los detalles se proporcionan utilizando la clase Especificación de horarios de apertura  . Model: [http://schema.org/hoursAvailable](http://schema.org/hoursAvailable)  
	- `availableLanguage[*]`: Idioma que alguien puede utilizar con o en el artículo, servicio o lugar. Utilice uno de los códigos de idioma del estándar IETF BCP 47. Está implementada la opción Texto pero también podría ser Idioma  . Model: [http://schema.org/availableLanguage](http://schema.org/availableLanguage)  
	- `contactOption[*]`: Una opción disponible en este punto de contacto (por ejemplo, un número gratuito o asistencia para personas con problemas de audición)  . Model: [http://schema.org/contactOption](http://schema.org/contactOption)  
	- `contactType[string]`: Tipo de contacto de este artículo    
	- `email[idn-email]`: Dirección de correo electrónico del propietario    
	- `faxNumber[string]`: El número de fax  . Model: [http://schema.org/Text](http://schema.org/Text)  
	- `name[string]`: El nombre de este artículo    
	- `productSupported[string]`: El producto o servicio con el que está relacionado este punto de contacto de asistencia (por ejemplo, asistencia para una línea de productos concreta). Puede tratarse de un producto o línea de productos específicos (por ejemplo, "iPhone") o de una categoría general de productos o servicios (por ejemplo, "smartphones").  . Model: [http://schema.org/Text](http://schema.org/Text)  
	- `telephone[string]`: Teléfono de este contacto    
- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `description[string]`: Descripción de este artículo  - `id[*]`: Identificador único de la entidad  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `municipalityInfo[object]`: Información municipal correspondiente a esta observación.  . Model: [https://schema.org/Text](https://schema.org/Text)	- `cityID[string]`: ID de la ciudad correspondiente a esta observación.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `cityName[string]`: Nombre de la ciudad correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `district[string]`: Nombre del distrito correspondiente a esta observación.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `stateName[string]`: Nombre del estado correspondiente a esta observación.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `ulbName[string]`: Nombre de la Entidad Local Urbana correspondiente a esta observación.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `wardID[string]`: ID de pabellón correspondiente a esta observación.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `wardName[string]`: Nombre del pabellón correspondiente a esta observación.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `wardNum[number]`: Número de pabellón correspondiente a esta observación.  . Model: [https://schema.org/Number](https://schema.org/Number)  
	- `zoneID[string]`: ID de zona correspondiente a esta observación.  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `name[string]`: El nombre de este artículo  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `refSeeAlso[array]`: Lista de referencias a una o varias entidades relacionadas  . Model: [https://schema.org/URL](https://schema.org/URL)- `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `type[string]`: Tipo de entidad NGSI. Tiene que ser PointOfInterest  - `wardId[string]`: Ward ID de la entidad correspondiente a esta observación  - `zoneId[string]`: ID de zona de la entidad correspondiente a esta observación  - `zoneName[string]`: Nombre de zona de la entidad correspondiente a esta observación  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `category`  - `id`  - `name`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Esta entidad se utiliza en aplicaciones que emplean datos espaciales y es aplicable a los segmentos verticales de Automoción, Medio Ambiente, Industria y Ciudad Inteligente y a las aplicaciones IoT relacionadas. Este modelo de datos se ha creado en colaboración con la GSMA y los miembros del [IoT Big Data Project](http://www.gsma.com/iot/iot-big-data/). Creado con contribuciones del proyecto IUDX.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción de las propiedades del modelo de datos  
Ordenados alfabéticamente (pulse para más detalles)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PointOfInterest:    
  description: This entity contains a harmonised geographic description of a Point of Interest    
  properties:    
    additionalInfoURL:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: URL from which additional information of the subject can be obtained    
      x-ngsi:    
        type: Relationship    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'The country. For example, Spain'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: 'The locality in which the street address is, and which is in the region'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: 'The region in which the locality is, and which is in the country'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: 'The post office box number for PO box addresses. For example, 03578'    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: 'The postal code. For example, 24004'    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    category:    
      description: Category of this point of interest    
      items:    
        type: string    
      minItems: 1    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    contactPoint:    
      description: The details to contact with the item    
      properties:    
        areaServed:    
          description: The geographic area where a service or offered item is provided. Supersedes serviceArea    
          type: string    
          x-ngsi:    
            type: Property    
        availabilityRestriction:    
          anyOf:    
            - description: Array of identifiers format of any NGSI entity    
              items:    
                maxLength: 256    
                minLength: 1    
                pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
                type: string    
              type: array    
              x-ngsi:    
                type: Property    
            - description: Array of identifiers format of any NGSI entity    
              items:    
                format: uri    
                type: string    
              type: array    
              x-ngsi:    
                type: Property    
          description: This property links a contact point to information about when the contact point is not available. The details are provided using the Opening Hours Specification class    
          x-ngsi:    
            model: http://schema.org/hoursAvailable    
            type: Relationship    
        availableLanguage:    
          anyOf:    
            - anyOf:    
                - type: string    
                - items:    
                    type: string    
                  type: array    
          description: 'A language someone may use with or at the item, service or place. Please use one of the language codes from the IETF BCP 47 standard. It is implemented the Text option but it could be also Language'    
          x-ngsi:    
            model: http://schema.org/availableLanguage    
            type: Property    
        contactOption:    
          anyOf:    
            - type: string    
            - items:    
                type: string    
              type: array    
          description: An option available on this contact point (e.g. a toll-free number or support for hearing-impaired callers)    
          x-ngsi:    
            model: http://schema.org/contactOption    
            type: Property    
        contactType:    
          description: Contact type of this item    
          type: string    
          x-ngsi:    
            type: Property    
        email:    
          description: Email address of owner    
          format: idn-email    
          type: string    
          x-ngsi:    
            type: Property    
        faxNumber:    
          description: The fax number    
          type: string    
          x-ngsi:    
            model: http://schema.org/Text    
            type: Property    
        name:    
          description: The name of this item    
          type: string    
          x-ngsi:    
            type: Property    
        productSupported:    
          description: The product or service this support contact point is related to (such as product support for a particular product line). This can be a specific product or product line (e.g. 'iPhone') or a general category of products or services (e.g. 'smartphones')    
          type: string    
          x-ngsi:    
            model: http://schema.org/Text    
            type: Property    
        telephone:    
          description: Telephone of this contact    
          type: string    
          x-ngsi:    
            type: Property    
        url:    
          description: URL which provides a description or further information about this item    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/ContactPoint    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: Geojson reference to the item. Point    
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
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
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
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
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
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
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
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    municipalityInfo:    
      description: Municipality information corresponding to this observation.    
      properties:    
        cityID:    
          description: City ID corresponding to this observation.    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        cityName:    
          description: City name corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        district:    
          description: District name corresponding to this observation.    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        stateName:    
          description: Name of the state corresponding to this observation.    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        ulbName:    
          description: Name of the Urban Local Body corresponding to this observation.    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        wardID:    
          description: Ward ID corresponding to this observation.    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        wardName:    
          description: Ward name corresponding to this observation.    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        wardNum:    
          description: Ward number corresponding to this observation.    
          type: number    
          x-ngsi:    
            model: https://schema.org/Number    
            type: Property    
        zoneID:    
          description: Zone ID corresponding to this observation.    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        zoneName:    
          description: Zone name corresponding to this observation.    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    refSeeAlso:    
      description: List of references to one or more related entities    
      items:    
        anyOf:    
          - anyOf:    
              - description: Identifier format of any NGSI entity    
                maxLength: 256    
                minLength: 1    
                pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
                type: string    
                x-ngsi:    
                  type: Property    
              - description: Identifier format of any NGSI entity    
                format: uri    
                type: string    
                x-ngsi:    
                  type: Property    
            description: Unique identifier of the entity    
            x-ngsi:    
              type: Property    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be PointOfInterest    
      enum:    
        - PointOfInterest    
      type: string    
      x-ngsi:    
        type: Property    
    wardId:    
      description: Ward ID of the entity corresponding to this observation    
      type: string    
      x-ngsi:    
        type: Property    
    zoneId:    
      description: Zone ID of the entity corresponding to this observation    
      type: string    
      x-ngsi:    
        type: Property    
    zoneName:    
      description: Zone name of the entity corresponding to this observation    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - category    
    - name    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.PointOfInterest/PointOfInterest/schema.json    
  x-model-tags: IUDX    
  x-version: 0.3.0    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
#### PointOfInterest NGSI-v2 key-values Ejemplo  
He aquí un ejemplo de un PointOfInterest en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PointOfInterest-A-Concha-123456",  
  "type": "PointOfInterest",  
  "name": "Playa de a Concha",  
  "description": "La Playa de A Concha se presenta como una continuación de la Playa de Compostela, una de las más frecuentadas de Vilagarcía.",  
  "address": {  
    "addressCountry": "ES",  
    "addressLocality": "Vilagarcía de Arousa"  
  },  
  "category": [  
    "113"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -8.768460000000001,  
      42.60214472222222  
    ]  
  },  
  "municipalityInfo":{  
    "district":"Bangalore Urban",  
    "ulbName":"BMC",  
    "cityID":"23",  
    "stateName":"Karnataka",  
    "cityName":"Bangalore",  
    "zoneID":"2",  
    "wardNum":4  
  },  
  "source": "http://www.tourspain.es",  
  "refSeeAlso": [  
    "Beach-A-Concha-123456"  
  ],  
  "wardId": "",  
  "zoneId": "",  
  "additionalInfoURL": "urn:ngsi-ld:Point:34E4:A234",  
  "zoneName": ""  
}  
```  
</details>  
#### PointOfInterest NGSI-v2 normalizado Ejemplo  
He aquí un ejemplo de un PointOfInterest en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "PointOfInterest-A-Concha-123456",  
  "type": "PointOfInterest",  
  "category": {  
    "type": "array",  
    "value": [  
      "113"  
    ]  
  },  
  "description": {  
    "type": "Text",  
    "value": "La Playa de A Concha se presenta como una continuaciin de la Playa de Compostela, una de las mis frecuentadas de Vilagarcia."  
  },  
  "refSeeAlso": {  
    "type": "array",  
    "value": [  
      "Beach-A-Concha-123456"  
    ]  
  },  
  "source": {  
    "type": "Text",  
    "value": "http://www.tourspain.es"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -8.768460000000001,  
        42.60214472222222  
      ]  
    }  
  },  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "addressCountry": "ES",  
      "addressLocality": "Vilagarcia de Arousa"  
    }  
  },  
  "municipalityInfo": {  
    "type": "StructureValue",  
    "value": {  
      "district":"Bangalore Urban",  
      "ulbName":"BMC",  
      "cityID":"23",  
      "stateName":"Karnataka",  
      "cityName":"Bangalore",  
      "zoneID":"2",  
      "wardNum":4  
    }  
  },  
  "name": {  
    "type": "Text",  
    "value": "Playa de a Concha"  
  },  
  "wardId": {  
    "type": "Text",  
    "value": ""  
  },  
  "zoneId": {  
    "type": "Text",  
    "value": ""  
  },  
  "additionalInfoURL": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:Point:34E4:A234"  
  },  
  "zoneName": {  
    "type": "Text",  
    "value": ""  
  }  
}  
```  
</details>  
#### PointOfInterest NGSI-LD key-values Ejemplo  
He aquí un ejemplo de un PointOfInterest en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PointOfInterest:PointOfInterest-A-Concha-123456",  
  "type": "PointOfInterest",  
  "additionalInfoURL": "urn:ngsi-ld:Point:34E4:A234",  
  "address": {  
    "addressCountry": "ES",  
    "addressLocality": "Vilagarcia de Arousa"  
  },  
  "category": [  
    "113"  
  ],  
  "description": "La Playa de A Concha se presenta como una continuacion de la Playa de Compostela, una de las mas frecuentadas de Vilagarcia.",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -8.768460000000001,  
      42.60214472222222  
    ]  
  },  
  "municipalityInfo":{  
    "district":"Bangalore Urban",  
    "ulbName":"BMC",  
    "cityID":"23",  
    "stateName":"Karnataka",  
    "cityName":"Bangalore",  
    "zoneID":"2",  
    "wardNum":4  
  },  
  "name": "Playa de a Concha",  
  "refSeeAlso": [  
    "urn:ngsi-ld:SeeAlso:Beach-A-Concha-123456"  
  ],  
  "source": "http://www.tourspain.es",  
  "wardId": "",  
  "zoneId": "",  
  "zoneName": "",  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.PointOfInterest/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### PuntoDeInterés NGSI-LD normalizado Ejemplo  
He aquí un ejemplo de un PointOfInterest en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PointOfInterest:PointOfInterest-A-Concha-123456",  
  "type": "PointOfInterest",  
  "additionalInfoURL": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Point:34E4:A234"  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "ES",  
      "addressLocality": "Vilagarcia de Arousa"  
    }  
  },  
  "category": {  
    "type": "Property",  
    "value": [  
      "113"  
    ]  
  },  
  "description": {  
    "type": "Property",  
    "value": "La Playa de A Concha se presenta como una continuacion de la Playa de Compostela, una de las mas frecuentadas de Vilagarcia."  
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
  "municipalityInfo": {  
    "type": "Property",  
    "value": {  
      "district":"Bangalore Urban",  
      "ulbName":"BMC",  
      "cityID":"23",  
      "stateName":"Karnataka",  
      "cityName":"Bangalore",  
      "zoneID":"2",  
      "wardNum":4  
    }  
  },  
  "name": {  
    "type": "Property",  
    "value": "Playa de a Concha"  
  },  
  "refSeeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:SeeAlso:Beach-A-Concha-123456"  
    ]  
  },  
  "source": {  
    "type": "Property",  
    "value": "http://www.tourspain.es"  
  },  
  "wardId": {  
    "type": "Property",  
    "value": ""  
  },  
  "zoneId": {  
    "type": "Property",  
    "value": ""  
  },  
  "zoneName": {  
    "type": "Property",  
    "value": ""  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.PointOfInterest/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
