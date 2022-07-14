import wikipedia
import time

def salvarArquivo(pesq, text):
    arq = open('pesquisa-'+pesq+'.txt', 'w', encoding="utf-8")
    arq.writelines(text)
    arq.close()

def wiki():
    wikipedia.set_lang("pt")
    #print(wikipedia.summary('Doctor Who'))

    print(f'Bem vindo ao sistema de pesquisa TESEU')
    pesq = input('Digite qual a sua pesquisa: ')
    
    wiki = wikipedia.page(pesq)
    
    print('pesquisando', end='')
    for i in '...':
        time.sleep(1)
        print(i, end='')
    print('\n')
    text = wiki.content
    salvarArquivo(pesq, text)
    print('Salvo Com Sucesso! \n')

    #print(text)

while True:
    wiki()

    n = input('deseja uma nova pesquisa? (S or N) ')
    if n in 'sS':
        break