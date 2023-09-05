<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Magasin  
================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.PointOfInterest/blob/master/Store/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Cette entité Type de modèles de magasins/commerces dans la ville.**  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse postale et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La région dans laquelle se trouve la localité et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local.    
	- `postOfficeBoxNumber[string]`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[string]`: Catégorie du magasin. Enum :'AutoPartsStore,BikeStore,BookStore,ClothingStore,ComputerStore,ConvenienceStore,DepartmentStore,ElectronicsStore,Florist,FurnitureStore,GardenStore,GroceryStore,HardwareStore,HobbyShop,HomeGoodsStore,Bijouterie,LiquorStore,MensClothingStore,MobilePhoneStore,MovieRentalStore,MusicStore,OfficeEquipmentStore,OutletStore,PawnShop,PetStore,ShoeStore,SportingGoodsStore,TireShop,ToyStore,WholesaleStore'  . Model: [https://schema.org/Text](https://schema.org/Text)- `currenciesAccepted[array]`: Enum :'AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BOV, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHE, CHF, CHW, CLF, CLP, CNY, COP, COU, CRC, CUC, CUP, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, INR, IQD, IRR, ISK, JMD, JOD, JPY, KES, KGS, KHR, KMF, KPW, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MXV, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, SSP, STN, SVC, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, USD, USN, UYI, UYU, UYW, UZS, VES, VND, VUV, WST, XAF, XAG, XAU, XBA, XBB, XBC, XBD, XCD, XDR, XOF, XPD, XPF, XPT, XSU, XTS, XUA, XXX, YER, ZAR, ZMW, ZWL. Devises acceptées dans ce magasin. Elle utilise le format de devise ISO 4217 (par exemple USD, EUR).  . Model: [https://es.wikipedia.org/wiki/ISO_4217](https://es.wikipedia.org/wiki/ISO_4217)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `email[email]`: L'adresse électronique de ce magasin  . Model: [https://schema.org/Text](https://schema.org/Text)- `endDate[date-time]`: La date et l'heure de fin de l'élément (dans le format de date ISO 8601).  . Model: [https://schema.org/endDate](https://schema.org/endDate)- `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `logo[uri]`: Un logo associé à ce magasin.  . Model: [https://schema.org/URL](https://schema.org/URL)- `name[string]`: Le nom de cet élément  - `openingHours[string]`: Les heures d'ouverture générales d'un commerce. Les heures d'ouverture peuvent être spécifiées sous la forme d'une plage horaire hebdomadaire, en commençant par les jours, puis les heures par jour. Plusieurs jours peuvent être énumérés en séparant chaque jour par une virgule ','. Les jours ou les plages horaires sont spécifiés à l'aide d'un trait d'union "-". Les jours sont spécifiés à l'aide des combinaisons de deux lettres suivantes : Mo, Tu, We, Th, Fr, Sa, Su. Les heures sont indiquées au format 24:00. Par exemple, 15 heures est spécifié comme 15:00, 10 heures comme 10:00. Voici un exemple : <time itemprop='openingHours' datetime='Tu,Th 16:00-20:00'>Mardi et jeudi 4-8pm</time>. Si un commerce est ouvert 7 jours sur 7, il peut être spécifié comme <time itemprop='openingHours' datetime='Mo-Su'>Lundi à dimanche, toute la journée</time>.  . Model: [https://schema.org/openingHours](https://schema.org/openingHours)- `openingHoursSpecification[array]`: Valeur structurée fournissant des informations sur les heures d'ouverture d'un lieu ou d'un certain service à l'intérieur d'un lieu.  . Model: [https://schema.org/openingHoursSpecification](https://schema.org/openingHoursSpecification)- `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `paymentAccepted[array]`: Modes de paiement acceptés dans ce magasin  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `startDate[date-time]`: La date et l'heure de début de l'élément (au format ISO 8601).  . Model: [https://schema.org/startDate](https://schema.org/startDate)- `telephone[string]`: Le numéro de téléphone de ce magasin  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: Type d'entité NGSI. Il doit s'agir d'un magasin  - `url[uri]`: Site Internet contenant des informations sur le magasin  . Model: [https://schema.org/URL](https://schema.org/URL)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `description`  - `id`  - `name`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Le modèle est basé sur celui défini par [Schema.org](https://schema.org/Store). En particulier, le modèle contient un sous-ensemble des propriétés définies dans le lien mentionné, ainsi qu'une liste de catégories de magasins, qui peuvent ensuite être spécialisées en types concrets (voir [https://schema.org/Store](https://schema.org/Store)).  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modèle de données description des propriétés  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Store:    
  description: This entity Type models stores/shops in the city.    
  properties:    
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
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
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
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: https://es.wikipedia.org/wiki/ISO_4217    
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
    email:    
      description: The email address of this store    
      format: email    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    endDate:    
      description: The end date and time of the item (in ISO 8601 date format).    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/endDate    
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
    logo:    
      description: 'An associated logo for this store. '    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    openingHours:    
      description: 'The general opening hours for a business. Opening hours can be specified as a weekly time range, starting with days, then times per day. Multiple days can be listed with commas '','' separating each day. Day or time ranges are specified using a hyphen ''-''. Days are specified using the following two-letter combinations: Mo, Tu, We, Th, Fr, Sa, Su. Times are specified using 24:00 format. For example, 3pm is specified as 15:00, 10am as 10:00. Here is an example: <time itemprop=''openingHours'' datetime=''Tu,Th 16:00-20:00''>Tuesdays and Thursdays 4-8pm</time>. If a business is open 7 days a week, then it can be specified as <time itemprop=''openingHours'' datetime=''Mo-Su''>Monday through Sunday, all day</time>'    
      type: string    
      x-ngsi:    
        model: https://schema.org/openingHours    
        type: Property    
    openingHoursSpecification:    
      description: A structured value providing information about the opening hours of a place or a certain service inside a place    
      items:    
        properties:    
          closes:    
            description: ' 	The closing hour of the place or service on the given day(s) of the week'    
            format: time    
            type: string    
            x-ngsi:    
              type: Property    
          dayOfWeek:    
            anyOf:    
              - description: Array of days of the week    
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
                x-ngsi:    
                  type: Property    
              - description: Array of days of the week    
                enum:    
                  - https://schema.org/Monday    
                  - https://schema.org/Tuesday    
                  - https://schema.org/Wednesday    
                  - https://schema.org/Thursday    
                  - https://schema.org/Friday    
                  - https://schema.org/Saturday    
                  - https://schema.org/Sunday    
                  - https://schema.org/PublicHolidays    
                type: string    
                x-ngsi:    
                  type: Property    
            description: 'The day of the week for which these opening hours are valid. URLs from GoodRelations (http://purl.org/goodrelations/v1) are used (for Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday plus a special entry for PublicHolidays)'    
            type: string    
            x-ngsi:    
              model: http://schema.org/dayOfWeek    
              type: Property    
          opens:    
            description: The opening hour of the place or service on the given day(s) of the week    
            format: time    
            type: string    
            x-ngsi:    
              type: Property    
          validFrom:    
            anyOf:    
              - description: ""    
                format: date    
                type: string    
                x-ngsi:    
                  model: http://schema.org/Date    
                  type: Property    
              - description: ""    
                format: date-time    
                type: string    
                x-ngsi:    
                  model: http://schema.org/DateTime    
                  type: Property    
            description: 'The date when the item becomes valid. A date value in the form CCYY-MM-DD or a combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] in ISO 8601 date format'    
            x-ngsi:    
              type: Property    
          validThrough:    
            anyOf:    
              - description: ""    
                format: date    
                type: string    
                x-ngsi:    
                  model: http://schema.org/Date    
                  type: Property    
              - description: ""    
                format: date-time    
                type: string    
                x-ngsi:    
                  model: http://schema.org/DateTime    
                  type: Property    
            description: 'The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours. A date value in the form CCYY-MM-DD or a combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] in ISO 8601 date format'    
            type: string    
            x-ngsi:    
              type: Property    
        type: object    
      minItems: 1    
      type: array    
      x-ngsi:    
        model: https://schema.org/openingHoursSpecification    
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
    paymentAccepted:    
      description: Payment method accepted in this store    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
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
    startDate:    
      description: The start date and time of the item (in ISO 8601 date format).    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/startDate    
        type: Property    
    telephone:    
      description: The telephone number of this store    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be Store    
      enum:    
        - Store    
      type: string    
      x-ngsi:    
        type: Property    
    url:    
      description: Website with information about the store    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
  required:    
    - id    
    - type    
    - name    
    - description    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/Store/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.PointOfInterest/Store/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### Stocker les valeurs de clés NGSI-v2 Exemple  
Voici un exemple de magasin au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### Store NGSI-v2 normalisé Exemple  
Voici un exemple de magasin au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec la norme NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
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
    "type": "array",  
    "value": [  
      "EUR"  
    ]  
  },  
  "paymentAccepted:": {  
    "type": "array",  
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
    "type": "URL",  
    "value": "https://exampleStoreUrl.com"  
  },  
  "category": {  
    "type": "Text",  
    "value": "GroceryStore"  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.PointOfInterest/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Stocker les valeurs de clés NGSI-LD Exemple  
Voici un exemple de magasin au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Store:santander:COM4111",  
  "type": "Store",  
  "category": "GroceryStore",  
  "currenciesAccepted": [  
    "EUR"  
  ],  
  "dataProvider": "http://www.smartsantander.eu/",  
  "description": "Cosmetica natural fabricada en Santander.",  
  "email": "email@example.com",  
  "image": "http://www.comerciosantander.com/imagenes/Comercios/124F214A-CE55-5A33-A77D-679C0F848FFC.jpg/resize/50/100/",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -3.8077562,  
      43.4628255  
    ]  
  },  
  "logo": "http://www.comerciosantander.com/imagenes/Comercios/124F214A-CE55-5A33-A77D-679C0F848FFC_logo.jpg/resize/50/100",  
  "name": "MARTA KAUFMANN",  
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
  "paymentAccepted:": [  
    "cash",  
    "paypal"  
  ],  
  "source": "https://api.smartsantander.eu/",  
  "telephone": "(+34) 942 123 123",  
  "url": "https://exampleStoreUrl.com",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.PointOfInterest/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Store NGSI-LD normalisé Exemple  
Voici un exemple de magasin au format JSON-LD normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Store:santander:COM4111",  
  "type": "Store",  
  "source": {  
    "type": "Property",  
    "value": "https://api.smartsantander.eu/"  
  },  
  "dataProvider": {  
    "type": "Property",  
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
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
