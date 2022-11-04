<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: Strand  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.PointOfInterest/blob/master/Beach/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Diese Einheit enthält eine harmonisierte geografische Beschreibung eines Strandes.**  
Version: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `accessType[array]`: Enum:'privateVehicle, boat, onFoot, publicTransport'. Beschreibt, wie man zu diesem Strand gelangt.  . Model: [https://schema.org/Text](https://schema.org/Text)- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `beachType[array]`: Art des Strandes nach verschiedenen Kriterien. Enum:'whiteSand, urban, isolated, calmWaters, blueFlag, Q-Quality, strongWaves, windy, blackSand'. Oder jeder andere Wert, der von einer Anwendung benötigt wird.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated[string]`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified[string]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description[string]`: Eine Beschreibung dieses Artikels  - `facilities[array]`: Beschreibt die verschiedenen Einrichtungen, die dieser Strand bietet. Enum:'Strandpromenade, Duschen, Reinigungsservice, Rettungsschwimmer, Sonnenschirmverleih, Liegestuhlverleih, Wasserfahrzeugverleih, Toiletten, Touristenbüro, Abfallbehälter, Telefon, Surfübungsplatz, Behindertengerecht'  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: Eindeutiger Bezeichner der Entität  - `length[number]`: Länge des Strandes  . Model: [https://schema.org/length](https://schema.org/length)- `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels.  - `occupationRate[string]`: Typischer Belegungsgrad dieses Strandes. Enum:'niedrig, mittel, hoch, keine'  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `peopleOccupancy[number]`: Anzahl der Personen am Standort  . Model: [https://schema.org/Number](https://schema.org/Number)- `refSeeAlso[array]`: Liste von Verweisen auf eine oder mehrere verwandte Entitäten.  . Model: [https://schema.org/URL](https://schema.org/URL)- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Es wird empfohlen, den voll qualifizierten Domänennamen des Quellanbieters oder die URL des Quellobjekts zu verwenden.  - `type[string]`: NGSI-Entitätstyp. Es muss Strand sein  - `width[number]`: Breite dieses Strandes  . Model: [https://schema.org/width](https://schema.org/width)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `id`  - `location`  - `name`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Es wird in Anwendungen verwendet, die räumliche Daten nutzen, und ist für die vertikalen Segmente Tourismus, Umwelt und Smart City sowie für damit verbundene IoT-Anwendungen geeignet. Besonderer Dank geht an [TURESPAÑA] (https://www.tourspain.es/en-us), der einige Beispiele zur Verfügung gestellt hat, die die Entwicklung dieses Datenmodells inspiriert haben.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
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
Dieser Entitätstyp wurde als Erweiterung von [https://schema.org/Beach](https://schema.org/Beach) entwickelt, so dass jede von schema.org spezifizierte Eigenschaft, deren Domäne `https://schema.org/Beach` ist, von Anwendungen verwendet werden kann.  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### Strand NGSI-v2 Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen Strand im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### Strand NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen Strand im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
#### Strand NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen Strand im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### Strand NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen Strand im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
