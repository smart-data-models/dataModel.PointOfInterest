Entidad: Museo  
==============  
[Licencia abierta](https://github.com/smart-data-models//dataModel.PointOfInterest/blob/master/Museum/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Un museo**  

## Lista de propiedades  

- `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `artPeriod`: Valores permitidos:-Los definidos por [Wikipedia](https://en.wikipedia.org/wiki/Art_periods).- Cualquier otro valor extendido que necesite una aplicación y que no esté descrito por el recurso anterior.  - `buildingType`: Tipo de edificio que alberga el museo. Enum:'lugar prehistórico, acrópolis, alcazaba,acueducto, alcázar, anfiteatro, arco, arquitectura polular,basílica, camino, capilla, cartuja, casa nobiliaria, residencia, castillo, castro, catacumbas, catedral, claustro, convento, cueva prehistórica, dolmen, edificio de oficinas, edificio de viviendas, edificio industrial, edificio militar, ermita, fortaleza, grupos escultóricos, iglesia, jardín, lonja, masía, masía fortificada, alminar, monasterio, monolito, murallas, necrópolis, menhir, mansión, palacio, panteón, pazo, pirámide, puente, puerta, pórtico, recinto amurallado, santuario, tumba, sinagoga, taulasTalayotsNavetas, templo, fuente, torre, sitio arqueológico, universidad, cementerio, templo fortificado, ingeniería civil, plaza, seminario, plaza de toros, edificio público, ciudad, cuevas y minas turísticas, catedral, mezquita, circo, túmulo".  - `contactPoint`: Punto de contacto del museo.  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `facilities`: Describe las diferentes instalaciones que ofrece este museo. Enum:'ascensor, cafetería, tienda, auditorio, sala de conferencias, audioguía, guardarropa, para discapacitados, para bebés, visita guiada, restaurante, rampa, reserva'. o cualquier otro valor que necesite una aplicación.  - `featuredArtist`: Artista(s) principal(es) en este museo.  - `historicalPeriod`: Un intervalo de tiempo ISO8601. Por ejemplo, 1920/1940. El segundo elemento del intervalo puede dejarse vacío para indicar "hasta ahora". Una lista de años separados por comas, por ejemplo 1620,1625,1718.       - Un siglo, representado por un patrón de años, por ejemplo 19xx correspondería al siglo XX. Y 196x correspondería a la década de los sesenta.  - `id`: Identificador único de la entidad  - `location`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `museumType`: Tipo de museo según el contenido expuesto. Enum:Artes aplicadas, ciencia y tecnología, bellas artes, música, historia, arte sacro, arqueología, especialidades, artes decorativas, literatura, medicina y farmacia, marítimo, transportes, militar, cera, artes populares y tradiciones, numismática, unesco, cerámica, artes suntuarias, ciencias naturales, prehistoria, etnología, ferrocarril, minería, textil, escultura, multidisciplinar, pintura, paleontología, arte moderno, temático, arquitectura, casa-museo, museo catedralicio, museo diocesano, universitario, arte contemporáneo, taurino". Otra posible fuente para los tipos de museos no contemplados anteriormente es [Wikipedia](https://en.wikipedia.org/wiki/Category:Types_of_museum).  - `name`: El nombre de este artículo.  - `openingHoursSpecification`: Un valor estructurado que proporciona información sobre el horario de apertura de un lugar o de un determinado servicio dentro de un lugar  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `refSeeAlso`: Lista de referencias a una o más entidades relacionadas.  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `touristArea`: Zona turística en la que se encuentra este museo. La semántica precisa puede depender de la aplicación o del país o región de destino. Por ejemplo, "Costa del Sol".  - `type`: Tipo de entidad NGSI. Tiene que ser Museo    
Propiedades requeridas  
- `id`  - `location`  - `name`  - `type`    
Esta entidad contiene una descripción geográfica armonizada de un museo. Se usa en aplicaciones que utilizan datos espaciales y es aplicable a los segmentos verticales de Turismo, Cultura y Ciudades Inteligentes y a las aplicaciones de IoT relacionadas. Un agradecimiento especial a [TURESPAÑA](https://www.tourspain.es/en-us) que proporcionó algunos ejemplos que inspiraron el desarrollo de este modelo de datos.  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
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
    artPeriod:    
      description: 'Allowed values:-Those defined by [Wikipedia](https://en.wikipedia.org/wiki/Art_periods).- Any other extended value needed by an application and not described by the above resource.'    
      items:    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: 'https://schema.org/Text.Corresponds to the art period(s) of the exhibitions made by this museum'    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    contactPoint:    
      description: 'Contact point for the museum.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/ContactPoint    
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
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: https://schema.org/Text    
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
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: https://schema.org/Person    
    historicalPeriod:    
      description: 'An ISO8601 time interval. For example 1920/1940. The second element of the interval can be left empty to denote ''till now''. A comma separated list of years, for instance 1620,1625,1718.       -   A century, represented by a year pattern, for instance 19xx would correspond to the twentieth century. And 196x would correspond to the sixties decade.'    
      items:    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: https://schema.org/Text    
    id:    
      anyOf: *museum_-_properties_-_id_-_anyof    
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
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: https://schema.org/Text    
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
        anyOf: *museum_-_properties_-_id_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    refSeeAlso:    
      description: 'List of references to one or more related entities.'    
      items:    
        anyOf:    
          - anyOf: *museum_-_properties_-_id_-_anyof    
            description: 'Property. Unique identifier of the entity'    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: https://schema.org/URL    
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
    touristArea:    
      description: 'Tourist area at which this museum is located. Precise semantics might depend on the application or target country or region. For instance `Costa del Sol`.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    type:    
      description: 'NGSI Entity type. It has to be Museum'    
      enum:    
        - Museum    
      type: Property    
  required:    
    - id    
    - type    
    - location    
    - name    
  type: object    
```  
</details>    
Este tipo de entidad ha sido diseñado como una extensión de [https://schema.org/Museum](https://schema.org/Museum) para que cualquier propiedad especificada por schema.org y cuyo dominio sea `https://schema.org/Museum` pueda ser utilizada por las aplicaciones.  
## Ejemplo de carga útil  
#### Museo NGSI-v2 valores-clave Ejemplo  
Aquí hay un ejemplo de un Museo en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### Museo NGSI-v2 normalizado Ejemplo  
He aquí un ejemplo de un Museo en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### Museo NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un Museo en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### Museo NGSI-LD normalizado Ejemplo  
He aquí un ejemplo de un Museo en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud