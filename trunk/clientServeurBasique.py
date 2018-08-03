# -*- coding: utf-8 -*-
"""
Script clientServeurBasique.py
==============================

Script permettant de tester manuellement le protocole d'échange avec le serveur de
la bataille navale.
"""
__author__ = "C. BARAS"
__version__ = "1.0"

import socket

print "*** Script clientServeurBasique.py ***"

# Variable globale
COMMANDES = { '[pseudo]' : '[pseudo]nom',
              '[attente]' : '[ack]', 
              '[start]' : '[ack]',
              '[cible]' : '[tir]Ln',
              '[commande_invalide]' : '[ack]',
              '[tir]' : '[resultat]Ln|res',
              '[resultat]' : '[ack]',
              '[flotte]' : '[flotteadverse]sous-marin|Ln|Ln|Ln|porte-avions|Ln|Ln|Ln|Ln|Ln|torpilleur|Ln|Ln|croiseur|Ln|Ln|Ln|Ln|contre-torpilleurs|Ln|Ln|Ln]', 
              '[flotteadverse]' : '[ack]',
              '[fin]' : None
              }
print u"> Liste des commandes du serveur et des réponses à fournir"
print "\n".join( [ " "*3 + cle + " -> " + (valeur if valeur != None else "pas de reponse") for (cle, valeur) in COMMANDES.items() ] )
              
# Initialisations des paramètres du serveur
hote = 'localhost' # ip
port= 12800        # port
 
# Connexion au serveur par création et ouverture d'un objet socket 
# permettant la connexion avec le serveur
try :
    socketActif = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketActif.connect( (hote, port) )
    estConnecte = True
    print u"> Connexion établie avec le serveur %s sur le port %d" % (hote, port)
except socket.error:
    print u"> La connexion a échouée"
    socketActif = None
    estConnecte = False

# Boucle traitant les échanges avec le serveur : chaque commande 
# reçue du serveur doit être suivie d'une réponse appropriée 
# envoyée parle client
reponse = ""
while reponse != "[quit]" and estConnecte == True :

    # Lecture de la commande du serveur
    try : 
        recu = socketActif.recv(1024)
        print u"commande reçue du serveur : ", recu
    except socket.error : 
        # Problème dans la connexion impliquant la déconnexion du client
        estConnecte = False

    # Saisie de la réponse du client    
    reponse = raw_input("saisir votre reponse ou [quit]>")
        
    # Envoi de la réponse au serveur
    if reponse != "[quit]" :                   
        socketActif.send(reponse)
# Fin de la boucle de traitement

# Déconnexion du serveur
try :
    socketActif.close()
    print u"Deconnexion du serveur %s réussie" % hote
except : 
    pass

# Fin du sript
print u"*** fin du script clientServeurBasique.py ***"  
