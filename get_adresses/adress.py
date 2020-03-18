import requests

response = requests.get('https://ws.geonorge.no/adresser/v1/')
print(response.status_code) # If 200 you are good to go

def samlet():
    nord = input('lat/nord:')
    oest = input('lon/øst:')
    rundt = input('radius:')
    return f'https://ws.geonorge.no/adresser/v1/punktsok?radius={rundt}&lat={nord}&lon={oest}&treffPerSide=10&side=0&asciiKompatibel=true'

#61.086398, 10.485384 just an example
response = requests.get(samlet())

result = response.json()

for i in result['adresser']:
    print(i['adressetekst'], i['postnummer'], i['kommunenavn'])