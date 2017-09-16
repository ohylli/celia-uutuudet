# -*- coding: utf-8 -*-

# luokat uutuusluetteloiden käsittelyyn
from uutuusluettelo import Uutuusluettelo

# määritetään mitä uutuusluetteloita käsitellään
# luettelosta määritetään osoite mistä uutuudet löytyvät
# tiedosto, johon ne tallennetaan ja luokka, jonka instanssilla luettelo käsitellään
luettelot = [
    {
        'url': 'https://www.celianet.fi/kirjavinkit/uutuuskirjat-aikuisille/',
        'tiedosto': 'aikuisten_uutuudet.txt',
        'luettelo': Uutuusluettelo
    },
    {
        'url': 'https://www.celianet.fi/kirjavinkit/lasten-uutuuskirjat/',
        'tiedosto': 'lasten_ja_nuorten_uutuudet.txt',
        'luettelo': Uutuusluettelo
    }
]

# käsitellään jokainen luettelo
for luettelo in luettelot:
    # luodaan luettelon käsittely luokasta instanssi, jolle annetaan osoite, josta luettelo löytyy ja nimi tiedostolle, johon uutuudet tallennetaan
    hakija = luettelo['luettelo']( luettelo['url'], luettelo['tiedosto'] )
    # haetaan kirjat ja tallennetaan tiedostoon
    hakija.haeKirjat()