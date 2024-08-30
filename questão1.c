#include <stdio.h>
int main(){
    char nome[60];
    float si, sf, a;
    printf("Nome: ");
    fflush(stdin);
    fgets(nome, 60, stdin);
    printf("Salário atual: ");
    scanf("%f", &si);
    if(si<=400){a=1.15;}
    else if(si<=700){a=1.12;}
    else if(si<=1000){a=1.10;}
    else if(si<=1800){a=1.07;}
    else if(si<=2500){a=1.04;}
    else{a=1.0;}
    sf=si*a;
    a=100*(a-1.0);
    printf("\nNome: %sPorcentagem de aumento: %.2f\nSalário atual: %.2f\nNovo salário: %.2f\n", nome, a, si, sf);
    return 0;
}

