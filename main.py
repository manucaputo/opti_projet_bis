"""Auteurs : Team de bg's"""


from random import randint, random
from math import exp

with open("data1.dat", "r") as f:
# Lecture du fichier
    x = []
    N = int(f.readline())
    E = int(f.readline())
    B = int(f.readline())

    for line in f:
        x.extend(line.strip().split('\t'))


x_bis = map(int, x)
x_list=list(x_bis)
print(len(x_list))
print(sum(x_list))
vec = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
#vec = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2,2,2,2,2,2]
print(B*E/N)
nbrdiv = int(B*E/N)

diviseur=[]
somdiviseur=B*E
print("nombre de divison nécessaire",somdiviseur)
bol = False
if (nbrdiv==1):

    for i in range(N):
        if (somdiviseur == N-i):
            bol = True

        if (bol ==True):
            diviseur.append(1)
        else:
            somdiviseur = somdiviseur -2
            diviseur.append(2)
else:
    for i in range(N):
        diviseur.append(nbrdiv)
print(diviseur)
print("taille du vec divisuer",len(diviseur))
print("somme du vec diviseur",sum(diviseur))

if(sum(diviseur)<(B*E)):
    for i in range(len(diviseur)):
        diviseur[i]+=1
        if(sum(diviseur)==(B*E)):
            break
print(diviseur)
print("taille du vec diviseur2",len(diviseur))
print("somme du vec diviseur2",sum(diviseur))
somme=0

def cost(listvaleur,listdivisuer,E ):
    list=[]
    somme2=0


    for i in range(len(listvaleur)):
        dec=0
        for j in range(listdivisuer[i]):
            if (listdivisuer[i]==1):
                list.append(listvaleur[i])
            else:
                dec+=listvaleur[i]/listdivisuer[i]-int(listvaleur[i]/listdivisuer[i])
                if(j==listdivisuer[i]-1):
                    list.append(int(listvaleur[i]/listdivisuer[i])+round(dec))
                else :
                    list.append(int(listvaleur[i] / listdivisuer[i]))



    list2=sorted(list,reverse=True)




    for i in range(len(list2)):
        if(i%E==0):

            somme2+=list2[i]



    #somme = list2[0]+list2[10]+list2[20]

    return (somme2,list2)

T,listT=cost(x_list,diviseur,E)
print("valeur de T",T)

def voisinageDivision(vec, iter, nbr,x_list,E,T):
    bestprix=float('inf')
    listDesValeurs=[]
    for j in range(nbr):
        list = []
        if (j==0):
            best=vec[:]

        for i in range(iter):
            tmp=best[:]
            a= randint(0,len(vec)-1)
            b = randint(0,len(vec)-1)
            if (tmp[a]>1):
                tmp[a]=tmp[a]-1
                tmp[b]=tmp[b]+1

            c = randint(0,len(vec)-1)
            d = randint(0, len(vec) - 1)
            val = tmp[c]
            tmp[c]=tmp[d]
            tmp[d] = val
            list.append(tmp)


        for d in range(len(list)):
            prix,listDesValeurs= cost(x_list,list[d],E)
            if (prix<=bestprix):
                bestprix=prix
                best=list[d]
                bestListDesValeurs= listDesValeurs
            """
            else:
                diff= bestprix - prix
                P= exp(diff/(T/100))
                x=random()
               # print("dif",diff,"p",P,"x",x)
                #if(x<=P):
                #    bestprix=prix
            """
    print("meilleur cout",bestprix)
    print(best)
    print(bestListDesValeurs)
    print(len(bestListDesValeurs),sum(bestListDesValeurs))


    return best



"""
def cost(listvaleur,listdivisuer,E ):
    list=[]
    somme2=0


    for i in range(len(listvaleur)):
        dec=0
        for j in range(listdivisuer[i]):
            if (listdivisuer[i]==1):
                list.append(listvaleur[i])
            else:
                dec+=listvaleur[i]/listdivisuer[i]-int(listvaleur[i]/listdivisuer[i])
                if(j==listdivisuer[i]-1):
                    list.append(int(listvaleur[i]/listdivisuer[i])+round(dec))
                else :
                    list.append(int(listvaleur[i] / listdivisuer[i]))



    list2=sorted(list,reverse=True)




    for i in range(len(list2)):
        if(i%E==0):

            somme2+=list2[i]



    #somme = list2[0]+list2[10]+list2[20]

    return (somme2,list2)

"""



listtest = voisinageDivision(diviseur,50,1000,x_list,E,T)

print(listtest)


