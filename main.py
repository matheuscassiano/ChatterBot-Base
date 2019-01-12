#-*- coding: utf-8 -*-
import os
from chatterbot.trainers import ListTrainer # Importa o metodo para treinar o Bot com arquios de texto
from chatterbot import ChatBot

		
bot = ChatBot('Martha') # Define o "Nome" do Bot e faz com que a variavel "bot" seja equivalente a ele
bot.set_trainer(ListTrainer) # Faz com que o programa importe listas externas para treinar as suas repostas

for arq in os.listdir('arq'):
	chats = open('arq/' + arq, 'r').readlines() # Ler o conteudo das listas de frases que estão na pasta "arq"
	bot.train(chats) # Treinar as respostas do Bot de acordo com o conteudo das listas

while True: # Loop para que sempre que o Bot responder algo seja possivel inserir outra frase
	frase = input('Você: ') # Por meio desta variavel o programa ira armazenar o que o usuario digitou
	resp = bot.get_response(frase) # Ele irá analizar sua frase com o que disponivel nas listas e irá encontrar uma resposta
	print('Robô: '+str(resp)+'\n') # Ele irá mostrar a resposta na tela(podendo ser o terminal, ou caso esteja usando uma API pode ser um aplicativo de menssagens)