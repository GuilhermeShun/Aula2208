q_num=0
q_imp=0
q_par=0
soma=0
q_1=0
q_2=0
q_3=0
q_4=0
q_5=0
maior=0
menor=0

while True:
    if (bool(input("Deseja continuar? (sim: <enter>, não: digite algo) "))==True):
        if(q_num==0):
            print("\nPrograma encerrado.\n")
        break

    while True:
        num=float(input("\nNúmero: "))
        if(num==int(num)):
            num=int(num)
            break
        else:
            print("Número inválido. Insira um número inteiro.")

    soma=soma+num

    if(num%2==0):
        q_par+=1
    else:
        q_imp+=1

    q_num+=1

    if(num<0):
        q_1+=1
    elif(num<15):
        q_2+=1
    elif(num<100):
        q_3+=1
    elif(num<1000):
        q_4+=1
    else:
        q_5+=1

    if(q_num==1):
        maior=num
        menor=num
    else:
        if(num>=maior):
            maior=num
        if(num<=menor):
            menor=num

if(q_num>=1):
    print("\nMédia aritmética: ", (soma/q_num))
    print("Menor número: ", menor)
    print("Maior número: ", maior)
    print("Faixa 1: ", q_1, "elementos")
    print("Faixa 2: ", q_2, "elementos")
    print("Faixa 3: ", q_3, "elementos")
    print("Faixa 4: ", q_4, "elementos")
    print("Faixa 5: ", q_5, "elementos")
    print("Número de ímpares: ", q_imp)    
    print("Número de pares: ", q_par)    
    print("\nPrograma encerrado")        

