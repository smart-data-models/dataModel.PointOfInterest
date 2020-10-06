Store
  - required
    - oneOf:
      - address
      - location
    - name
    - description
    - currenciesAccepted
  - type: "object"  
   - allOf:
      - $ref: "https://raw.githubusercontent.com/smart-data-models/data-models/master/ngsi-ld.yaml#Common"

  - description: > 
    ## Description 
    This entity Type models stores/shops in the city. The model is based on the one defined by [Schema.org](https://schema.org/Store). In particular, the model contains a subset of the properties defined in the mentioned link, and a list of store categories, that can be afterwards specialized as concrete Types (see [https://schema.org/Store](https://schema.org/Store)). 

  ## Data Model
  - properties
    - source : 
      - x-ngsi: 
        - type: "Property"
        - model: "https://schema.org/URL"
      - type: "string 
      - format: "uri" 
      - description: Specifies the URL to the source of this data (either organization or where relevant more specific source)

    - dataProvider: 
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/URL"
      - type: "string"
      - format: "URL"
      - description: Specifies the URL to information about the provider of this information

    - address:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/address"
      - $ref: "https://smart-data-models.github.io/data-models/schema.org.yaml#/address"

    - location: 
      - x-ngsi:
        - type: "Property"
        - model: "https://tools.ietf.org/html/rfc7946"
      - $ref: "https://raw.githubusercontent.com/smart-data-models/data-models/master/ngsi-ld.yaml#location" 

    - name: 
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Text"
      - type: "string"  
      - description: The name of the store.

    - description : 
      - x-ngsi: 
        - type: "Property"
        - model: "https://schema.org/description"
      - type: "string"
      - description: Description of this store.

    - imageUrl: 
      - x-ngsi: 
        - type: "Property"
        - model: "https://schema.org/URL"
      - type: "string"
      - format: "URL" 
      - description: URL pointing to an image of this store.

    - currenciesAccepted : 
      - x-ngsi:
        - type: "Property"
        - model: "https://es.wikipedia.org/wiki/ISO_4217" 
      - type: "array"
      - items: 
        - type: "string"
        - enum:  [
              "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BOV", "BRL", "BSD", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF", "CHE", "CHF", "CHW", "CLF", "CLP", "CNY", "COP", "COU", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRU", "MUR", "MVR", "MWK", "MXN", "MXV", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "SSP", "STN", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "USN", "UYI", "UYU", "UYW", "UZS", "VES", "VND", "VUV", "WST", "XAF", "XAG", "XAU", "XBA", "XBB", "XBC", "XBD", "XCD", "XDR", "XOF", "XPD", "XPF", "XPT", "XSU", "XTS", "XUA", "XXX", "YER", "ZAR", "ZMW", "ZWL"
            ]
      - description: Currencies accepted in this store. It uses  ISO 4217 currency format (e.g. USD, EUR)

    - paymentAccepted: 
      - x-ngsi: 
        - type: "Property"
        - model: "https://schema.org/Text"
      - type: array
      - items: 
        - type: "string"
      - description: Payment method accepted in this store.

    - openingHoursSpecification: 
      - x-ngsi: 
        - type: "Property"
        - model: "http://schema.org/openingHoursSpecification"
      - type: "array"
      - items:
        - $ref: ""
      - description: Opening hours of this stop.

    - logo: 
      - x-ngsi: 
        - type: "Property"
        - model: "https://schema.org/URL"
      - type: "string"
      - format: "URL"
      - description: An associated logo for this store.

    - telephone: 
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Text"
      - type: "string"  
      - description: The telephone number of this store.

    - email: 
      - x-ngsi: 
        - type: "Property"
        - model: "https://schema.org/Text"
      - type: "string"  
      - description: The email address of this store.

    - url: 
      - x-ngsi: 
        - type: "Property"
        - model: "https://schema.org/URL"
      - type: "string"
      - format: "URL"  
      - property: Website with information about the store.

    - category: 
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Text"
      - type: "string"
      - enum:  [
            "AutoPartsStore",
            "BikeStore",
            "BookStore",
            "ClothingStore",
            "ComputerStore",
            "ConvenienceStore",
            "DepartmentStore",
            "ElectronicsStore",
            "Florist",
            "FurnitureStore",
            "GardenStore",
            "GroceryStore",
            "HardwareStore",
            "HobbyShop",
            "HomeGoodsStore",
            "JewelryStore",
            "LiquorStore",
            "MensClothingStore",
            "MobilePhoneStore",
            "MovieRentalStore",
            "MusicStore",
            "OfficeEquipmentStore",
            "OutletStore",
            "PawnShop",
            "PetStore",
            "ShoeStore",
            "SportingGoodsStore",
            "TireShop",
            "ToyStore",
            "WholesaleStore"
          ]  
      - description: Category of the store
