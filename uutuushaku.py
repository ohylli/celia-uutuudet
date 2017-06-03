# -*- coding: utf-8 -*-

# kirjasto HTTP pyyntöjen tekemiseen eli nettisivun hakuun
import requests
# kirjasto HTML:n parsimiseen
from bs4 import BeautifulSoup

# celian uutuudet sivun osoite
UUTUUDET_URL = 'https://www.celianet.fi/kirjavinkit/uutuuskirjat-aikuisille/'
# nimi tiedostolle johon uutuudet tallennetaan
TIEDOSTO_NIMI = 'uutuudet.txt'

# funktio joka kirjoittaa annetun sisällön annettuun tiedostoon
def kirjoita( tiedosto, sisältö ):
    # lisätään pari rivinvaihtoa sisällön perään ja tallennetaan utf-8 koodauksella
    tiedosto.write( bytes( sisältö +'\r\n\r\n', 'utf-8' ))

# haetaan uutuudet sisältävä nettisivu
vastaus = requests.get( UUTUUDET_URL )
# tarkistetaan, että pyyntö onnistui
if vastaus.status_code != 200:
    print( 'Uutuusluettelon haku epäonnistui. HTTP status koodi: ' +str( vastaus.status_code ))
    # lopetetaan ohjelma
    quit()
    
# avataan tiedosto tietojen tallentamista varten
tiedosto = open( TIEDOSTO_NIMI, 'wb' )
# parsitaan uutuudet sivun html
uutuudetSivu = BeautifulSoup( vastaus.text, 'html.parser' )

# käydään sivun sisältö läpi elementti kerrallaan
# lähtien ensimmäisestä kolmos tason ) otsikosta (h3, joka on sivun pääsisältö alueella
# tarkemmin käsitellään ensimmäistä h3:a edeltävää elementtiä seuraavat saman tason elementit
# näin ensimmäinenkin h3 tulee mukaan
for elementti in uutuudetSivu.find( role='main' ).h3.previous_sibling.next_siblings:
    if elementti.name == 'h3':
        # elementti on otsikko, jossa on uutuuskategorian nimi kuten jännityskirjallisuus tai pistekirjat
        # otetaan otsikon teksti ja kirjoitetaan tiedostoon
        kategoria = elementti.get_text() 
        kirjoita( tiedosto, kategoria )
        
    elif elementti.name == 'p':
        # elementti on tekstikappale, jossa kirjan nimi, tekijä ja tunnus
        # otetaan nämä tiedot talteen ja kirjoitetaan tiedostoon
        kirja = elementti.get_text()
        kirjoita( tiedosto, kirja )
        # kappaleessa on myös linkki kirjan kuvauksen sisältävälle sivulle
        # otetaan osoite talteen
        kirjaURL = elementti.a['href']
        # ja haetaan kirjan tiedot sisältävä sivu
        vastaus = requests.get( kirjaURL )
        # tarkistetaan onnistuiko
        if vastaus.status_code != 200:
            print( 'Kirjan ' +elementti.a.get_text() +' tietojen haku epäonnistui. HTTP status koodi: ' +str( vastaus.status_code ))
            
        # parsitaan kirjan kuvauksen sisältävän sivun html
        kirjaSivu = BeautifulSoup( vastaus.text, 'html.parser' )
        # kuvaus on sivun ensimmäisessä tekstikappaleessa
        # otetaan talteen ja kirjoitetaan tiedostoon
        kuvaus = kirjaSivu.p.get_text()
        kirjoita( tiedosto, kuvaus )
        
# valmista tuli, suljetaan tiedosto
tiedosto.close()