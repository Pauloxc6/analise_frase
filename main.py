# -*- coding: utf-8 -*-
# libs
import os
import spacy
import pyfiglet
import platform
import datetime
from colorama import init, Fore, Back, Style

#Cor
init(autoreset=True)

#Hora é data
ht = datetime.datetime.now().time()
hf = ht.strftime("%H:%M:%S")

dt = datetime.date.today()
df = dt.strftime("%d/%m/%Y")

# Função para limpar a tela em Unix ou Windows
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

#Banner
ascii_banner = pyfiglet.figlet_format("Analise de frase")
print(ascii_banner)
print("-"*72)
print(Fore.BLUE + "By: @pauloxc6 \t" + f'(| Hora: {hf} | Data: {df} |)' + Fore.RESET)
print(Fore.BLUE + "Github: Pauloxc6" + Fore.RESET)
print("-"*72)
print()


# Carrega o modelo para a língua portuguesa
nlp = spacy.load('pt_core_news_sm')

while True:
    # Pede ao usuário para inserir uma frase
    #frase = input('Insira uma frase para análise (ou digite "sair" para encerrar o programa): ')
    print('Insira uma frase para análise (ou digite "sair" para encerrar o programa)')
    frase = input(Fore.YELLOW + f'root@{platform.system()}:~# ' + Fore.RESET)
    print()

    # Verifica se o usuário digitou "sair" para encerrar o programa
    if frase.lower() == 'sair' or frase.lower() == 'quit' or frase.lower() == 'exit':
        print("Saindo ....")
        break

    # Verifica não digitou nada
    if len(frase.strip()) == 0:
        print("Você prescisa digitar um frase para o programa funcionar")
        print("Ex: Faz muito calor")
        break

    # Analisa a frase com a biblioteca SpaCy
    doc = nlp(frase)

    # Imprime a frase
    print("="*72)
    print(f"Análise da frase : ({frase})")
    print("="*72)

    # Encontra o sujeito da frase
    sujeito = None
    for token in doc:
        if token.dep_ == 'nsubj':
            sujeito = token.text
            break

    # Encontra o verbo da frase
    verbo = None
    for token in doc:
        if token.pos_ == 'VERB':
            verbo = token
            break
    
    if verbo is None:
        print("Não foi possível identificar um verbo na frase.")
    else:
        complementos = []
        for child in verbo.children:
            if child.dep_ in ("obj", "iobj"):
                complementos.append(f"{child.text} ({child.dep_})")
 
        if not complementos:
            print(f"Verbo: {verbo.text} (vi)")
        elif len(complementos) == 1:
            print(f"Verbo: {verbo.text} (vtd)")
            print(f"Complemento: {complementos[0]}")
        else:
            print(f"Verbo: {verbo.text} (vtdi)")
            print("Complementos:")
            for c in complementos:
                print(f"- {c}")

    # Identifica os complementos do verbo
    complementos = {}
    for child in verbo.children:
        if child.dep_ in ['obj', 'iobj', 'obl']:
            complementos[child.dep_] = child.text

    # Classifica os complementos do verbo
    complementos_classificados = {}
    for dep, text in complementos.items():
        if dep == 'obj':
            complementos_classificados['Objeto direto'] = text
        elif dep == 'iobj':
            complementos_classificados['Objeto indireto'] = text
        elif dep == 'obl':
            complementos_classificados['Complemento oblíquo'] = text

    # Classifica o verbo de acordo com sua transitividade
    vtd = 'Objeto direto' in complementos_classificados
    vti = 'Objeto indireto' in complementos_classificados
    vtdi = vtd and vti

    # Imprime o resultado da análise
    print("-"*72)
    print(f'Sujeito: {sujeito}')
    print(f'Verbo: {verbo.text}')
    print("-"*72)
    if vtdi:
        print('Transitividade: Verbo transitivo direto e indireto (vtdi)')
        print(f'Objeto direto: {complementos["obj"]}')
        print(f'Objeto indireto: {complementos["iobj"]}')
    elif vtd:
        print('Transitividade: Verbo transitivo direto (vtd)')
        print(f'Objeto direto: {complementos["obj"]}')
    elif vti:
        print('Transitividade: Verbo transitivo indireto (vti)')
        print(f'Objeto indireto: {complementos["iobj"]}')
    else:
        print('Transitividade: Verbo intransitivo (vi)')
    for complemento, texto in complementos_classificados.items():
        posicao = [token.i for token in doc if token.text == texto][0] + 1 # obtém a posição do complemento na frase
        print(f'{complemento} (posição: {posicao}): {texto}') # imprime a posição e o texto do complemento
    print("="*72)
    print()
