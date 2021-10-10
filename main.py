# Declaration de variable 

A =15
B = 4
C=A+B
print('la valeur de ', A, '+', B, 'est', C)
D=A*B
print('la valeur de ', A, '*', B, 'est', D)

E=A^B
print('la valeur de ', A, '^', B, 'est', E)

F=A/B
print('la valeur de ', A, '/', B, 'est', F)

G=A%B
print('la valeur de ', A, '%', B, 'est', G)
print()
print()


#------------------------------------------------------CREATION DU DICTIONNAIRE 
print('MON DICTIONNAIRE ')
mon_dic = { 'A+B':C, 'A*B':D, 'A^B':E, 'A*B':F, 'A%B':G}
print()

#LISTE DES CLES DU DICTIONNAIRE
print('LES CLES ')
print()
key_list= list(mon_dic.keys())
print(key_list)

print()

#LES VALEURS DU DICTIONNAIRE
print('LES VALEURS ')
print()
values_list=list(mon_dic.values())
print(values_list)

#LES PAIRES CLES-VALEURS 

print(mon_dic)

#--------------------------------------CREATION D'UN TUPLE AVEC LES VALEURS DE A, B ET C
my_tuple=(A,B,C)

#AJOUT DE LA VALEUR DE D AU TUPLE 

d=(D,)
my_tuple=my_tuple+d
print(my_tuple) 

#IMPOSSIBLE DE MOFIFIER DES ELEMENTS DANS UN TUPLE

#IMPOSSIBLE DE SUPPRIMER AUSSI LES ELEMENTS DANS UN TUPLE

#-----------------------CREATION DES LISTES


#LISTE 1 CONTENANT LES LETTRES A, B, C ET D

liste_1=['A', 'B', 'C', 'D']

#LISTE 2 CONTENANT LES VALEURS DE A, B, C ET D

liste__2 =[A, B, C, D] 

#LISTE 3 CONTENANT LISTE 1 ET 2

liste_3=[liste_1,liste__2]
liste_1.append(E)
liste_1.append(F)

del liste_1[1]
liste_1[0]='G'
print(liste_1)