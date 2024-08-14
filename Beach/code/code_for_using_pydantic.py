from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import (
    AnyUrl,
    AwareDatetime,
    BaseModel,
    Field,
    RootModel,
    confloat,
    constr,
)


class AccessTypeEnum(Enum):
    privateVehicle = 'privateVehicle'
    boat = 'boat'
    onFoot = 'onFoot'
    publicTransport = 'publicTransport'


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


class BeachTypeEnum(Enum):
    whiteSand = 'whiteSand'
    urban = 'urban'
    isolated = 'isolated'
    calmWaters = 'calmWaters'
    blueFlag = 'blueFlag'
    Q_Quality = 'Q-Quality'
    strongWaves = 'strongWaves'
    windy = 'windy'
    blackSand = 'blackSand'


class Facility(Enum):
    promenade = 'promenade'
    showers = 'showers'
    cleaningServices = 'cleaningServices'
    lifeGuard = 'lifeGuard'
    sunshadeRental = 'sunshadeRental'
    sunLoungerRental = 'sunLoungerRental'
    waterCraftRental = 'waterCraftRental'
    toilets = 'toilets'
    touristOffice = 'touristOffice'
    litterBins = 'litterBins'
    telephone = 'telephone'
    surfPracticeArea = 'surfPracticeArea'
    accessforDisabled = 'accessforDisabled'


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


class OccupationRate(Enum):
    high = 'high'
    medium = 'medium'
    low = 'low'
    none = 'none'


class Type6(Enum):
    Beach = 'Beach'


class Beach(BaseModel):
    accessType: Optional[List[AccessTypeEnum]] = Field(
        None,
        description="Enum:'privateVehicle, boat, onFoot, publicTransport'. Describes how to get to this beach",
        min_length=1,
    )
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    beachType: Optional[List[BeachTypeEnum]] = Field(
        None,
        description="Type of beach according to different criteria. Enum:'whiteSand, urban, isolated, calmWaters, blueFlag, Q-Quality, strongWaves, windy, blackSand'. Or any other value needed by an application",
        min_length=1,
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
    dateObserved: Optional[AwareDatetime] = Field(
        None, description='Date of the observed entity defined by the user'
    )
    description: Optional[str] = Field(None, description='A description of this item')
    facilities: Optional[List[Facility]] = Field(
        None,
        description="Describes different facilities offered by this beach. Enum:'promenade, showers, cleaningServices, lifeGuard, sunshadeRental, sunLoungerRental, waterCraftRental, toilets, touristOffice, litterBins, telephone,surfPracticeArea, accessforDisabled'",
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
    length: Optional[float] = Field(None, description='Length of this beach')
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    occupationRate: Optional[OccupationRate] = Field(
        None,
        description="Typical occupation rate of this beach. Enum:'low, medium, high, none'",
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
    peopleOccupancy: Optional[confloat(ge=0.0)] = Field(
        None, description='Amount of people at the location'
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
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be Beach'
    )
    width: Optional[float] = Field(None, description='Width of this beach')
