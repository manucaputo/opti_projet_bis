from random import randint, random
from math import exp

with open("data10.dat", "r") as f:
# Lecture du fichier
    x = []
    N = int(f.readline())
    E = int(f.readline())
    B = int(f.readline())

    for line in f:
        x.extend(line.strip().split('\t'))

x_bis = map(int, x)
x_list=list(x_bis) #list des élément à diviser
print("nombre d'élément à diviser",len(x_list))
print("somme de tout les éléments",sum(x_list))
nbrmoyen=int((sum(x_list)/(B*E))) # valeur moyenne par case

somdiviseur=B*E
print("nombre de divison nécessaire",somdiviseur)

#création du vecteur de diviseur
diviseur2=[]
x_list_copie= x_list[:]
for i in range(len(x_list_copie)):
    div=1
    while True:
        if ((x_list_copie[i]-(nbrmoyen))>=0):
            x_list_copie[i]=x_list_copie[i]-nbrmoyen
            div+=1
        else:
            diviseur2.append(div)
            break

#si la somme du vecteur de diviseur n'est pas bonne

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

print("taille du vec diviseur2",len(diviseur2))
print("somme du vec diviseur2",sum(diviseur2))
somme=0
###############
#Bilal
class Partition():
    def __init__(self, List):
        self.List = List
        self.value = 0

    def setSum(self):
        self.value = sum(self.List)


class Element():
    def __init__(self, Id, value):
        self.Id = Id
        self.value = value

def countEL(El, l, c):
    z = 1
    after = 0
    before = 0

    while (True):
        if El[l * c].Id == El[l * c - z].Id:
            after += 1
            z += 1
        else:
            break
    z = 1
    while (True):
        if El[l * c].Id == El[l * c + z].Id:
            before += 1
            z += 1
        else:
            break

    return after, before

def Greedy(L, B, c,cut):
    Al = [j for j in range(len(cut)) for k in range(cut[j])]
    El = [Element(Al[j], L[j]) for j in range(len(Al))]
    El.sort(key=lambda x: x.value, reverse=True)
    Old = list(El[:])
    Part = [Partition([el.value for el in El if el.Id == i]) for i in list(set([el.Id for el in El]))]

    for l in range(B):
        if l > 0:
            if El[l * c - 1].value == El[l * c].value:
                after, before = countEL(El, l, c)
                if before > 0:

                    diff2 = El[(l - 1) * c].value - El[l * c - 1].value
                    add = diff2
                    diff = [int((after * diff2) / (before + 1)) for j in range(before)]
                    diff.append(after * diff2 - sum(diff))
                    for k in range(after):
                        El[l * c - k - 1].value += add
                    for k in range(len(diff)):
                        El[l * c + k].value -= diff[k]
                    Part = [Partition([el.value for el in El if el.Id == i]) for i in list(set([el.Id for el in El]))]
                    El.sort(key=lambda x: x.value, reverse=True)

    cost = sum([El[l * c].value for l in range(B)])
    vec = [el.value for el in El]
    Part = [Partition([el.value for el in El if el.Id == i]) for i in list(set([el.Id for el in El]))]
    return cost,vec,Part
###########

#fonction pour calculer le cout
def cost(listvaleur,listdivisuer,E ):
    list=[]
    somme2=0
    # boucle pour diviser en part égale
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
    list2=sorted(list,reverse=True) #list trier
    for i in range(len(list2)): #calcul du cout
        if(i%E==0):
            somme2+=list2[i]
    return (somme2,list2,list)

#calcul pour un paramétre du recuit simulé
T,listT,R=cost(x_list,diviseur2,E)
print("valeur de T",T)
# fonction pour le recuit simulé
def voisinageDivision2(vec, iter, nbr,x_list,E,T):
    bestprix = float('inf')
    bestprixVrai = float('inf')
    T_initial=T

    for j in range(nbr):
        list = []
        if (j == 0):
            best = vec[:]
        # création du voisinage
        # Ajouter de 1 pour un diviseur et diminution de 1 pour un divisuer
        # transpotition de 2 divisuer
        for i in range(iter):
            tmp = best[:]
            a = randint(0, len(vec) - 1)
            b = randint(0, len(vec) - 1)
            if (tmp[a] > 1):
                tmp[a] = tmp[a] - 1
                tmp[b] = tmp[b] + 1
            c = randint(0, len(vec) - 1)
            d = randint(0, len(vec) - 1)
            val = tmp[c]
            tmp[c] = tmp[d]
            tmp[d] = val
            list.append(tmp)

        # pour prendre le meilleur dans le voisinage
        listDesCout=[]
        listDesVec=[]
        listPasTrierVec=[]
        #calcul du cout pour chaque élément du voisinage
        for d in range(len(list)):
            prix, listDesValeurs,listPasTrier = cost(x_list, list[d], E)
            listDesCout.append(prix)
            listDesVec.append(listDesValeurs)
            listPasTrierVec.append(listPasTrier)
        prixPourMin=float('inf')
        indice=0
        # garde que l'élément du voisinage avec le cout le plus faible
        for i in range(len(listDesCout)):
            if(listDesCout[i]<prixPourMin):
                prixPourMin=listDesCout[i]
                indice=i
        vecteurValeur= listDesVec[indice]
        vecteurValeurpastrier=listPasTrierVec[indice]
        vecteurDiv=list[indice]
        prixGreedy, listDesValeursGreedy,Part = Greedy(vecteurValeurpastrier, B, E,vecteurDiv)

        prix=prixGreedy
        vecteurValeur=listDesValeursGreedy
        if (prix <= bestprixVrai):
                bestprixVrai = prix
                bestvrai=vecteurDiv
                bestvraiListDesValeurs= vecteurValeur
                bestPart=Part

        if (prix <= bestprix):
                bestprix = prix
                best = vecteurDiv
                bestListDesValeurs = vecteurValeur
        # tentative d'acception de la solution si elle est pas meilleur
        else:
                diff = bestprix - prix
                P = exp(diff / (T))
                x = random()
                #print("dif",diff,"p",P,"x",x, "T",T)
                if (x <= P):
                    bestprix = prix
                    best = list[indice]
                    bestListDesValeurs = listDesVec[indice]
        #modification de la valeur de T
        if(j%5==0):
           T=T*0.95
        if(T<T_initial/1000):
            break

    print(len(bestvraiListDesValeurs), sum(bestvraiListDesValeurs))
    print("valeur de T", T)
    return bestvrai, bestvraiListDesValeurs, bestprixVrai,bestPart

print("#################################")
vec,valeurs,prix,Part = voisinageDivision2(diviseur2,N*2,700,x_list,E,T)
print("diviseur", vec)
print(sum(vec))
print("valeurs", valeurs)
print("prix",prix)

#for P in Part:
#    print(P.List, "     ", sum(P.List))

#Ecriture du fichier de sortie
with open("testData22.txt", 'w', encoding='utf-8') as f:

    for i in range(len(x_list)):

        f.write(str(i+1)+" "+str(x_list[i])+" "+str(len(Part[i].List)))
        for j in Part[i].List:
            f.write(" "+str(j))
        f.write("\n")
    it=0
    for i in range(len(valeurs)):
            if(i%10==0):
                it+=1
                f.write("B"+str(it)+" "+str(valeurs[i])+"\n")
    f.write("COST"+" "+str(prix))
