# Celia uutuudet

Celia uutuudet on työkalu tekstimuotoisten uutuuskirjaluetteloiden luomiseen [Celia kirjaston](http://www.celia.fi) nettisivuilta löytyvistä  uutuusluetteloista.
Sivustolla olevat uutuusluettelot eivät sisällä suoraan kirjojen kuvauksia, vaan ne joutuu katsomaan erikseen linkin takana olevalta sivulta. Jotkut käyttäjät kokevat tällaisen uutuusluettelon
hankalaksi. Tämä työkalu luo eri uutuusluettelosivuista uutuusluettelon tekstitiedostoon, joka sisältää kirjojen kuvaukset.

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
    
Luo uutuusluettelot:

    python uutuushaku.py
    
Jokaisesta uutuudet sivusta aikuisten uutuudet, ja lasten ja nuorten uutuudet luodaan oma tekstitiedosto. Kun seuraavan kerran ajat ohjelman
luotuihin uutuusluetteloihin tulee vain ne kirjat, jotka on lisätty uutuudet sivuille edellisen luettelon luontikerran jälkeen. Tiedostossa vanhat.json pidetään kirjaa edellisen ajokerran uusimmista kirjoista eri kategorioissa.
Se ylikirjoitetaan ohjelman jokaisella ajokerralla, mutta siitä luodaan ennen ylikirjoitusta kopio tiedostoon edelliset_vanhat.json.

## Ohjelman rakenne

Ohjelma koostuu neljästä lähdekooditiedostosta:

- uutuushaku.py: pääohjelma, joka aloittaa uutuuksien haun
- uutuusluettelo.py: sisältää luokan uutuusluettelosivujen käsittelyyn
- kirja.py: sisältää luokan yksittäisen kirjan tiedot sisältävän sivun käsittelyyn
- kasitellyt.py: sisältää Käsitellyt luokan, jolla pidetään kirjaa edellisellä kerralla jo käsitellyistä kirjoista

Pääohjelma luo eri uutuusluettelosivujen käsittelemiseen oman Uutuusluettelo tai sen aliluokan instanssin. Uutuusluettelo instanssi käy annetun uutuusluettelo sivun läpi kirjoittaen sen sisältöä annetun nimiseen tekstitiedostoon.
Uutuusluettelo käyttää KirjaSivu luokan instansseja yksittäisen kirjan tiedot sisältävien sivujen käsittelyyn eli kirjan tietojen hakemiseen sivulta.
Uuutuusluettelo käyttää Käsitellyt luokkaa kirjan pitämiseen siitä, mitkä kirjat eri kategorioista on käsitelty edellisellä kerralla. Luokan avulla myös tallennetaan tämän hetken uusimmat kirjat seuraavaa kertaa varten.