import Moeda

while True:
    try:
        Moeda.menu()
        escolha=int(input("Converter R$ para qual moeda?: "))
        if escolha==4:
            break
        elif escolha==1:
            moeda="USDBRL"
            valor_para_converter=float(input(f"Qual valor a ser convertido em {moeda}:"))
            valor_convertido=Moeda.converter(moeda,valor_para_converter)
            print(Moeda.formatacao(valor_convertido))
        elif escolha==2:
            moeda="EURBRL"
            valor_para_converter=float(input(f"Qual valor a ser convertido em {moeda}: "))
            valor_convertido=Moeda.converter(moeda,valor_para_converter)
            print(Moeda.formatacao(valor_convertido))
        elif escolha==3:
            moeda="BTCBRL"
            valor_para_converter=float(input(f"Qual valor a ser comvertido em {moeda}: "))
            valor_convertido=Moeda.converter(moeda,valor_para_converter)
            print(Moeda.formatacao(valor_convertido))
    except:
        print("\033[31mErro!! Colocaques algo errado\033[m")
        continue
print("-"*40)
print(">>>Volte Sempre<<<")