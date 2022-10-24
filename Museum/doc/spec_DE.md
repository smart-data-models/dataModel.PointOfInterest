<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: Museum  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.PointOfInterest/blob/master/Museum/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Allgemeine Beschreibung: **Ein Museum**  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `artPeriod[array]`: Erlaubte Werte: - Die in [Wikipedia] (https://en.wikipedia.org/wiki/Art_periods) definierten Werte. - Jeder andere erweiterte Wert, der von einer Anwendung benötigt wird und nicht durch die oben genannte Ressource beschrieben ist.  . Model: [https://schema.org/Text.Corresponds to the art period(s) of the exhibitions made by this museum](https://schema.org/Text.Corresponds to the art period(s) of the exhibitions made by this museum)- `buildingType[array]`: Art des Gebäudes, in dem das Museum untergebracht ist. Enum:'PrähistorischerOrt, Akropolis, Alcazaba, Aquädukt, Alcazar, Amphitheater, Bogen, PolularArchitektur, Basilika, Straße, Kapelle, Cartuja, Adelshaus, Residenz, Burg, Castro, Katakomben, Kathedrale, Kloster, Kloster, prähistorische Höhle, Dolmen, Bürogebäude, Wohngebäude, Industriegebäude, Militärgebäude, Einsiedelei, Festung, Skulpturengruppen, Kirche, Garten, Fischmarkt, Masia, Masia Fortificada, Minarett, Kloster, Monolith, Mauern, Nekropole, Menhir, Herrenhaus, Palast, Pantheon, Pazo, Pyramide, Brücke, Tor, Arkade, ummauerter Bereich, Heiligtum, Grab, Synagoge, TaulasTalayotsNavetas, Theatrum, Tempel, Quelle, Turm, archäologische Stätte, Universität, Friedhof, befestigter Tempel, Ingenieurbau, Platz, Seminar, Stierkampfarena, öffentliches Gebäude, Stadt, Höhlen und touristische Minen, Kathedrale, Moschee, Zirkus, Grabhügel'  . Model: [https://schema.org/Text](https://schema.org/Text)- `contactPoint[object]`: Kontaktstelle für das Museum.  . Model: [https://schema.org/ContactPoint](https://schema.org/ContactPoint)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated[string]`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified[string]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description[string]`: Eine Beschreibung dieses Artikels  - `facilities[array]`: Beschreibt die verschiedenen Einrichtungen, die dieses Museum bietet. Enum:'Aufzug, Cafeteria, Shop, Hörsaal, Konferenzraum, Audioguide, Garderobe, fürBehinderte, fürBabys,Führung, Restaurant, Rampe, Reservierung'. oder jeder andere Wert, der von einer Anwendung benötigt wird.  . Model: [https://schema.org/Text](https://schema.org/Text)- `featuredArtist[array]`: Wichtigste(r) Künstler in diesem Museum.  . Model: [https://schema.org/Person](https://schema.org/Person)- `historicalPeriod[array]`: Ein ISO8601-Zeitintervall. Zum Beispiel 1920/1940. Das zweite Element des Intervalls kann leer gelassen werden, um "bis jetzt" zu kennzeichnen. Eine durch Komma getrennte Liste von Jahren, z. B. 1620, 1625, 1718.       - Ein Jahrhundert, dargestellt durch ein Jahresmuster, z. B. 19xx würde dem zwanzigsten Jahrhundert entsprechen. Und 196x würde dem Jahrzehnt der sechziger Jahre entsprechen.  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: Eindeutiger Bezeichner der Entität  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `museumType[array]`: Typ des Museums entsprechend dem ausgestellten Inhalt. Aufzählung:AngewandteKunst,WissenschaftUndTechnik,BildendeKunst,Musik,Geschichte,SakraleKunst,Archäologie,Spezialitäten,DekorativeKunst,Literatur,MedizinUndApotheke,Schifffahrt,Transport,Militär,Wachs,VolkskunstUndTraditionen,Numismatik,Unesco,Keramik,Bekleidungskunst, Naturwissenschaft, Prähistorie, Ethnologie, Eisenbahn, Bergbau, Textil, Bildhauerei, Multidisziplinär, Malerei, Paläontologie, Moderne Kunst, Thematisch, Architektur, Museumshaus, Kathedralenmuseum, Diözesanmuseum, Universität, Zeitgenössische Kunst, Stierkampf". Eine weitere mögliche Quelle für oben nicht abgedeckte Museumstypen ist [Wikipedia] (https://en.wikipedia.org/wiki/Category:Types_of_museum).  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: Der Name dieses Artikels.  - `openingHoursSpecification[array]`: Ein strukturierter Wert, der Informationen über die Öffnungszeiten eines Ortes oder einer bestimmten Dienstleistung an einem Ort liefert  . Model: [https://schema.org/openingHoursSpecification](https://schema.org/openingHoursSpecification)- `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `refSeeAlso[array]`: Liste von Verweisen auf eine oder mehrere verwandte Entitäten.  . Model: [https://schema.org/URL](https://schema.org/URL)- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `touristArea[string]`: Touristengebiet, in dem sich das Museum befindet. Die genaue Semantik kann von der Anwendung oder dem Zielland oder der Region abhängen. Zum Beispiel `Costa del Sol`.  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI-Entitätstyp. Es muss Museum sein  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `id`  - `location`  - `name`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Diese Einheit enthält eine harmonisierte geografische Beschreibung eines Museums. Es wird in Anwendungen verwendet, die räumliche Daten nutzen, und ist für die vertikalen Segmente Tourismus, Kultur und Smart City sowie für damit verbundene IoT-Anwendungen geeignet. Besonderer Dank geht an [TURESPAÑA] (https://www.tourspain.es/en-us), die einige Beispiele zur Verfügung gestellt hat, die die Entwicklung dieses Datenmodells inspiriert haben.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Museum:    
  description: 'A museum'    
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
    artPeriod:    
      description: 'Allowed values:-Those defined by [Wikipedia](https://en.wikipedia.org/wiki/Art_periods).- Any other extended value needed by an application and not described by the above resource.'    
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
      description: 'Contact point for the museum.'    
      type: object    
      x-ngsi:    
        model: https://schema.org/ContactPoint    
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
      description: 'Describes different facilities offered by this museum. Enum:''elevator, cafeteria, shop, auditory,conferenceRoom, audioguide, cloakRoom, forDisabled, forBabies,guidedTour, restaurant, ramp, reservation''. or any other value needed by an application.'    
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
      description: 'Main featured artist(s) at this museum.'    
      items:    
        anyOf:    
          - anyOf: &museum_-_properties_-_id_-_anyof    
              - description: 'Property. Identifier format of any NGSI entity'    
                maxLength: 256    
                minLength: 1    
                pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
                type: string    
              - description: 'Property. Identifier format of any NGSI entity'    
                format: uri    
                type: string    
            description: 'Property. Unique identifier of the entity'    
          - type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: https://schema.org/Person    
        type: Property    
    historicalPeriod:    
      description: 'An ISO8601 time interval. For example 1920/1940. The second element of the interval can be left empty to denote ''till now''. A comma separated list of years, for instance 1620,1625,1718.       -   A century, represented by a year pattern, for instance 19xx would correspond to the twentieth century. And 196x would correspond to the sixties decade.'    
      items:    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    id:    
      anyOf: *museum_-_properties_-_id_-_anyof    
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
    museumType:    
      description: 'Type of museum according to the exhibited content. Enum:''appliedArts, scienceAndTechnology, fineArts,music, history, sacredArt, archaeology, specials,decorativeArts, literature, medicineAndPharmacy, maritime,transports, military, wax, popularArtsAndTraditions,numismatic, unesco, ceramics, sumptuaryArts, naturalScience,prehistoric, ethnology, railway, mining, textile, sculpture,multiDisciplinar, painting, paleonthology, modernArt,thematic, architecture, museumHouse, cathedralMuseum,diocesanMuseum, universitary, contemporaryArt, bullfighting''. Other possible source for museum types not covered above is [Wikipedia](https://en.wikipedia.org/wiki/Category:Types_of_museum).'    
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
        anyOf: *museum_-_properties_-_id_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    refSeeAlso:    
      description: 'List of references to one or more related entities.'    
      items:    
        anyOf:    
          - anyOf: *museum_-_properties_-_id_-_anyof    
            description: 'Property. Unique identifier of the entity'    
      minItems: 1    
      type: array    
      uniqueItems: true    
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
    touristArea:    
      description: 'Tourist area at which this museum is located. Precise semantics might depend on the application or target country or region. For instance `Costa del Sol`.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be Museum'    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/Museum/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.PointOfInterest/Museum/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
Dieser Entitätstyp wurde als Erweiterung von [https://schema.org/Museum](https://schema.org/Museum) entwickelt, so dass jede von schema.org spezifizierte Eigenschaft, deren Domäne `https://schema.org/Museum` ist, von Anwendungen verwendet werden kann.  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### Museum NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für ein Museum im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### Museum NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein Museum im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
#### Museum NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für ein Museum im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
            "streetAddress": "Plaza Dels \u00c0ngels, 1",  
            "type": "PostalAddress"  
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
        "https://raw.githubusercontent.com/smart-data-models/data-models/master/context.jsonld",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.PointOfInterest/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### Museum NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein Museum im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Museum:Museum-Barcelona-MACBA-1234",  
    "type": "Museum",  
    "address": {  
        "addressCountry": "ES",  
        "addressLocality": "Barcelona",  
        "streetAddress": "Plaza Dels \u00c0ngels, 1",  
        "type": "PostalAddress"  
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
        "https://raw.githubusercontent.com/smart-data-models/data-models/master/context.jsonld",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.PointOfInterest/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
