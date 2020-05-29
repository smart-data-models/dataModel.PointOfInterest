# Store

## Description

This entity Type models stores/shops in the city. The model is based on the one defined by [Schema.org](https://schema.org/Store). In particular, the model contains a subset of the properties defined in the mentioned link, and a list of store categories, that can be afterwards specialized as concrete Types (see [https://schema.org/Store](https://schema.org/Store)). 

Link to the [specification](./doc/spec.md)

## Examples of use

### Normalized Example

Normalized NGSI response 

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
    "type": "geo:json",
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
        "opens": "00:01",
        "closes": "23:59",
        "dayOfWeek": [
          "Friday",
          "Monday",
          "Thursday",
          "Tuesday",
          "Wednesday"
        ]
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
### key-value pairs Example

Sample uses simplified representation for data consumers `?options=keyValues`

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
      "opens": "00:01",
      "closes": "23:59",
      "dayOfWeek": [
        "Friday",
        "Monday",
        "Thursday",
        "Tuesday",
        "Wednesday"
      ]
    }
  ],
  "logo": "http://www.comerciosantander.com/imagenes/Comercios/124F214A-CE55-5A33-A77D-679C0F848FFC_logo.jpg/resize/50/100",
  "telephone": "(+34) 942 123 123",
  "email": "email@example.com",
  "url": "https://exampleStoreUrl.com",
  "category": "GroceryStore"
}
```

### LD Example
Sample uses the NGSI-LD representation. 


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
  "entityVersion": 2.0,
  "location": {
    "type": "Property",
    "value": {
      "type": "Point",
      "coordinates": [
        -3.8077562,
        43.4628255
      ]
    }
  },
  "name": {
    "type": "Property",
    "value": "MARTA KAUFMANN"
  },
  "description": {
    "type": "Property",
    "value": "Cosmetica natural fabricada en Santander."
  },
  "image": {
    "type": "Property",
    "value": "http://www.comerciosantander.com/imagenes/Comercios/124F214A-CE55-5A33-A77D-679C0F848FFC.jpg/resize/50/100/"
  },
  "currenciesAccepted": {
    "type": "Property",
    "value": [
      "EUR"
    ]
  },
  "paymentAccepted:": {
    "type": "Property",
    "value": [
      "cash",
      "paypal"
    ]
  },
  "openingHoursSpecification": {
    "type": "Property",
    "value": [
      {
        "opens": "00:01",
        "closes": "23:59",
        "dayOfWeek": [
          "Friday",
          "Monday",
          "Thursday",
          "Tuesday",
          "Wednesday"
        ]
      }
    ]
  },
  "logo": {
    "type": "Property",
    "value": "http://www.comerciosantander.com/imagenes/Comercios/124F214A-CE55-5A33-A77D-679C0F848FFC_logo.jpg/resize/50/100"
  },
  "telephone": {
    "type": "Property",
    "value": "(+34) 942 123 123"
  },
  "email": {
    "type": "Property",
    "value": "email@example.com"
  },
  "url": {
    "type": "Property",
    "value": "https://exampleStoreUrl.com"
  },
  "category": {
    "type": "Property",
    "value": "GroceryStore"
  }
}
```

## Open issues