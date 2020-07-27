# WEB SCRAPPING - EXEMPLO 3
# BUSCAS POR NOTÍCIAS

import requests
from bs4 import BeautifulSoup
import csv
import webbrowser
from tkinter import *
import textwrap

def searchNews(subjectVar, lb_news):
	url_base = 'https://g1.globo.com/busca/?q='

	busca = subjectVar.get()

	resposta = requests.get(url_base + busca)

	site = BeautifulSoup(resposta.text, 'html.parser')

	#print(site.prettify())

	noticias = site.findAll('div', attrs={'class': 'widget--info__text-container'})

	lb_pos = 0

	news_list = [['Título', 'Descrição', 'Link']]

	for noticia in noticias:
		titulo = noticia.find('div', attrs={'class': 'widget--info__title'}).text

		descricao = noticia.find('p', attrs={'class': 'widget--info__description'}).text

		link = noticia.find('a')
		link = 'https:' + link['href']

		titulo = titulo[9:-7]

		news_list.append([titulo, descricao, link])

		lb_news.insert(lb_pos, titulo)
		lb_pos += 1

	arquivo = open('news.csv', 'w')
	escritor = csv.writer(arquivo, delimiter=';', lineterminator='\n')

	escritor.writerows(news_list)

def newsDetails(lb):
	title = lb.get(lb.curselection())

	arquivo = open('news.csv', 'r')

	planilha = csv.reader(arquivo, delimiter=';', lineterminator='\n')

	for line in planilha:
		if (line[0] == title):
			noticia = line
			break

	top = Toplevel()
	top.title('News Details')
	top['padx'] = 20

	# Wraping the news description
	titulo = textwrap.fill(noticia[0], 60)
	descricao = textwrap.fill(noticia[1], 60)

	l_title = Label(top, text=titulo, font=('Roboto Slab', 14, 'bold'))
	l_description = Label(top, text=descricao, font=('Roboto Slab', 11))
	b_open = Button(top, text='Abrir no Navegador', command=lambda: webbrowser.open(noticia[2]), font=('Roboto Slab', 11))

	top['background'] = 'grey25'
	l_title['bg'] = 'grey25'
	l_title['fg'] = 'grey99'
	l_description['bg'] = 'grey25'
	l_description['fg'] = 'grey99'

	l_title.pack(pady=10)
	l_description.pack(pady=10)
	b_open.pack(pady=10)