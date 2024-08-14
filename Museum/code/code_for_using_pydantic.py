from __future__ import annotations

from datetime import date, time
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, RootModel, constr


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class BuildingTypeEnum(Enum):
    prehistoricPlace = 'prehistoricPlace'
    acropolis = 'acropolis'
    alcazaba = 'alcazaba'
    aqueduct = 'aqueduct'
    alcazar = 'alcazar'
    amphitheatre = 'amphitheatre'
    arch = 'arch'
    polularArchitecture = 'polularArchitecture'
    basilica = 'basilica'
    road = 'road'
    chapel = 'chapel'
    cartuja = 'cartuja'
    nobleHouse = 'nobleHouse'
    residence = 'residence'
    castle = 'castle'
    castro = 'castro'
    catacombs = 'catacombs'
    cathedral = 'cathedral'
    cloister = 'cloister'
    convent = 'convent'
    prehistoricCave = 'prehistoricCave'
    dolmen = 'dolmen'
    officeBuilding = 'officeBuilding'
    houseBuilding = 'houseBuilding'
    industrialBuilding = 'industrialBuilding'
    militaryBuilding = 'militaryBuilding'
    hermitage = 'hermitage'
    fortress = 'fortress'
    sculpturalGroups = 'sculpturalGroups'
    church = 'church'
    garden = 'garden'
    fishMarket = 'fishMarket'
    masia = 'masia'
    masiaFortificada = 'masiaFortificada'
    minaret = 'minaret'
    monastery = 'monastery'
    monolith = 'monolith'
    walls = 'walls'
    necropolis = 'necropolis'
    menhir = 'menhir'
    mansion = 'mansion'
    palace = 'palace'
    pantheon = 'pantheon'
    pazo = 'pazo'
    pyramid = 'pyramid'
    bridge = 'bridge'
    gate = 'gate'
    arcade = 'arcade'
    walledArea = 'walledArea'
    sanctuary = 'sanctuary'
    grave = 'grave'
    synagogue = 'synagogue'
    taulasTalayotsNavetas = 'taulasTalayotsNavetas'
    theathre = 'theathre'
    temple = 'temple'
    spring = 'spring'
    tower = 'tower'
    archeologicalSite = 'archeologicalSite'
    university = 'university'
    graveyard = 'graveyard'
    fortifiedTemple = 'fortifiedTemple'
    civilEngineering = 'civilEngineering'
    square = 'square'
    seminar = 'seminar'
    bullfightingRing = 'bullfightingRing'
    publicBuilding = 'publicBuilding'
    town = 'town'
    cavesAndTouristicMines = 'cavesAndTouristicMines'
    proCathedral = 'proCathedral'
    mosque = 'mosque'
    circus = 'circus'
    burialMound = 'burialMound'


class Facility(Enum):
    elevator = 'elevator'
    cafeteria = 'cafeteria'
    shop = 'shop'
    auditory = 'auditory'
    conferenceRoom = 'conferenceRoom'
    audioguide = 'audioguide'
    cloakRoom = 'cloakRoom'
    forDisabled = 'forDisabled'
    forBabies = 'forBabies'
    guidedTour = 'guidedTour'
    restaurant = 'restaurant'
    ramp = 'ramp'
    reservation = 'reservation'


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class MuseumTypeEnum(Enum):
    appliedArts = 'appliedArts'
    scienceAndTechnology = 'scienceAndTechnology'
    fineArts = 'fineArts'
    music = 'music'
    history = 'history'
    sacredArt = 'sacredArt'
    archaeology = 'archaeology'
    specials = 'specials'
    decorativeArts = 'decorativeArts'
    literature = 'literature'
    medicineAndPharmacy = 'medicineAndPharmacy'
    maritime = 'maritime'
    transports = 'transports'
    military = 'military'
    wax = 'wax'
    popularArtsAndTraditions = 'popularArtsAndTraditions'
    numismatic = 'numismatic'
    unesco = 'unesco'
    ceramics = 'ceramics'
    sumptuaryArts = 'sumptuaryArts'
    naturalScience = 'naturalScience'
    prehistoric = 'prehistoric'
    ethnology = 'ethnology'
    railway = 'railway'
    mining = 'mining'
    textile = 'textile'
    sculpture = 'sculpture'
    multiDisciplinar = 'multiDisciplinar'
    painting = 'painting'
    paleonthology = 'paleonthology'
    modernArt = 'modernArt'
    thematic = 'thematic'
    architecture = 'architecture'
    museumHouse = 'museumHouse'
    cathedralMuseum = 'cathedralMuseum'
    diocesanMuseum = 'diocesanMuseum'
    universitary = 'universitary'
    contemporaryArt = 'contemporaryArt'
    bullfighting = 'bullfighting'


class DayOfWeek(Enum):
    Monday = 'Monday'
    Tuesday = 'Tuesday'
    Wednesday = 'Wednesday'
    Thursday = 'Thursday'
    Friday = 'Friday'
    Saturday = 'Saturday'
    Sunday = 'Sunday'
    PublicHolidays = 'PublicHolidays'


class DayOfWeek1(Enum):
    https___schema_org_Monday = 'https://schema.org/Monday'
    https___schema_org_Tuesday = 'https://schema.org/Tuesday'
    https___schema_org_Wednesday = 'https://schema.org/Wednesday'
    https___schema_org_Thursday = 'https://schema.org/Thursday'
    https___schema_org_Friday = 'https://schema.org/Friday'
    https___schema_org_Saturday = 'https://schema.org/Saturday'
    https___schema_org_Sunday = 'https://schema.org/Sunday'
    https___schema_org_PublicHolidays = 'https://schema.org/PublicHolidays'


class OpeningHoursSpecificationItem(BaseModel):
    closes: Optional[time] = Field(
        None,
        description=' \\tThe closing hour of the place or service on the given day(s) of the week',
    )
    dayOfWeek: Optional[Union[DayOfWeek, DayOfWeek1]] = Field(
        None,
        description='The day of the week for which these opening hours are valid. URLs from GoodRelations (http://purl.org/goodrelations/v1) are used (for Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday plus a special entry for PublicHolidays)',
    )
    opens: Optional[time] = Field(
        None,
        description='The opening hour of the place or service on the given day(s) of the week',
    )
    validFrom: Optional[Union[date, AwareDatetime]] = Field(
        None,
        description='The date when the item becomes valid. A date value in the form CCYY-MM-DD or a combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] in ISO 8601 date format',
    )
    validThrough: Optional[Union[date, AwareDatetime]] = Field(
        None,
        description='The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours. A date value in the form CCYY-MM-DD or a combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] in ISO 8601 date format',
    )


class Type6(Enum):
    Museum = 'Museum'


class Museum(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    artPeriod: Optional[List[str]] = Field(
        None,
        description='Allowed values:-Those defined by [Wikipedia](https://en.wikipedia.org/wiki/Art_periods).- Any other extended value needed by an application and not described by the above resource',
        min_length=1,
    )
    buildingType: Optional[List[BuildingTypeEnum]] = Field(
        None,
        description="Type of building that hosts the museum. Enum:'prehistoricPlace, acropolis, alcazaba,aqueduct, alcazar, amphitheatre, arch, polularArchitecture,basilica, road, chapel, cartuja, nobleHouse, residence,castle, castro, catacombs, cathedral, cloister, convent,prehistoricCave, dolmen, officeBuilding, houseBuilding,industrialBuilding, militaryBuilding, hermitage, fortress,sculpturalGroups, church, garden, fishMarket, masia,masiaFortificada, minaret, monastery, monolith, walls,necropolis, menhir, mansion, palace, pantheon, pazo,pyramid, bridge, gate, arcade, walledArea, sanctuary,grave, synagogue, taulasTalayotsNavetas, theathre, temple,spring, tower, archeologicalSite, university, graveyard,fortifiedTemple, civilEngineering, square, seminar,bullfightingRing, publicBuilding, town, cavesAndTouristicMines,proCathedral, mosque, circus, burialMound'",
    )
    contactPoint: Optional[Dict[str, Any]] = Field(
        None, description='Contact point for the museum'
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    facilities: Optional[List[Facility]] = Field(
        None,
        description="Describes different facilities offered by this museum. Enum:'elevator, cafeteria, shop, auditory,conferenceRoom, audioguide, cloakRoom, forDisabled, forBabies,guidedTour, restaurant, ramp, reservation'. or any other value needed by an application",
        min_length=1,
    )
    featuredArtist: Optional[
        List[
            Optional[
                Union[
                    Union[
                        constr(
                            pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                            min_length=1,
                            max_length=256,
                        ),
                        AnyUrl,
                    ],
                    str,
                ]
            ]
        ]
    ] = Field(None, description='Main featured artist(s) at this museum')
    historicalPeriod: Optional[List[str]] = Field(
        None,
        description="An ISO8601 time interval. For example 1920/1940. The second element of the interval can be left empty to denote 'till now'. A comma separated list of years, for instance 1620,1625,1718.       -   A century, represented by a year pattern, for instance 19xx would correspond to the twentieth century. And 196x would correspond to the sixties decade",
        min_length=1,
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    museumType: Optional[List[MuseumTypeEnum]] = Field(
        None,
        description="Type of museum according to the exhibited content. Enum:'appliedArts, scienceAndTechnology, fineArts,music, history, sacredArt, archaeology, specials,decorativeArts, literature, medicineAndPharmacy, maritime,transports, military, wax, popularArtsAndTraditions,numismatic, unesco, ceramics, sumptuaryArts, naturalScience,prehistoric, ethnology, railway, mining, textile, sculpture,multiDisciplinar, painting, paleonthology, modernArt,thematic, architecture, museumHouse, cathedralMuseum,diocesanMuseum, universitary, contemporaryArt, bullfighting'. Other possible source for museum types not covered above is [Wikipedia](https://en.wikipedia.org/wiki/Category:Types_of_museum)",
        min_length=1,
    )
    name: Optional[str] = Field(None, description='The name of this item')
    openingHoursSpecification: Optional[List[OpeningHoursSpecificationItem]] = Field(
        None,
        description='A structured value providing information about the opening hours of a place or a certain service inside a place',
        min_length=1,
    )
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    refSeeAlso: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(None, description='List of references to one or more related entities')
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    touristArea: Optional[str] = Field(
        None,
        description='Tourist area at which this museum is located. Precise semantics might depend on the application or target country or region. For instance `Costa del Sol`',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be Museum'
    )
