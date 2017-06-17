# Celia uutuudet

Celia uutuudet on työkalu tekstimuotoisten uutuuskirjaluetteloiden luomiseen [Celia kirjaston](http://www.celia.fi) nettisivuilta löytyvästä  uutuusluetteloista.
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
    
Jokaisesta uutuudet sivusta aikuisten uutuudet, nuorten uutuudet ja lasten uutuudet luodaan oma tekstitiedosto.

## Ohjelman rakenne

Ohjelma koostuu kolmesta lähdekooditiedostosta:

- uutuushaku.py: pääohjelma, joka aloittaa uutuuksien haun
- uutuusluettelo.py: sisältää luokat uutuusluettelosivujen käsittelyyn
- kirja.py: sisältää luokan yksittäisen kirjan tiedot sisältävän sivun käsittelyyn

Pääohjelma luo eri uutuusluettelosivujen käsittelemiseen oman Uutuusluettelo tai sen aliluokan instanssin. Uutuusluettelo instanssi käy annetun uutuusluettelo sivun läpi kirjoittaen sen sisältöä annetun nimiseen tekstitiedostoon.
Uutuusluettelo käyttää KirjaSivu luokan instansseja yksittäisen kirjan tiedot sisältävien sivujen käsittelyyn eli kirjan tietojen hakemiseen sivulta.