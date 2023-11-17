<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体商店    
====<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.PointOfInterest/blob/master/Store/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全局描述：**该实体类型为城市中的商店/店铺模型。    
版本： 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 属性列表    
<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。    
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理      
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[string]`: 商店类别。枚举：汽车配件商店、自行车商店、书店、服装店、计算机商店、便利店、百货商店、电子商店、花店、家具店、花园商店、杂货店、五金店、爱好商店、家居用品店、珠宝店、酒类店、男装店、手机店、电影租赁店、音乐店、办公设备店、奥特莱斯店、当铺、宠物店、鞋店、体育用品店、轮胎店、玩具店、批发店  . Model: [https://schema.org/Text](https://schema.org/Text)- `currenciesAccepted[array]`: 枚举：aed, afn, all, amd, ang, aoa, ars, aud, awg, azn, bam, bbd, bdt, bgn, bhd, bif, bmd, bnd, bob, bov, brl, bsd、btn, bwp, byn, bzd, cad, cdf, che, chf, chw, clf, clp, cny, cop, cou, crc, cuc, cup, cve, czk, djf, dkk, dop、DZD、EGP、IRN、ETB、EUR、FJD、FKP、GBP、GEL、GHS、GIP、GMD、GNF、GTQ、GYD、HKD、HNL、HRK、HTG、HUF、IDR、IS、INR、IQD、IRR、IHK、JMD、JOD、JPY、KES、KGS、KHR、KMF、KPW、KRW、KWD、KYD、KZT、LAK、LBP、LKR、LDR、LSL、LYD、MAD、MDL、MGA、MKD、MMK、MNT、MOP、MRU、MUR、MVR、MWK、MXN、MXV、MYR、MZN、NAD、NGN、NIO、NOK、NPR、NZD、OMR、PAB、PEN、PGK、PHP、PKR、PLN、PYG、QAR、RON、RSD、RUB、RWF、SAR、SBD、SCR、SDG、SEK、SGD、SHP、SLL、SOS、SRD、SSP、STN、SVC、SYP、SZL、TGB、TJS、TMT、TND、TOP、TRU、TD、TWD、TZS、UAH、UGX、USD、USN、UYI、UYU、UYW、UZS、VES、VND、VUV、wst、xaf、xag、xau、xba、xbb、xbc、xbd、xcd、xdr、xof、xpd、xpf、xpt、xsu、xts、xua、xxx、yer、zar、zmw、zwl。该商店接受的货币。它使用 ISO 4217 货币格式（如美元、欧元）  . Model: [https://es.wikipedia.org/wiki/ISO_4217](https://es.wikipedia.org/wiki/ISO_4217)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `email[email]`: 该商店的电子邮件地址  . Model: [https://schema.org/Text](https://schema.org/Text)- `endDate[date-time]`: 项目的结束日期和时间（ISO 8601 日期格式）。  . Model: [https://schema.org/endDate](https://schema.org/endDate)- `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `logo[uri]`: 该商店的相关标识。  . Model: [https://schema.org/URL](https://schema.org/URL)- `name[string]`: 该项目的名称  - `openingHours[string]`: 企业的一般营业时间。营业时间可以指定为每周的时间范围，从天开始，然后是每天的时间。可以用逗号", "分隔多天。使用连字符"-"指定日或时间范围。使用以下双字母组合指定天数：Mo、Tu、We、Th、Fr、Sa、Su。时间使用 24:00 格式指定。例如，下午 3 点指定为 15:00，上午 10 点指定为 10:00。下面是一个示例：<time itemprop='openingHours' datetime='Tu,Th 16:00-20:00'>星期二和星期四下午 4-8 点</time>。如果一家企业每周营业 7 天，则可以指定为 <time itemprop='openingHours'datetime='Mo-Su'>周一至周日全天</time>。  . Model: [https://schema.org/openingHours](https://schema.org/openingHours)- `openingHoursSpecification[array]`: 一个结构化数值，提供有关某个场所或场所内某项服务开放时间的信息  . Model: [https://schema.org/openingHoursSpecification](https://schema.org/openingHoursSpecification)- `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `paymentAccepted[array]`: 本店接受的付款方式  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `startDate[date-time]`: 项目的开始日期和时间（ISO 8601 日期格式）。  . Model: [https://schema.org/startDate](https://schema.org/startDate)- `telephone[string]`: 该商店的电话号码  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI 实体类型。必须是存储  - `url[uri]`: 提供商店信息的网站  . Model: [https://schema.org/URL](https://schema.org/URL)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
所需属性    
- `description`  - `id`  - `name`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
该模型基于 [Schema.org](https://schema.org/Store) 所定义的模型。特别是，该模型包含了上述链接中定义的属性子集，以及一个商店类别列表，之后可将其专门化为具体类型（见 [https://schema.org/Store](https://schema.org/Store)）。    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 属性的数据模型描述    
按字母顺序排列（点击查看详情）    
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
## 有效载荷示例    
#### 存储 NGSI-v2 密钥值 示例    
下面是一个以 JSON-LD 格式作为键值的存储示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
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
#### NGSI-v2 标准化存储示例    
下面是一个规范化 JSON-LD 格式的存储示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
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
#### 存储 NGSI-LD 键值 示例    
下面是一个以 JSON-LD 格式作为键值的存储示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
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
#### NGSI-LD 标准化存储示例    
下面是一个规范化 JSON-LD 格式的存储示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
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
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
