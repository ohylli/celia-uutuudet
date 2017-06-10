# Celia uutuudet

Celia uutuudet on työkalu tekstimuotoisen uutuuskirjaluettelon luomiseen [Celia kirjaston](http://www.celia.fi) nettisivuilta löytyvästä  [uutuusluettelosta](https://www.celianet.fi/kirjavinkit/uutuuskirjat-aikuisille/).
Sivustolla oleva uutuusluettelo ei sisällä suoraan kirjojen kuvauksia, vaan ne joutuu katsomaan erikseen linkin takana olevalta sivulta. Jotkut käyttäjät kokevat tällaisen uutuusluettelon
hankalaksi. Tämä työkalu luo uutuusluettelon tekstitiedostoon, joka sisältää kirjojen kuvaukset.

## Vaatimukset

Tarvitset seuraavaat koodin hakemiseen ja käyttämiseen:

- git (ei pakollinen): versionhallinta koodin hakemiseen
- python versio 3
- pip: vaadittujen kirjastojen asennus

## Asennus ja käyttö

Hae koodi ja siirry sen hakemistoon. Gitiä käyttämällä seuraavasti:

    git clone https://github.com/ohylli/celia-uutuudet.git
    cd celia-uutuudet
    
Halutessasi luo ensiksi virtuaaliympäristö projektille:

    python -m venv env
    # aktivoi ympäristö windowsissa
    env\Scripts\activate.bat
    # aktivoi Linusissa tai Macilla
    source env/bin/activate

Asenna ohjelman tarvitsemat kirjastot:

    pip install -r requirements.txt
    
Luo uutuusluettelo:

    python uutuushaku.py
    
Luetelo luodaan tiedostoon uutuudet.txt.