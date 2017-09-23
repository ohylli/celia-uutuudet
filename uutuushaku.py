# -*- coding: utf-8 -*-

# luokka uutuusluetteloiden käsittelyyn
from uutuusluettelo import Uutuusluettelo
# luokka kirjanpitämiseen edellisen luettelon luonti kkerran kirjoista
from kasitellyt import Käsitellyt

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

# olio, josta luetaan edellisen luettelon luonti kerran uusimmat kirjat eri kategorioista, joita vanhempia
# kirjoja ei lisätä nyt luotaviin luetteloihin.
# tähän myös tallennetaan tällä hetkellä uusimmat kirjat eri kategorioista, jolloin niitä ei luetteloida ensi kerralla
# tiedot luetaan ja tallennetaan json muodossa vanhat.json tiedostoon
vanhat = Käsitellyt( "vanhat.json" )
# käsitellään jokainen luettelo
for luettelo in luettelot:
    # luodaan luettelon käsittely luokasta instanssi, jolle annetaan osoite, josta luettelo löytyy, nimi tiedostolle, johon uutuudet tallennetaan, sekä tiedot käsitellyistä kirjoista
    hakija = luettelo['luettelo']( luettelo['url'], luettelo['tiedosto'], vanhat )
    # haetaan kirjat ja tallennetaan tiedostoon
    hakija.haeKirjat()

# tallennetaan tämän luettelon eri kategorioiden uusimmat seuraavaa kertaa varten    
vanhat.tallenna()