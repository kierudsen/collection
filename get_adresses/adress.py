import requests


class GetAdress:

    def __init__(self, nord, oest, radius):
        self.nord = nord
        self.oest = oest
        self.radius = radius
        self.response = requests.get(
            f'https://ws.geonorge.no/adresser/v1/punktsok?radius={self.radius}&lat={self.nord}&lon={self.oest}&treffPerSide=10&side=0&asciiKompatibel=true')

    def is_ok(self):
        return self.response.status_code

    def get_list(self):
        result = self.response.json()
        adr_list = []
        for i in result['adresser']:
            adr_list.append(i['adressetekst'])
        return adr_list
