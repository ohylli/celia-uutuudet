# -*- coding: utf-8 -*-
# sisältää luokat uutuusluettelosivun käsittelyyn

# kirjasto HTTP pyyntöjen tekemiseen eli nettisivun hakuun
import requests
# kirjasto HTML:n parsimiseen
from bs4 import BeautifulSoup

# luokka yksittäisen kirjan tiedot sisältävän sivun käsittelyyn
from kirja import KirjaSivu

class Uutuusluettelo():
    """Luokka uutuusluettelosivun käsittelyyn
    
    Luokka käy uutuudet sivun sisällön läpi luoden siitä tekstimuotoisen uutuusluettelon."""
    
    def __init__( self, luetteloUrl, tiedostonimi ):
        """Luo Utuusluettelo käsittelemään annettu uutuudet sivu, jonka sisältö tallennetaan annetun nimiseen tiedostoon."""
        # uutuudet sivun osoite
        self.url = luetteloUrl
        # avataan tiedosto tietojen tallentamista varten
        self.tiedosto = open( tiedostonimi, 'wb' )

    def kirjoita( self, sisältö ):
        """Kirjoittaa annetun sisällön luettelotiedostoon."""
        # lisätään pari rivinvaihtoa sisällön perään ja tallennetaan utf-8 koodauksella
        self.tiedosto.write( bytes( sisältö +'\r\n\r\n', 'utf-8' ))

    def haeSivu( self, url ):
        """Hakee annetussa osoitteessa olevan sivun.
        
        Palauttaa valmiiksi käsitellyn HTML:n BeautifulSoup oliona.
        Ohjelman suoritus lopetetaan, jos sivua ei saada haettua."""
        # haetaan sivu
        vastaus = requests.get( url )
        # tarkistetaan, että pyyntö onnistui
        if vastaus.status_code != 200:
            print( 'Sivun ' +url +'  haku epäonnistui. HTTP status koodi: ' +str( vastaus.status_code ))
            # lopetetaan ohjelma
            quit()

         # parsitaan sivun HTML
        return BeautifulSoup( vastaus.text, 'html.parser' )
        
    def haeKirjat( self ):
        """Hakee uutuussivun kirjat ja tallentaa niiden tiedot tekstitiedostoon."""
        # haetaan ja parsitaan uutuudet sivun html
        self.uutuudetSivu = self.haeSivu( self.url )
        # käsitellään sivun sisältö
        # käsitteleLuettelo generaattori palauttaa joko sivun eri kirja kategorioiden otsikoita
        # tai yksittäisen kirjan tiedot sisältävän sivun osoitteen
        for elementti in self.käsitteleLuetteloSivu():
            if elementti['tyyppi'] == 'kategoria':
                # elementti on kirjakategorian otsikko, joka kirjoitetaan luettelotiedostoon
                self.kirjoita( elementti['kategoria'] )
        
            elif elementti['tyyppi'] == 'linkki':
                # elementti on linkki yksittäisen kirjan tiedot sivulle
                kirjaUrl = elementti['kirjaURL']
                if '/sv/' in kirjaUrl:
                    # luettelossa on linkki ruotsin kieliselle kirjan tiedot sivulle. jätetään käsittelemättä
                    # yksi tällainen tuli kerran vastaan. jos näitä tulee enemmän pitänee tehdä käsittely myös ruotsin kieliselle sivulle
                    continue
                    
                # haetaan kirjan tiedot sisältävä sivu
                kirjaSivu = self.haeSivu( kirjaUrl )
                # luodaan KirjaSivu olio käsittelemään kirjan tiedot
                # haetaan KirjaSivulta kirjan tiedot tekstimuodossa
                kirjaTiedot = KirjaSivu( kirjaSivu, kirjaUrl ).käsitteleKirjaSivu()
                # tallennetaan tiedot tiedostoon
                self.kirjoita( kirjaTiedot )
    
        # valmista tuli, suljetaan tiedosto
        self.tiedosto.close()
        
    def käsitteleLuetteloSivu( self ):
        """Generaattori funktio uutuudet sivun läpikäymiseen.
        
        Metodi generoi sivun sisällöstä sanakirjoja, joissa on elementin tiedot.
        Elementit ovat joko sivun eri kirja kategorioiden nimiä tai linkkejä kirjan tiedot sisältävälle sivulle.
        Sanakirjan tyyppi attribuutti kertoo tyypin, joka on joko kategoria tai linkki.
        Kategoria tyypin elementillä on lisäksi kategoria attribuuutti ja linkki tyypillä linkki."""
        # käydään sivun sisältö läpi elementti kerrallaan
        # lähtien ensimmäisestä kiinnostavasta elementistä, joka haetaan omalla metodillaan
        # käsitellään tätä elementtiä seuraavat saman tason elementit, jotka ovat joko otsikoita tai tekstikappaleita
        for elementti in self.ekaElementti().next_siblings:
            if elementti.name in [ 'h1', 'h2', 'h3', 'h4', 'h5', 'h6' ]:
                # elementti on otsikko, jossa on uutuuskategorian nimi kuten jännityskirjallisuus tai pistekirjat
                # otetaan otsikon teksti 
                kategoria = elementti.get_text() 
                # generoidaan elementti kategoriasta
                yield { 'tyyppi': 'kategoria', 'kategoria': kategoria }
                
            elif elementti.name == 'p':
                # tekstikappale, jossa on yksi tai useampi linkki kirja sivulle
                for linkki in elementti.find_all( 'a' ):
                    # tehdään linkistä elementti
                    tulos = { 'tyyppi': 'linkki' }
                    # otetaan linkin osoite talteen
                    tulos['kirjaURL'] = linkki['href']
                    yield tulos
                    
    def ekaElementti( self ):
        """Metodi ensimmäisen sivun kiinnostavan elementin hakemiseen."""
        # haetaan sivun pääosion ensimmäistä kolmos tason otsikkoa edeltävä elementti
        return self.uutuudetSivu.find( role='main' ).h3.previous_sibling
        
class NuortenUutuudet( Uutuusluettelo ):
    """Uutuusluettelon aliluokka nuorten uutuudetsivun käsittelyyn
    
    Sivun rakenne on hieman erilainen tarkemmin sen pääosiossa luettelo alkaa toisesta kolmostason otsikosta ei ensimmäisestä."""

    def ekaElementti( self ):
        """Metodi ensimmäisen käsiteltävän elementin hakuun."""
        # haetaan sivun pääosion toista kakkostason otsikkoa edeltävä elementti
        return self.uutuudetSivu.find( role='main' ).find_all( 'h2', limit = 2 )[1].previous_sibling