﻿#-------------------------------------------------------------------------------
# Name:        module1
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


import flottes
import terminal
import random
import ast #ce module permet de tranformer une str en dict --> utilisé pour la restaurationde partie

def ajoutePseudo( maflotte, chaine ) :
    maflotte["pseudo"] = chaine


##print 'hello'
flottevide=flottes.InitialisationdDuneFlotteVide()
##print flottevide

maFlotte=flottevide
saFlotte=flottevide


choixdelaflotte= terminal.saisieModeInitialisationDesFlottes()                  #Initialisation des flottes



if choixdelaflotte == 'endur':
    Flotte = flottes.initialisationFlottesParDictionnairesFixes()
    maFlotte = Flotte[0]
    saFlotte = Flotte[1]
elif choixdelaflotte == 'manuel+aleatoire':
    terminal.placeflottemanuel(maFlotte)
    saFlotte=flottes.flottealeatoire
elif choixdelaflotte == 'aleatoire':
    maFlotte=flottes.choixFlotteAleatoire(maFlotte)
    saFlotte=flottes.choixFlotteAleatoire(saFlotte)
elif choixdelaflotte == 'restaure':
    maFlotte = ast.literal_eval(flottes.restaurationPartie(maFlotte,saFlotte)[0])##transforme la chaine de caractere recupere en en dictionnaire
    saFlotte = ast.literal_eval(flottes.restaurationPartie(maFlotte,saFlotte)[1])                               #Initialisation des flottes



##print maFlotte,id(maFlotte)
##print saFlotte,id(saFlotte)

##print 'conditions de depart',##maFlotte,saFlotte
##print flottes.estUnesFlotteCoulee(maFlotte),
##print flottes.estUnesFlotteCoulee(saFlotte)


print "Initialisation des flottes"
print "--------------------------"
terminal.flotteTextuelle(maFlotte)
terminal.flotte2D(maFlotte)

choixmodedejeu = terminal.modedejeu()
findepartie = False
lasteffect='null'
if choixmodedejeu == 'manuel':                                                  #Boucle de jeu manuel
    n=0

    while flottes.estUnesFlotteCoulee(maFlotte) == False and flottes.estUnesFlotteCoulee(saFlotte) == False and findepartie == False:
        n+=1
        print                                                                   #Tour du joueur
        print 'Iteration',n,') joueur joue'
        terminal.flotte2D(saFlotte,cachee=True)
        case =terminal.saisieCibleValideOuCommande() #permet de stoper la partie
        if case != 'stop' and case !='sauv':
            effetcourant= flottes.analysetir(saFlotte,case)
            if lasteffect == 'touche' and effetcourant == 'touche':             #Permet de devoiler une case surprise si deux touche d affile sont effectuees

                print ' Vous avez declanche la case surprise !'                 #boucle de gestion de la case random
                listealph = flottes.string.uppercase
                indiceligne=listealph[0:10]
                indicecolonne=[1,2,3,4,5,6,7,8,9,10]
                caserdm= random.choice(indiceligne)+str(random.choice(indicecolonne))
                print caserdm
                while caserdm in maFlotte['tirs']:
                    caserdm = random.choice(indiceligne)+str(random.choice(indicecolonne))
                flottes.analysetir(saFlotte,caserdm)
                lasteffect='null'
            else:              lasteffect=effetcourant


            n+=1
            print                                                               #Tour de l'ordi si lacommande tapée n'est pas stop ou sauv
            print 'Iteration',n,') Vous jouer pour l ordinateur'
            terminal.flotte2D(maFlotte,cachee=False)
            case = terminal.saisieCibleValideOuCommande()
            if case != 'stop' and case !='sauv':
                flottes.analysetir(maFlotte,case)
            elif case == 'sauv':
                flottes.sauvegardePartie(maFlotte,saFlotte)
                findepartie=True
            elif case == 'stop':
                findepartie=True
        elif case == 'sauv':
            flottes.sauvegardePartie(maFlotte,saFlotte)
            findepartie=True
        elif case == 'stop':
            findepartie=True

    if flottes.estUnesFlotteCoulee(maFlotte) == True:
        print 'l ordinateur a gagne'
    elif flottes.estUnesFlotteCoulee(saFlotte) == True:
        print 'Bravo vous avez gagne !!'



elif choixmodedejeu == 'auto':                                                  #Boucle de jeu manuel/auto
    n=0

    while flottes.estUnesFlotteCoulee(maFlotte) == False and flottes.estUnesFlotteCoulee(saFlotte) == False and findepartie == False:
        n+=1
        print                                                                   #Tour du joueur
        print 'Iteration',n,') joueur joue'
        terminal.flotte2D(saFlotte,cachee=True)

        case =terminal.saisieCibleValideOuCommande()
        if case != 'stop' and case !='sauv':
            effetcourant= flottes.analysetir(saFlotte,case)
            if lasteffect == 'touche' and effetcourant == 'touche':             #Permet de devoiler une case surprise si deux touche d affile sont effectuees

                print ' Vous avez declanche la case surprise !'                 #boucle de gestion de la case random
                listealph = flottes.string.uppercase
                indiceligne=listealph[0:10]
                indicecolonne=[1,2,3,4,5,6,7,8,9,10]
                caserdm= random.choice(indiceligne)+str(random.choice(indicecolonne))
                print caserdm
                while caserdm in maFlotte['tirs']:
                    caserdm = random.choice(indiceligne)+str(random.choice(indicecolonne))
                flottes.analysetir(saFlotte,caserdm)
                lasteffect='null'
            else:              lasteffect=effetcourant

        elif case == 'sauv':
            flottes.sauvegardePartie(maFlotte,saFlotte)
            findepartie=True
        elif case == 'stop':
            findepartie=True
                                                                                #Tour de l'ordi
        n+=1
        print
        print 'Iteration',n,') l ordinateur joue'
        listealph = flottes.string.uppercase
        indiceligne=listealph[0:10]
        indicecolonne=[1,2,3,4,5,6,7,8,9,10]
        caserdm= random.choice(indiceligne)+str(random.choice(indicecolonne))
        while caserdm in maFlotte['tirs']:
            caserdm = random.choice(indiceligne)+str(random.choice(indicecolonne))
        flottes.analysetir(maFlotte,caserdm)
        terminal.flotte2D(maFlotte,cachee=False)
    if flottes.estUnesFlotteCoulee(maFlotte) == True:
        print 'l ordinateur a gagne'
    elif flottes.estUnesFlotteCoulee(saFlotte) == True:
        print 'Bravo vous avez gagne !!'



elif choixmodedejeu == 'avance':                                                  #Boucle de jeu manuel/auto
    n=0

    while flottes.estUnesFlotteCoulee(maFlotte) == False and flottes.estUnesFlotteCoulee(saFlotte) == False and findepartie == False:
        n+=1
        print                                                                   #Tour du joueur
        print 'Iteration',n,') joueur joue'
        terminal.flotte2D(saFlotte,cachee=True)

        case =terminal.saisieCibleValideOuCommande()
        if case != 'stop' and case !='sauv':
            flottes.analysetir(saFlotte,case)
        elif case == 'sauv':
            flottes.sauvegardePartie(maFlotte,saFlotte)
            findepartie=True
        elif case == 'stop':
            findepartie=True
                                                                                #Tour de l'ordi
        n+=1
        print
        print 'Iteration',n,') l ordinateur joue'
        listealph = flottes.string.uppercase
        indiceligne=listealph[0:10]
        indicecolonne=[1,2,3,4,5,6,7,8,9,10]
        caserdm= random.choice(indiceligne)+str(random.choice(indicecolonne))
        while caserdm in maFlotte['tirs']:
            caserdm = random.choice(indiceligne)+str(random.choice(indicecolonne))
        flottes.analysetir(maFlotte,caserdm)
        terminal.flotte2D(maFlotte,cachee=False)
    if flottes.estUnesFlotteCoulee(maFlotte) == True:
        print 'l ordinateur a gagne'
    elif flottes.estUnesFlotteCoulee(saFlotte) == True:
        print 'Bravo vous avez gagne !!'





##print maFlotte,'est'
##terminal.flotte2D(maFlotte)
##print saFlotte,'est'
##terminal.flotte2D(saFlotte)


##ajoutePseudo(maFlotte,'Joueur1')
