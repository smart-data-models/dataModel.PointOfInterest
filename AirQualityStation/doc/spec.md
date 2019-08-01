# Air quality station

The formal documentation is not available yet. In the meantime please check some
of the examples of use.

**Note**: JSON Schemas are intended to capture the data type and associated
constraints of the different Attributes, regardless their final representation
format in NGSI(v2, LD).

## Examples of use

    {
      "address": {
        "addressCountry": "ES",
        "addressLocality": "Madrid",
        "streetAddress": "Plaza de España"
      },
      "category": "AirQualityStation",
      "location": {
        "type": "Point",
        "coordinates": [
          -3.712247222222222,
          40.423852777777775
        ]
      },
      "name": "Pza. de España",
      "source": "http://datos.madrid.es",
      "type": "PointOfInterest",
      "id": "AirQualityStation-ES-Madrid-004"
    }
