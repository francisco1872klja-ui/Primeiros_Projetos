while True:
    try:
        print("[1]Gerar nova tabuada\n[2]Ver histórico de tabuadas\n[3]sair")
        escolha=int(input("Qual sua escolha?: "))
        print("-"*40)
        if escolha==3:
            break
        elif escolha==1:
            numero=int(input("Qual tabuada gerar?: "))
            #diferenciar a tabuada
            with open("historico_tabuada.txt","a")as arquivo:
                arquivo.write(f"{f"Escrevendo a tabua do {numero}":-^40}\n")
                for i in range(11):
                    resultado=f"{numero} x {i} = {numero*i}"
                    print(resultado)
                    arquivo.write(f"{resultado}\n")
                print("-"*40)
        elif escolha==2:
            #abre o arquivo e fala o que tem dentro
            with open("historico_tabuada.txt","r",encoding="utf-8") as arquivo:
                conteudo=arquivo.read()
            print(conteudo) 
    except:
        print("\033[31mNão foi possível gerar a tauada\033[m")
        continue
print(">>>VOLTE SEMPRE<<<")
