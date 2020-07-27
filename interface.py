from tkinter import *
from backend import *

janela = Tk()
janela.title('News')
janela['background'] = 'grey25'
janela['padx'] = 20
janela['pady'] = 20

# FRAMES
main = Frame(janela)
buttons = Frame(janela)

# VARIABLES
subjectVar = StringVar()
subjectVar.set('Pressione enter para pesquisar...')

# WIDGETS
l_title = Label(main, text='Agregador de Notícias')

l_subject = Label(main, text='Assunto')
e_subject = Entry(main, textvariable=subjectVar)

l_results = Label(main, text='Resultados da Pesquisa')
lb_news = Listbox(main)
lb_news.bind('<Double-1>', lambda event: newsDetails(lb_news))

e_subject.bind('<Return>', lambda event: searchNews(subjectVar, lb_news))

b_open = Button(buttons, text='Ver detalhes', command=lambda: newsDetails(lb_news), font=('Roboto Slab', 10))

# CUSTOMIZATION
main['background'] = 'grey25'
buttons['background'] = 'grey25'

l_title['font'] = ('Roboto Slab', 20, 'bold')
l_title['bg'] = 'grey25'
l_title['fg'] = 'grey99'
l_subject['font'] = ('Roboto Slab', 10)
l_subject['bg'] = 'grey25'
l_subject['fg'] = 'grey99'
e_subject['font'] = ('Roboto Slab', 12)
e_subject['bg'] = 'grey25'
e_subject['fg'] = 'grey99'
e_subject['width'] = 100
l_results['font'] = ('Roboto Slab', 10)
l_results['bg'] = 'grey25'
l_results['fg'] = 'grey99'
lb_news['font'] = ('Roboto Slab', 12)
lb_news['bg'] = 'grey25'
lb_news['fg'] = 'grey99'
lb_news['width'] = 100

b_open['bg'] = 'grey99'

# POSITION
main.pack()
buttons.pack()

l_title.pack(pady=(5,10))
l_subject.pack(anchor=W, pady=(5,2))
e_subject.pack(pady=(5,10))
l_results.pack(anchor=W, pady=(5,2))
lb_news.pack(pady=(5,10))
b_open.grid(row=0, pady=(5,10))

janela.mainloop()