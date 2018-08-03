#-------------------------------------------------------------------------------
# Name:        Sans nom1
# Purpose:
#
# Author:      jaming
#
# Created:     05/04/2016
# Copyright:   (c) jaming 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#!/ usr/bin/env python
# -*- coding : UTF -8 -*-
def indicesVersCaseLn(indices): #?op
    ligne=str(indices[0])
    colonne=str(indices[1])
    indices=ligne+colonne
    return (indices)


def caseLnVersIndices(indices): #OP
##    indices=str(indices)
    temp= indices.split(indices[0])
    ligne=(indices[0])
    colonne=temp[-1]
    indices=[ligne,colonne]
    return (indices)

def estUneCaseValide(case): #OP
    case = str(case)
    temp= case.split(case[0]) ## permet de récupérer l'indice meme si n> 9
    ##print temp[-1]   ##temp[-1] correspond à l'indice de la colonne
    if case[0]!='A' and case[0]!='B' and case[0]!='C' and case[0]!='D' and case[0]!='E' and case[0]!='F' and case[0]!='G' and case[0]!='H' and case[0]!='I' and case[0]!='J' :
        return False
    elif temp[-1] !='1' and temp[-1] !='2' and temp[-1] !='3' and temp[-1] !='4' and temp[-1] !='5' and temp[-1] !='6' and temp[-1] !='7' and temp[-1] !='8' and temp[-1] !='9' and temp[-1] !='10':
        return False
    return True

#print indicesVersCaseLn(['K','10'])
#print caseLnVersIndices('K4')
#print pp[0]



