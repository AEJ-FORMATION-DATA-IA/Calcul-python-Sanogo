a = input('Veuillez entrer un entier')
if type(a)==int:
    b= input('Veuillez entrez un autre entier')
    if type(b)==int:
        a+b
        print('le resultat de ',a,'+',b,'est ', a+b)
    else:
        print('Vous avez fait une erreur')
else:
    print('Vous avez fait une erreur')
