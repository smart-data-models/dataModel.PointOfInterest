<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティ店舗  
========<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.PointOfInterest/blob/master/Store/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述です。**このエンティティは、都市にある店舗/ショップをモデル化しています。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: この項目の別称  - `areaServed[string]`: サービスまたは提供品が提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[string]`: 店舗のカテゴリ。Enumです。'AutoPartsStore,BikeStore,BookStore,ClothingStore,ComputerStore,ConvenienceStore,DepartmentStore,ElectronicsStore,Florist,FurnitureStore,GardenStore,GroceryStore,HardwareStore,HobbyShop,HomeGoodsStore,ジュエリーストア、リカーストア、メンズウェアストア、携帯電話ストア、映画レンタルストア、ミュージックストア、オフィス用品ストア、アウトレットストア、質屋、ペットストア、靴屋、スポーツ用品店、タイヤショップ、おもちゃ屋、卸売店'。  . Model: [https://schema.org/Text](https://schema.org/Text)- `currenciesAccepted[array]`: Enum:'aed, afn, all, amd, ang, aoa, ars, aud, awg, azn, bam, bbd, bdt, bgn, bhd, bif, bmd, bnd, bob, bov, brl, bsd,btn、bwp、byn、bzd、cad、cdf、che、chf、chw、clf、clp、cny、cop、cou、crc、cuc、cup、cve、czk、djf、dkk、dop,dzd、egp、ern、etb、eur、fjd、fkp、gbp、gel、ghs、gip、gmd、gnf、gtq、gyd、hkd、hnl、hrk、htg、huf、iDR、inr.、ir、ir、inr,iqd、irr、isk、jmd、jod、jpy、kes、kgs、khr、kmf、kpw、krw、kwd、kyd、kzt、lak、lbp、lkr、lrd、lsl、lyd、mad,MDL、MGA、MKD、MMK、MNT、MOP、MRU、MUR、MVR、MWK、MXN、MXV、MYR、MZN、NAD、NN、NIO、NOK、NR、NZD、OMR、PAB、PEN。pgk、php、pkr、pln、pyg、qar、ron、rsd、rub、rwf、sar、sbd、scr、sdg、sgd、shp、sll、sos、srd、ssp、stn.svc、syp、sp、sn,svc, syp, szl, thb, tjs, tmt, tnd, top, try, ttd, twd, tzs, uah, ugx, usd, usn, uyi, uyu, uyw, uzs, ves, vnd, vuv.WST, XAF, XAG, XAF, VAF, VAF, VAF, VAF, VAF, VAF, VAF, VAF, VAF, VAF, VAF。wst, xaf, xag, xau, xba, xbb, xbc, xbd, xcd, xdr, xof, xpd, xpf, xpt, xsu, xts, xua, xxx, yer, zar, zmw, zwl.このストアで利用可能な通貨ISO 4217の通貨形式を使用しています（例：USD、EUR)  . Model: [https://es.wikipedia.org/wiki/ISO_4217](https://es.wikipedia.org/wiki/ISO_4217)- `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `email[string]`: 当店のメールアドレスです。  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: エンティティの一意な識別子  - `location[*]`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `logo[string]`: 当店の関連ロゴです。  . Model: [https://schema.org/URL](https://schema.org/URL)- `name[string]`: このアイテムの名称です。  - `openingHoursSpecification[array]`: ある場所の営業時間や、ある場所の中の特定のサービスに関する情報を提供する構造化された値  . Model: [https://schema.org/openingHoursSpecification](https://schema.org/openingHoursSpecification)- `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリストです。  - `paymentAccepted[array]`: 当店でご利用いただけるお支払い方法です。  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `telephone[string]`: 当店の電話番号です。  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI エンティティタイプ。これはStoreでなければなりません。  - `url[string]`: お店の情報を掲載したウェブサイト。  . Model: [https://schema.org/URL](https://schema.org/URL)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必要なプロパティ  
- `description`  - `id`  - `name`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
このモデルは [Schema.org](https://schema.org/Store) で定義されたものをベースにしています。特に、このモデルは、前述のリンクで定義されているプロパティのサブセットと、ストアカテゴリのリストを含んでおり、これらは後に具体的なTypeとして特化できます([https://schema.org/Store](https://schema.org/Store)を参照)。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
    email:    
      description: 'The email address of this store.'    
      format: email    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
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
      x-ngsi:    
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
      x-ngsi:    
        type: Geoproperty    
    logo:    
      description: 'An associated logo for this store. '    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    openingHoursSpecification:    
      description: 'A structured value providing information about the opening hours of a place or a certain service inside a place'    
      items:    
        properties:    
          closes:    
            format: time    
            pattern: ^(2[0-3]|[01][0-9]):?([0-5][0-9]):?([0-5][0-9])(\.[0-9]*)?(Z|[+-](?:2[0-3]|[01][0-9])(?::?(?:[0-5][0-9]))?)$    
            type: string    
          dayOfWeek:    
            anyOf:    
              - description: 'Property. Array of days of the week.'    
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
              - description: 'Property. Array of days of the week.'    
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
            description: 'Property. Model:''http://schema.org/dayOfWeek''. The day of the week for which these opening hours are valid. URLs from GoodRelations (http://purl.org/goodrelations/v1) are used (for Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday plus a special entry for PublicHolidays).'    
            type: string    
          opens:    
            format: time    
            pattern: ^(2[0-3]|[01][0-9]):?([0-5][0-9]):?([0-5][0-9])(\.[0-9]*)?(Z|[+-](?:2[0-3]|[01][0-9])(?::?(?:[0-5][0-9]))?)$    
            type: string    
          validFrom:    
            anyOf:    
              - description: 'Property. Model:''http://schema.org/Date.'    
                format: date    
                type: string    
              - description: 'Property. Model:''http://schema.org/DateTime.'    
                format: date-time    
                type: string    
            description: 'Property. The date when the item becomes valid. A date value in the form CCYY-MM-DD or a combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] in ISO 8601 date format.'    
          validThrough:    
            anyOf:    
              - description: 'Property. Model:''http://schema.org/Date.'    
                format: date    
                type: string    
              - description: 'Property. Model:''http://schema.org/DateTime.'    
                format: date-time    
                type: string    
            description: 'Property. The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours. A date value in the form CCYY-MM-DD or a combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] in ISO 8601 date format.'    
            type: string    
        type: object    
      minItems: 1    
      type: array    
      x-ngsi:    
        model: https://schema.org/openingHoursSpecification    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *store_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    paymentAccepted:    
      description: 'Payment method accepted in this store.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
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
    telephone:    
      description: 'The telephone number of this store.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be Store'    
      enum:    
        - Store    
      type: string    
      x-ngsi:    
        type: Property    
    url:    
      description: 'Website with information about the store.'    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
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
## ペイロードの例  
#### NGSI-v2鍵の保存例  
ここでは、StoreをJSON-LD形式でkey-valuesとした場合の例を示す。これは `options=keyValues` を使用した場合に NGSI-v2 と互換性があり、個々のエンティティのコンテキストデータが返される。  
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
#### NGSI-v2 正規化されたものを格納 例  
以下は、StoreをJSON-LD形式で正規化した例である。これはオプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
</details>  
#### NGSI-LDのキー値を格納する 例  
ここでは、StoreをJSON-LD形式でkey-valuesとした場合の例を示す。これは `options=keyValues` を使用した場合に NGSI-LD と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Store:santander:COM4111",  
    "type": "Store",  
    "category": {  
        "type": "Text",  
        "value": "GroceryStore"  
    },  
    "currenciesAccepted": {  
        "type": "StructuredValue",  
        "value": [  
            "EUR"  
        ]  
    },  
    "dataProvider": {  
        "type": "Text",  
        "value": "http://www.smartsantander.eu/"  
    },  
    "description": {  
        "type": "Text",  
        "value": "Cosmetica natural fabricada en Santander."  
    },  
    "email": {  
        "type": "Text",  
        "value": "email@example.com"  
    },  
    "image": {  
        "type": "Text",  
        "value": "http://www.comerciosantander.com/imagenes/Comercios/124F214A-CE55-5A33-A77D-679C0F848FFC.jpg/resize/50/100/"  
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
    "logo": {  
        "type": "Text",  
        "value": "http://www.comerciosantander.com/imagenes/Comercios/124F214A-CE55-5A33-A77D-679C0F848FFC_logo.jpg/resize/50/100"  
    },  
    "name": {  
        "type": "Text",  
        "value": "MARTA KAUFMANN"  
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
    "paymentAccepted:": {  
        "type": "StructuredValue",  
        "value": [  
            "cash",  
            "paypal"  
        ]  
    },  
    "source": {  
        "type": "Text",  
        "value": "https://api.smartsantander.eu/"  
    },  
    "telephone": {  
        "type": "Text",  
        "value": "(+34) 942 123 123"  
    },  
    "url": {  
        "type": "Text",  
        "value": "https://exampleStoreUrl.com"  
    },  
    "@context": [  
        "https://smart-data-models.github.io/data-models/context.jsonld",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.PointOfInterest/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### NGSI-LDを正規化して保存する 例  
以下は、StoreをJSON-LD形式で正規化した例である。これはオプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
        "https://smart-data-models.github.io/data-models/context.jsonld",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.PointOfInterest/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
