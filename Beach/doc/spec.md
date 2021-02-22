Entity: Beach  
=============  
[Open License](https://github.com/smart-data-models//dataModel.PointOfInterest/blob/master/Beach/LICENSE.md)  
Global description: **This entity contains a harmonised geographic description of a beach.**  

## List of properties  

- `accessType`: Enum:'privateVehicle, boat, onFoot, publicTransport'. Describes how to get to this beach.  - `address`: The mailing address.  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided  - `beachType`: Type of beach according to different criteria. Enum:'whiteSand, urban, isolated, calmWaters, blueFlag, Q-Quality, strongWaves, windy, blackSand'. Or any other value needed by an application.  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `facilities`: Describes different facilities offered by this beach. Enum:'promenade, showers, cleaningServices, lifeGuard, sunshadeRental, sunLoungerRental, waterCraftRental, toilets, touristOffice, litterBins, telephone,surfPracticeArea, accessforDisabled'  - `id`: Unique identifier of the entity  - `length`: Length of this beach  - `location`:   - `name`: The name of this item.  - `occupationRate`: Typical occupation rate of this beach. Enum:'low, medium, high'  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `refSeeAlso`: List of references to one or more related entities.  - `seeAlso`: list of uri pointing to additional resources about the item  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `type`: NGSI Entity type. It has to be Beach  - `width`: Width of this beach    
Required properties  
- `id`  - `location`  - `name`  - `type`    
It is used in applications that use spatial data and is applicable to Tourism, Environment, and Smart City vertical segments and related IoT applications. Special thanks to [TURESPAÑA](https://www.tourspain.es/en-us) who provided some examples which  inspired the development of this data model.  
## Data Model description of properties  
Sorted alphabetically (click for details)  
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
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/Text'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/Text'''    
          type: string    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/Text'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/Text'''    
          type: string    
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
      description: 'Unique identifier of the entity'    
      type: Property    
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
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    refSeeAlso:    
      description: 'List of references to one or more related entities.'    
      items:    
        anyOf: *beach_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
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
        units: meter.    
  required:    
    - id    
    - type    
    - location    
    - name    
  type: object    
```  
</details>    
This entity type has been designed as an extension of [https://schema.org/Beach](https://schema.org/Beach) so that any property specified by schema.org and which domain is `https://schema.org/Beach` can be used by applications.  
## Example payloads    
#### Beach NGSI V2 key-values Example    
Here is an example of a Beach in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### Beach NGSI V2 normalized Example    
Here is an example of a Beach in JSON format as normalized. This is compatible with NGSI V2 when not using options and returns the context data of an individual entity.  
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
#### Beach NGSI-LD key-values Example    
Here is an example of a Beach in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### Beach NGSI-LD normalized Example    
Here is an example of a Beach in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
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
