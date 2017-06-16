# -*- coding: utf-8 -*-

from uutuusluettelo import Uutuusluettelo

haku = Uutuusluettelo( 'https://www.celianet.fi/kirjavinkit/uutuuskirjat-aikuisille/', 'uutuudet.txt' )
haku.haeKirjat()