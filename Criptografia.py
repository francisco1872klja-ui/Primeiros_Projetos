import secrets
import string
def criptografar():
    chaves=string.digits
    with open("Diario.txt","r",encoding="utf-8") as diario:
        texto_completo=diario.read()
    cript_txt=""
    txt_chave=""
    with open("Chave_Cripto.txt","a",encoding="utf-8") as chave_txt:        
            for i in texto_completo:
                chave_str=secrets.choice(chaves)
                txt_chave+=chave_str

                chave_int=int(chave_str)
                numero_cripto=ord(i)+chave_int
                cript_txt+=chr(numero_cripto)
            chave_txt.write(f"{txt_chave}\n")
    return cript_txt

def Des_cricriptografar():
    texto_descriptografado=[]
    chaves_int=[]
    with open("Chave_Cripto.txt","r",encoding="utf-8") as chave:
        for linha in chave:
            linha_limpa=linha.strip()
            for digito in linha:
                if digito.isdigit():
                    numero=int(digito)
                    chaves_int.append(numero)
    with open("Diario.txt","r",encoding="utf-8") as diario:
        conteudo_cripto=diario.read()
        frase_atual=""
        for letra_cript,chave_da_vez in zip(conteudo_cripto,chaves_int):
                if letra_cript=='\n':
                    continue
                numero_int=ord(letra_cript)-chave_da_vez
                if numero_int<0:
                    numero_int=(numero_int+1114111)%1114111
                letra_normal=chr(numero_int)
                frase_atual+=letra_normal
        texto_descriptografado.append(frase_atual)
    return texto_descriptografado

def menu():
    print(f"{"Diário":-^40}")
    print("[1]Escrever no diário\n[2]ver diario\n[3]Voltar o diario ao normal\n[4]criptografar\n[5]limpar as chaves\n[6]sair")

