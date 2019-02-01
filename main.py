import urna_poo as u
from tkinter import *

status = 0
brancos = 0
nulos = 0
fFim = None
lFim = None
fRel = None
fFotoP = None
fFotoV = None
fNulo = None


def setNum(n):
    aux = num.cget('text')
    aux = list(aux)
    if aux[0] == '_':
        aux[0] = n
    elif aux[2] == '_':
        aux[2] = n
    aux = ''.join(aux)
    num['text'] = aux


def um():
    setNum('1')


def dois():
    setNum('2')


def tres():
    setNum('3')


def quatro():
    setNum('4')


def cinco():
    setNum('5')


def seis():
    setNum('6')


def sete():
    setNum('7')


def oito():
    setNum('8')


def nove():
    setNum('9')


def zero():
    setNum('0')


def fim():
    global status, fFim, lFim
    if status == 1 or status == 2:
        fFim = Frame(frame2, width=900, height=600, bg=AZUL)
        fFim.place(relx=0.0, rely=0.0, x=0, y=0)
        lFim = Label(frame2, bg=AZUL, font=fonte2, text='FIM')
        lFim.place(relx=0.0, rely=0.0, x=400, y=280)
    else:
        fFim.destroy()
        lFim.destroy()


def branco():
    global brancos, status, fRel, nulos
    if status == 0:
        if num['text'] == '9 9':
            status = 2
            posy = 100
            fRel = Frame(frame2, width=900, height=600, bg=AZUL)
            fRel.place(relx=0.0, rely=0.0, x=0, y=0)
            lRel = Label(fRel, bg=AZUL, fg=PRETO, font=fonte2, text='Relatório de Votos')
            lRel.place(relx=0.0, rely=0.0, x=30, y=30)
            for c in u.cands:
                lFim = Label(fRel, bg=AZUL, font=fonte3, text=f'{c.nome}: {c.totvotos}')
                lFim.place(relx=0.0, rely=0.0, x=30, y=posy)
                posy += 30
            lFim = Label(fRel, bg=AZUL, font=fonte3, text=f'Brancos: {brancos}')
            lFim.place(relx=0.0, rely=0.0, x=30, y=posy)
            posy += 30
            lFim = Label(fRel, bg=AZUL, font=fonte3, text=f'Nulos: {nulos}')
            lFim.place(relx=0.0, rely=0.0, x=30, y=posy)
            posy += 30
        else:
            brancos += 1
            fRel = Frame(frame2, width=900, height=600, bg=AZUL)
            fRel.place(relx=0.0, rely=0.0, x=0, y=0)
            lRel = Label(fRel, bg=AZUL, fg=PRETO, font=fonte2, text='FIM')
            lRel.place(relx=0.0, rely=0.0, x=400, y=270)
            fRel.after(3000, fRel.destroy)
    elif status == 2:
        fRel.destroy()
        corrigir()


def corrigir():
    global status, fFotoP, fFotoV, fNulo
    num['text'] = '_ _'
    l2['text'] = ''
    l4['text'] = ''
    l6['text'] = ''
    status = 0
    if fFotoP and fFotoV is not None:
        fFotoP.destroy()
        fFotoV.destroy()
    if fNulo is not None:
        fNulo.destroy()


def confirmar():
    global status, lFim, fFim, fFotoP, fFotoV, nulos, fNulo
    achou = False
    aux = num.cget('text')
    aux = list(aux)
    aux.pop(1)
    aux = ''.join(aux)
    aux = int(aux)
    if status == 0:
        for c in u.cands:
            if aux == c.numero:
                achou = True
                l2['text'] = c.nome
                l4['text'] = c.vice
                l6['text'] = c.partido
                foto = PhotoImage(file=c.foto[0])
                fFotoP = Label(frame2, width=150, height=200, image=foto, bd=0)
                fFotoP.image = foto
                fFotoP.place(relx=0.0, rely=0.0, x=700, y=200)
                foto = PhotoImage(file=c.foto[1])
                fFotoV = Label(frame2, width=120, height=160, image=foto, bd=0)
                fFotoV.image = foto
                fFotoV.place(relx=0.0, rely=0.0, x=730, y=420)
                status = 1
        if not achou:
            fNulo = Frame(frame2, width=900, height=600, bg=AZUL)
            fNulo.place(relx=0.0, rely=0.0, x=0, y=0)
            lNulo = Label(fNulo, bg=AZUL, font=fonte2, text='Anular voto?')
            lNulo.place(relx=0.0, rely=0.0, x=320, y=280)
            status = 2
    elif status == 1:
        for c in u.cands:
            if aux == c.numero:
                c.totvotos += 1
        fim()
        status = 0
        lFim.after(3000, fim)
        fFim.after(3000, fim)
        corrigir()
    elif status == 2:
        nulos += 1
        fim()
        status = 0
        lFim.after(3000, fim)
        fFim.after(3000, fim)
        corrigir()


BRANCO = '#FFFFFF'
PRETO = '#000000'
AZUL = '#b1d2f4'

fonte = ('Arial', '50')
fonte2 = ('Arial', '35')
fonte3 = ('Arial', '18')

i = Tk()

i.title('Urna Eletrônica')
i.geometry('1440x700')
i['bg'] = BRANCO
logo = PhotoImage(file=r'D:\Documentos\Python\MeusTestes\Interfaces Gráficas\Urna\Imagens\logo_full.png')

# Espaço acima da tela
frame3 = Frame(i, height=40)
frame3['bg'] = BRANCO
frame3.pack()

# Área frontal
frame1 = Frame(i)
frame1['bg'] = BRANCO
frame1.pack()

subframe1 = Frame(frame1)
subframe1.pack()

# Tela
frame2 = Frame(subframe1, width=900, height=600)
frame2['bg'] = AZUL
frame2.pack(side=LEFT)

# Números na tela
l_num = Label(frame2, text='Número:', bg=AZUL, fg=PRETO, font=fonte2)
l_num.place(relx=0.0, rely=0.0, x=30, y=198)
num = Label(frame2, text='_ _', bg=AZUL, fg=PRETO, font=fonte)
num.place(relx=0.0, rely=0.0, x=240, y=190)

# Tipo de voto
l0 = Label(frame2, text='SEU VOTO PARA', bg=AZUL, fg=PRETO, font=fonte3)
l0.place(relx=0.0, rely=0.0, x=10, y=10)

lPresidente = Label(frame2, text='PRESIDENTE', bg=AZUL, fg=PRETO, font=fonte2)
lPresidente.place(relx=0.0, rely=0.0, x=150, y=50)

# Label nome
l1 = Label(frame2, text='Candidato:', font=fonte2, bg=AZUL)
l1.place(relx=0.0, rely=0.0, x=30, y=300)
l2 = Label(frame2, text='', font=fonte2, bg=AZUL)
l2.place(relx=0.0, rely=0.0, x=270, y=300)
l3 = Label(frame2, text='Vice:', font=fonte2, bg=AZUL)
l3.place(relx=0.0, rely=0.0, x=30, y=380)
l4 = Label(frame2, text='', font=fonte2, bg=AZUL)
l4.place(relx=0.0, rely=0.0, x=150, y=380)
l5 = Label(frame2, text='Partido:', font=fonte2, bg=AZUL)
l5.place(relx=0.0, rely=0.0, x=30, y=460)
l6 = Label(frame2, text='', font=fonte2, bg=AZUL)
l6.place(relx=0.0, rely=0.0, x=210, y=460)

# Separação entre tela e painel
frame_sep = Frame(subframe1, width=50, height=600)
frame_sep['bg'] = BRANCO
frame_sep.pack(side=LEFT)

# Painel com o logo
lLogo = Label(subframe1, width=404, height=97)
lLogo['bg'] = BRANCO
lLogo['image'] = logo
lLogo.image = logo
lLogo.pack()

# Painel das teclas
frame4 = Frame(subframe1, width=400, height=500)
frame4['bg'] = '#292929'
frame4.pack()

# Botões
botoes = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
nomes_botoes = ('um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'zero')

for n in range(len(botoes)):
    if n % 3 == 0:
        subframe2 = Frame(frame4)
        subframe2.pack()
    a = Button(subframe2, text=botoes[n], bg='black', fg='white', width=18, height=5, command=eval(nomes_botoes[n]))
    a.pack(side=LEFT)

# Espaço para os botões inferiores
subframe3 = Frame(frame4)
subframe3.pack()
frame5 = Frame(subframe3, height=50, width=408)
frame5['bg'] = '#292929'
frame5.pack()

# Botões inferiores
a = Button(subframe3, text='BRANCO', bg='white', fg='black', width=18, height=5, command=branco)
a.pack(side=LEFT)
a = Button(subframe3, text='CORRIGE', bg='orange', fg='black', width=18, height=5, command=corrigir)
a.pack(side=LEFT)
a = Button(subframe3, text='CONFIRMA', bg='green', fg='black', width=18, height=5, command=confirmar)
a.pack()

# Espaço abaixo dos botões inferiores
subframe4 = Frame(frame4)
subframe4.pack()
frame6 = Frame(subframe4, height=20, width=400, bg='#292929')
frame6.pack()

i.mainloop()
