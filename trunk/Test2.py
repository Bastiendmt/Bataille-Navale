#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Bastien
#
# Created:     06/04/2016
# Copyright:   (c) Bastien 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import terminal
import flottes
import jeuConsole
import string

#terminal.hello()


def creationdeliste():
    listecomplete= string.uppercase ## lsite de l'alphabet
    liste='liste'
    grille={}
    for elm in listecomplete:
        variable = liste+elm ##on attribue un indice de ligne (A...Z) a liste
        variable=[]
        grille[elm]=variable
    print grille




def flotte2D(flotte,cachee=False):
    print flottes.positionsDesBateaux










maflotte=jeuConsole.maflotte ##
print maflotte
