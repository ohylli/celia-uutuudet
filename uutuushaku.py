﻿# -*- coding: utf-8 -*-

# kirjasto HTTP pyyntöjen tekemiseen eli nettisivun hakuun
import requests
# kirjasto HTML:n parsimiseen
from bs4 import BeautifulSoup

class UutuusHaku():
    
    def __init__( self, luetteloUrl, tiedostonimi ):
        # uutuudet sivun osoite
        self.url = luetteloUrl
        # avataan tiedosto tietojen tallentamista varten
        self.tiedosto = open( tiedostonimi, 'wb' )

    # funktio joka kirjoittaa annetun sisällön annettuun tiedostoon
    def kirjoita( self, sisältö ):
        # lisätään pari rivinvaihtoa sisällön perään ja tallennetaan utf-8 koodauksella
        self.tiedosto.write( bytes( sisältö +'\r\n\r\n', 'utf-8' ))

    def haeSivu( self, url ):
        vastaus = requests.get( url )
        # tarkistetaan, että pyyntö onnistui
        if vastaus.status_code != 200:
            print( 'Sivun haku epäonnistui. HTTP status koodi: ' +str( vastaus.status_code ))
            # lopetetaan ohjelma
            quit()
            
        return BeautifulSoup( vastaus.text, 'html.parser' )
        
    def haeKirjat( self ):
        # haetaan ja parsitaan uutuudet sivun html
        self.uutuudetSivu = self.haeSivu( self.url )
        for elementti in self.käsitteleSivu():
            if elementti['tyyppi'] == 'kategoria':
                self.kirjoita( elementti['kategoria'] )
        
            elif elementti['tyyppi'] == 'linkki':
                self.kirjoita( elementti['kirja'] )
                # ja haetaan kirjan tiedot sisältävä sivu
                # parsitaan kirjan kuvauksen sisältävän sivun html
                kirjaSivu = self.haeSivu( elementti['kirjaURL'] )
                # kuvaus on sivun ensimmäisessä tekstikappaleessa
                # otetaan talteen ja kirjoitetaan tiedostoon
                kuvaus = kirjaSivu.p.get_text()
                self.kirjoita( kuvaus )
    
        # valmista tuli, suljetaan tiedosto
        self.tiedosto.close()
        
    def käsitteleSivu( self ):
        # käydään sivun sisältö läpi elementti kerrallaan
        # lähtien ensimmäisestä kolmos tason ) otsikosta (h3, joka on sivun pääsisältö alueella
        # tarkemmin käsitellään ensimmäistä h3:a edeltävää elementtiä seuraavat saman tason elementit
        # näin ensimmäinenkin h3 tulee mukaan
        for elementti in self.uutuudetSivu.find( role='main' ).h3.previous_sibling.next_siblings:
            if elementti.name == 'h3':
                # elementti on otsikko, jossa on uutuuskategorian nimi kuten jännityskirjallisuus tai pistekirjat
                # otetaan otsikon teksti ja kirjoitetaan tiedostoon
                kategoria = elementti.get_text() 
                yield { 'tyyppi': 'kategoria', 'kategoria': kategoria }
                
            elif elementti.name == 'p':
                tulos = { 'tyyppi': 'linkki' }
                # elementti on tekstikappale, jossa kirjan nimi, tekijä ja tunnus
                # otetaan nämä tiedot talteen 
                tulos['kirja'] = elementti.get_text()
                # kappaleessa on myös linkki kirjan kuvauksen sisältävälle sivulle
                # otetaan osoite talteen
                tulos['kirjaURL'] = elementti.a['href']
                yield tulos
                        
if __name__ == '__main__':
    haku = UutuusHaku( 'https://www.celianet.fi/kirjavinkit/uutuuskirjat-aikuisille/', 'uutuudet.txt' )
    haku.haeKirjat()