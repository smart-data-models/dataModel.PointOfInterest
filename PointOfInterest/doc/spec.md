<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: PointOfInterest  
=======================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.PointOfInterest/blob/master/PointOfInterest/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **This entity contains a harmonised geographic description of a Point of Interest**  
version: 0.3.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `additionalInfoURL[*]`: URL from which additional information of the subject can be obtained  - `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: The country. For example, Spain  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: The locality in which the street address is, and which is in the region  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: The region in which the locality is, and which is in the country  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: A district is a type of administrative division that, in some countries, is managed by the local government    
	- `postOfficeBoxNumber[string]`: The post office box number for PO box addresses. For example, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: The postal code. For example, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: The street address  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Number identifying a specific property on a public street    
- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[array]`: Category of this point of interest  . Model: [https://schema.org/Text](https://schema.org/Text)- `contactPoint[object]`: The details to contact with the item  . Model: [https://schema.org/ContactPoint](https://schema.org/ContactPoint)	- `areaServed[string]`: The geographic area where a service or offered item is provided. Supersedes serviceArea    
	- `availabilityRestriction[*]`: This property links a contact point to information about when the contact point is not available. The details are provided using the Opening Hours Specification class  . Model: [http://schema.org/hoursAvailable](http://schema.org/hoursAvailable)  
	- `availableLanguage[*]`: A language someone may use with or at the item, service or place. Please use one of the language codes from the IETF BCP 47 standard. It is implemented the Text option but it could be also Language  . Model: [http://schema.org/availableLanguage](http://schema.org/availableLanguage)  
	- `contactOption[*]`: An option available on this contact point (e.g. a toll-free number or support for hearing-impaired callers)  . Model: [http://schema.org/contactOption](http://schema.org/contactOption)  
	- `contactType[string]`: Contact type of this item    
	- `email[idn-email]`: Email address of owner    
	- `faxNumber[string]`: The fax number  . Model: [http://schema.org/Text](http://schema.org/Text)  
	- `name[string]`: The name of this item    
	- `productSupported[string]`: The product or service this support contact point is related to (such as product support for a particular product line). This can be a specific product or product line (e.g. 'iPhone') or a general category of products or services (e.g. 'smartphones')  . Model: [http://schema.org/Text](http://schema.org/Text)  
	- `telephone[string]`: Telephone of this contact    
	- `url[uri]`: URL which provides a description or further information about this item    
- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `description[string]`: A description of this item  - `id[*]`: Unique identifier of the entity  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `municipalityInfo[object]`: Municipality information corresponding to this observation.  . Model: [https://schema.org/Text](https://schema.org/Text)	- `cityID[string]`: City ID corresponding to this observation.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `cityName[string]`: City name corresponding to this observation  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `district[string]`: District name corresponding to this observation.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `stateName[string]`: Name of the state corresponding to this observation.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `ulbName[string]`: Name of the Urban Local Body corresponding to this observation.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `wardID[string]`: Ward ID corresponding to this observation.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `wardName[string]`: Ward name corresponding to this observation.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `wardNum[number]`: Ward number corresponding to this observation.  . Model: [https://schema.org/Number](https://schema.org/Number)  
	- `zoneID[string]`: Zone ID corresponding to this observation.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `zoneName[string]`: Zone name corresponding to this observation.  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `name[string]`: The name of this item  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `refSeeAlso[array]`: List of references to one or more related entities  . Model: [https://schema.org/URL](https://schema.org/URL)- `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `type[string]`: NGSI Entity type. It has to be PointOfInterest  - `wardId[string]`: Ward ID of the entity corresponding to this observation  - `zoneId[string]`: Zone ID of the entity corresponding to this observation  - `zoneName[string]`: Zone name of the entity corresponding to this observation  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `category`  - `id`  - `name`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
This entity is used in applications that use spatial data and is applicable to Automotive, Environment, Industry and Smart City vertical segments and related IoT applications. This data model has been created in cooperation with the GSMA and the members of the [IoT Big Data Project](http://www.gsma.com/iot/iot-big-data/). Created with contributions of IUDX project.  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
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
    capacity:    
      description: The total number of people which can be allocated at the same time    
      type: number    
      x-ngsi:    
        type: Property    
    category:    
      description: Category of this point of interest    
      items:    
        type: string    
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
          description: The fax number of the item    
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
    image:    
      description: An image of the item    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
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
    occupancy:    
      description: The count of people in the in the point of Interest. It should be smaller than capacity    
      type: number    
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
    priceRange:    
      description: String describing the range of prices of the access to the Point of Interest    
      type: string    
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
    relevance:    
      description: Relevance of the point of interest in order to be presented in different zoom levels. 0 is best larger values means lower relevance    
      type: number    
      x-ngsi:    
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
    title:    
      description: This property contains a name given to the Point of interest beyond specific name.    
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
    - name    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2024 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.PointOfInterest/PointOfInterest/schema.json    
  x-model-tags: IUDX    
  x-version: 0.3.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
#### PointOfInterest NGSI-v2 key-values Example    
Here is an example of a PointOfInterest in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PointOfInterest-A-Concha-123456",  
  "type": "PointOfInterest",  
  "name": "Playa de a Concha",  
  "description": "La Playa de A Concha se presenta como una continuaci\u00f3n de la Playa de Compostela, una de las m\u00e1s frecuentadas de Vilagarc\u00eda.",  
  "address": {  
    "addressCountry": "ES",  
    "addressLocality": "Vilagarc\u00eda de Arousa"  
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
  "municipalityInfo": {  
    "district": "Bangalore Urban",  
    "ulbName": "BMC",  
    "cityID": "23",  
    "stateName": "Karnataka",  
    "cityName": "Bangalore",  
    "zoneID": "2",  
    "wardNum": 4  
  },  
  "source": "http://www.tourspain.es",  
  "refSeeAlso": [  
    "Beach-A-Concha-123456"  
  ],  
  "wardId": "",  
  "zoneId": "",  
  "additionalInfoURL": "urn:ngsi-ld:Point:34E4:A234",  
  "zoneName": "",  
  "title": "Cusamè",  
  "relevance": 1,  
  "image": "https://smartdatamodels.org/extra/cusame.png",  
  "priceRange": "25-150€",  
  "capacity": 55,  
  "occupancy": 50  
}  
```  
</details>  
#### PointOfInterest NGSI-v2 normalized Example    
Here is an example of a PointOfInterest in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "PointOfInterest-A-Concha-123456",  
  "type": "PointOfInterest",  
  "category": {  
    "type": "StructuredValue",  
    "value": [  
      "113"  
    ]  
  },  
  "description": {  
    "type": "Text",  
    "value": "La Playa de A Concha se presenta como una continuaciin de la Playa de Compostela, una de las mis frecuentadas de Vilagarcia."  
  },  
  "refSeeAlso": {  
    "type": "StructuredValue",  
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
    "type": "StructuredValue",  
    "value": {  
      "addressCountry": "ES",  
      "addressLocality": "Vilagarcia de Arousa"  
    }  
  },  
  "municipalityInfo": {  
    "type": "StructuredValue",  
    "value": {  
      "district": "Bangalore Urban",  
      "ulbName": "BMC",  
      "cityID": "23",  
      "stateName": "Karnataka",  
      "cityName": "Bangalore",  
      "zoneID": "2",  
      "wardNum": 4  
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
    "type": "Text",  
    "value": "urn:ngsi-ld:Point:34E4:A234"  
  },  
  "zoneName": {  
    "type": "Text",  
    "value": ""  
  },  
  "title": {  
    "type": "Text",  
    "value": "Cusamè"  
  },  
  "relevance": {  
    "type": "Number",  
    "value": 1  
  },  
  "image": {  
    "type": "URL",  
    "value": "https://smartdatamodels.org/extra/cusame.png"  
  },  
  "priceRange": {  
    "type": "Text",  
    "value": "25-150€"  
  },  
  "capacity": {  
    "type": "Number",  
    "value": 55  
  },  
  "occupancy": {  
    "type": "Number",  
    "value": 50  
  }  
}  
```  
</details>  
#### PointOfInterest NGSI-LD key-values Example    
Here is an example of a PointOfInterest in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
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
  "municipalityInfo": {  
    "district": "Bangalore Urban",  
    "ulbName": "BMC",  
    "cityID": "23",  
    "stateName": "Karnataka",  
    "cityName": "Bangalore",  
    "zoneID": "2",  
    "wardNum": 4  
  },  
  "name": "Playa de a Concha",  
  "refSeeAlso": [  
    "urn:ngsi-ld:SeeAlso:Beach-A-Concha-123456"  
  ],  
  "source": "http://www.tourspain.es",  
  "wardId": "",  
  "zoneId": "",  
  "zoneName": "",  
  "title": "Cusamè",  
  "relevance": 1,  
  "image": "https://smartdatamodels.org/extra/cusame.png",  
  "priceRange": "25-150€",  
  "capacity": 55,  
  "occupancy": 50  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.PointOfInterest/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### PointOfInterest NGSI-LD normalized Example    
Here is an example of a PointOfInterest in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
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
  "title": {  
    "type": "Property",  
    "value": "Cusamè"  
  },  
  "relevance": {  
    "type": "Property",  
    "value": 1  
  },  
  "image": {  
    "type": "Property",  
    "value": "https://smartdatamodels.org/extra/cusame.png"  
  },  
  "priceRange": {  
    "type": "Property",  
    "value": "25-150€"  
  },  
  "capacity": {  
    "type": "Property",  
    "value": 55  
  },  
  "occupancy": {  
    "type": "Property",  
    "value": 50  
  }  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.PointOfInterest/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
