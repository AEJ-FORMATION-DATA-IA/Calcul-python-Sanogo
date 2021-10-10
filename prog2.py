
a= input('veuillez entrer un entier svp')
if type(a)==int:
    b= input('Veuillez entrer un autre entier svp')
    if type(b)==int:
        if (a>b): 
            print(a,'est superieur a',b)
        elif (a<b): 
            print(a,'est inferieur a',b)
        else:
            print(a,'et',b,'sont egaux')
    else:
        print('Vous avez fait une erreur')
else:
    print('Vous avez fait une erreur')