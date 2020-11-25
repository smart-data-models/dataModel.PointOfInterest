Entity: Store  
=============  
This specification is a **temporal version**. It is automatically generated from the  documented properties described in the schema.json condensed into the file `model.yaml`. A temporary `new_model.yaml` file has been created in every data model to avoid impacting into existing scripts. Thus, the specification will be incomplete as long as the schema.json is not updated to the new format (documenting properties). Once updated the `model.yaml` (`new_model.yaml`) needs to be updated as well (automatically) . Further info in this [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). As long as it is a provisional format any [feedback is welcomed in this form](https://smartdatamodels.org/index.php/submit-an-issue-2/) choosing option `Feedback on the new specification`  
Global description: **A point of interest store**  

## List of properties  

`address`: The mailing address.  `alternateName`: An alternative name for this item  `areaServed`: The geographic area where a service or offered item is provided.  `category`:   `currenciesAccepted`:   `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  `description`:   `email`:   `id`:   `image`:   `location`:   `logo`:   `name`:   `openingHoursSpecification`:   `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  `paymentAccepted`:   `seeAlso`:   `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  `telephone`:   `type`: NGSI Entity type  `url`:   ## Data Model description of properties  
Sorted alphabetically  
```yaml  
Store:    
  description: 'A point of interest store'    
  properties:    
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
    category:    
      enum:    
        - AutoPartsStore    
        - BikeStore    
        - BookStore    
        - ClothingStore    
        - ComputerStore    
        - ConvenienceStore    
        - DepartmentStore    
        - ElectronicsStore    
        - Florist    
        - FurnitureStore    
        - GardenStore    
        - GroceryStore    
        - HardwareStore    
        - HobbyShop    
        - HomeGoodsStore    
        - JewelryStore    
        - LiquorStore    
        - MensClothingStore    
        - MobilePhoneStore    
        - MovieRentalStore    
        - MusicStore    
        - OfficeEquipmentStore    
        - OutletStore    
        - PawnShop    
        - PetStore    
        - ShoeStore    
        - SportingGoodsStore    
        - TireShop    
        - ToyStore    
        - WholesaleStore    
      type: string    
    currenciesAccepted:    
      items:    
        enum:    
          - AED    
          - AFN    
          - ALL    
          - AMD    
          - ANG    
          - AOA    
          - ARS    
          - AUD    
          - AWG    
          - AZN    
          - BAM    
          - BBD    
          - BDT    
          - BGN    
          - BHD    
          - BIF    
          - BMD    
          - BND    
          - BOB    
          - BOV    
          - BRL    
          - BSD    
          - BTN    
          - BWP    
          - BYN    
          - BZD    
          - CAD    
          - CDF    
          - CHE    
          - CHF    
          - CHW    
          - CLF    
          - CLP    
          - CNY    
          - COP    
          - COU    
          - CRC    
          - CUC    
          - CUP    
          - CVE    
          - CZK    
          - DJF    
          - DKK    
          - DOP    
          - DZD    
          - EGP    
          - ERN    
          - ETB    
          - EUR    
          - FJD    
          - FKP    
          - GBP    
          - GEL    
          - GHS    
          - GIP    
          - GMD    
          - GNF    
          - GTQ    
          - GYD    
          - HKD    
          - HNL    
          - HRK    
          - HTG    
          - HUF    
          - IDR    
          - ILS    
          - INR    
          - IQD    
          - IRR    
          - ISK    
          - JMD    
          - JOD    
          - JPY    
          - KES    
          - KGS    
          - KHR    
          - KMF    
          - KPW    
          - KRW    
          - KWD    
          - KYD    
          - KZT    
          - LAK    
          - LBP    
          - LKR    
          - LRD    
          - LSL    
          - LYD    
          - MAD    
          - MDL    
          - MGA    
          - MKD    
          - MMK    
          - MNT    
          - MOP    
          - MRU    
          - MUR    
          - MVR    
          - MWK    
          - MXN    
          - MXV    
          - MYR    
          - MZN    
          - NAD    
          - NGN    
          - NIO    
          - NOK    
          - NPR    
          - NZD    
          - OMR    
          - PAB    
          - PEN    
          - PGK    
          - PHP    
          - PKR    
          - PLN    
          - PYG    
          - QAR    
          - RON    
          - RSD    
          - RUB    
          - RWF    
          - SAR    
          - SBD    
          - SCR    
          - SDG    
          - SEK    
          - SGD    
          - SHP    
          - SLL    
          - SOS    
          - SRD    
          - SSP    
          - STN    
          - SVC    
          - SYP    
          - SZL    
          - THB    
          - TJS    
          - TMT    
          - TND    
          - TOP    
          - TRY    
          - TTD    
          - TWD    
          - TZS    
          - UAH    
          - UGX    
          - USD    
          - USN    
          - UYI    
          - UYU    
          - UYW    
          - UZS    
          - VES    
          - VND    
          - VUV    
          - WST    
          - XAF    
          - XAG    
          - XAU    
          - XBA    
          - XBB    
          - XBC    
          - XBD    
          - XCD    
          - XDR    
          - XOF    
          - XPD    
          - XPF    
          - XPT    
          - XSU    
          - XTS    
          - XUA    
          - XXX    
          - YER    
          - ZAR    
          - ZMW    
          - ZWL    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
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
      type: string    
    email:    
      format: email    
      type: string    
    id:    
      anyOf: &store_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
    image:    
      format: uri    
      type: string    
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
    logo:    
      format: uri    
      type: string    
    name:    
      type: string    
    openingHoursSpecification:    
      description: ""    
      items:    
        properties:    
          closes:    
            format: time    
            type: string    
          dayOfWeek:    
            enum:    
              - Monday    
              - Tuesday    
              - Wednesday    
              - Thursday    
              - Friday    
              - Saturday    
              - Sunday    
              - PublicHolidays    
            type: string    
          opens:    
            format: time    
            type: string    
          validFrom:    
            format: date-time    
            type: string    
          validThrough:    
            format: date-time    
            type: string    
      minItems: 1    
      type: 'Property.A structured value providing information about the opening hours of a place or a certain service inside a place.'    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *store_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    paymentAccepted:    
      items:    
        type: string    
      type: array    
    seeAlso:    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    telephone:    
      type: string    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - Store    
      type: string    
    url:    
      format: uri    
      type: string    
  required:    
    - id    
    - type    
    - name    
    - description    
  type: object    
```  
Here is an example of a Store in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:Store:santander:COM4111",  
  "type": "Store",  
  "source": "https://api.smartsantander.eu/",  
  "dataProvider": "http://www.smartsantander.eu/",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -3.8077562,  
      43.4628255  
    ]  
  },  
  "name": "MARTA KAUFMANN",  
  "description": "Cosmetica natural fabricada en Santander.",  
  "image": "http://www.comerciosantander.com/imagenes/Comercios/124F214A-CE55-5A33-A77D-679C0F848FFC.jpg/resize/50/100/",  
  "currenciesAccepted": [  
    "EUR"  
  ],  
  "paymentAccepted:": [  
    "cash",  
    "paypal"  
  ],  
  "openingHoursSpecification": [  
    {  
      "opens": "00:02:00",  
      "closes": "23:59:00",  
      "dayOfWeek": "Monday"  
    },  
    {  
      "opens": "00:01:00",  
      "closes": "23:59:00",  
      "dayOfWeek": "Tuesday"  
    },  
    {  
      "opens": "00:01:00",  
      "closes": "23:59:00",  
      "dayOfWeek": "Wednesday"  
    },  
    {  
      "opens": "00:01:00",  
      "closes": "23:59:00",  
      "dayOfWeek": "Thursday"  
    },  
    {  
      "opens": "00:01:00",  
      "closes": "23:59:00",  
      "dayOfWeek": "Friday"  
    }  
  ],  
  "logo": "http://www.comerciosantander.com/imagenes/Comercios/124F214A-CE55-5A33-A77D-679C0F848FFC_logo.jpg/resize/50/100",  
  "telephone": "(+34) 942 123 123",  
  "email": "email@example.com",  
  "url": "https://exampleStoreUrl.com",  
  "category": "GroceryStore"  
}  
```  
Here is an example of a Store in JSON format as normalized. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:Store:santander:COM4111",  
  "type": "Store",  
  "source": {  
    "type": "Text",  
    "value": "https://api.smartsantander.eu/"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "http://www.smartsantander.eu/"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -3.8077562,  
        43.4628255  
      ]  
    }  
  },  
  "name": {  
    "type": "Text",  
    "value": "MARTA KAUFMANN"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Cosmetica natural fabricada en Santander."  
  },  
  "image": {  
    "type": "Text",  
    "value": "http://www.comerciosantander.com/imagenes/Comercios/124F214A-CE55-5A33-A77D-679C0F848FFC.jpg/resize/50/100/"  
  },  
  "currenciesAccepted": {  
    "type": "StructuredValue",  
    "value": [  
      "EUR"  
    ]  
  },  
  "paymentAccepted:": {  
    "type": "StructuredValue",  
    "value": [  
      "cash",  
      "paypal"  
    ]  
  },  
  "openingHoursSpecification": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "opens": "00:02:00",  
        "closes": "23:59:00",  
        "dayOfWeek": "Monday"  
      },  
      {  
        "opens": "00:01:00",  
        "closes": "23:59:00",  
        "dayOfWeek": "Tuesday"  
      },  
      {  
        "opens": "00:01:00",  
        "closes": "23:59:00",  
        "dayOfWeek": "Wednesday"  
      },  
      {  
        "opens": "00:01:00",  
        "closes": "23:59:00",  
        "dayOfWeek": "Thursday"  
      },  
      {  
        "opens": "00:01:00",  
        "closes": "23:59:00",  
        "dayOfWeek": "Friday"  
      }  
    ]  
  },  
  "logo": {  
    "type": "Text",  
    "value": "http://www.comerciosantander.com/imagenes/Comercios/124F214A-CE55-5A33-A77D-679C0F848FFC_logo.jpg/resize/50/100"  
  },  
  "telephone": {  
    "type": "Text",  
    "value": "(+34) 942 123 123"  
  },  
  "email": {  
    "type": "Text",  
    "value": "email@example.com"  
  },  
  "url": {  
    "type": "Text",  
    "value": "https://exampleStoreUrl.com"  
  },  
  "category": {  
    "type": "Text",  
    "value": "GroceryStore"  
  }  
}  
```  
Here is an example of a Store in JSON-LD format as key-values. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
  "@context": [  
    "https://smart-data-models.github.io/data-models/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:Store:santander:COM4111",  
  "type": "Store",  
  "source": "https://api.smartsantander.eu/",  
  "dataProvider": "http://www.smartsantander.eu/",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -3.8077562,  
      43.4628255  
    ]  
  },  
  "name": "MARTA KAUFMANN",  
  "description": "Cosmetica natural fabricada en Santander.",  
  "image": "http://www.comerciosantander.com/imagenes/Comercios/124F214A-CE55-5A33-A77D-679C0F848FFC.jpg/resize/50/100/",  
  "currenciesAccepted": [  
    "EUR"  
  ],  
  "paymentAccepted:": [  
    "cash",  
    "paypal"  
  ],  
  "openingHoursSpecification": [  
    {  
      "opens": "00:02:00",  
      "closes": "23:59:00",  
      "dayOfWeek": "Monday"  
    },  
    {  
      "opens": "00:01:00",  
      "closes": "23:59:00",  
      "dayOfWeek": "Tuesday"  
    },  
    {  
      "opens": "00:01:00",  
      "closes": "23:59:00",  
      "dayOfWeek": "Wednesday"  
    },  
    {  
      "opens": "00:01:00",  
      "closes": "23:59:00",  
      "dayOfWeek": "Thursday"  
    },  
    {  
      "opens": "00:01:00",  
      "closes": "23:59:00",  
      "dayOfWeek": "Friday"  
    }  
  ],  
  "logo": "http://www.comerciosantander.com/imagenes/Comercios/124F214A-CE55-5A33-A77D-679C0F848FFC_logo.jpg/resize/50/100",  
  "telephone": "(+34) 942 123 123",  
  "email": "email@example.com",  
  "url": "https://exampleStoreUrl.com",  
  "category": "GroceryStore"  
}  
```  
Here is an example of a Store in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
 "@context": [  
    "https://smart-data-models.github.io/data-models/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:Store:santander:COM4111",  
  "type": "Store",  
  "source": {  
    "type": "Text",  
    "value": "https://api.smartsantander.eu/"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "http://www.smartsantander.eu/"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -3.8077562,  
        43.4628255  
      ]  
    }  
  },  
  "name": {  
    "type": "Text",  
    "value": "MARTA KAUFMANN"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Cosmetica natural fabricada en Santander."  
  },  
  "image": {  
    "type": "Text",  
    "value": "http://www.comerciosantander.com/imagenes/Comercios/124F214A-CE55-5A33-A77D-679C0F848FFC.jpg/resize/50/100/"  
  },  
  "currenciesAccepted": {  
    "type": "StructuredValue",  
    "value": [  
      "EUR"  
    ]  
  },  
  "paymentAccepted:": {  
    "type": "StructuredValue",  
    "value": [  
      "cash",  
      "paypal"  
    ]  
  },  
  "openingHoursSpecification": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "opens": "00:02:00",  
        "closes": "23:59:00",  
        "dayOfWeek": "Monday"  
      },  
      {  
        "opens": "00:01:00",  
        "closes": "23:59:00",  
        "dayOfWeek": "Tuesday"  
      },  
      {  
        "opens": "00:01:00",  
        "closes": "23:59:00",  
        "dayOfWeek": "Wednesday"  
      },  
      {  
        "opens": "00:01:00",  
        "closes": "23:59:00",  
        "dayOfWeek": "Thursday"  
      },  
      {  
        "opens": "00:01:00",  
        "closes": "23:59:00",  
        "dayOfWeek": "Friday"  
      }  
    ]  
  },  
  "logo": {  
    "type": "Text",  
    "value": "http://www.comerciosantander.com/imagenes/Comercios/124F214A-CE55-5A33-A77D-679C0F848FFC_logo.jpg/resize/50/100"  
  },  
  "telephone": {  
    "type": "Text",  
    "value": "(+34) 942 123 123"  
  },  
  "email": {  
    "type": "Text",  
    "value": "email@example.com"  
  },  
  "url": {  
    "type": "Text",  
    "value": "https://exampleStoreUrl.com"  
  },  
  "category": {  
    "type": "Text",  
    "value": "GroceryStore"  
  }  
}  
```  
