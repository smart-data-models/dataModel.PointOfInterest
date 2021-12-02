エンティティビーチ  
=========  
[オープンライセンス](https://github.com/smart-data-models//dataModel.PointOfInterest/blob/master/Beach/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述。**このエンティティは、ビーチの調和のとれた地理的記述を含んでいます。  

## プロパティのリスト  

- `accessType`: Enum:'privateVehicle, boat, onFoot, publicTransport'.このビーチへの行き方を説明します。  - `address`: 郵送先住所  - `alternateName`: このアイテムの別称  - `areaServed`: サービスや提供されるアイテムが提供される地理的なエリア  - `beachType`: さまざまな基準によるビーチのタイプ。Enum:'whiteSand, urban, isolated, calmWaters, blueFlag, Q-Quality, strongWaves, windy, blackSand'.または、アプリケーションが必要とするその他の値。  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `description`: このアイテムの説明  - `facilities`: このビーチで提供されている様々な施設について説明しています。Enum:'遊歩道、シャワー、清掃サービス、ライフガード、日除けのレンタル、サンラウンジャーのレンタル、水上バイクのレンタル、トイレ、ツーリストオフィス、ゴミ箱、電話、サーフィン練習場、障害者のための施設'  - `id`: エンティティのユニークな識別子  - `length`: このビーチの長さ  - `location`: アイテムへのGeojson参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygonのいずれかです。  - `name`: このアイテムの名前です。  - `occupationRate`: このビーチの典型的な占有率。Enum:'低、中、高、なし'  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `peopleOccupancy`: その場所にいる人の数  - `refSeeAlso`: 1つまたは複数の関連するエンティティへの参照のリスト。  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `type`: NGSI エンティティタイプ。それはBeachでなければならない。  - `width`: このビーチの幅    
必須項目  
- `id`  - `location`  - `name`  - `type`    
空間データを使用するアプリケーションで使用され、観光、環境、スマートシティの垂直セグメントと関連するIoTアプリケーションに適用されます。このデータモデルの開発にインスピレーションを与えたいくつかの例を提供してくれた[TURESPAÑA](https://www.tourspain.es/en-us)に特に感謝します。  
## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます）  
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
      x-ngsi:    
        type: Geoproperty    
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
このエンティティタイプは、[https://schema.org/Beach](https://schema.org/Beach)の拡張として設計されており、schema.orgで指定され、ドメインが`https://schema.org/Beach`であるプロパティをアプリケーションで使用できるようになっています。  
## ペイロードの例  
#### ビーチNGSI-v2のキーバリューの例  
ここでは、Beachをkey-valuesとしてJSON-LD形式で出力した例を紹介します。これは`options=keyValues`を使った場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### ビーチNGSI-v2の正規化例  
正規化されたJSON-LD形式のBeachの例を示します。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### ビーチNGSI-LDのキーバリューの例  
ここでは、Beachをkey-valuesとしてJSON-LD形式で表現した例を紹介します。これは`options=keyValues`を使った場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
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
  "occupationRate": {  
    "type": "Property",  
    "value": "high"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Playa de a Concha"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### ビーチ NGSI-LDの正規化例  
正規化されたJSON-LD形式のBeachの例を示します。これはオプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
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
  "id": "urn:ngsi-ld:Beach:Beach-A-Concha-123456",  
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
  "type": "Beach",  
  "width": 51  
}  
```  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。