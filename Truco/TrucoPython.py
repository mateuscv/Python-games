# encoding=utf-8

### 0.0 # TRUCO PYTHON ###

# 0.1 # LIB : #

from graphics import *
import pygame as pg
import random

pg.mixer.init()


### 1.0 # MENU / INTEGRAÇAO ENTRE JANELAS ###

## FUNÇÕES:

# 1.1 # MENU:

def menu():
    j = GraphWin("Truco Python", 850, 700)
    j.setBackground(color_rgb(9, 107, 42))

    # Nota: Se o computador não suportar o carregamento de imagens
    # png pela graphics.py (o que é raro), comente as linhas 29 e 30 com "#" antes delas
    # e substitua "png" por "gif" na linha 34. As imagens .gif tem MUITO menos qualidade e
    # comprometem a experiência visual.

    fundo = Image(Point(425, 350), "./bg/fundomenu.png")
    fundo.draw(j)
    x = 300
    y = 0
    j.master.geometry('%dx%d+%d+%d' % (850, 700, x, y))
    header = Image(Point(415, 180), "./GUI/Truco2.png")
    header.draw(j)

    VersionNumber = Text(Point(30, 680), "v1.0")
    VersionNumber.draw(j)

    play, rules, quit, creds, msk = botoes(j)

    on = 1

    onoff = Text(Point(msk.getCenter().getX(), msk.getCenter().getY() - 35), "ON")
    onoff.setSize(14)
    onoff.draw(j)

    musica = pg.mixer.Sound("./sfx/tema.ogg")
    musica.play(-1)

    while True:
        ck = j.getMouse()
        if ck is None:
            pass
        # JOGAR
        elif dentromenu(ck, play):
            musica.stop()
            j = gamewin(j)
            return j
        # REGRAS
        elif dentromenu(ck, rules):
            musica.stop()
            j = regras(j)
            return j
        # CRÉDITOS
        elif dentromenu(ck, creds):
            musica.stop()
            j = creditos(j)
            return j
        # SAIR
        elif dentromenu(ck, quit):
            musica.stop()
            j.close()
        # SOM
        elif dentromenu(ck, msk):
            if on == 1:
                musica.stop()
                on = 0
                onoff.setText("OFF")
            else:
                musica.play(-1)
                on = 1
                onoff.setText("ON")


# 1.2 # BOTOES GRAFICOS:

def botoes(win):
    # Jogar
    play = Rectangle(Point(302, 410), Point(528, 360))
    botaoplay = Image(play.getCenter(), "./GUI/botao.gif")
    botaoplay.draw(win)
    tplay = Text(play.getCenter(), "JOGAR")
    tplay.setFill(color_rgb(244, 217, 7))
    tplay.draw(win)
    # Regras
    rules = Rectangle(Point(302, 485), Point(528, 435))
    botaorules = Image(rules.getCenter(), "./GUI/botao.gif")
    botaorules.draw(win)
    trules = Text(rules.getCenter(), "COMO JOGAR")
    trules.setFill(color_rgb(244, 217, 7))
    trules.draw(win)
    # Créditos
    creds = Rectangle(Point(302, 560), Point(528, 510))
    botaocreds = Image(creds.getCenter(), "./GUI/botao.gif")
    botaocreds.draw(win)
    tcreds = Text(creds.getCenter(), "CRÉDITOS")
    tcreds.setFill(color_rgb(244, 217, 7))
    tcreds.draw(win)
    # Sair
    quit = Rectangle(Point(302, 635), Point(528, 585))
    botaoquit = Image(quit.getCenter(), "./GUI/botao.gif")
    botaoquit.draw(win)
    tquit = Text(quit.getCenter(), "SAIR")
    tquit.setFill(color_rgb(244, 217, 7))
    tquit.draw(win)
    # Som
    snd = Rectangle(Point(780, 690), Point(840, 640))
    botaosom = Image(snd.getCenter(), "./GUI/som.gif")
    botaosom.draw(win)
    return play, rules, quit, creds, snd


# 1.3 # TESTE AREA DO CLIQUE:

def dentromenu(ck, bt):
    lleft = bt.getP1()
    uright = bt.getP2()
    if ((lleft.getX() < ck.getX()) and (ck.getX() < uright.getX())) and (
                (lleft.getY() > ck.getY()) and (ck.getY() > uright.getY())):
        return True
    else:
        return False


# 1.4 # TESTE ÁREA DO CLIQUE CIRCULAR:

def dentromenur(ck, bt):
    center = bt.getCenter()
    raio = bt.getRadius()
    if ((abs(ck.getX() - center.getX()) <= raio)) and ((abs(ck.getY() - center.getY()) <= raio)):
        return True
    else:
        return False


# 1.5 # REGRAS:

def regras(win):
    win.close()
    j = GraphWin("Regras do Truco", 800, 600)
    j.master.geometry('%dx%d+%d+%d' % (800, 600, 225, 0))
    rulesi = Image(Point(400, 300), "./bg/Regrasph.gif")
    rulesi.draw(j)
    j.getMouse()
    rulesi = Image(Point(400, 300), "./bg/regras2.gif")
    rulesi.draw(j)
    j.getMouse()
    rulesi = Image(Point(400, 300), "./bg/regras3.gif")
    rulesi.draw(j)
    j.getMouse()
    rulesi = Image(Point(400, 300), "./bg/regras4.gif")
    rulesi.draw(j)
    j.getMouse()
    j.close()
    j = menu()
    return j


# 1.6 # CRÉDITOS:

def creditos(win):
    win.close()
    j = GraphWin("Truco Python: Créditos", 800, 600)
    j.master.geometry('%dx%d+%d+%d' % (800, 600, 225, 0))
    c1 = Image(Point(400, 300), "./bg/cred1.gif")
    c2 = Image(Point(400, 300), "./bg/cred2.gif")
    c3 = Image(Point(400, 300), "./bg/cred3.gif")
    c4 = Image(Point(400, 300), "./bg/cred4.gif")
    creditos = [c1, c2, c3, c4]
    for x in creditos:
        x.draw(j)
        j.getMouse()
        x.undraw()
    playing = 0
    j.close()
    j = menu()
    return j


# 1.7 # ABERTURA JOGO:

def gamewin(win):
    win.close()
    j = GraphWin("Truco Python - Execução", 1024, 700)
    j.master.geometry('%dx%d+%d+%d' % (1024, 700, 225, 0))
    j.setBackground(color_rgb(30, 80, 40))
    t = Text(Point(512, 350), "PRONTO?")
    t.setOutline(color_rgb(255, 255, 255))
    t.setSize(22)
    t.draw(j)
    t1 = Text(Point(512, 380), "Clique na tela para jogar.")
    t1.setOutline(color_rgb(255, 255, 255))
    t1.setSize(18)
    t1.draw(j)
    j.getMouse()
    t.undraw()
    t1.undraw()
    fundo = Image(Point(512, 350), "./GUI/fundo.gif")
    fundo.draw(j)
    return j


### 2.0 # ESTRUTURA DO JOGO ###

## FUNÇÕES:

# 2.1 # CARTAS:

# 2.1.1 # NAIPES:

def naipes():
    O = []
    C = []
    P = []
    E = []
    cont = 0
    while cont < 10:
        if cont < 7:
            O.append(["O", cont + 1])
        elif cont == 7:
            O.append(["O", 10])
        elif cont == 8:
            O.append(["O", 11])
        elif cont == 9:
            O.append(["O", 12])
        cont += 1
    cont = 0
    while cont < 10:
        if cont < 7:
            C.append(["C", cont + 1])
        elif cont == 7:
            C.append(["C", 10])
        elif cont == 8:
            C.append(["C", 11])
        elif cont == 9:
            C.append(["C", 12])
        cont += 1
    cont = 0
    while cont < 10:
        if cont < 7:
            P.append(["P", cont + 1])
        elif cont == 7:
            P.append(["P", 10])
        elif cont == 8:
            P.append(["P", 11])
        elif cont == 9:
            P.append(["P", 12])
        cont += 1
    cont = 0
    while cont < 10:
        if cont < 7:
            E.append(["E", cont + 1])
        elif cont == 7:
            E.append(["E", 10])
        elif cont == 8:
            E.append(["E", 11])
        elif cont == 9:
            E.append(["E", 12])
        cont += 1
    img(O, C, P, E)
    return O, C, P, E


# 2.1.2 # IMAGENS E VALOR DAS CARTAS:

def img(n1, n2, n3, n4):
    # Ouro:

    O1i = Image(Point(512, 575), "./Imagens/O1.gif")
    O2i = Image(Point(512, 575), "./Imagens/O2.gif")
    O3i = Image(Point(512, 575), "./Imagens/O3.gif")
    O4i = Image(Point(512, 575), "./Imagens/O4.gif")
    O5i = Image(Point(512, 575), "./Imagens/O5.gif")
    O6i = Image(Point(512, 575), "./Imagens/O6.gif")
    O7i = Image(Point(512, 575), "./Imagens/O7.gif")
    O10i = Image(Point(512, 575), "./Imagens/O10.gif")
    O11i = Image(Point(512, 575), "./Imagens/O11.gif")
    O12i = Image(Point(512, 575), "./Imagens/O12.gif")

    n1[0].append(O1i)
    n1[0].append(8)
    n1[1].append(O2i)
    n1[1].append(9)
    n1[2].append(O3i)
    n1[2].append(10)
    n1[3].append(O4i)
    n1[3].append(1)
    n1[4].append(O5i)
    n1[4].append(2)
    n1[5].append(O6i)
    n1[5].append(3)
    n1[6].append(O7i)
    n1[6].append(11)
    n1[7].append(O10i)
    n1[7].append(5)
    n1[8].append(O11i)
    n1[8].append(6)
    n1[9].append(O12i)
    n1[9].append(7)

    cont = 0
    while cont < 7:
        n1[cont].append(cont + 1)
        cont += 1
    while cont < len(n1):
        n1[cont].append(0)
        cont += 1

    # Copas:

    C1i = Image(Point(512, 575), "./Imagens/C1.gif")
    C2i = Image(Point(512, 575), "./Imagens/C2.gif")
    C3i = Image(Point(512, 575), "./Imagens/C3.gif")
    C4i = Image(Point(512, 575), "./Imagens/C4.gif")
    C5i = Image(Point(512, 575), "./Imagens/C5.gif")
    C6i = Image(Point(512, 575), "./Imagens/C6.gif")
    C7i = Image(Point(512, 575), "./Imagens/C7.gif")
    C10i = Image(Point(512, 575), "./Imagens/C10.gif")
    C11i = Image(Point(512, 575), "./Imagens/C11.gif")
    C12i = Image(Point(512, 575), "./Imagens/C12.gif")
    n2[0].append(C1i)
    n2[0].append(8)
    n2[1].append(C2i)
    n2[1].append(9)
    n2[2].append(C3i)
    n2[2].append(10)
    n2[3].append(C4i)
    n2[3].append(1)
    n2[4].append(C5i)
    n2[4].append(2)
    n2[5].append(C6i)
    n2[5].append(3)
    n2[6].append(C7i)
    n2[6].append(4)
    n2[7].append(C10i)
    n2[7].append(5)
    n2[8].append(C11i)
    n2[8].append(6)
    n2[9].append(C12i)
    n2[9].append(7)

    cont = 0
    while cont < 7:
        n2[cont].append(cont + 1)
        cont += 1
    while cont < len(n2):
        n2[cont].append(0)
        cont += 1

    # Paus:

    P1i = Image(Point(512, 575), "./Imagens/P1.gif")
    P2i = Image(Point(512, 575), "./Imagens/P2.gif")
    P3i = Image(Point(512, 575), "./Imagens/P3.gif")
    P4i = Image(Point(512, 575), "./Imagens/P4.gif")
    P5i = Image(Point(512, 575), "./Imagens/P5.gif")
    P6i = Image(Point(512, 575), "./Imagens/P6.gif")
    P7i = Image(Point(512, 575), "./Imagens/P7.gif")
    P10i = Image(Point(512, 575), "./Imagens/P10.gif")
    P11i = Image(Point(512, 575), "./Imagens/P11.gif")
    P12i = Image(Point(512, 575), "./Imagens/P12.gif")
    n3[0].append(P1i)
    n3[0].append(13)
    n3[1].append(P2i)
    n3[1].append(9)
    n3[2].append(P3i)
    n3[2].append(10)
    n3[3].append(P4i)
    n3[3].append(1)
    n3[4].append(P5i)
    n3[4].append(2)
    n3[5].append(P6i)
    n3[5].append(3)
    n3[6].append(P7i)
    n3[6].append(4)
    n3[7].append(P10i)
    n3[7].append(5)
    n3[8].append(P11i)
    n3[8].append(6)
    n3[9].append(P12i)
    n3[9].append(7)

    cont = 0
    while cont < 7:
        n3[cont].append(cont + 1)
        cont += 1
    while cont < len(n3):
        n3[cont].append(0)
        cont += 1

    # Espadas:

    E1i = Image(Point(512, 575), "./Imagens/E1.gif")
    E2i = Image(Point(512, 575), "./Imagens/E2.gif")
    E3i = Image(Point(512, 575), "./Imagens/E3.gif")
    E4i = Image(Point(512, 575), "./Imagens/E4.gif")
    E5i = Image(Point(512, 575), "./Imagens/E5.gif")
    E6i = Image(Point(512, 575), "./Imagens/E6.gif")
    E7i = Image(Point(512, 575), "./Imagens/E7.gif")
    E10i = Image(Point(512, 575), "./Imagens/E10.gif")
    E11i = Image(Point(512, 575), "./Imagens/E11.gif")
    E12i = Image(Point(512, 575), "./Imagens/E12.gif")
    n4[0].append(E1i)
    n4[0].append(14)
    n4[1].append(E2i)
    n4[1].append(9)
    n4[2].append(E3i)
    n4[2].append(10)
    n4[3].append(E4i)
    n4[3].append(1)
    n4[4].append(E5i)
    n4[4].append(2)
    n4[5].append(E6i)
    n4[5].append(3)
    n4[6].append(E7i)
    n4[6].append(12)
    n4[7].append(E10i)
    n4[7].append(5)
    n4[8].append(E11i)
    n4[8].append(6)
    n4[9].append(E12i)
    n4[9].append(7)

    cont = 0
    while cont < 7:
        n4[cont].append(cont + 1)
        cont += 1
    while cont < len(n4):
        n4[cont].append(0)
        cont += 1


def verso():
    Verso = Image(Point(512, 35), "./Imagens/Verso.gif")
    Verso1 = Image(Point(512, 35), "./Imagens/Verso.gif")
    Verso2 = Image(Point(512, 35), "./Imagens/Verso.gif")

    return Verso, Verso1, Verso2


# 2.2 # BARALHO:

# 2.2.1 # EMBARALHARAMENTO:

def embaralhar(n1, n2, n3, n4):
    B = []
    for x in n1:
        B.append(x)
    for x in n2:
        B.append(x)
    for x in n3:
        B.append(x)
    for x in n4:
        B.append(x)
    random.shuffle(B)
    return B


# 2.3 # MÃO:

# 2.3.1 # DISTRIBUIÇÃO NA MÃO:

def mao(baralho):
    m = []
    mAI = []
    x = 0
    cont = 0
    while x < 3:
        m.append(baralho[cont])
        cont += 1
        mAI.append(baralho[cont])
        x += 1
        cont += 1
    return m, mAI


# 2.3.2 # DESENHO DA MÃO:

def desenhamao(lmao, win):
    cont = 0
    for carta in lmao:
        if cont == 0:
            carta[2].undraw()
            carta[2].draw(win)
            carta[2].move(-160, 10)
        elif cont == 1:
            carta[2].undraw()
            carta[2].draw(win)
            carta[2].move(0, 10)
        elif cont == 2:
            carta[2].undraw()
            carta[2].draw(win)
            carta[2].move(160, 10)
        cont += 1


# 2.3.3 # DESENHO MÃO AI:

def desenhoai(v, v1, v2, win):
    v.undraw()
    v1.undraw()
    v2.undraw()
    v1.draw(win)
    v2.draw(win)
    v1.move(-112, 0)
    v2.move(112, 0)
    v.draw(win)


# 2.4 # TURNOS DA RODADA:

# 2.4.1 # TURNO JOGADOR:

def jogarcartap1(cont, lmao, lmao2, win, v1, v2, v3, s, startvalue1, svt, vcartaai, contp, contai, pt, ptai, contvez,
                 tcp, tcai,
                 lcj):
    global Botao
    global joga1sfx
    global espadaosfx
    global truco
    global ptruco
    global truconegadoj
    global trucoast
    global retrucoast
    global v4ast
    global florast
    global envast
    global Benvido
    global Et
    global Bflor
    global Ft
    global Renvido
    global Ret
    global flor
    global florastAI
    global pretruco
    global envido_pedido
    global valorenvidoAI
    Botao.setOutline(color_rgb(160, 110, 11))
    Botao.setFill(color_rgb(58, 34, 5))
    Tbt.setFill(color_rgb(255, 255, 255))
    if Tbt.getText() == "-" or (ptruco == True and truco != 2):
        Botao.setFill(color_rgb(96, 90, 90))
        Botao.setOutline(color_rgb(137, 132, 132))
        Tbt.setFill(color_rgb(137, 132, 132))
    Benvido.setOutline(color_rgb(160, 110, 11))
    Benvido.setFill(color_rgb(58, 34, 5))
    Et.setOutline(color_rgb(255, 255, 255))
    Espera = Text(Point(512, 360), "Aguardando...")
    Act = Text(Point(512, 320), "QUERO!")
    Act.setSize(32)
    Rjt = Text(Point(512, 320), "Não!")
    Rjt.setSize(32)
    Espera.setSize(25)
    EnvidoCall = Text(Point(512, 320), "ENVIDO!")
    EnvidoCall.setSize(32)
    if (lmao[0][0] == lmao[1][0]) and (lmao[0][0] == lmao[2][0]) and (
                lmao[1][0] == lmao[2][0]) and contvez == 1 and flor != 1:
        Bflor.setOutline(color_rgb(160, 110, 11))
        Bflor.setFill(color_rgb(58, 34, 5))
        Ft.setOutline(color_rgb(255, 255, 255))
    svt.undraw()
    svt = Text(Point(108, 630), "Você")
    svt.setFill(color_rgb(255, 255, 255))
    svt.setSize(18)
    svt.draw(j)
    c1 = Rectangle(Point(274, 696), Point(428, 467))
    c2 = Rectangle(Point(435, 698), Point(589, 470))
    c3 = Rectangle(Point(597, 697), Point(749, 469))



    while True:
        ck = win.getMouse()
        if ck is None:
            pass

        # Botão de ação

        elif dentromenur(ck, Botao):
            if truco == 0:
                Pediu = Text(Point(512, 320), "TRUCO!")
                ptruco = True
                Pediu.setSize(32)
                Pediu.draw(win)
                time.sleep(.40)
                Espera.draw(win)
                time.sleep(.85)
                Pediu.undraw()
                Espera.undraw()
                if truco == 0:
                    act = random.randint(0, 1)
                    if act == 0 and contp != 14:
                        pass
                        rjtrnd = random.randint(1, 3)
                        if rjtrnd == 1:
                            Rjt.draw(win)
                            time.sleep(.7)
                            Rjt.undraw()
                        elif rjtrnd == 2:
                            Rjt.setText("Não quero!")
                            Rjt.draw(win)
                            time.sleep(.7)
                            Rjt.undraw()
                        else:
                            Rjt.setText("Acha que sou louco?")
                            Rjt.draw(win)
                            time.sleep(.7)
                            Rjt.undraw()
                        truconegadoj = 1
                        valorp = 0
                        return turno(cont, valorp, vcartaai, contp, contai, win, pt, ptai, tcp, tcai, lmao, lmao2, s,
                                     startvalue1, svt,
                                     lcj)
                    else:
                        truco = 1
                        Act.draw(win)
                        Botao.setFill(color_rgb(96, 90, 90))
                        Botao.setOutline(color_rgb(137, 132, 132))
                        Tbt.setFill(color_rgb(137, 132, 132))
                        time.sleep(.7)
                        Act.undraw()

                        # RETRUCO

            elif truco == 1 and ptruco == False and retrucoast != "*":
                Pediu = Text(Point(512, 320), "RETRUCO!")
                pretruco = True
                Pediu.setSize(32)
                Pediu.draw(win)
                time.sleep(.40)
                Espera.draw(win)
                time.sleep(.85)
                Pediu.undraw()
                Espera.undraw()
                act = random.randint(0, 1)
                if act == 0 and contp < 13:
                    rjtrnd = random.randint(1, 3)
                    if rjtrnd == 1:
                        Rjt.draw(win)
                        time.sleep(.7)
                        Rjt.undraw()
                        valorp = 0
                    elif rjtrnd == 2:
                        Rjt.setText("Não quero!")
                        Rjt.draw(win)
                        time.sleep(.7)
                        Rjt.undraw()
                        valorp = 0
                    else:
                        Rjt.setText("Acha que sou louco?")
                        Rjt.draw(win)
                        time.sleep(.7)
                        Rjt.undraw()
                        valorp = 0
                    truco = 1
                    truconegadoj = 1
                    return turno(cont, valorp, vcartaai, contp, contai, win, pt, ptai, tcp, tcai, lmao, lmao2, s,
                                 startvalue1, svt,
                                 lcj)
                else:
                    truco = 2
                    Tbt.setText("-")
                    Act.draw(win)
                    Botao.setFill(color_rgb(96, 90, 90))
                    Botao.setOutline(color_rgb(137, 132, 132))
                    Tbt.setFill(color_rgb(137, 132, 132))
                    time.sleep(.7)
                    Act.undraw()
                retrucoast = "*"

                # VALE QUATRO

            elif truco == 2 and pretruco == False and v4ast != "*":
                Pediu = Text(Point(512, 320), "VALE QUATRO!!")
                pretruco = True
                Pediu.setSize(32)
                Pediu.draw(win)
                time.sleep(.40)
                Espera.draw(win)
                time.sleep(.85)
                Pediu.undraw()
                Espera.undraw()
                act = random.randint(0, 1)
                if act == 0 and contp < 12:
                    rjtrnd = random.randint(1, 3)
                    if rjtrnd == 1:
                        Rjt.draw(win)
                        time.sleep(.7)
                        Rjt.undraw()
                        valorp = 0
                    elif rjtrnd == 2:
                        Rjt.setText("Não quero!")
                        Rjt.draw(win)
                        time.sleep(.7)
                        Rjt.undraw()
                        valorp = 0
                    else:
                        Rjt.setText("Acha que sou louco?")
                        Rjt.draw(win)
                        time.sleep(.7)
                        Rjt.undraw()
                        valorp = 0
                    truco = 2
                    truconegadoj = 1
                    return turno(cont, valorp, vcartaai, contp, contai, win, pt, ptai, tcp, tcai, lmao, lmao2, s,
                                 startvalue1, svt,
                                 lcj)
                else:
                    truco = 3
                    Tbt.setText("-")
                    Act.draw(win)
                    Botao.setFill(color_rgb(96, 90, 90))
                    Botao.setOutline(color_rgb(137, 132, 132))
                    Tbt.setFill(color_rgb(137, 132, 132))
                    time.sleep(.7)
                    Act.undraw()
                v4ast = "*"

        # Botão de flor

        elif dentromenur(ck, Bflor):
            if florast != "*" and flor != 1 and contvez == 1 and lmao[0][0]==lmao[1][0] and lmao[1][0]==lmao[2][0]:
                decflor = Text(Point(512, 330), "FLOR!")
                decflor.setSize(32)
                decflor.setFill(color_rgb(0, 0, 0))
                decflor.draw(win)
                animflor(win)
                time.sleep(.2)
                decflor.undraw()
                contp += 3
                strc = contp
                pt.setText(strc)
                Bflor.setOutline(color_rgb(137, 132, 132))
                Bflor.setFill(color_rgb(96, 90, 90))
                Ft.setOutline(color_rgb(137, 132, 132))
                Benvido.setOutline(color_rgb(137, 132, 132))
                Benvido.setFill(color_rgb(96, 90, 90))
                Et.setOutline(color_rgb(137, 132, 132))
                flor = 1
                if testefim(contp, contai):
                    fim(contp, contai, win)
            florast = "*"

        # Botão de envido

        elif dentromenur(ck, Benvido):
            if flor == 0 and contvez == 1 and (
                                lmao[0][0] != lmao[1][0] or lmao[0][0] != lmao[2][0] or lmao[1][0] != lmao[2][0]):
                if (lmao[0][0] == lmao[1][0]):
                    valorenvido = 20 + lmao[0][4] + lmao[1][4]
                elif (lmao[0][0] == lmao[2][0]):
                    valorenvido = 20 + lmao[0][4] + lmao[2][4]
                elif (lmao[1][0] == lmao[2][0]):
                    valorenvido = 20 + lmao[1][4] + lmao[2][4]
                else:
                    valorenvido = 0
                if envast != "*":
                    draw = 1
                    Renvido.draw(win)
                    Ret.draw(win)
                    Fenvido.draw(win)
                    Fet.draw(win)
                    while True:
                        ck = win.getMouse()
                        if ck is None:
                            pass

                        elif dentromenur(ck, Renvido):
                            envast = "*"
                            EnvidoCall.setText("REAL ENVIDO!")
                            EnvidoCall.draw(win)
                            envido_pedido = 1
                            if draw == 1:
                                time.sleep(1)
                                Espera.draw(win)

                                # AI
                                if valorenvidoAI == 0 and contvez == 1:
                                    if (lmao2[0][0] == lmao2[1][0]):
                                        valorenvidoAI = 20 + lmao2[0][4] + lmao2[1][4]
                                    elif (lmao2[0][0] == lmao2[2][0]):
                                        valorenvidoAI = 20 + lmao2[0][4] + lmao2[2][4]
                                    elif (lmao2[1][0] == lmao2[2][0]):
                                        valorenvidoAI = 20 + lmao2[1][4] + lmao2[2][4]
                                    else:
                                        valorenvidoAI = 0

                                if valorenvidoAI >= 27:
                                    envrnd = random.randint(0, 50)
                                elif valorenvidoAI >= 32:
                                    envrnd = 40
                                else:
                                    envrnd = 0

                                if contp == 14:
                                    envrnd = 0

                                time.sleep(2)
                                EnvidoCall.undraw()
                                Espera.undraw()

                                if ((lmao2[0][0] == lmao2[1][0]) and (lmao2[1][0] == lmao2[2][0])):
                                    cfr = 1
                                else:
                                    cfr = 0

                                if envrnd >= 40 and cfr == 0:
                                    Act.draw(win)
                                    time.sleep(1)
                                    Act.undraw()
                                    if comparaenvido(valorenvido, valorenvidoAI, win):
                                        contp += 3
                                        spt = str(contp)
                                        pt.setText(spt)
                                        if testefim(contp, contai):
                                            fim(contp, contai, win)
                                    else:
                                        contai += 3
                                        spt = str(contai)
                                        ptai.setText(spt)
                                        if testefim(contp, contai):
                                            fim(contp, contai, win)
                                    time.sleep(2)
                                elif cfr == 1 and flor != 1:
                                    if florastAI != "*":
                                        decflor = Text(Point(512, 330), "FLOR!")
                                        decflor.setSize(32)
                                        decflor.draw(win)
                                        animflor(win)
                                        time.sleep(.2)
                                        contai += 3
                                        strcAI = contai
                                        ptai.setText(strcAI)
                                        decflor.undraw()
                                        flor = 1
                                        if testefim(contp, contai):
                                            fim(contp, contai, win)
                                    florastAI = "*"
                                else:
                                    Rjt.draw(win)
                                    contp += 1
                                    spt = str(contp)
                                    pt.setText(spt)
                                    time.sleep(2)
                                    Rjt.undraw()
                                    if testefim(contp, contai):
                                        fim(contp, contai, win)

                                Renvido.undraw()
                                Fenvido.undraw()
                                Ret.undraw()
                                Fet.undraw()

                        elif dentromenur(ck, Fenvido):
                            envast = "*"
                            EnvidoCall.setText("FALTA ENVIDO!")
                            EnvidoCall.draw(win)
                            envido_pedido = 1
                            if draw == 1:
                                time.sleep(1)
                                Espera.draw(win)

                                # AI
                                if valorenvidoAI == 0 and contvez == 1:
                                    if (lmao2[0][0] == lmao2[1][0]):
                                        valorenvidoAI = 20 + lmao2[0][4] + lmao2[1][4]
                                    elif (lmao2[0][0] == lmao2[2][0]):
                                        valorenvidoAI = 20 + lmao2[0][4] + lmao2[2][4]
                                    elif (lmao2[1][0] == lmao2[2][0]):
                                        valorenvidoAI = 20 + lmao2[1][4] + lmao2[2][4]
                                    else:
                                        valorenvidoAI = 0

                                if valorenvidoAI >= 30:
                                    envrnd = random.randint(0, 50)
                                elif valorenvidoAI >= 32:
                                    envrnd = 40
                                else:
                                    envrnd = 0

                                if contp == 14:
                                    envrnd = 0

                                time.sleep(2)
                                EnvidoCall.undraw()
                                Espera.undraw()

                                if ((lmao2[0][0] == lmao2[1][0]) and (lmao2[1][0] == lmao2[2][0])):
                                    cfr = 1
                                else:
                                    cfr = 0

                                if envrnd >= 40 and cfr == 0:
                                    Act.draw(win)
                                    time.sleep(1)
                                    Act.undraw()
                                    if comparaenvido(valorenvido, valorenvidoAI, win):
                                        contp += 15 - contai
                                        spt = str(contp)
                                        pt.setText(spt)
                                        if testefim(contp, contai):
                                            fim(contp, contai, win)
                                    elif cfr == 1 and flor != 1:
                                        if florastAI != "*":
                                            decflor = Text(Point(512, 330), "FLOR!")
                                            decflor.setSize(32)
                                            decflor.draw(win)
                                            animflor(win)
                                            time.sleep(.2)
                                            contai += 3
                                            strcAI = contai
                                            ptai.setText(strcAI)
                                            time.sleep(.8)
                                            decflor.undraw()
                                            flor = 1
                                            if testefim(contp, contai):
                                                fim(contp, contai, win)
                                        florastAI = "*"
                                    else:
                                        contai += 15 - contp
                                        spt = str(contai)
                                        ptai.setText(spt)
                                        if testefim(contp, contai):
                                            fim(contp, contai, win)
                                    time.sleep(2)
                                else:
                                    Rjt.draw(win)
                                    contp += 1
                                    spt = str(contp)
                                    pt.setText(spt)
                                    time.sleep(2)
                                    Rjt.undraw()
                                    if testefim(contp, contai):
                                        fim(contp, contai, win)

                                Renvido.undraw()
                                Fenvido.undraw()
                                Ret.undraw()
                                Fet.undraw()

                        elif dentromenur(ck, Benvido):
                            envast = "*"
                            EnvidoCall.draw(win)
                            envido_pedido = 1
                            time.sleep(1)
                            Espera.draw(win)

                            # AI
                            if valorenvidoAI == 0 and contvez == 1:
                                if (lmao2[0][0] == lmao2[1][0]):
                                    valorenvidoAI = 20 + lmao2[0][4] + lmao2[1][4]
                                elif (lmao2[0][0] == lmao2[2][0]):
                                    valorenvidoAI = 20 + lmao2[0][4] + lmao2[2][4]
                                elif (lmao2[1][0] == lmao2[2][0]):
                                    valorenvidoAI = 20 + lmao2[1][4] + lmao2[2][4]
                                else:
                                    valorenvidoAI = 0

                            if valorenvidoAI >= 23 and valorenvidoAI <= 26:
                                envrnd = random.randint(0, 100)
                            elif valorenvidoAI >= 26:
                                envrnd = random.randint(38, 100)
                            else:
                                envrnd = random.randint(-255, 41)

                            if contp == 14:
                                envrnd = 0

                            time.sleep(2)
                            EnvidoCall.undraw()
                            Espera.undraw()

                            if ((lmao2[0][0] == lmao2[1][0]) and (lmao2[1][0] == lmao2[2][0])):
                                cfr = 1
                            else:
                                cfr = 0

                            if envrnd >= 40 and cfr == 0:
                                Act.draw(win)
                                time.sleep(1)
                                Act.undraw()
                                if comparaenvido(valorenvido, valorenvidoAI, win):
                                    contp += 2
                                    spt = str(contp)
                                    pt.setText(spt)
                                elif cfr == 1 and flor != 1:
                                    if florastAI != "*":
                                        decflor = Text(Point(512, 330), "FLOR!")
                                        decflor.setSize(32)
                                        decflor.draw(win)
                                        animflor(win)
                                        time.sleep(.2)
                                        contai += 3
                                        strcAI = contai
                                        ptai.setText(strcAI)
                                        time.sleep(.4)
                                        decflor.undraw()
                                        flor = 1
                                    florastAI = "*"
                                else:
                                    contai += 2
                                    spt = str(contai)
                                    ptai.setText(spt)
                                    if testefim(contp, contai):
                                        fim(contp, contai, win)
                                time.sleep(2)
                            else:
                                Rjt.draw(win)
                                contp += 1
                                spt = str(contp)
                                pt.setText(spt)
                                time.sleep(2)
                                Rjt.undraw()
                                if testefim(contp, contai):
                                    fim(contp, contai, win)

                            Renvido.undraw()
                            Fenvido.undraw()
                            Ret.undraw()
                            Fet.undraw()
                        else:
                            Renvido.undraw()
                            Fenvido.undraw()
                            Ret.undraw()
                            Fet.undraw()
                            draw = 0
                        break
        # Carta 1
        elif dentromenu(ck, c1):
            if lmao[0] != "*":
                valorp = lmao[0][3]
                if valorp == 14:
                    espadaosfx.play()
                else:
                    joga1sfx.play()
                time.sleep(.15)
                lcj.append(lmao[0][2])
                lmao[0][2].undraw()
                if s == 0:
                    lmao[0][2].draw(win)
                    if contvez == 1:
                        lmao[0][2].move(-258, -270)
                    elif contvez == 2:
                        lmao[0][2].move(85, -270)
                    elif contvez == 3:
                        lmao[0][2].move(428, -270)
                    lmao[0] = "*"
                    return jogarcartaai1(cont, lmao2, lmao, win, v1, v2, v3, s, startvalue1, svt, valorp, contp, contai,
                                         pt, ptai,
                                         contvez,
                                         tcp, tcai, lcj)

                else:
                    lmao[0][2].draw(win)
                    if contvez == 1:
                        lmao[0][2].move(-109, -270)
                    elif contvez == 2:
                        lmao[0][2].move(234, -270)
                    elif contvez == 3:
                        lmao[0][2].move(577, -270)
                    lmao[0] = "*"
                    return turno(cont, valorp, vcartaai, contp, contai, win, pt, ptai, tcp, tcai, lmao, lmao2, s,
                                 startvalue1, svt,
                                 lcj)

        # Carta 2
        elif dentromenu(ck, c2):
            if lmao[1] != "*":
                valorp = lmao[1][3]
                if valorp == 14:
                    espadaosfx.play()
                else:
                    joga1sfx.play()
                time.sleep(.15)
                lmao[1][2].undraw()
                lcj.append(lmao[1][2])
                if s == 0:
                    lmao[1][2].draw(win)
                    if contvez == 1:
                        lmao[1][2].move(-418, -270)
                    elif contvez == 2:
                        lmao[1][2].move(-75, -270)
                    elif contvez == 3:
                        lmao[1][2].move(268, -270)
                    lmao[1] = "*"
                    return jogarcartaai1(cont, lmao2, lmao, win, v1, v2, v3, s, startvalue1, svt, valorp, contp, contai,
                                         pt, ptai,
                                         contvez,
                                         tcp, tcai, lcj)

                else:
                    lmao[1][2].draw(win)
                    if contvez == 1:
                        lmao[1][2].move(-269, -270)
                    elif contvez == 2:
                        lmao[1][2].move(74, -270)
                    elif contvez == 3:
                        lmao[1][2].move(417, -270)
                    lmao[1] = "*"
                    return turno(cont, valorp, vcartaai, contp, contai, win, pt, ptai, tcp, tcai, lmao, lmao2, s,
                                 startvalue1, svt,
                                 lcj)

        # Carta 3
        elif dentromenu(ck, c3):
            if lmao[2] != "*":
                valorp = lmao[2][3]
                if valorp == 14:
                    espadaosfx.play()
                else:
                    joga1sfx.play()
                time.sleep(.15)
                lmao[2][2].undraw()
                lcj.append(lmao[2][2])
                if s == 0:
                    lmao[2][2].draw(win)
                    if contvez == 1:
                        lmao[2][2].move(-578, -270)
                    elif contvez == 2:
                        lmao[2][2].move(-235, -270)
                    elif contvez == 3:
                        lmao[2][2].move(108, -270)
                    lmao[2] = "*"
                    return jogarcartaai1(cont, lmao2, lmao, win, v1, v2, v3, s, startvalue1, svt, valorp, contp, contai,
                                         pt, ptai,
                                         contvez,
                                         tcp, tcai, lcj)

                else:
                    lmao[2][2].draw(win)
                    if contvez == 1:
                        lmao[2][2].move(-429, -270)
                    elif contvez == 2:
                        lmao[2][2].move(-86, -270)
                    elif contvez == 3:
                        lmao[2][2].move(257, -270)
                    lmao[2] = "*"
                    return turno(cont, valorp, vcartaai, contp, contai, win, pt, ptai, tcp, tcai, lmao, lmao2, s,
                                 startvalue1, svt,
                                 lcj)


# 2.4.2 # TURNO INTELIGÊNCIA ARTIFICIAL:

def jogarcartaai1(cont, lmao, lmao2, win, v1, v2, v3, s, startvalue1, svt, vcartap, contp, contai, pt, ptai, contvez,
                  tcp, tcai,
                  lcj):
    global trucoast
    global envido_pedido
    global truco
    global trucoastAI
    global ptruco
    global Botao
    global truconegadoai
    global truconegadoj
    global Tbt
    global yes
    global no
    global jogaAIsfxsfx
    global espadaosfx
    global Benvido
    global Et
    global florastAI
    global flor
    global Bflor
    global Ft
    global retrucoastAI
    global v4astAI
    global valorenvidoAI
    global retrucoast
    global v4ast
    Botao.setFill(color_rgb(96, 90, 90))
    Botao.setOutline(color_rgb(137, 132, 132))
    Tbt.setFill(color_rgb(137, 132, 132))
    Benvido.setOutline(color_rgb(137, 132, 132))
    Benvido.setFill(color_rgb(96, 90, 90))
    Et.setOutline(color_rgb(137, 132, 132))
    Bflor.setFill(color_rgb(96, 90, 90))
    Bflor.setOutline(color_rgb(137, 132, 132))
    Ft.setFill(color_rgb(137, 132, 132))
    EnvidoCall = Text(Point(512, 320), "ENVIDO!")
    EnvidoCall.setSize(32)
    Espera = Text(Point(512, 360), "Aceitar?")
    Espera.setSize(25)
    svt.undraw()
    svt = Text(Point(108, 630), "Oponente")
    svt.setFill(color_rgb(255, 255, 255))
    svt.setSize(18)
    svt.draw(j)
    trd = random.randint(0, 100)
    frd = random.randint(0, 100)
    erd = random.randint(0, 100)

    valorenvidoAI = 0

    if flor != 1 and contvez == 1:

        if (lmao[0][0] == lmao[1][0]):
            valorenvidoAI = 20 + lmao[0][4] + lmao[1][4]
        elif (lmao[0][0] == lmao[2][0]):
            valorenvidoAI = 20 + lmao[0][4] + lmao[2][4]
        elif (lmao[1][0] == lmao[2][0]):
            valorenvidoAI = 20 + lmao[1][4] + lmao[2][4]
        else:
            valorenvidoAI = 0
    else:
        valorenvidoAI = 0

    if (lmao[0][0] == lmao[1][0]) and (lmao[0][0] == lmao[2][0]) and (
                lmao[1][0] == lmao[2][0]) and contvez == 1 and flor != 1 and frd <= 95:
        time.sleep(1.2)
        if florastAI != "*":
            decflor = Text(Point(512, 330), "FLOR!")
            decflor.setSize(32)
            decflor.draw(win)
            animflor(win)
            time.sleep(.2)
            contai += 3
            strcAI = contai
            ptai.setText(strcAI)
            time.sleep(1.2)
            decflor.undraw()
            if testefim(contp, contai):
                fim(contp, contai, win)
            flor = 1
        florastAI = "*"

    if flor == 1:
        valorenvidoAI = 0

    # valorenvidoj

    valorenvido = 0

    if contvez == 1 and envido_pedido == 0:
        if (lmao2[0][0] == lmao2[1][0]):
            valorenvido = 20 + lmao2[0][4] + lmao2[1][4]
        elif (lmao2[0][0] == lmao2[2][0]):
            valorenvido = 20 + lmao2[0][4] + lmao2[2][4]
        elif (lmao2[1][0] == lmao2[2][0]):
            valorenvido = 20 + lmao2[1][4] + lmao2[2][4]
        else:
            valorenvido = 0

    b = 0

    if valorenvidoAI >= 30 and contvez == 1 and envido_pedido == 0 and trucoast != "*":
        if erd >= 70:
            envido_pedido = 1
            time.sleep(1)
            EnvidoCall.setText("FALTA ENVIDO!")
            EnvidoCall.draw(win)
            time.sleep(1)
            Espera.draw(win)
            b = 3

        else:
            envido_pedido = 1
            time.sleep(1)
            EnvidoCall.setText("REAL ENVIDO!")
            EnvidoCall.draw(win)
            time.sleep(1)
            Espera.draw(win)
            b = 2

    elif valorenvidoAI >= 32 and contvez == 1 and envido_pedido == 0 and trucoast != "*":
        if erd >= 5:
            envido_pedido = 1
            time.sleep(1)
            EnvidoCall.setText("FALTA ENVIDO!")
            EnvidoCall.draw(win)
            time.sleep(1)
            Espera.draw(win)
            b = 3

    elif valorenvidoAI >= 25 and contvez == 1 and envido_pedido == 0 and trucoast != "*":
        if erd <= 85:
            envido_pedido = 1
            time.sleep(1)
            EnvidoCall.setText("ENVIDO!")
            EnvidoCall.draw(win)
            time.sleep(1)
            Espera.draw(win)
            b = 1

    elif valorenvidoAI > 20 and contvez == 1 and envido_pedido == 0 and trucoast != "*":
        if erd <= 25:
            envido_pedido = 1
            time.sleep(1)
            EnvidoCall.setText("ENVIDO!")
            EnvidoCall.draw(win)
            time.sleep(1)
            Espera.draw(win)
            b = 1

    # Checar se o oponente não tem flor:

    if (lmao2[0][0] == lmao2[1][0]) and (lmao2[1][0] == lmao2[2][0]) and contvez == 1 and flor != 1:
        lit = 1
        Bflor.setOutline(color_rgb(160, 110, 11))
        Bflor.setFill(color_rgb(58, 34, 5))
        Ft.setOutline(color_rgb(255, 255, 255))
    else:
        lit = 0

    florinimiga = 0

    while b != 0 and florinimiga == 0:
        ck = win.getMouse()
        if ck is None:
            pass
        elif dentromenur(ck, yes):
            EnvidoCall.undraw()
            Espera.undraw()
            if comparaenvido(valorenvido, valorenvidoAI, win) == False:
                if b == 1:
                    contai += 2
                    ptai.setText(contai)
                    if testefim(contp, contai):
                        fim(contp, contai, win)
                elif b == 2:
                    contai += 3
                    ptai.setText(contai)
                    if testefim(contp, contai):
                        fim(contp, contai, win)
                elif b == 3:
                    contai += 15 - contp
                    ptai.setText(contai)
                    if testefim(contp, contai):
                        fim(contp, contai, win)
            else:
                if b == 1:
                    contp += 2
                    pt.setText(contp)
                    if testefim(contp, contai):
                        fim(contp, contai, win)
                elif b == 2:
                    contp += 3
                    pt.setText(contp)
                    if testefim(contp, contai):
                        fim(contp, contai, win)
                elif b == 3:
                    contp += 15 - contai
                    pt.setText(contp)
                    if testefim(contp, contai):
                        fim(contp, contai, win)
            b = 0
        elif dentromenur(ck, no):
            b = 0
            contai += 1
            ptai.setText(contai)
            EnvidoCall.undraw()
            Espera.undraw()
            if testefim(contp, contai):
                fim(contp, contai, win)
        elif dentromenur(ck, Bflor) and (lit == 1) and flor != 1:
            EnvidoCall.undraw()
            Espera.undraw()
            decflor = Text(Point(512, 330), "CONTRA FLOR É PROIBIDO!")
            decflor.setSize(32)
            decflor.setFill(color_rgb(0, 0, 0))
            decflor.draw(win)
            animflor(win)
            time.sleep(0.8)
            decflor.undraw()
            contp += 3
            pt.setText(contp)
            if testefim(contp, contai):
                fim(contp, contai, win)
            florinimiga = 1
            flor = 1

    Bflor.setFill(color_rgb(96, 90, 90))
    Bflor.setOutline(color_rgb(137, 132, 132))
    Ft.setFill(color_rgb(137, 132, 132))

    # TRUCO AI
    if trd >= 85:
        if truco == 0:
            if trucoastAI != "*":
                time.sleep(1)
                Pediu = Text(Point(512, 320), "TRUCO!")
                ptruco = False
                Botao.setOutline(color_rgb(160, 110, 11))
                Botao.setFill(color_rgb(58, 34, 5))
                Tbt.setOutline(color_rgb(255, 255, 255))
                Pediu.setSize(32)
                Pediu.draw(win)
                time.sleep(.40)
                Espera.draw(win)
                a = 1
                Tbt.setText("R")
                while a != 2:
                    ck = win.getMouse()
                    if ck is None:
                        pass
                    # Aceitar ou não truco
                    elif dentromenur(ck, yes):
                        truco = 1
                        a = 2
                    elif dentromenur(ck, no):
                        truconegadoai = 1
                        vcartap = 0
                        vcartaai = 0
                        Pediu.undraw()
                        Espera.undraw()
                        return turno(cont, vcartap, vcartaai, contp, contai, win, pt, ptai, tcp, tcai, lmao, lmao2, s,
                                     startvalue1, svt,
                                     lcj)
                    elif dentromenur(ck, Botao) and retrucoast != "*":
                        Espera.undraw()
                        time.sleep(.25)
                        Pediu.undraw()
                        retrucoast = "*"
                        Pediu.setText("QUERO RETRUCO!")
                        Espera.setText("Aguardando...")
                        Pediu.draw(win)
                        Espera.draw(win)
                        time.sleep(1.2)
                        Espera.undraw()
                        retrnd = random.randint(0, 150)
                        if retrnd >= 100:
                            Pediu.undraw()
                            Pediu.setText("QUERO!")
                            Pediu.draw(win)
                            time.sleep(1.20)
                            Pediu.undraw()
                            truco = 2
                        else:
                            Pediu.undraw()
                            Pediu.setText("NÃO QUERO!")
                            Pediu.draw(win)
                            truconegadoj = 1
                            truco = 1
                            vcartap = 0
                            vcartaai = 0
                            time.sleep(1.25)
                            Pediu.undraw()
                            return turno(cont, vcartap, vcartaai, contp, contai, win, pt, ptai, tcp, tcai, lmao, lmao2,
                                         s,
                                         startvalue1, svt,
                                         lcj)
                        a = 2
                        Tbt.setText("-")
                        Botao.setFill(color_rgb(96, 90, 90))
                        Botao.setOutline(color_rgb(137, 132, 132))
                        Tbt.setFill(color_rgb(137, 132, 132))

                Pediu.undraw()
                Espera.undraw()
            trucoastAI = "*"

        # RETRUCO AI

        elif truco == 1:
            if retrucoastAI != "*" and ptruco == True:
                time.sleep(1)
                Pediu = Text(Point(512, 320), "RETRUCO!")
                pretruco = False
                Pediu.setSize(32)
                Botao.setOutline(color_rgb(160, 110, 11))
                Botao.setFill(color_rgb(58, 34, 5))
                Tbt.setOutline(color_rgb(255, 255, 255))
                Pediu.draw(win)
                time.sleep(.40)
                Espera.draw(win)
                a = 1
                Tbt.setText("V4")
                while a != 2:
                    ck = win.getMouse()
                    if ck is None:
                        pass
                    # Aceitar ou não retruco
                    elif dentromenur(ck, yes):
                        truco = 2
                        a = 2
                    elif dentromenur(ck, no):
                        truconegadoai = 1
                        vcartap = 0
                        vcartaai = 0
                        Pediu.undraw()
                        Espera.undraw()
                        return turno(cont, vcartap, vcartaai, contp, contai, win, pt, ptai, tcp, tcai, lmao, lmao2, s,
                                     startvalue1, svt,
                                     lcj)
                    elif dentromenur(ck, Botao) and v4ast != "*":
                        Espera.undraw()
                        time.sleep(.25)
                        Pediu.undraw()
                        v4ast = "*"
                        Pediu.setText("QUERO VALE QUATRO!")
                        Espera.setText("Aguardando...")
                        Pediu.draw(win)
                        Espera.draw(win)
                        time.sleep(1.2)
                        Espera.undraw()
                        retrnd = random.randint(0, 150)
                        if retrnd >= 130:
                            Pediu.undraw()
                            Pediu.setText("QUERO!")
                            Pediu.draw(win)
                            time.sleep(1.20)
                            Pediu.undraw()
                            truco = 3
                        else:
                            Pediu.undraw()
                            Pediu.setText("NÃO QUERO!")
                            Pediu.draw(win)
                            truconegadoj = 1
                            truco = 2
                            vcartap = 0
                            vcartaai = 0
                            time.sleep(1.25)
                            Pediu.undraw()
                            return turno(cont, vcartap, vcartaai, contp, contai, win, pt, ptai, tcp, tcai, lmao, lmao2,
                                         s,
                                         startvalue1, svt,
                                         lcj)
                        a = 2
                        Tbt.setText("-")
                        Botao.setFill(color_rgb(96, 90, 90))
                        Botao.setOutline(color_rgb(137, 132, 132))
                        Tbt.setFill(color_rgb(137, 132, 132))
                Pediu.undraw()
                Espera.undraw()
            retrucoastAI = "*"

        # VALE QUATRO AI

        elif truco == 2:
            if v4astAI != "*" and ptruco == False:
                v4rnd = random.randint(0, 150)
                if v4rnd >= 100:
                    time.sleep(1)
                    Pediu = Text(Point(512, 320), "VALE QUATRO!")
                    Pediu.setSize(32)
                    Pediu.draw(win)
                    time.sleep(.40)
                    Espera.draw(win)
                    a = 1
                    while a != 2:
                        ck = win.getMouse()
                        if ck is None:
                            pass
                        # Aceitar ou não retruco
                        elif dentromenur(ck, yes):
                            truco = 3
                            Tbt.setText("-")
                            Botao.setFill(color_rgb(96, 90, 90))
                            Botao.setOutline(color_rgb(137, 132, 132))
                            Tbt.setFill(color_rgb(137, 132, 132))
                            a = 2
                        elif dentromenur(ck, no):
                            truconegadoai = 1
                            vcartap = 0
                            vcartaai = 0
                            Pediu.undraw()
                            Espera.undraw()
                            return turno(cont, vcartap, vcartaai, contp, contai, win, pt, ptai, tcp, tcai, lmao, lmao2,
                                         s,
                                         startvalue1, svt,
                                         lcj)
                    Pediu.undraw()
                    Espera.undraw()
                v4astAI = "*"

    c = random.randint(0, 2)
    while lmao[c] == "*":
        c = random.randint(0, 2)
    t = random.uniform(1, 2)
    time.sleep(t)
    if c == 0:
        v1.undraw()
    elif c == 1:
        v2.undraw()
    else:
        v3.undraw()
    valorai = lmao[c][3]
    if lmao[c][2] is not None:
        lmao[c][2].undraw()
    if valorai == 14:
        espadaosfx.play()
    else:
        jogaAIsfx.play()
    time.sleep(.10)
    lmao[c][2].draw(win)
    lcj.append(lmao[c][2])
    if s == 0:
        if contvez == 1:
            lmao[c][2].move(-269, -260)
        elif contvez == 2:
            lmao[c][2].move(74, -260)
        elif contvez == 3:
            lmao[c][2].move(417, -260)
        lmao[c] = "*"
        return turno(cont, vcartap, valorai, contp, contai, win, pt, ptai, tcp, tcai, lmao, lmao2, s, startvalue1, svt,
                     lcj)
    elif s == 1:
        if contvez == 1:
            lmao[c][2].move(-418, -260)
        elif contvez == 2:
            lmao[c][2].move(-75, -260)
        elif contvez == 3:
            lmao[c][2].move(268, -260)
        lmao[c] = "*"
        return jogarcartap1(cont, lmao2, lmao, win, v1, v2, v3, s, startvalue1, svt, valorai, contp, contai, pt, ptai,
                            contvez, tcp,
                            tcai,
                            lcj)


# 2.5 # ESTRUTURA DE TURNOS:

# 2.5.1 # COMPARAÇÃO E PONTUAÇÃO:

def turno(cont, vcartap, vcartaai, contp, contai, win, pt, ptai, tempcontp, tempcontai, lmao, lmao2, startvalue,
          startvalue1, svt,
          lcj):
    global truco
    global truconegadoj
    global truconegadoai
    global venc1
    svt.undraw()
    if truconegadoj == 1:
        tempcontp = 2
    elif truconegadoai == 1:
        tempcontai = 2
    if tempcontp < 2 and tempcontai < 2:
        if vcartap > vcartaai:
            tempcontp += 1
            if startvalue == 1:
                startvalue -= 1
            if contvez == 1:
                venc1 = 0
        elif vcartap == vcartaai:
            if startvalue == 0:
                if tempcontai == 0 and tempcontp == 0:
                    tempcontai += 1
                    tempcontp += 1
                elif tempcontp == 0:
                    tempcontp += 1
                elif tempcontai == 0:
                    tempcontai += 1
                startvalue += 1
            else:
                if tempcontp == 0 and tempcontai == 0:
                    tempcontp += 1
                    tempcontai += 1
                elif tempcontp == 0:
                    tempcontp += 1
                elif tempcontai == 0:
                    tempcontai += 1
                startvalue -= 1
            if contvez == 2:
                if venc1 == 0:
                    tempcontp = 2
                else:
                    tempcontai = 2
            if contvez == 3 or truconegadoai == 1:
                undraw_all(lcj)
        else:
            tempcontai += 1
            if contvez == 1:
                venc1 = 1
            if startvalue == 0:
                startvalue += 1

    if tempcontp == 2:
        undraw_all(lcj)
        if truco == 0:
            contp += 1
            s = str(contp)
            pt.setText(s)
            if testefim(contp, contai):
                fim(contp, contai, win)
        elif truco == 1:
            contp += 2
            s = str(contp)
            pt.setText(s)
            if testefim(contp, contai):
                fim(contp, contai, win)
        elif truco == 2:
            contp += 3
            s = str(contp)
            pt.setText(s)
            if testefim(contp, contai):
                fim(contp, contai, win)
        else:
            contp += 4
            s = str(contp)
            pt.setText(s)
            if testefim(contp, contai):
                fim(contp, contai, win)
        if startvalue1 == 1:
            startvalue = 0
            startvalue1 = 0
        else:
            startvalue = 1
            startvalue1 = 1
        cont = 3
        return contp, contai, pt, ptai, startvalue, startvalue1, lmao, lmao2, tempcontp, tempcontai, cont, lcj
    elif tempcontai == 2:
        undraw_all(lcj)
        if truco == 0:
            contai += 1
            s = str(contai)
            ptai.setText(s)
            if testefim(contp, contai):
                fim(contp, contai, win)
        elif truco == 1:
            contai += 2
            s = str(contai)
            ptai.setText(s)
            if testefim(contp, contai):
                fim(contp, contai, win)
        elif truco == 2:
            contai += 3
            s = str(contai)
            ptai.setText(s)
            if testefim(contp, contai):
                fim(contp, contai, win)
        else:
            contai += 4
            s = str(contai)
            ptai.setText(s)
            if testefim(contp, contai):
                fim(contp, contai, win)
        if startvalue1 == 1:
            startvalue = 0
            startvalue1 = 0
        else:
            startvalue = 1
            startvalue1 = 1
        cont = 3
        return contp, contai, pt, ptai, startvalue, startvalue1, lmao, lmao2, tempcontp, tempcontai, cont, lcj
    return contp, contai, pt, ptai, startvalue, startvalue1, lmao, lmao2, tempcontp, tempcontai, cont, lcj


# 2.6 # UTILITÁRIOS:

# 2.6.1 # APAGAMENTO DAS MÃOS E CAMPO:

def undraw_all(listaa):
    global lcj
    global m
    time.sleep(1)
    for k, v in enumerate(lcj):
        lcj[k].undraw()
    for l in m:
        if isinstance(l, list):
            l[2].undraw()

    Verso.undraw()
    Verso1.undraw()
    Verso2.undraw()
    del lcj
    del m
    lcj, m = [], []


# 2.6.2 # ENVIDO:

def comparaenvido(vep, veAI, win):
    global stv1
    VencedorE = Text(Point(512, 320), "Você venceu o envido, com " + str(vep) + " pontos!")
    VencedorE.setSize(24)
    if vep > veAI:
        time.sleep(1)
        VencedorE.draw(win)
        time.sleep(3.15)
        VencedorE.undraw()
        return True
    elif veAI > vep:
        VencedorE.setText("O oponente venceu o envido, com " + str(veAI) + " pontos.")
        time.sleep(1)
        VencedorE.draw(win)
        time.sleep(3.15)
        VencedorE.undraw()
        return False
    elif stv1 == 0:
        time.sleep(1)
        VencedorE.draw(win)
        time.sleep(3.15)
        VencedorE.undraw()
        return True
    else:
        VencedorE.setText("O oponente venceu o envido, com " + str(veAI) + " pontos.")
        time.sleep(1)
        VencedorE.draw(win)
        time.sleep(3.15)
        VencedorE.undraw()
        return False


# 2.6.3 # TESTE DE PONTUAÇÃO:

def testefim(contp, contai):
    if contp >= 15 or contai >= 15:
        return True


# 2.6.4 # ANIMAÇÃO:

def animflor(win):
    global sparkle
    x = random.randint(100, 924)
    y = random.randint(100, 600)
    x1 = random.randint(100, 924)
    y1 = random.randint(100, 600)
    x2 = random.randint(100, 924)
    y2 = random.randint(100, 924)

    while (x == x1 or x == x2 or x1 == x2) or (abs(x - x2) <= 55 or abs(x - x1) <= 55 or abs(x1 - x2) <= 55):
        x = random.randint(100, 924)
        x1 = random.randint(100, 924)
        x2 = random.randint(100, 924)

    while (y == y1 or y == y2 or y1 == y2) or (abs(y - y2) <= 55 or abs(y - y1) <= 55 or abs(y1 - y2) <= 55):
        y = random.randint(100, 924)
        y1 = random.randint(100, 924)
        y2 = random.randint(100, 924)

    flor1 = [Image(Point(x, y), "./vfx/flor1.gif"), Image(Point(x, y), "./vfx/flor2.gif")]
    flor2 = [Image(Point(x1, y1), "./vfx/flor1.gif"), Image(Point(x1, y1), "./vfx/flor2.gif")]
    flor3 = [Image(Point(x2, y2), "./vfx/flor1.gif"), Image(Point(x2, y2), "./vfx/flor2.gif")]

    sparkle.play()

    x = 0
    while x < 15:
        flor1[0].draw(win)
        flor2[0].draw(win)
        flor3[0].draw(win)
        time.sleep(0.2)
        flor1[1].draw(win)
        flor2[1].draw(win)
        flor3[1].draw(win)
        time.sleep(0.2)
        flor1[0].undraw()
        flor1[1].undraw()
        flor2[0].undraw()
        flor2[1].undraw()
        flor3[0].undraw()
        flor3[1].undraw()
        x = x + 1


# 2.6.5 # FINALIZAÇÃO:

def fim(contp, contai, win):
    global victory
    global defeat

    venceu = Text(Point(512, 300), "Encerrado")
    venceu.setSize(22)
    venceu.setFill(color_rgb(255, 255, 255))

    if contp >= 15:
        victory.play()
        time.sleep(.2)
        venceu.setText("VOCÊ VENCEU!")
        time.sleep(2)
        venceu.draw(win)
    elif contai >= 15:
        defeat.play()
        time.sleep(.2)
        venceu.setText("O oponente venceu.")
        venceu.draw(win)

    time.sleep(2)

    sair = Text(Point(512, 350), "Clique na tela para fechar.")
    sair.setSize(18)
    sair.setFill(color_rgb(255, 255, 255))
    sair.draw(win)

    win.getMouse()
    win.close()


## CÓDIGO:

playing = 0

j = menu()

## LOADS:

embaralharsfx = pg.mixer.Sound("./sfx/cardFan1.ogg")
joga1sfx = pg.mixer.Sound("./sfx/cardPlace3.ogg")
jogaAIsfx = pg.mixer.Sound("./sfx/cardPlace4.ogg")
espadaosfx = pg.mixer.Sound("./sfx/cardShove1.ogg")
victory = pg.mixer.Sound("./sfx/victory.ogg")
defeat = pg.mixer.Sound("./sfx/sigh.ogg")
sparkle = pg.mixer.Sound("./sfx/sparkle.ogg")

## JANELA DO JOGO:

Botao = Circle(Point(960, 50), 30)
Botao.setOutline(color_rgb(160, 110, 11))
Botao.setFill(color_rgb(58, 34, 5))
Botao.draw(j)
Tbt = Text(Point(960, 52), "T")
Tbt.setFace("arial")
Tbt.setSize(22)
Tbt.setOutline(color_rgb(255, 255, 255))
Tbt.draw(j)

Benvido = Circle(Point(887, 52), 25)
Benvido.setOutline(color_rgb(160, 110, 11))
Benvido.setFill(color_rgb(58, 34, 5))
Benvido.draw(j)
Et = Text(Point(887, 53), "E")
Et.setFace("arial")
Et.setSize(20)
Et.setOutline(color_rgb(255, 255, 255))
Et.draw(j)

Renvido = Circle(Point(832, 52), 20)
Renvido.setOutline(color_rgb(160, 110, 11))
Renvido.setFill(color_rgb(58, 34, 5))
Ret = Text(Point(832, 53), "RE")
Ret.setFace("arial")
Ret.setSize(14)
Ret.setOutline(color_rgb(255, 255, 255))

Fenvido = Circle(Point(887, 107), 20)
Fenvido.setOutline(color_rgb(160, 110, 11))
Fenvido.setFill(color_rgb(58, 34, 5))
Fet = Text(Point(887, 108), "FE")
Fet.setFace("arial")
Fet.setSize(14)
Fet.setOutline(color_rgb(255, 255, 255))

Bflor = Circle(Point(960, 120), 25)
Bflor.setOutline(color_rgb(137, 132, 132))
Bflor.setFill(color_rgb(96, 90, 90))
Bflor.draw(j)
Ft = Text(Point(960, 120), "F")
Ft.setFace("arial")
Ft.setSize(20)
Ft.setOutline(color_rgb(137, 132, 132))
Ft.draw(j)

yes = Circle(Point(835, 650), 25)
yes.setOutline(color_rgb(15, 188, 18))
yes.setFill(color_rgb(4, 112, 6))
yes.draw(j)
yest = Text(Point(835, 650), "✓")
yest.setSize(24)
yest.setFill(color_rgb(15, 188, 18))
yest.draw(j)

no = Circle(Point(905, 650), 25)
no.setOutline(color_rgb(255, 13, 0))
no.setFill(color_rgb(155, 22, 15))
no.draw(j)
noT = Text(Point(905, 650), "✗")
noT.setSize(24)
noT.setFill(color_rgb(255, 13, 0))
noT.draw(j)

PontosP = Text(Point(1004, 680), "0")
PontosP.setFill(color_rgb(255, 255, 255))
PontosP.setSize(22)
PontosP.draw(j)
PontosAI = Text(Point(20, 20), "0")
PontosAI.setFill(color_rgb(255, 255, 255))
PontosAI.setSize(22)
PontosAI.draw(j)

startvalue = random.randint(0, 1)
stv1 = startvalue

tturno = Text(Point(110, 590), "TURNO:")
tturno.setSize(20)
tturno.setFill(color_rgb(255, 255, 255))
tturno.draw(j)

if startvalue == 0:
    startvaluet = Text(Point(108, 630), "Você")
    startvaluet.setFill(color_rgb(255, 255, 255))
    startvaluet.setSize(18)
    startvaluet.draw(j)
else:
    startvaluet = Text(Point(108, 630), "Oponente")
    startvaluet.setFill(color_rgb(255, 255, 255))
    startvaluet.setSize(18)
    startvaluet.draw(j)

contai = 0
contp = 0
vai = 0
vp = 0
cont = 0
contvez = 1
tcp = 0
tcai = 0
lcj = []
venc1 = 0

while contp <= 15 and contai <= 15:
    envido_pedido = 0
    valorenvidoAI = 0
    truco = 0
    ptruco = False
    pretruco = False
    Tbt.setText("T")
    trucoast = 0
    retrucoast = 0
    v4ast = 0
    trucoastAI = 0
    flor = 0
    florast = 0
    florastAI = 0
    retrucoastAI = 0
    v4astAI = 0
    envast = 0
    truconegadoj = 0
    truconegadoai = 0
    O, C, P, E = naipes()
    B = embaralhar(O, C, P, E)
    m, mAI = mao(B)
    embaralharsfx.play()
    time.sleep(1)
    desenhamao(m, j)
    Verso, Verso1, Verso2 = verso()
    desenhoai(Verso, Verso1, Verso2, j)
    while cont < 3:
        if startvalue == 0:
            contp, contai, pt, ptai, startvalue, stv1, mAI, m, tcp, tcai, cont, lcj = jogarcartap1(cont, m, mAI, j,
                                                                                                   Verso,
                                                                                                   Verso1,
                                                                                                   Verso2, startvalue,
                                                                                                   stv1, startvaluet,
                                                                                                   vai,
                                                                                                   contp, contai,
                                                                                                   PontosP,
                                                                                                   PontosAI,
                                                                                                   contvez,
                                                                                                   tcp, tcai, lcj)
        else:
            contp, contai, pt, ptai, startvalue, stv1, m, mAI, tcp, tcai, cont, lcj = jogarcartaai1(cont, mAI, m, j,
                                                                                                    Verso,
                                                                                                    Verso1,
                                                                                                    Verso2, startvalue,
                                                                                                    stv1, startvaluet,
                                                                                                    vp,
                                                                                                    contp, contai,
                                                                                                    PontosP,
                                                                                                    PontosAI,
                                                                                                    contvez, tcp, tcai,
                                                                                                    lcj)
        contvez += 1
        cont += 1
    contvez = 1
    tcp = 0
    tcai = 0
    cont = 0

fim(contp, contai, j)

j.mainloop()
