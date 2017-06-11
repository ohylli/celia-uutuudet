# -*- coding: utf-8 -*-

class KirjaSivu():
    """docstring for KirjaSivu"""
    
    pohja = '''{nimi} / {tekijä} {id}
{url}

{kuvaus}'''
    
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
        return self.pohja.format( **kirja )
        
    def haeTaulukosta( self, tieto, oletus = None ):
        td = self.tiedotTaulukko.find( 'td', text = tieto )
        if td != None:
            return td.next_sibling.string
        
        else:
            return oletus