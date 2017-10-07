# -*- coding: utf-8 -*-

from email.mime.text import MIMEText
import smtplib
import json

# Luettelon alkuun liitettävä teksti
alku = '''Tämä luettelo on luotu ja lähetetty automaattisesti, joten se saattaa sisältää virheitä. Luettelon luomiseen käytetyn ohjelman lähdekoodi on saatavissa osoitteessa:
https://github.com/ohylli/celia-uutuudet

'''

class Postittaja():
    """Luokka uutuusluetteloiden lähettämiseen sähköpostilla."""
    
    def __init__( self ):
        '''Luo Postittaja posti.json konfiguraatio tiedoston määräämillä asetuksilla.'''
        # lue konfiguraatio tiedostosta ja muunna json python sanakirjaksi
        with open( 'posti.json', 'r', encoding = 'utf-8' ) as tiedosto:
            konfiguraatio = json.load( tiedosto )
            
        # tallenna konfiguraation sisältö muuttujiin
        self.lähettäjä = konfiguraatio[ 'lähettäjä' ]
        self.vastaanottajat = konfiguraatio[ 'vastaanottajat' ]
        if 'piilo_vastaanottajat' in konfiguraatio:
            self.piiloVastaanottajat = konfiguraatio[ 'piilo_vastaanottajat' ]
            
        else:
            self.piiloVastaanottajat = None
            
        palvelinNimi = konfiguraatio['palvelin']
        portti = konfiguraatio[ 'portti' ]
        käyttäjä = konfiguraatio[ 'käyttäjä' ]
        salasana = konfiguraatio[ 'salasana' ]
        
        # Luo asiakas sähköpostipalvelimelle, joka on määritelty konfiguraatiotiedostossa
        # käytetään heti SSL salattua yhteyttä
        # ainakin soneran palvelin mail.inet.fi vaatii heti salatun yhteyden eli ei voida luoda salaamatonta asiakasta ja sitten käynnistää salattua yhteyttä
        self.palvelin = smtplib.SMTP_SSL( palvelinNimi, portti )
        # kirjaudutaan palvelimelle konfiguraatiossa olleilla käyttäjätunnuksella ja salasanalla
        self.palvelin.login( käyttäjä, salasana )
        
    def postita( self, luettelo ):
        '''Postittaa parametrina saadun luettelo sanakirjan määrittämän uutuusluettelon.'''
        # luetaan uutuusluettelon sisältö tiedostosta
        tiedosto = open( luettelo['tiedosto'], 'r' )
        runko = tiedosto.read()
        if len( runko ) == 0:
            print( 'Luettelo {} on tyhjä eikä sitä postiteta.'.format( luettelo['tiedosto'] ))
            return
            
        tiedosto.close()
        # luodaan tekstimuotoinen lähetettävä viesti, jonka rungoksi asetetaan luettelon sisältö
        viesti = MIMEText( alku +runko, 'plain' )
        # asetetaan viestin lähettäjä
        viesti['From'] = self.lähettäjä
        # asetetaan vastaanottajat. Yhdistetään vastaanottaja listan osoitteet yhdeksi merkkijonoksi pilkulla eroteltuna
        viesti['To'] = ','.join( self.vastaanottajat )
        # Jos on määritelty Bcc eli piilotetut vastaanottajat lisätään ne
        if self.piiloVastaanottajat != None:
            viesti['Bcc'] = ','.join( self.piiloVastaanottajat )
            
        # asetetaan viestin otsikoksi luettelon otsikko
        viesti['Subject'] = luettelo['otsikko']
        # lähetetään viesti
        self.palvelin.send_message( viesti )