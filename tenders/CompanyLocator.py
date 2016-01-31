import googlemaps


class CompanyLocator:
    def __init__(self, gmapsClient):
        self.gmapsClient = gmapsClient

    def getLocation(self, address):
        geocodeResult = self.gmapsClient.geocode(address)
        # print(json.dumps(geocodeResult, indent=4, sort_keys=True))
        location = geocodeResult[0].get('geometry').get('location')
        return location
