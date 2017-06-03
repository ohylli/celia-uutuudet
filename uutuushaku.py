#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

UUTUUDET_URL = 'https://www.celianet.fi/kirjavinkit/uutuuskirjat-aikuisille/'
TIEDOSTO_NIMI = 'uutuudet.txt'

def kirjoita( tiedosto, sisältö ):
    tiedosto.write( bytes( sisältö +'\r\n\r\n', 'utf-8' ))

if __name__ == '__main__':
    vastaus = requests.get( UUTUUDET_URL )
    if vastaus.status_code != 200:
        print( 'Uutuusluettelon haku epäonnistui. HTTP status koodi: ' +str( vastaus.status_code ))
        
    tiedosto = open( TIEDOSTO_NIMI, 'wb' )
    uutuudetSivu = BeautifulSoup( vastaus.text, 'html.parser' )
    for elementti in uutuudetSivu.find( role='main' ).h3.previous_sibling.next_siblings:
        if elementti.name == 'h3':
            kategoria = elementti.get_text() 
            kirjoita( tiedosto, kategoria )
            
        elif elementti.name == 'p':
            kirja = elementti.get_text()
            kirjoita( tiedosto, kirja )
            kirjaURL = elementti.a['href']
            vastaus = requests.get( kirjaURL )
            if vastaus.status_code != 200:
                print( 'Kirjan ' +elementti.a.get_text() +' tietojen haku epäonnistui. HTTP status koodi: ' +str( vastaus.status_code ))
                
            kirjaSivu = BeautifulSoup( vastaus.text, 'html.parser' )
            kuvaus = kirjaSivu.p.get_text()
            kirjoita( tiedosto, kuvaus )