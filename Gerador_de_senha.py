import secrets
import string


letras_minusculas=string.ascii_lowercase
letras_maiusculas=string.ascii_uppercase
numeros=string.digits
simbolos=string.punctuation
todos_os_caractres=letras_maiusculas+letras_minusculas+numeros+simbolos
while True:
    try:
        qst_de_caractres=int(input("Qual o tamanho da senha?: "))
        print(f"{f"Gerando senha":-^40}")
        senha=""
        for i in range(qst_de_caractres):
            sorteio_caractres=secrets.choice(todos_os_caractres)
            senha+=sorteio_caractres
        print(senha)
        print(f"a senha teve {len(senha)} de tamanho!!")
        print("-"*40)
        escolha=str(input("Deseja gerar outra senha?[s/n]: ")).lower().strip()[0]
        while escolha!="s" and escolha!="n":
            escolha=str(input("Deseja gerar outra senha?[s/n]: ")).lower().strip()[0]
        if escolha=="s":
            continue
        elif escolha=="n":
            break
    except:
        print(f"\033[31Não foi possivél gerar senha\033[m")
        continue
print(">>>VOLTE SEMPRE<<<")
