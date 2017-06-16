# -*- coding: utf-8 -*-

from uutuusluettelo import Uutuusluettelo

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
    }
]

for luettelo in luettelot:
    hakija = luettelo['luettelo']( luettelo['url'], luettelo['tiedosto'] )
    hakija.haeKirjat()