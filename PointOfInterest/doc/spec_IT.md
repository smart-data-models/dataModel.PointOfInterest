<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: PuntoInteresse  
======================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.PointOfInterest/blob/master/PointOfInterest/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Questa entità contiene una descrizione geografica armonizzata di un punto di interesse**.  
versione: 0.3.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `additionalInfoURL[*]`: URL da cui è possibile ottenere ulteriori informazioni sull'argomento  - `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestita dal governo locale.    
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Numero che identifica una proprietà specifica su una strada pubblica    
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `capacity[number]`: Il numero totale di persone che possono essere assegnate contemporaneamente  - `category[array]`: Categoria di questo punto di interesse  . Model: [https://schema.org/Text](https://schema.org/Text)- `contactPoint[object]`: I dati da contattare con l'articolo  . Model: [https://schema.org/ContactPoint](https://schema.org/ContactPoint)	- `areaServed[string]`: L'area geografica in cui viene fornito un servizio o un articolo offerto. Sostituisce ServiceArea    
	- `availabilityRestriction[*]`: Questa proprietà collega un punto di contatto a informazioni su quando il punto di contatto non è disponibile. I dettagli sono forniti utilizzando la classe Specifica degli orari di apertura  . Model: [http://schema.org/hoursAvailable](http://schema.org/hoursAvailable)  
	- `availableLanguage[*]`: Una lingua che qualcuno può usare con o per l'oggetto, il servizio o il luogo. Utilizzare uno dei codici lingua dello standard BCP 47 dell'IETF. È stata implementata l'opzione Testo, ma potrebbe essere anche Lingua.  . Model: [http://schema.org/availableLanguage](http://schema.org/availableLanguage)  
	- `contactOption[*]`: Un'opzione disponibile su questo punto di contatto (ad esempio un numero verde o un supporto per chi chiama con problemi di udito)  . Model: [http://schema.org/contactOption](http://schema.org/contactOption)  
	- `contactType[string]`: Tipo di contatto di questo articolo    
	- `email[idn-email]`: Indirizzo e-mail del proprietario    
	- `faxNumber[string]`: Il numero di fax dell'articolo  . Model: [http://schema.org/Text](http://schema.org/Text)  
	- `name[string]`: Il nome di questo elemento    
	- `productSupported[string]`: Il prodotto o il servizio a cui si riferisce il punto di contatto dell'assistenza (ad esempio, l'assistenza per una particolare linea di prodotti). Può trattarsi di un prodotto o di una linea di prodotti specifici (ad esempio, "iPhone") o di una categoria generale di prodotti o servizi (ad esempio, "smartphone").  . Model: [http://schema.org/Text](http://schema.org/Text)  
	- `telephone[string]`: Telefono di questo contatto    
	- `url[uri]`: URL che fornisce una descrizione o ulteriori informazioni su questo elemento    
- `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `id[*]`: Identificatore univoco dell'entità  - `image[uri]`: Un'immagine dell'articolo  . Model: [https://schema.org/URL](https://schema.org/URL)- `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `municipalityInfo[object]`: Informazioni sul comune corrispondenti a questa osservazione.  . Model: [https://schema.org/Text](https://schema.org/Text)	- `cityID[string]`: ID della città corrispondente a questa osservazione.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `cityName[string]`: Nome della città corrispondente a questa osservazione  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `district[string]`: Nome del distretto corrispondente a questa osservazione.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `stateName[string]`: Nome dello stato corrispondente a questa osservazione.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `ulbName[string]`: Nome dell'ente locale urbano corrispondente a questa osservazione.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `wardID[string]`: ID del reparto corrispondente a questa osservazione.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `wardName[string]`: Nome del reparto corrispondente a questa osservazione.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `wardNum[number]`: Numero del reparto corrispondente a questa osservazione.  . Model: [https://schema.org/Number](https://schema.org/Number)  
	- `zoneID[string]`: ID della zona corrispondente a questa osservazione.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `zoneName[string]`: Nome della zona corrispondente a questa osservazione.  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `name[string]`: Il nome di questo elemento  - `occupancy[number]`: Il numero di persone presenti nel punto di interesse. Dovrebbe essere inferiore alla capacità  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `priceRange[string]`: Stringa che descrive l'intervallo di prezzi dell'accesso al Punto di Interesse  - `refSeeAlso[array]`: Elenco di riferimenti a una o più entità correlate  . Model: [https://schema.org/URL](https://schema.org/URL)- `relevance[number]`: Rilevanza del punto di interesse per essere presentato in diversi livelli di zoom. 0 è il migliore Valori maggiori significano minore rilevanza  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `title[string]`: Questa proprietà contiene un nome dato al Punto di interesse oltre al nome specifico.  - `type[string]`: Tipo di entità NGSI. Deve essere PointOfInterest.  - `wardId[string]`: ID del rione dell'entità corrispondente a questa osservazione  - `zoneId[string]`: ID della zona dell'entità corrispondente a questa osservazione  - `zoneName[string]`: Nome della zona dell'entità corrispondente a questa osservazione  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `id`  - `name`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
Questa entità è utilizzata nelle applicazioni che utilizzano dati spaziali ed è applicabile ai segmenti verticali Automotive, Ambiente, Industria e Smart City e alle relative applicazioni IoT. Questo modello di dati è stato creato in collaborazione con il GSMA e i membri del [IoT Big Data Project](http://www.gsma.com/iot/iot-big-data/). Creato con il contributo del progetto IUDX.  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PointOfInterest:    
  description: This entity contains a harmonised geographic description of a Point of Interest    
  properties:    
    additionalInfoURL:    
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
      description: URL from which additional information of the subject can be obtained    
      x-ngsi:    
        type: Relationship    
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
    capacity:    
      description: The total number of people which can be allocated at the same time    
      type: number    
      x-ngsi:    
        type: Property    
    category:    
      description: Category of this point of interest    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    contactPoint:    
      description: The details to contact with the item    
      properties:    
        areaServed:    
          description: The geographic area where a service or offered item is provided. Supersedes serviceArea    
          type: string    
          x-ngsi:    
            type: Property    
        availabilityRestriction:    
          anyOf:    
            - description: Array of identifiers format of any NGSI entity    
              items:    
                maxLength: 256    
                minLength: 1    
                pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
                type: string    
              type: array    
              x-ngsi:    
                type: Property    
            - description: Array of identifiers format of any NGSI entity    
              items:    
                format: uri    
                type: string    
              type: array    
              x-ngsi:    
                type: Property    
          description: This property links a contact point to information about when the contact point is not available. The details are provided using the Opening Hours Specification class    
          x-ngsi:    
            model: http://schema.org/hoursAvailable    
            type: Relationship    
        availableLanguage:    
          anyOf:    
            - anyOf:    
                - type: string    
                - items:    
                    type: string    
                  type: array    
          description: 'A language someone may use with or at the item, service or place. Please use one of the language codes from the IETF BCP 47 standard. It is implemented the Text option but it could be also Language'    
          x-ngsi:    
            model: http://schema.org/availableLanguage    
            type: Property    
        contactOption:    
          anyOf:    
            - type: string    
            - items:    
                type: string    
              type: array    
          description: An option available on this contact point (e.g. a toll-free number or support for hearing-impaired callers)    
          x-ngsi:    
            model: http://schema.org/contactOption    
            type: Property    
        contactType:    
          description: Contact type of this item    
          type: string    
          x-ngsi:    
            type: Property    
        email:    
          description: Email address of owner    
          format: idn-email    
          type: string    
          x-ngsi:    
            type: Property    
        faxNumber:    
          description: The fax number of the item    
          type: string    
          x-ngsi:    
            model: http://schema.org/Text    
            type: Property    
        name:    
          description: The name of this item    
          type: string    
          x-ngsi:    
            type: Property    
        productSupported:    
          description: The product or service this support contact point is related to (such as product support for a particular product line). This can be a specific product or product line (e.g. 'iPhone') or a general category of products or services (e.g. 'smartphones')    
          type: string    
          x-ngsi:    
            model: http://schema.org/Text    
            type: Property    
        telephone:    
          description: Telephone of this contact    
          type: string    
          x-ngsi:    
            type: Property    
        url:    
          description: URL which provides a description or further information about this item    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
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
    image:    
      description: An image of the item    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
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
    municipalityInfo:    
      description: Municipality information corresponding to this observation.    
      properties:    
        cityID:    
          description: City ID corresponding to this observation.    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        cityName:    
          description: City name corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        district:    
          description: District name corresponding to this observation.    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        stateName:    
          description: Name of the state corresponding to this observation.    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        ulbName:    
          description: Name of the Urban Local Body corresponding to this observation.    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        wardID:    
          description: Ward ID corresponding to this observation.    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        wardName:    
          description: Ward name corresponding to this observation.    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        wardNum:    
          description: Ward number corresponding to this observation.    
          type: number    
          x-ngsi:    
            model: https://schema.org/Number    
            type: Property    
        zoneID:    
          description: Zone ID corresponding to this observation.    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        zoneName:    
          description: Zone name corresponding to this observation.    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    occupancy:    
      description: The count of people in the in the point of Interest. It should be smaller than capacity    
      type: number    
      x-ngsi:    
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
    priceRange:    
      description: String describing the range of prices of the access to the Point of Interest    
      type: string    
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
    relevance:    
      description: Relevance of the point of interest in order to be presented in different zoom levels. 0 is best larger values means lower relevance    
      type: number    
      x-ngsi:    
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
    title:    
      description: This property contains a name given to the Point of interest beyond specific name.    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be PointOfInterest    
      enum:    
        - PointOfInterest    
      type: string    
      x-ngsi:    
        type: Property    
    wardId:    
      description: Ward ID of the entity corresponding to this observation    
      type: string    
      x-ngsi:    
        type: Property    
    zoneId:    
      description: Zone ID of the entity corresponding to this observation    
      type: string    
      x-ngsi:    
        type: Property    
    zoneName:    
      description: Zone name of the entity corresponding to this observation    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - name    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2024 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.PointOfInterest/PointOfInterest/schema.json    
  x-model-tags: IUDX    
  x-version: 0.3.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### Valori chiave di PointOfInterest NGSI-v2 Esempio  
Ecco un esempio di PointOfInterest in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PointOfInterest-A-Concha-123456",  
  "type": "PointOfInterest",  
  "name": "Playa de a Concha",  
  "description": "La Playa de A Concha se presenta como una continuaci\u00f3n de la Playa de Compostela, una de las m\u00e1s frecuentadas de Vilagarc\u00eda.",  
  "address": {  
    "addressCountry": "ES",  
    "addressLocality": "Vilagarc\u00eda de Arousa"  
  },  
  "category": [  
    "113"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -8.768460000000001,  
      42.60214472222222  
    ]  
  },  
  "municipalityInfo": {  
    "district": "Bangalore Urban",  
    "ulbName": "BMC",  
    "cityID": "23",  
    "stateName": "Karnataka",  
    "cityName": "Bangalore",  
    "zoneID": "2",  
    "wardNum": 4  
  },  
  "source": "http://www.tourspain.es",  
  "refSeeAlso": [  
    "Beach-A-Concha-123456"  
  ],  
  "wardId": "",  
  "zoneId": "",  
  "additionalInfoURL": "urn:ngsi-ld:Point:34E4:A234",  
  "zoneName": "",  
  "title": "Cusamè",  
  "relevance": 1,  
  "image": "https://smartdatamodels.org/extra/cusame.png",  
  "priceRange": "25-150€",  
  "capacity": 55,  
  "occupancy": 50  
}  
```  
</details>  
#### PointOfInterest NGSI-v2 normalizzato Esempio  
Ecco un esempio di PointOfInterest in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "PointOfInterest-A-Concha-123456",  
  "type": "PointOfInterest",  
  "category": {  
    "type": "StructuredValue",  
    "value": [  
      "113"  
    ]  
  },  
  "description": {  
    "type": "Text",  
    "value": "La Playa de A Concha se presenta como una continuaciin de la Playa de Compostela, una de las mis frecuentadas de Vilagarcia."  
  },  
  "refSeeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "Beach-A-Concha-123456"  
    ]  
  },  
  "source": {  
    "type": "Text",  
    "value": "http://www.tourspain.es"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -8.768460000000001,  
        42.60214472222222  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "addressCountry": "ES",  
      "addressLocality": "Vilagarcia de Arousa"  
    }  
  },  
  "municipalityInfo": {  
    "type": "StructuredValue",  
    "value": {  
      "district": "Bangalore Urban",  
      "ulbName": "BMC",  
      "cityID": "23",  
      "stateName": "Karnataka",  
      "cityName": "Bangalore",  
      "zoneID": "2",  
      "wardNum": 4  
    }  
  },  
  "name": {  
    "type": "Text",  
    "value": "Playa de a Concha"  
  },  
  "wardId": {  
    "type": "Text",  
    "value": ""  
  },  
  "zoneId": {  
    "type": "Text",  
    "value": ""  
  },  
  "additionalInfoURL": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Point:34E4:A234"  
  },  
  "zoneName": {  
    "type": "Text",  
    "value": ""  
  },  
  "title": {  
    "type": "Text",  
    "value": "Cusamè"  
  },  
  "relevance": {  
    "type": "Number",  
    "value": 1  
  },  
  "image": {  
    "type": "URL",  
    "value": "https://smartdatamodels.org/extra/cusame.png"  
  },  
  "priceRange": {  
    "type": "Text",  
    "value": "25-150€"  
  },  
  "capacity": {  
    "type": "Number",  
    "value": 55  
  },  
  "occupancy": {  
    "type": "Number",  
    "value": 50  
  }  
}  
```  
</details>  
#### Valori chiave di PointOfInterest NGSI-LD Esempio  
Ecco un esempio di PointOfInterest in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PointOfInterest:PointOfInterest-A-Concha-123456",  
  "type": "PointOfInterest",  
  "additionalInfoURL": "urn:ngsi-ld:Point:34E4:A234",  
  "address": {  
    "addressCountry": "ES",  
    "addressLocality": "Vilagarcia de Arousa"  
  },  
  "category": [  
    "113"  
  ],  
  "description": "La Playa de A Concha se presenta como una continuacion de la Playa de Compostela, una de las mas frecuentadas de Vilagarcia.",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -8.768460000000001,  
      42.60214472222222  
    ]  
  },  
  "municipalityInfo": {  
    "district": "Bangalore Urban",  
    "ulbName": "BMC",  
    "cityID": "23",  
    "stateName": "Karnataka",  
    "cityName": "Bangalore",  
    "zoneID": "2",  
    "wardNum": 4  
  },  
  "name": "Playa de a Concha",  
  "refSeeAlso": [  
    "urn:ngsi-ld:SeeAlso:Beach-A-Concha-123456"  
  ],  
  "source": "http://www.tourspain.es",  
  "wardId": "",  
  "zoneId": "",  
  "zoneName": "",  
  "title": "Cusamè",  
  "relevance": 1,  
  "image": "https://smartdatamodels.org/extra/cusame.png",  
  "priceRange": "25-150€",  
  "capacity": 55,  
  "occupancy": 50  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.PointOfInterest/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### PointOfInterest NGSI-LD normalizzato Esempio  
Ecco un esempio di PointOfInterest in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PointOfInterest:PointOfInterest-A-Concha-123456",  
  "type": "PointOfInterest",  
  "additionalInfoURL": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Point:34E4:A234"  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "ES",  
      "addressLocality": "Vilagarcia de Arousa"  
    }  
  },  
  "category": {  
    "type": "Property",  
    "value": [  
      "113"  
    ]  
  },  
  "description": {  
    "type": "Property",  
    "value": "La Playa de A Concha se presenta como una continuacion de la Playa de Compostela, una de las mas frecuentadas de Vilagarcia."  
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
  "municipalityInfo": {  
    "type": "Property",  
    "value": {  
      "district":"Bangalore Urban",  
      "ulbName":"BMC",  
      "cityID":"23",  
      "stateName":"Karnataka",  
      "cityName":"Bangalore",  
      "zoneID":"2",  
      "wardNum":4  
    }  
  },  
  "name": {  
    "type": "Property",  
    "value": "Playa de a Concha"  
  },  
  "refSeeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:SeeAlso:Beach-A-Concha-123456"  
    ]  
  },  
  "source": {  
    "type": "Property",  
    "value": "http://www.tourspain.es"  
  },  
  "wardId": {  
    "type": "Property",  
    "value": ""  
  },  
  "zoneId": {  
    "type": "Property",  
    "value": ""  
  },  
  "zoneName": {  
    "type": "Property",  
    "value": ""  
  },  
  "title": {  
    "type": "Property",  
    "value": "Cusamè"  
  },  
  "relevance": {  
    "type": "Property",  
    "value": 1  
  },  
  "image": {  
    "type": "Property",  
    "value": "https://smartdatamodels.org/extra/cusame.png"  
  },  
  "priceRange": {  
    "type": "Property",  
    "value": "25-150€"  
  },  
  "capacity": {  
    "type": "Property",  
    "value": 55  
  },  
  "occupancy": {  
    "type": "Property",  
    "value": 50  
  }  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.PointOfInterest/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
