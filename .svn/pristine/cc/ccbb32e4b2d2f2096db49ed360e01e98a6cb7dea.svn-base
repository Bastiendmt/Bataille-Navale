#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      dumontba
#
# Created:     05/04/2016
# Copyright:   (c) dumontba 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#!/ usr/bin/env python
# -*- coding : UTF -8 -*-
__author__="DUMONT B."
__version__="0.1"
##print "Variable __name__ dans module", __name__


##import jeuConsole
##import flottes
import terminal
import string
import ntpath
import ast


##import os

Flotte =terminal.flottes.initialisationFlottesParDictionnairesFixes()
maFlotte = Flotte[0]
saFlotte = Flotte[1]

##variable='ppppp'
##fl=open('statistiques.bin','w')
##fl.writelines('nombre de partie jouée =')
##fl.write('\n')  ##passe sur une deuxieme ligne
##fl.write('Nombres de partie gagnées')
##fl.write('\n')  ##passe sur une deuxieme ligne
##fl.write('Nombres de partie perdues')
##fl.close()

def ajouteStat(pseudo,victoire):
    fl=open('statistiques.bin','a')
    dictionnaire = { 'Parties':0,'Victoires':0,'Defaites':0}
    dico={pseudo:dictionnaire}
    fl.write(str(dico))
    fl.write('\n')




def restaurationPartie(maFlotte,saFlotte):  #OP
    if ntpath.isfile('sauvegarde.bin') == True:
        fich=open('sauvegarde.bin','r')
        texte=fich.readlines()
        maFlotte= texte[0]
        saFlotte= texte[1]
        return maFlotte,saFlotte
    else: return False

restaurationPartie(maFlotte,saFlotte)
maFlotte = ast.literal_eval(restaurationPartie(maFlotte,saFlotte)[0])##transforme la chaine de caractere recupere en en dictionnaire
saFlotte = ast.literal_eval(restaurationPartie(maFlotte,saFlotte)[1])






if __name__ == '__main__' :
    # code d'auto-test
    print
    print "Voici l'auto-test du module"

    print "TEST 1) Test de hello()"
    #hello()