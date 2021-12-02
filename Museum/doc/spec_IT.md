Entità: Museo  
=============  
[Licenza aperta](https://github.com/smart-data-models//dataModel.PointOfInterest/blob/master/Museum/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Un museo**  

## Elenco delle proprietà  

- `address`: L'indirizzo postale  - `alternateName`: Un nome alternativo per questa voce  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `artPeriod`: Valori consentiti:- Quelli definiti da [Wikipedia](https://en.wikipedia.org/wiki/Art_periods).- Qualsiasi altro valore esteso necessario a un'applicazione e non descritto dalla risorsa precedente.  - `buildingType`: Tipo di edificio che ospita il museo. Enum:'luogo preistorico, acropoli, alcazaba, acquedotto, alcazar, anfiteatro, arco, architettura polare, basilica, strada, cappella, cartuja, casa nobile, residenza, castello, castro, catacombe, cattedrale, chiostro, convento, grotta preistorica, dolmen, officeBuilding, houseBuilding, industrialBuilding, militaryBuilding, hermitage, fortress, sculpturalGroups, church, garden, fishMarket, masia, masiaFortificada, minaret, monastero, monolite, mura, necropoli, menhir, palazzo, palazzo, pantheon, pazo, piramide, ponte, porta, porticato, area murata, santuario, tomba, sinagoga, taulasTalayotsNavetas, theathre, tempio, sorgente, torre, sito archeologico, università, cimitero, tempio fortificato, ingegneria civile, piazza, seminario, arena per la corrida, edificio pubblico, città, grotte e miniere turistiche, pro-cattedrale, moschea, circo, tumulo funerario".  - `contactPoint`: Punto di contatto per il museo.  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `description`: Una descrizione di questo articolo  - `facilities`: Descrive diversi servizi offerti da questo museo. Enum:'ascensore, caffetteria, negozio, auditorio, sala conferenze, audioguida, guardaroba, per disabili, per bambini, visita guidata, ristorante, rampa, prenotazione'. o qualsiasi altro valore necessario per un'applicazione.  - `featuredArtist`: Artista/i principale/i in evidenza in questo museo.  - `historicalPeriod`: Un intervallo di tempo ISO8601. Per esempio 1920/1940. Il secondo elemento dell'intervallo può essere lasciato vuoto per indicare "fino ad ora". Un elenco di anni separati da virgole, per esempio 1620,1625,1718.       - Un secolo, rappresentato da un modello di anno, per esempio 19xx corrisponderebbe al ventesimo secolo. E 196x corrisponderebbe al decennio degli anni sessanta.  - `id`: Identificatore unico dell'entità  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `museumType`: Tipo di museo secondo il contenuto esposto. Enum:'arti applicate, scienza e tecnologia, belle arti, musica, storia, arte sacra, archeologia, speciali, arti decorative, letteratura, medicina e farmacia, marittima, trasporti, militare, cera, arti popolari e tradizioni, numismatica, unesco, ceramica, arti suntuarie, scienze naturali, preistorica, etnologia, ferroviaria, mineraria, tessile, scultura, multidisciplinare, pittura, paleontologia, arte moderna, tematica, architettura, casa-museo, museo della cattedrale, museo diocesano, universitario, arte contemporanea, corrida". Un'altra possibile fonte per i tipi di museo non coperti sopra è [Wikipedia](https://en.wikipedia.org/wiki/Category:Types_of_museum).  - `name`: Il nome di questo articolo.  - `openingHoursSpecification`: Un valore strutturato che fornisce informazioni sugli orari di apertura di un luogo o di un certo servizio all'interno di un luogo  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `refSeeAlso`: Elenco di riferimenti a una o più entità correlate.  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `touristArea`: Zona turistica in cui si trova questo museo. La semantica precisa potrebbe dipendere dall'applicazione o dal paese o regione di destinazione. Per esempio `Costa del Sol`.  - `type`: Tipo di entità NGSI. Deve essere Museo    
Proprietà richieste  
- `id`  - `location`  - `name`  - `type`    
Questa entità contiene una descrizione geografica armonizzata di un museo. Si usa in applicazioni che utilizzano dati spaziali ed è applicabile ai segmenti verticali Turismo, Cultura e Smart City e alle relative applicazioni IoT. Un ringraziamento speciale a [TURESPAÑA](https://www.tourspain.es/en-us) che ha fornito alcuni esempi che hanno ispirato lo sviluppo di questo modello di dati.  
## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
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
Questo tipo di entità è stato progettato come estensione di [https://schema.org/Museum](https://schema.org/Museum) in modo che qualsiasi proprietà specificata da schema.org e il cui dominio è `https://schema.org/Museum` possa essere usata dalle applicazioni.  
## Esempio di payloads  
#### Museo NGSI-v2 valori chiave Esempio  
Ecco un esempio di un Museo in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### Museo NGSI-v2 normalizzato Esempio  
Ecco un esempio di un Museo in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
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
#### Museo NGSI-LD valori-chiave Esempio  
Ecco un esempio di un Museo in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### Museo NGSI-LD normalizzato Esempio  
Ecco un esempio di un Museo in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/data-models/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
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
  "id": "urn:ngsi-ld:Museum:Museum-Barcelona-MACBA-1234",  
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
  "type": "Museum"  
}  
```  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per avere una risposta su come trattare le unità di grandezza