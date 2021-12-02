Entité : Store  
==============  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.PointOfInterest/blob/master/Store/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Cette entité Type modélise les magasins/ateliers de la ville.**  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `category`: Catégorie du magasin. Enum :'Magasin de pièces détachées, Magasin de vélos, Librairie, Magasin de vêtements, Magasin d'ordinateurs, Dépanneur, Grand magasin, Magasin d'électronique, Fleuriste, Magasin de meubles, Magasin de jardinage, Epicerie, Quincaillerie, Hobby, Magasin d'articles ménagers,Bijouterie, Magasin de spiritueux, Magasin de vêtements pour hommes, Magasin de téléphones portables, Magasin de location de films, Magasin de musique, Magasin d'équipement de bureau, Magasin d'usine, Mont-de-piété, Magasin d'animaux domestiques, Magasin de chaussures, Magasin d'articles de sport, Magasin de pneus, Magasin de jouets, Magasin de gros'.  - `currenciesAccepted`: Enum :AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BOV, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHE, CHF, CHW, CLF, CLP, CNY, COP, COU, CRC, CUC, CUP, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JMD, JOD, JPY, KES, KGS, KHR, KMF, KPW, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MXV, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SVC, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USN, UYI, UYU, UYW, UZS, VES, VND, VUV, WST, XAF, XAG, XAU, XBA, XBB, XBC, XBD, XCD, XDR, XOF, XPD, XPF, XPT, XSU, XTS, XUA, XXX, YER, ZAR, ZMW, ZWL. Devises acceptées dans ce magasin. Il utilise le format de devise ISO 4217 (par exemple, USD, EUR).  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `email`: L'adresse électronique de ce magasin.  - `id`: Identifiant unique de l'entité  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `logo`: Un logo associé pour ce magasin.  - `name`: Le nom de cet élément.  - `openingHoursSpecification`: Une valeur structurée fournissant des informations sur les heures d'ouverture d'un lieu ou d'un certain service à l'intérieur d'un lieu.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `paymentAccepted`: Mode de paiement accepté dans ce magasin.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `telephone`: Le numéro de téléphone de ce magasin.  - `type`: Type d'entité NGSI. Il doit s'agir de Store  - `url`: Site web contenant des informations sur le magasin.    
Propriétés requises  
- `description`  - `id`  - `name`  - `type`    
Le modèle est basé sur celui défini par [Schema.org](https://schema.org/Store). En particulier, le modèle contient un sous-ensemble des propriétés définies dans le lien mentionné, et une liste de catégories de magasins, qui peuvent être ensuite spécialisées en tant que types concrets (voir [https://schema.org/Store](https://schema.org/Store)).  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Store:    
  description: 'This entity Type models stores/shops in the city.'    
  properties:    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    category:    
      description: 'Category of the store. Enum:''AutoPartsStore,BikeStore,BookStore,ClothingStore,ComputerStore,ConvenienceStore,DepartmentStore,ElectronicsStore,Florist,FurnitureStore,GardenStore,GroceryStore,HardwareStore,HobbyShop,HomeGoodsStore,JewelryStore,LiquorStore,MensClothingStore,MobilePhoneStore,MovieRentalStore,MusicStore,OfficeEquipmentStore,OutletStore,PawnShop,PetStore,ShoeStore,SportingGoodsStore,TireShop,ToyStore,WholesaleStore'''    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    currenciesAccepted:    
      description: 'Enum:''AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BOV, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHE, CHF, CHW, CLF, CLP, CNY, COP, COU, CRC, CUC, CUP, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JMD, JOD, JPY, KES, KGS, KHR, KMF, KPW, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MXV, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SVC, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USN, UYI, UYU, UYW, UZS, VES, VND, VUV, WST, XAF, XAG, XAU, XBA, XBB, XBC, XBD, XCD, XDR, XOF, XPD, XPF, XPT, XSU, XTS, XUA, XXX, YER, ZAR, ZMW, ZWL. Currencies accepted in this store. It uses ISO 4217 currency format (e.g. USD, EUR)'    
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
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: https://es.wikipedia.org/wiki/ISO_4217    
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
    email:    
      description: 'The email address of this store.'    
      format: email    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
      description: 'Unique identifier of the entity'    
      type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
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
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
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
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
      type: Geoproperty    
    logo:    
      description: 'An associated logo for this store. '    
      format: uri    
      type: Property    
      x-ngsi:    
        model: https://schema.org/URL    
    name:    
      description: 'The name of this item.'    
      type: Property    
    openingHoursSpecification:    
      description: 'A structured value providing information about the opening hours of a place or a certain service inside a place'    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/openingHoursSpecification    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *store_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    paymentAccepted:    
      description: 'Payment method accepted in this store.'    
      items:    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    telephone:    
      description: 'The telephone number of this store.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    type:    
      description: 'NGSI Entity type. It has to be Store'    
      enum:    
        - Store    
      type: Property    
    url:    
      description: 'Website with information about the store.'    
      format: uri    
      type: Property    
      x-ngsi:    
        model: https://schema.org/URL    
  required:    
    - id    
    - type    
    - name    
    - description    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### Stocker les valeurs de clés NGSI-v2 Exemple  
Voici un exemple d'un magasin au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### Store NGSI-v2 normalisé Exemple  
Voici un exemple d'un magasin au format JSON-LD tel que normalisé. Ceci est compatible avec NGSI-v2 lorsqu'on n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### Stocker les valeurs de clés NGSI-LD Exemple  
Voici un exemple d'un magasin au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### Magasin NGSI-LD normalisé Exemple  
Voici un exemple de magasin au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude