<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：博物馆  
======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.PointOfInterest/blob/master/Museum/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述**博物馆***  
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
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `artPeriod[array]`: 允许的值：- [维基百科](https://en.wikipedia.org/wiki/Art_periods)所定义的值。- 应用程序所需的任何其他扩展值，但上述资源未对其进行描述  . Model: [https://schema.org/Text.Corresponds to the art period(s) of the exhibitions made by this museum](https://schema.org/Text.Corresponds to the art period(s) of the exhibitions made by this museum)- `buildingType[array]`: 博物馆所在建筑的类型。枚举：史前遗址、卫城、阿卡萨巴、导水管、阿卡萨尔、圆形剧场、拱门、圆形建筑、大教堂、道路、小教堂、卡图哈、贵族宅邸、住宅、城堡、城堡、地下墓穴、大教堂、回廊、修道院、史前洞穴、石墓、办公建筑、住宅建筑、工业建筑、军事建筑、隐居地、堡垒、雕塑、修道院、史前洞穴、石墓、办公建筑、住宅建筑、工业建筑、军事建筑、隐居地、堡垒、雕塑群、教堂、花园、鱼市场、masia、masiaFortificada、尖塔、寺院、巨石、城墙、墓地、墓穴、豪宅、宫殿、万神殿、帕索、金字塔、桥、门、拱廊、围墙区、圣所、坟墓、犹太教堂、塔拉约茨纳维塔斯（taulasTalayotsNavetas）、墓穴、寺庙、泉水、塔、考古遗址、大学、墓地、碉堡、土木工程、广场、研讨会、斗牛场、公共建筑、城镇、洞穴和旅游矿山、主教堂、清真寺、马戏团、坟场  . Model: [https://schema.org/Text](https://schema.org/Text)- `contactPoint[object]`: 博物馆联络点  . Model: [https://schema.org/ContactPoint](https://schema.org/ContactPoint)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `facilities[array]`: 介绍博物馆提供的各种设施。枚举："电梯、自助餐厅、商店、听觉、会议室、语音导览、衣帽间、残疾人专用、婴儿专用、导游、餐厅、坡道、预订"。 或应用程序需要的任何其他值。  . Model: [https://schema.org/Text](https://schema.org/Text)- `featuredArtist[array]`: 该博物馆的主要特色艺术家  . Model: [https://schema.org/Person](https://schema.org/Person)- `historicalPeriod[array]`: ISO8601 时间间隔。例如 1920/1940。时间间隔的第二个元素可以留空，表示 "直到现在"。以逗号分隔的年份列表，例如 1620、1625、1718。       - 一个世纪，用年份模式表示，例如 19xx 表示二十世纪。196x 则对应六十年代的十年。  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `museumType[array]`: 根据展出内容划分的博物馆类型。枚举：应用艺术、科学与技术、美术、音乐、历史、神圣艺术、考古学、特种艺术、装饰艺术、文学、医学与药学、航海、运输、军事、蜡像、流行艺术与传统、钱币、教科文组织、陶瓷、服饰艺术、自然科学、史前、人种学、铁路、采矿、纺织、雕塑、多学科、绘画、古生物学、现代艺术、自然科学、史前、人种学、铁路、采矿、纺织、雕塑、多学科、绘画、古生物学、现代艺 术、专题、建筑、博物馆之家、大教堂博物馆、教区博物馆、大学博物馆、当代艺术、斗牛"。以上未涉及的博物馆类型的其他可能来源是 [维基百科](https://en.wikipedia.org/wiki/Category:Types_of_museum)。  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: 该项目的名称  - `openingHoursSpecification[array]`: 一个结构化数值，提供有关某个场所或场所内某项服务开放时间的信息  . Model: [https://schema.org/openingHoursSpecification](https://schema.org/openingHoursSpecification)- `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `refSeeAlso[array]`: 一个或多个相关实体的参考资料列表  . Model: [https://schema.org/URL](https://schema.org/URL)- `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `touristArea[string]`: 博物馆所在的旅游区。精确的语义可能取决于应用或目标国家或地区。例如 "太阳海岸  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI 实体类型。它必须是博物馆  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `location`  - `name`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
该实体包含博物馆的统一地理描述。它用于使用空间数据的应用程序，适用于旅游、文化和智能城市垂直细分市场以及相关的物联网应用程序。特别感谢 [TURESPAÑA](https://www.tourspain.es/en-us)，他们提供的一些示例为本数据模型的开发提供了灵感。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排列（点击查看详情）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Museum:    
  description: A museum    
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
    artPeriod:    
      description: 'Allowed values:-Those defined by [Wikipedia](https://en.wikipedia.org/wiki/Art_periods).- Any other extended value needed by an application and not described by the above resource'    
      items:    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: 'https://schema.org/Text.Corresponds to the art period(s) of the exhibitions made by this museum'    
        type: Property    
    buildingType:    
      description: 'Type of building that hosts the museum. Enum:''prehistoricPlace, acropolis, alcazaba,aqueduct, alcazar, amphitheatre, arch, polularArchitecture,basilica, road, chapel, cartuja, nobleHouse, residence,castle, castro, catacombs, cathedral, cloister, convent,prehistoricCave, dolmen, officeBuilding, houseBuilding,industrialBuilding, militaryBuilding, hermitage, fortress,sculpturalGroups, church, garden, fishMarket, masia,masiaFortificada, minaret, monastery, monolith, walls,necropolis, menhir, mansion, palace, pantheon, pazo,pyramid, bridge, gate, arcade, walledArea, sanctuary,grave, synagogue, taulasTalayotsNavetas, theathre, temple,spring, tower, archeologicalSite, university, graveyard,fortifiedTemple, civilEngineering, square, seminar,bullfightingRing, publicBuilding, town, cavesAndTouristicMines,proCathedral, mosque, circus, burialMound'''    
      items:    
        enum:    
          - prehistoricPlace    
          - acropolis    
          - alcazaba    
          - aqueduct    
          - alcazar    
          - amphitheatre    
          - arch    
          - polularArchitecture    
          - basilica    
          - road    
          - chapel    
          - cartuja    
          - nobleHouse    
          - residence    
          - castle    
          - castro    
          - catacombs    
          - cathedral    
          - cloister    
          - convent    
          - prehistoricCave    
          - dolmen    
          - officeBuilding    
          - houseBuilding    
          - industrialBuilding    
          - militaryBuilding    
          - hermitage    
          - fortress    
          - sculpturalGroups    
          - church    
          - garden    
          - fishMarket    
          - masia    
          - masiaFortificada    
          - minaret    
          - monastery    
          - monolith    
          - walls    
          - necropolis    
          - menhir    
          - mansion    
          - palace    
          - pantheon    
          - pazo    
          - pyramid    
          - bridge    
          - gate    
          - arcade    
          - walledArea    
          - sanctuary    
          - grave    
          - synagogue    
          - taulasTalayotsNavetas    
          - theathre    
          - temple    
          - spring    
          - tower    
          - archeologicalSite    
          - university    
          - graveyard    
          - fortifiedTemple    
          - civilEngineering    
          - square    
          - seminar    
          - bullfightingRing    
          - publicBuilding    
          - town    
          - cavesAndTouristicMines    
          - proCathedral    
          - mosque    
          - circus    
          - burialMound    
        minItems: 1    
        type: string    
        uniqueItems: true    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    contactPoint:    
      description: Contact point for the museum    
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
    facilities:    
      description: 'Describes different facilities offered by this museum. Enum:''elevator, cafeteria, shop, auditory,conferenceRoom, audioguide, cloakRoom, forDisabled, forBabies,guidedTour, restaurant, ramp, reservation''. or any other value needed by an application'    
      items:    
        enum:    
          - elevator    
          - cafeteria    
          - shop    
          - auditory    
          - conferenceRoom    
          - audioguide    
          - cloakRoom    
          - forDisabled    
          - forBabies    
          - guidedTour    
          - restaurant    
          - ramp    
          - reservation    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    featuredArtist:    
      description: Main featured artist(s) at this museum    
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
          - type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: https://schema.org/Person    
        type: Property    
    historicalPeriod:    
      description: 'An ISO8601 time interval. For example 1920/1940. The second element of the interval can be left empty to denote ''till now''. A comma separated list of years, for instance 1620,1625,1718.       -   A century, represented by a year pattern, for instance 19xx would correspond to the twentieth century. And 196x would correspond to the sixties decade'    
      items:    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: https://schema.org/Text    
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
    museumType:    
      description: 'Type of museum according to the exhibited content. Enum:''appliedArts, scienceAndTechnology, fineArts,music, history, sacredArt, archaeology, specials,decorativeArts, literature, medicineAndPharmacy, maritime,transports, military, wax, popularArtsAndTraditions,numismatic, unesco, ceramics, sumptuaryArts, naturalScience,prehistoric, ethnology, railway, mining, textile, sculpture,multiDisciplinar, painting, paleonthology, modernArt,thematic, architecture, museumHouse, cathedralMuseum,diocesanMuseum, universitary, contemporaryArt, bullfighting''. Other possible source for museum types not covered above is [Wikipedia](https://en.wikipedia.org/wiki/Category:Types_of_museum)'    
      items:    
        enum:    
          - appliedArts    
          - scienceAndTechnology    
          - fineArts    
          - music    
          - history    
          - sacredArt    
          - archaeology    
          - specials    
          - decorativeArts    
          - literature    
          - medicineAndPharmacy    
          - maritime    
          - transports    
          - military    
          - wax    
          - popularArtsAndTraditions    
          - numismatic    
          - unesco    
          - ceramics    
          - sumptuaryArts    
          - naturalScience    
          - prehistoric    
          - ethnology    
          - railway    
          - mining    
          - textile    
          - sculpture    
          - multiDisciplinar    
          - painting    
          - paleonthology    
          - modernArt    
          - thematic    
          - architecture    
          - museumHouse    
          - cathedralMuseum    
          - diocesanMuseum    
          - universitary    
          - contemporaryArt    
          - bullfighting    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
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
    touristArea:    
      description: Tourist area at which this museum is located. Precise semantics might depend on the application or target country or region. For instance `Costa del Sol`    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be Museum    
      enum:    
        - Museum    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - location    
    - name    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/Museum/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.PointOfInterest/Museum/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
该实体类型是作为 [https://schema.org/Museum](https://schema.org/Museum)的扩展而设计的，因此应用程序可以使用由 schema.org 指定的、域为 `https://schema.org/Museum` 的任何属性。  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 有效载荷示例  
#### 博物馆 NGSI-v2 键值示例  
下面是一个以 JSON-LD 格式作为键值的博物馆示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "Museum-Barcelona-MACBA-1234",  
  "type": "Museum",  
  "address": {  
    "addressCountry": "ES",  
    "addressLocality": "Barcelona",  
    "streetAddress": "Plaza Dels Àngels, 1"  
  },  
  "alternateName": "MACBA",  
  "artPeriod": [  
    "contemporary"  
  ],  
  "description": "The MACBA was designed by the American architect Richard Meier and inaugurated in 1995.",  
  "facilities": [  
    "shop",  
    "cloakRoom",  
    "guidedTour"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      2.166877152,  
      41.383022358  
    ]  
  },  
  "museumType": [  
    "fineArts"  
  ],  
  "name": "Museo de Arte Contemporaneo de Barcelona",  
  "openingHoursSpecification": [  
    {  
      "dayOfWeek": "Monday",  
      "closes": "19:30:00",  
      "opens": "11:00:00"  
    },  
    {  
      "dayOfWeek": "Tuesday",  
      "closes": "19:30:00",  
      "opens": "11:00:00"  
    },  
    {  
      "dayOfWeek": "Wednesday",  
      "closes": "19:30:00",  
      "opens": "11:00:00"  
    },  
    {  
      "dayOfWeek": "Thursday",  
      "closes": "19:30:00",  
      "opens": "11:00:00"  
    },  
    {  
      "dayOfWeek": "Friday",  
      "closes": "19:30:00",  
      "opens": "11:00:00"  
    },  
    {  
      "dayOfWeek": "Saturday",  
      "closes": "21:00:00",  
      "opens": "10:00:00"  
    },  
    {  
      "dayOfWeek": "Sunday",  
      "closes": "15:00:00",  
      "opens": "10:00:00"  
    }  
  ],  
  "source": "http://www.tourspain.es",  
  "touristArea": "Barcelona-Capital"  
}  
```  
</details>  
#### 博物馆 NGSI-v2 标准化示例  
下面是一个规范化 JSON-LD 格式的博物馆示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "Museum-Barcelona-MACBA-1234",  
  "type": "Museum",  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "addressCountry": "ES",  
      "addressLocality": "Barcelona",  
      "streetAddress": "Plaza Dels \u00c0ngels, 1"  
    }  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "MACBA"  
  },  
  "artPeriod": {  
    "value": [  
      "contemporary"  
    ]  
  },  
  "description": {  
    "value": "The MACBA was designed by the American architect Richard Meier and inaugurated in 1995."  
  },  
  "facilities": {  
    "value": [  
      "shop",  
      "cloakRoom",  
      "guidedTour"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        2.1668771521199393,  
        41.38302235796602  
      ]  
    }  
  },  
  "museumType": {  
    "value": [  
      "fineArts"  
    ]  
  },  
  "name": {  
    "value": "Museo de Arte Contemporaneo de Barcelona"  
  },  
  "openingHoursSpecification": {  
    "value": [  
      {  
        "dayOfWeek": "Monday",  
        "closes": "19:30:00",  
        "opens": "11:00:00"  
      },  
      {  
        "dayOfWeek": "Tuesday",  
        "closes": "19:30:00",  
        "opens": "11:00:00"  
      },  
      {  
        "dayOfWeek": "Wednesday",  
        "closes": "19:30:00",  
        "opens": "11:00:00"  
      },  
      {  
        "dayOfWeek": "Thurday",  
        "closes": "19:30:00",  
        "opens": "11:00:00"  
      },  
      {  
        "dayOfWeek": "Friday",  
        "closes": "19:30:00",  
        "opens": "11:00:00"  
      },  
      {  
        "dayOfWeek": "Saturday",  
        "closes": "21:00:00",  
        "opens": "10:00:00"  
      },  
      {  
        "dayOfWeek": "Sunday",  
        "closes": "15:00:00",  
        "opens": "10:00:00"  
      }  
    ]  
  },  
  "source": {  
    "value": "http://www.tourspain.es"  
  },  
  "touristArea": {  
    "value": "Barcelona-Capital"  
  }  
}  
```  
</details>  
#### 博物馆 NGSI-LD 键值示例  
下面是一个以 JSON-LD 格式作为键值的博物馆示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Museum:Museum-Barcelona-MACBA-1234",  
    "type": "Museum",  
    "address": {  
        "addressCountry": "ES",  
        "addressLocality": "Barcelona",  
        "streetAddress": "Plaza Dels \u00c0ngels, 1",  
    },  
    "alternateName": "MACBA",  
    "artPeriod": [  
        "contemporary"  
    ],  
    "description": "The MACBA was designed by the American architect Richard Meier and inaugurated in 1995.",  
    "facilities": [  
        "shop",  
        "cloakRoom",  
        "guidedTour"  
    ],  
    "location": {  
        "coordinates": [  
            2.1668771521199393,  
            41.38302235796602  
        ],  
        "type": "Point"  
    },  
    "museumType": [  
        "fineArts"  
    ],  
    "name": "Museo de Arte Contemporaneo de Barcelona",  
    "openingHoursSpecification": [  
        {  
            "closes": "19:30:00",  
            "dayOfWeek": "Monday",  
            "opens": "11:00:00"  
        },  
        {  
            "closes": "19:30:00",  
            "dayOfWeek": "Tuesday",  
            "opens": "11:00:00"  
        },  
        {  
            "closes": "19:30:00",  
            "dayOfWeek": "Wednesday",  
            "opens": "11:00:00"  
        },  
        {  
            "closes": "19:30:00",  
            "dayOfWeek": "Thurday",  
            "opens": "11:00:00"  
        },  
        {  
            "closes": "19:30:00",  
            "dayOfWeek": "Friday",  
            "opens": "11:00:00"  
        },  
        {  
            "closes": "21:00:00",  
            "dayOfWeek": "Saturday",  
            "opens": "10:00:00"  
        },  
        {  
            "closes": "15:00:00",  
            "dayOfWeek": "Sunday",  
            "opens": "10:00:00"  
        }  
    ],  
    "source": "http://www.tourspain.es",  
    "touristArea": "Barcelona-Capital",  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.PointOfInterest/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### 博物馆 NGSI-LD 标准化示例  
下面是一个规范化 JSON-LD 格式的博物馆示例。在不使用选项的情况下，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Museum:Museum-Barcelona-MACBA-1234",  
  "type": "Museum",  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "ES",  
      "addressLocality": "Barcelona",  
      "streetAddress": "Plaza Dels \u00c0ngels, 1"  
    }  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "MACBA"  
  },  
  "artPeriod": {  
    "type": "Property",  
    "value": [  
      "contemporary"  
    ]  
  },  
  "description": {  
    "type": "Property",  
    "value": "The MACBA was designed by the American architect Richard Meier and inaugurated in 1995."  
  },  
  "facilities": {  
    "type": "Property",  
    "value": [  
      "shop",  
      "cloakRoom",  
      "guidedTour"  
    ]  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        2.1668771521199393,  
        41.38302235796602  
      ]  
    }  
  },  
  "museumType": {  
    "type": "Property",  
    "value": [  
      "fineArts"  
    ]  
  },  
  "name": {  
    "type": "Property",  
    "value": "Museo de Arte Contemporaneo de Barcelona"  
  },  
  "openingHoursSpecification": {  
    "type": "Property",  
    "value": [  
      {  
        "dayOfWeek": "Monday",  
        "closes": "19:30:00",  
        "opens": "11:00:00"  
      },  
      {  
        "dayOfWeek": "Tuesday",  
        "closes": "19:30:00",  
        "opens": "11:00:00"  
      },  
      {  
        "dayOfWeek": "Wednesday",  
        "closes": "19:30:00",  
        "opens": "11:00:00"  
      },  
      {  
        "dayOfWeek": "Thurday",  
        "closes": "19:30:00",  
        "opens": "11:00:00"  
      },  
      {  
        "dayOfWeek": "Friday",  
        "closes": "19:30:00",  
        "opens": "11:00:00"  
      },  
      {  
        "dayOfWeek": "Saturday",  
        "closes": "21:00:00",  
        "opens": "10:00:00"  
      },  
      {  
        "dayOfWeek": "Sunday",  
        "closes": "15:00:00",  
        "opens": "10:00:00"  
      }  
    ]  
  },  
  "source": {  
    "type": "Property",  
    "value": "http://www.tourspain.es"  
  },  
  "touristArea": {  
    "type": "Property",  
    "value": "Barcelona-Capital"  
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
