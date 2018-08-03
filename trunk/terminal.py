﻿#-------------------------------------------------------------------------------
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



import flottes
import string



def hello():
    print "hello world im bastien"

def flotteTextuelle(flotte):   #OP
    liste = flotte['bateaux']
    for elm in liste:
        print elm,':',  ##Affichage du bateau
        for case in liste[elm]:
            print case,
        print
        ##print liste[elm] ##Affichage des coordonnées

def saisieCibleValideOuCommande(): #OP
    case= raw_input("Rentrez une case au format Ln ; A<L<J ; 1<n<10 ; sauv pour sauvegarder la partie et stop pour arreter")
    if case== 'stop':
        return 'stop'
    elif case == 'sauv':
        return 'sauv'

    case = str(case)
    temp= case.split(case[0]) ## permet de récupérer l'indice meme si n> 9
    ##print temp[-1]   ##temp[-1] correspond à l'indice de la colonne

    if case[0]!='A' and case[0]!='B' and case[0]!='C' and case[0]!='D' and case[0]!='E' and case[0]!='F' and case[0]!='G' and case[0]!='H' and case[0]!='I' and case[0]!='J' :
        case = saisieCibleValideOuCommande()
    elif temp[-1] !='1' and temp[-1] !='2' and temp[-1] !='3' and temp[-1] !='4' and temp[-1] !='5' and temp[-1] !='6' and temp[-1] !='7' and temp[-1] !='8' and temp[-1] !='9' and temp[-1] !='10':
        case = saisieCibleValideOuCommande()
    return case


def flotte2D(flotte, cachee=False): #A optimiser
    listeA=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    listeB=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    listeC=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    listeD=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    listeE=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    listeF=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    listeG=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    listeH=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    listeI=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    listeJ=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

    grille={'A':listeA,'B':listeB,'C':listeC,'D':listeD,'E':listeE,'F':listeF,'G':listeG,'H':listeH,'I':listeI,'J':listeJ}

    if cachee == False:    ##Affichage d'une grille connue
        bt= flottes.positionsDesBateaux(flotte,exepte="")
        listetir=flotte['tirs']
        ##print bt
        print 'Votre flotte est la suivante :'
        for elm in bt:
            savepos = grille[elm[0]] ##On récupere la liste correspondant à la bonne ligne
            indice = elm.split(elm[0])  ## récupere l'indice meme si >9
            if elm in listetir:
                savepos[int(indice[1])-1]='X' ##on associe au bon indice soit X soit #
            else:savepos[int(indice[1])-1]='#'  ##affecte des # lorsque un bateau se trouve en cette postion
        ##print elm[0],elm[1],
        ##print savepos
            grille[elm[0]]=savepos

        for elm in listetir:                   #Affichage des tirs non touchés
            savepos = grille[elm[0]]
            indice = elm.split(elm[0])  ## récupere l'indice meme si >9
            if elm not in bt:
                savepos[int(indice[1])-1]='0'
            grille[elm[0]]=savepos



        listenum= ['1','2','3','4','5','6','7','8','9','10'] ##Ces 5 lignes permettent d'afficher les indices des colonnes
        listealph= string.uppercase
        print ' ',
        for elm in listenum:
            print elm,
        print

        i=0
        for elm in grille:
            print listealph[i],  ##Affichage de l'indice de la ligne
            nomdeliste = grille[listealph[i]]  ##Affecte à une variable une liste contenant la position des bateaux
            i+=1
            for elmt in nomdeliste:
                print elmt,        ## Affichage des # ; bateaux
            print

    elif cachee == True:              ##Affichage de la grille adverse
        bt=flotte['tirs']
        listebateau=flottes.positionsDesBateaux(flotte,exepte="")
        print 'la flotte ennemie est la suivante:',
        for elm in bt:
            savepos = grille[elm[0]]
            indice = elm.split(elm[0])  ## récupere l'indice meme si >9
            ##print flottes.analysetir(flotte,elm)
            ##print elm,
##            if flottes.analysetir(flotte,elm)=='touche':
##                savepos[int(indice[1])-1]='X'
            if elm in listebateau:                ##Verifie si un tir correspond a la case d'un bateau
                savepos[int(indice[1])-1]='X'
            else:
                savepos[int(indice[1])-1]='0'  ##affecte des # lorsque un bateau se trouve en cette postion
        ##print elm[0],elm[1],
        ##print savepos
            grille[elm[0]]=savepos

        listenum= ['1','2','3','4','5','6','7','8','9','10'] ##Ces 5 lignes permettent d'afficher les indices des colonnes
        listealph= string.uppercase
        print
        print ' ',
        for elm in listenum:
            print elm,
        print

        i=0
        for elm in grille:
            print listealph[i],  ##Affichage de l'indice de la ligne
            nomdeliste = grille[listealph[i]]  ##Affecte à une variable une liste contenant la position des bateaux
            i+=1
            for elmt in nomdeliste:
                print elmt,        ## Affichage des # ; bateaux
            print


def saisieModeInitialisationDesFlottes(): #OP
    print 'Mode de choix de la Flotte: '
    print '---------------------------'
    print '1> flottes initialisees en dur (choix par defaut)'
    print '2> flottes initialisees manuellement pour le joueur et aleatoirement pour l ordinateur'
    print '3> flottes initialisees aleatoirement pour les 2 joueurs '
    print '4> flottes restaurees de la derniere partie sauvegardee'
    entree= input("Votre choix ?")
    if entree== 1 :
        return 'endur'
    elif entree== 2:
        return 'manuel+aleatoire'
    elif entree==3:
        return 'aleatoire'
    elif entree==4:
        return 'restaure'
    else:
        choix =saisieModeInitialisationDesFlottes()
        return choix




def choixBateauAPositionner(flotte): #OP
    if flottes.estUneFlotteComplete(flotte) == True :
        return "stop"
    i=1
    listebateau=[]
    bateauxrestant = flotte['bateaux']
    for elm in bateauxrestant:
        print i,elm,flotte['bateaux'][elm]  ##Affichage des bateaux a positionner
        listebateau.append(elm)
        i+=1
    saisie= input("Quel bateau voulez-vous placer?")
    if saisie not in range(i):
        saisie =choixBateauAPositionner(flotte)
    else:
        return listebateau[saisie-1]  ## renvoie le bateau appele


def saisieDirectionValide(): #OP
    direction = raw_input("Entrez votre direction; vertical (v), ou horizontal (h)")
    if direction == 'v' or direction == 'vertical':
        return 'vertical'
    elif direction == 'h' or direction == 'horizontal':
        return 'horizontal'
    else:
        direction = saisieDirectionValide()
        return direction


def choixFlotteManuelConsole(flotte):   #OP           ##faire n appel a cette fonction tant que tout les bateaux ne sont pas placés, vérifier le positionnement des bateaux grace à flottes.estUneFlotteComplete()
    bateau =choixBateauAPositionner(flotte)
    positioninitiale=saisieCibleValideOuCommande()##commandes='5')
    direction = saisieDirectionValide()
    flottes.positionneBateauParDirection(flotte, bateau, positioninitiale, direction )
    return flotte



def placeflottemanuel(flotte):
    for elm in flotte['bateaux']:
        while flotte['bateaux'][elm] == []:          ## tant qu'un bateau n'a pas ete place, sa premiere case et sa direction change
            choixFlotteManuelConsole(flotte)


def modedejeu(): #OP
    print 'Mode de choix du jeu :'
    print '---------------------------'
    print '1> jeu entierement manuel '
    print '2> jeu automatique contre l ordinateur'
    print '3> jeu automatique avance  '
    entree= input("Votre choix ?")
    if entree== 1 :
        return 'manuel'
    elif entree== 2:
        return 'auto'
    elif entree==3:
        return 'avance'
    else:
        choix = modedejeu()
        return choix





maflotte=flottes.maFlotte
saflotte=flottes.saFlotte
flottevide=flottes.InitialisationdDuneFlotteVide()

##saflotte['tirs']=['F1','F2','B4']
##flottes.analysetir(saflotte,'H3')
##print saflotte
##
##flotte2D(saflotte,cachee=True)


##print modedejeu()


##print flottevide
##placeflottemanuel(flottevide)
##print flottevide
##saisieModeInitialisationDesFlottes()
##flotteTextuelle(maflotte)
##flotte2D(maflotte,cachee=False)
##raw_input()
##print choixBateauAPositionner(maflotte)

##print choixBateauAPositionner(flottevide)
##choixFlotteManuelConsole(flottevide)

##print flottevide
##choixFlotteManuelConsole(flottevide)
##print flottevide












































##if __name__ == '__main__' :
##    # code d'auto-test
##    print
##    print "Voici l'auto-test du module"
##
##    print "TEST 1) Test de hello()"
##    #hello()