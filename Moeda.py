import requests
def menu():
    print(f"{"Conversor de moeda":-^40}")
    print("[1]Dolar\n[2]Euro\n[3]Bitcoin\n[4]sair")
    
requisicao=requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
dado=requisicao.json()

def converter(nome,valor):
    conversao=0
    cotacao=float(dado[nome]["bid"])
    conversao=valor*cotacao
    return conversao

def formatacao(valor):
    valor_str=f"{valor:.2f}"
    inteiro,centavos=valor_str.split(".")
    inteiro_formatado=""
    cont=0
    for digito in reversed(inteiro):
        if cont==3:
            inteiro_formatado="."+inteiro_formatado
            cont=0
        inteiro_formatado=digito+inteiro_formatado
        cont+=1
    return f"R$ {inteiro_formatado},{centavos}"
