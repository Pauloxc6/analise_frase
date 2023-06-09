# analise_frase

Este é um código Python que permite ao usuário inserir uma frase e, em seguida, analisar sua estrutura gramatical usando a biblioteca SpaCy.

Se o usuário inserir uma frase, o código a analisa usando o SpaCy e imprime os resultados analisados, incluindo o sujeito, verbo e quaisquer objetos complementares. O código classifica o verbo como verbo transitivo ou intransitivo e identifica o tipo de complemento de objeto associado a ele.

Em resumo, esse código é um ponto de partida básico para analisar a estrutura gramatical de frases na língua portuguesa usando Python e a biblioteca SpaCy.

<!--IMG-->
<img src="https://github.com/Pauloxc6/analise_frase/blob/main/img/1.png" width="700px">

## Instalação
### Linux

1. Abra seu terminal é digite os seguintes comandos:<br/>
```
apt update && apt upgrade -y
git clone https://github.com/Pauloxc6/analise_frase/
cd ~/analise_frase
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 -m spacy download pt_core_news_sm
python3 main.py
```
ou
```
cd ~/analise_frase
make install
```
### Windows

1. Primeiro, instale a versão mais recente do [python](https://www.python.org/downloads/windows/). Verifique a arquitetura do seu processador (32 bits ou 64 bits).<br/>
2. Baixe o arquivo [.ZIP](https://github.com/Pauloxc6/analise_frase/archive/refs/heads/main.zip) e extraia-o em algum diretório do seu computador.
3. Abra seu prompt de comando (cmd)<br/>
   ``windowns + r`` é depois digite cmd (Inicie como administrador)
```
cd C:\Users\nome_do_usuario\analise_frase
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 -m spacy download pt_core_news_sm
python3 main.py
```
ou
```
cd C:\Users\nome_do_usuario\analise_frase
make 
```

## Licença

Este projeto está licenciado sob a [GNU General Public License v3.0](LICENSE).
