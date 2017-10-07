# Celia uutuudet

Celia uutuudet on työkalu tekstimuotoisten uutuuskirjaluetteloiden luomiseen [Celia kirjaston](http://www.celia.fi) nettisivuilta löytyvistä  uutuusluetteloista.
Sivustolla olevat uutuusluettelot eivät sisällä suoraan kirjojen kuvauksia, vaan ne joutuu katsomaan erikseen linkin takana olevalta sivulta. Jotkut käyttäjät kokevat tällaisen uutuusluettelon
hankalaksi. Tämä työkalu luo eri uutuusluettelosivuista uutuusluettelon tekstitiedostoon, joka sisältää kirjojen kuvaukset. Luodut uutuusluettelot voi myös ohjelman avulla lähettää sähköpostilla haluamilleen vastaanottajille.

## Vaatimukset

Tarvitset seuraavat koodin hakemiseen ja käyttämiseen:

- git (ei pakollinen): versionhallinta koodin hakemiseen
- python versio 3
- pip: vaadittujen kirjastojen asennus

## Asennus ja käyttö

Hae koodi ja siirry sen hakemistoon. Gitiä käyttämällä seuraavasti:

    git clone https://github.com/ohylli/celia-uutuudet.git
    cd celia-uutuudet
    
Vaihtoehtoisesti voit ladata koodin GitHubista zippakettina. Ladattuasi koodin halutessasi luo ensiksi virtuaaliympäristö projektille:

    python -m venv env
    # aktivoi ympäristö windowsissa
    env\Scripts\activate.bat
    # aktivoi Linuxissa tai Macilla
    source env/bin/activate

Asenna ohjelman tarvitsemat kirjastot:

    pip install -r requirements.txt
    
HUOM: riippuen Python asennuksestasi voivat komennot olla python3 ja pip3.

Luo uutuusluettelot:

    python uutuushaku.py
    
Jokaisesta uutuudet sivusta aikuisten uutuudet, ja lasten ja nuorten uutuudet luodaan oma tekstitiedosto. Kun seuraavan kerran ajat ohjelman
luotuihin uutuusluetteloihin tulee vain ne kirjat, jotka on lisätty uutuudet sivuille edellisen luettelon luontikerran jälkeen. Tiedostossa vanhat.json pidetään kirjaa edellisen ajokerran uusimmista kirjoista eri kategorioissa.
Se ylikirjoitetaan ohjelman jokaisella ajokerralla, mutta siitä luodaan ennen ylikirjoitusta kopio tiedostoon edelliset_vanhat.json.

Ohjelma voi lähetää uutuusluettelot myös sähköpostitse haluamillesi vastaanottajille. Käyttääksesi ominaisuuta tulee ohjelma ensiksi konfiguroida sitä varten. Tiedostossa posti.json on sähköpostin lähetykseen tarvittavat asetukset:

- lähettäjä: oma sähköpostiosoitteesi
- vastaanottajat: lista vastaanottajien sähköpostiosoitteita
- piilo_vastaanottajat: Lista vastaanottajia, joiden osoitteet eivät näy muille vastaanottajille eli jotka laitetaan viestin Bcc vastaanottajiksi. Tämä ei ole pakollinen kenttä.
- palvelin: SMTP sähköpostipalvelimen osoite esim. Soneralla mail.inet.fi
- portti: TCP portti, johon palvelimella yhdistetään
- käyttäjä: Käyttäjätunnuksesi SMTP palvelimelle
- salasana: Salasanasi sähköpostipalvelimelle.

Sähköpostitusta hallitaan komentorivi parametrilla -p tai --posti, joka hyväksyy seuraavat arvot:

- ei: Luetteloita ei postiteta. Tämä on oletusarvo parametrille.
- kyllä: luettelot postitetaan heti kun ne on luotu
- kysy: Jokaisen luettelon kohdalla kysytään postitetaanko se.
- heti: Uusia luetteloita ei luoda, vaan ohjelma olettaa löytävänsä aikaisemmin luodut luettelot, jotka se postittaa heti.

## Ohjelman rakenne

Ohjelma koostuu viidestä lähdekooditiedostosta:

- uutuushaku.py: pääohjelma, joka aloittaa uutuuksien haun
- uutuusluettelo.py: sisältää luokan uutuusluettelosivujen käsittelyyn
- kirja.py: sisältää luokan yksittäisen kirjan tiedot sisältävän sivun käsittelyyn
- kasitellyt.py: sisältää Käsitellyt luokan, jolla pidetään kirjaa edellisellä kerralla jo käsitellyistä kirjoista
- posti.py: Sisältää Postittaja luokan luetteloiden lähettämiseen sähköpostilla.

Pääohjelma luo eri uutuusluettelosivujen käsittelemiseen oman Uutuusluettelo tai sen aliluokan instanssin. Uutuusluettelo instanssi käy annetun uutuusluettelo sivun läpi kirjoittaen sen sisältöä annetun nimiseen tekstitiedostoon.
Uutuusluettelo käyttää KirjaSivu luokan instansseja yksittäisen kirjan tiedot sisältävien sivujen käsittelyyn eli kirjan tietojen hakemiseen sivulta.
uutuusluettelo käyttää Käsitellyt luokkaa kirjan pitämiseen siitä, mitkä kirjat eri kategorioista on käsitelty edellisellä kerralla. Luokan avulla myös tallennetaan tämän hetken uusimmat kirjat seuraavaa kertaa varten. Pääohjelma käyttää Postittaja luokkaa luetteloiden lähettämiseen sähköpostilla.