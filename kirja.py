# -*- coding: utf-8 -*-

class KirjaSivu():
    """Luokka yksittäisen kirjan tiedot sisältävän sivun käsittelyyn."""

        # tekstipohja luetteloon kirjoitettaville kirjan tiedoille: nimi, tekijä, id, tyyppikohtaiset tiedot, url ja kuvaus
        # pohjaa käytetään pythonin merkkijonon format metodin kanssa
    pohja = '''{nimi} / {tekijä} {id} {tyyppiTiedot}
{url}

{kuvaus}'''

    # pohjat erityyppisten kirjojen (äänikirja, pistekirja, elektroninen kirja) erityis tiedoille
    # esim. äänikirjalla on lukija ja kesto, pistekirjalla vihkojen määrä
    tyyppiPohjat = {
        'äänikirja': '''
lukija: {lukija}, kesto: {kesto}''',
    'pistekirja': '''
{pisteTiedot}''',
    'elektroninen': ''
    }
    
    def __init__( self, sivu, url ):
        """Luo KirjaSivu sivun valmiiksi parsitusta sisällöstä (BeautifulSoup olio) ja sivun osoitteesta."""
        self.sivu = sivu
        self.url = url
        # sivulla on taulukko, jossa on osa kirjan tiedoista
        self.tiedotTaulukko = self.sivu.table
        
    def käsitteleKirjaSivu( self ):
        """Käsittelee kirjan sivun ja palauttaa kirjan tiedot sisältävän merkkijonon, jonka voi kirjoittaa luetteloon."""
        # tallennetaan kirjan tiedot sanakirjaan
        kirja = { 'url': self.url }
        # kirjan id löytyy osoitteen lopusta polun viimeisenä kohtana
        kirja['id'] = self.url.split( '/' )[-2]
        # kirjan nimi on ensimmäisessä ykköstason otsikossa
        kirja['nimi'] = self.sivu.h1.string.strip()
        # kuvaus on sivun ensimmäisessä tekstikappaleessa
        kuvausKappale = self.sivu.p
        if kuvausKappale != None:
            kirja['kuvaus'] = kuvausKappale.get_text()
            
        else:
            # kappaletta ei löydy, ei kuvausta
            kirja['kuvaus'] = ''
            
        
        # tekijän nimi löytyy sivun taulukosta
        kirja['tekijä'] = self.haeTaulukosta( 'Tekijä', '' )
        # taulukon ulkoasu kohdassa mainitaan kirjan tyyppi
        ulkoasu = self.haeTaulukosta( 'Ulkoasu' )
        # tyyppi saadaan ulkoasun ensimmäisestä sanasta, loput ovat tyyppikohtaista lisätietoa
        tyyppi, tyyppiTiedot = ulkoasu.split( maxsplit = 1 )
        
        # haetaan kirjan tyyppikohtaiset tiedot
        if tyyppi in [ 'äänikirja', 'DaisyTrio', 'talbok' ]:
            # kirja on äänikirja
            tyyppi = 'äänikirja'
            # lukija ja kesto löytyvät taulukosta, mutta saattavat puuttua
            kirja['lukija'] = self.haeTaulukosta( 'Lukija', 'ei tiedossa' )
            kirja['kesto'] = self.haeTaulukosta( 'Kesto', 'ei tiedossa' )
            
        elif tyyppi == 'pistekirja':
            # pistekirjan tiedot ovat ulkoasu kohdan lopussa
            # ne ovat sulkumerkkien sisällä, jotka tässä poistetaan
            kirja['pisteTiedot'] = tyyppiTiedot[1:-1]
            
        elif tyyppi == 'elektroninen':
            # elektroniseen kirjaan liittyen ei haeta tyyppitietoja
            pass
            
        else:
            print( 'Tuntematon kirjan tyyppi ' +tyyppi )
            quit()
        
        # tehdään tyyppikohtaisista tiedoista luetteloon kirjoitettava versio
        # käytettävä pohja riippuu kirjan tyypistä
        kirja['tyyppiTiedot'] = self.tyyppiPohjat[tyyppi].format( **kirja )
        # tehdään kirjan tiedoista luetteloon kirjoitettava merkkijono pohjasta
        return self.pohja.format( **kirja )
        
    def haeTaulukosta( self, tieto, oletus = None ):
        """Hakee halutun tiedon kirjasivulla olevasta taulukosta. Palauttaa annetun oletuksen, jos taulukossa ei ole kysyttyä tietoa."""
        # haetaan taulukon solu, jossa on kysytty teksti
        td = self.tiedotTaulukko.find( 'td', text = tieto )
        if td != None:
            # tieto löytyi palautetaan se eli tekstin viereisen taulukon solun sisältö
            return td.next_sibling.string
        
        else:
            # tietoa ei löydy taulukosta
            return oletus