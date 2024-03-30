# Cotações de valor  Dólar, Euro, Bitcoin
import requests
from tkinter import *
#
def pegar_cotacoes():
    requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    #
    requisicao_dic = requisicao.json()
    #
    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']
    #
    texto = f'''
    Dólar $ {cotacao_dolar} 
    Euro € {cotacao_euro} 
    BTC ₿ {cotacao_btc}'''
    #
    texto_cotacoes['text'] = texto # trocando variavel por text 
    #escrito dentro do text=''
#
janela = Tk() # criando janela desktop
janela.title('Cotação Atual das Moedas') # mudando titulo da janela
janela.geometry('350x270')
#
texto_orientacao = Label(janela, text='Clique no botão para ver as cotações das moedas') # Label coloca o texto dentro da janela
texto_orientacao.grid(column=0, row=0, padx=10, pady=10) # grid() coloca na posição desejada
#
botao = Button(janela, text='Buscar Cotações', command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)
#
texto_cotacoes = Label(janela, text='')
texto_cotacoes.grid(column=0, row=2, padx=10, pady=10)
#
janela.mainloop() # deixa a janela exibida na tela
