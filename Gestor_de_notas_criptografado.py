import Criptografia
while True:
    try:
        Criptografia.menu()
        escolha=int(input("Qual sua escolha?: "))
        if escolha==6:
            break
        elif escolha==1:
            with open("Diario.txt","a") as diario:
                linha_diario=str(input("O que Deseja escrever?:"))
                diario.write(f"{linha_diario}\n")
        elif escolha==4:
            cripto_str=Criptografia.criptografar()
            with open("Diario.txt","w",encoding="utf-8"):
                pass
            with open("Diario.txt","a",encoding="utf-8") as diario:
                diario.write(f"{cripto_str}\n")
        elif escolha==2:
            with open("Diario.txt","r",encoding="utf-8") as diario:
                conteudo=diario.read()
                print(conteudo)
        elif escolha==3:
                linha_normal=Criptografia.Des_cricriptografar()
                with open("Diario.txt","w",encoding="utf-8") as diario:
                    for item in linha_normal:
                        diario.write(f"{item}\n")
        elif escolha==5:
            with open("Chave_Cripto.txt","w"):
                pass
    except:
        print("\033[31mErro:No tipo de dado!!\033[m")
        continue
print(">>>VOLTE SEMPRE<<<")
