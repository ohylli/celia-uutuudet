# -*- coding: utf-8 -*-

# luokat uutuusluetteloiden k‰sittelyyn
from uutuusluettelo import Uutuusluettelo, NuortenUutuudet

# m‰‰ritet‰‰n mit‰ uutuusluetteloita k‰sitell‰‰n
# luettelosta m‰‰ritet‰‰n osoite mist‰ uutuudet lˆytyv‰t
# tiedosto, johon ne tallennetaan ja luokka, jonka instanssilla luettelo k‰sitell‰‰n
luettelot = [
    {
        'url': 'https://www.celianet.fi/kirjavinkit/uutuuskirjat-aikuisille/',
        'tiedosto': 'aikuisten_uutuudet.txt',
        'luettelo': Uutuusluettelo
    },
    {
        'url': 'https://www.celianet.fi/kirjavinkit/lasten-uutuuskirjat/',
        'tiedosto': 'lasten_uutuudet.txt',
        'luettelo': Uutuusluettelo
    },
    {
        'url': 'https://www.celianet.fi/kirjavinkit/nuorten-uutuuskirjat/',
        'tiedosto': 'nuorten_uutuudet.txt',
        'luettelo': NuortenUutuudet
    }
]

# k‰sitell‰‰n jokainen luettelo
for luettelo in luettelot:
    # luodaan luettelon k‰sittely luokasta instanssi, jolle annetaan osoite, josta luettelo lˆytyy ja nimi tiedostolle, johon uutuudet tallennetaan
    hakija = luettelo['luettelo']( luettelo['url'], luettelo['tiedosto'] )
    # haetaan kirjat ja tallennetaan tiedostoon
    hakija.haeKirjat()