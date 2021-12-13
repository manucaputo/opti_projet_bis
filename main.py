"""Auteurs : Team de bg's"""


from random import randint, random
from math import exp

with open("data4.dat", "r") as f:
# Lecture du fichier
    x = []
    N = int(f.readline())
    E = int(f.readline())
    B = int(f.readline())

    for line in f:
        x.extend(line.strip().split('\t'))

x_bis = map(int, x)
x_list=list(x_bis)
print("nombre d'élément à diviser",len(x_list))
print("somme de tout les éléments",sum(x_list))
nbrmoyen=int((sum(x_list)/(B*E)))
print("division moyenne ",nbrmoyen)

print(B*E/N)
nbrdiv = int(B*E/N)

#création du vecteur de diviseur
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

#test d'un deuxiéme diviseur
diviseur2=[]
x_list_copie= x_list[:]
for i in range(len(x_list_copie)):
    div=1
    while True:
        if ((x_list_copie[i]-(2*nbrmoyen))>=0):
            x_list_copie[i]=x_list_copie[i]-nbrmoyen
            div+=1
        else:
            diviseur2.append(div)
            break




#si la somme du vecteur de diviseur n'est pas bonne
if(sum(diviseur)<(B*E)):
    for i in range(len(diviseur)):
        diviseur[i]+=1
        if(sum(diviseur)==(B*E)):
            break
if(sum(diviseur2)<(B*E)):
    for i in range(len(diviseur2)):
        diviseur2[i]+=1
        if(sum(diviseur2)==(B*E)):
            break
if(sum(diviseur2)>(B*E)):
    for i in range(len(diviseur2)):
        if(diviseur2[i]>1):
            diviseur2[i]-=1
        if(sum(diviseur2)==(B*E)):
            break
print("vec diviseur ",diviseur)

print("taille du vec divisuer",len(diviseur))
print("somme du vec diviseur",sum(diviseur))

print("vec diviseur 2 ",diviseur2)
print("taille du vec diviseur2",len(diviseur2))
print("somme du vec diviseur2",sum(diviseur2))
somme=0

#fonction pour calculer le cout
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
    return (somme2,list2)

#calcul pour un paramétre du recuit simulé
T,listT=cost(x_list,diviseur,E)
print("valeur de T",T)


# fonction pour créer le voisinage autour du vecteur de divion
# et recherche local
def voisinageDivision(vec, iter, nbr,x_list,E,T,T2):
    bestprix=float('inf')
    listDesValeurs=[]
    for j in range(nbr):
        list = []
        if (j==0):
            best=vec[:]

        # création du voisinage
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

        # pour prendre le meilleur dans le voisinage
        for d in range(len(list)):
            prix,listDesValeurs= cost(x_list,list[d],E)
            if (prix<=bestprix):
                bestprix=prix
                best=list[d]
                bestListDesValeurs= listDesValeurs
            """  
            else:
                diff= bestprix - prix
                P= exp(diff/(T/10))
                x=random()
                #print("dif",diff,"p",P,"x",x)
                if(x<=P):
                    bestprix=prix
                if (T>nbrmoyen):
                    T=T*0.9
            """


    print("meilleur cout",bestprix)
    print(best)
    print(bestListDesValeurs)
    print(len(bestListDesValeurs),sum(bestListDesValeurs))



    return best

def voisinageDivision2(vec, iter, nbr,x_list,E,T):
    bestprix=float('inf')
    listDesValeurs=[]
    for j in range(nbr):
        list = []
        if (j==0):
            best=vec[:]
        # création du voisinage
        for i in range(iter):
            tmp=best[:]

            a = randint(0, len(vec) - 1)
            b = randint(0, len(vec) - 1)
            if (tmp[a] > 1):
                tmp[a] = tmp[a] - 1
                tmp[b] = tmp[b] + 1


            val = tmp[i]
            tmp[i]=tmp[i+1]
            tmp[i+1] = val
            list.append(tmp)

        # pour prendre le meilleur dans le voisinage
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



#listtest = voisinageDivision2(diviseur,len(diviseur)-1,2000,x_list,E,T)
listtest = voisinageDivision(diviseur2,30,1000,x_list,E,T,T)

#print(listtest)


