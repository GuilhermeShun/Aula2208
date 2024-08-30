nome=str(input("Nome do funcionário: "))
si=float(input("Salário atual: "))
if(si<0):
    print("Salário inválido: valor negativo.")
else:
    if(si<=400):
        a=1.15
    elif(si<=700):
        a=1.12
    elif(si<=1000):
        a=1.10
    elif(si<=1800):
        a=1.07
    elif(si<=2500):
        a=1.04
    else:
        a=1.00
    sf=si*a
    print('\nNome: %s\nPorcentagem de aumento: %.2f\nSalário atual: %f\nNovo salário: %f\n' %(nome, 100*(a-1.0), si, sf))