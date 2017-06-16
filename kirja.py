# -*- coding: utf-8 -*-

class KirjaSivu():
    """docstring for KirjaSivu"""
    
    pohja = '''{nimi} / {tekijä} {id} {tyyppiTiedot}
{url}

{kuvaus}'''

    tyyppiPohjat = {
        'äänikirja': '''
lukija: {lukija}, kesto: {kesto}''',
    'pistekirja': '''
{pisteTiedot}''',
    'elektroninen': ''
    }
    
    def __init__( self, sivu, url ):
        self.sivu = sivu
        self.url = url
        self.tiedotTaulukko = self.sivu.table
        
    def käsitteleKirjaSivu( self ):
        # tallennetaan kirjan tiedot sanakirjaan
        kirja = { 'url': self.url }
        kirja['id'] = self.url.split( '/' )[-2]
        # kirjan nimi on ensimmäisessä ykköstason otsikossa
        kirja['nimi'] = self.sivu.h1.string.strip()
        # kuvaus on sivun ensimmäisessä tekstikappaleessa
        kirja['kuvaus'] = self.sivu.p.get_text()
        kirja['tekijä'] = self.haeTaulukosta( 'Tekijä', '' )
        ulkoasu = self.haeTaulukosta( 'Ulkoasu' )
        tyyppi, tyyppiTiedot = ulkoasu.split( maxsplit = 1 )
        
        if tyyppi in [ 'äänikirja', 'DaisyTrio', 'talbok' ]:
            tyyppi = 'äänikirja'
            kirja['lukija'] = self.haeTaulukosta( 'Lukija', 'ei tiedossa' )
            kirja['kesto'] = self.haeTaulukosta( 'Kesto', 'ei tiedossa' )
            
        elif tyyppi == 'pistekirja':
            kirja['pisteTiedot'] = tyyppiTiedot[1:-1]
            
        elif tyyppi == 'elektroninen':
            pass
            
        else:
            print( 'Tuntematon kirjan tyyppi ' +tyyppi )
            quit()
            
        kirja['tyyppiTiedot'] = self.tyyppiPohjat[tyyppi].format( **kirja )
        return self.pohja.format( **kirja )
        
    def haeTaulukosta( self, tieto, oletus = None ):
        td = self.tiedotTaulukko.find( 'td', text = tieto )
        if td != None:
            return td.next_sibling.string
        
        else:
            return oletus