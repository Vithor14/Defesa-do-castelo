import turtle as tt
import random
import time
from math import cos,radians

def distancia(angulo,passo = 1.0):
    res = cos(radians(angulo))
    if res == 0:
        return passo
    else:
        return passo/res
    

screen = tt.Screen()
screen.setup(1200,600)
screen.bgpic('base.gif')
screen.register_shape("knight.gif")
screen.register_shape("spartan.gif")
screen.register_shape("roman.gif")
screen.register_shape("ninja.gif")
screen.register_shape("logo2.gif")
screen.register_shape("gameover.gif")


tt.title('Defesa do castelo')
tt.shape("logo2.gif")
tt.showturtle()
pontos = -10

def start(x, y):
    global pontos
    pontos = 0
    tt.hideturtle()

while pontos != 0:
    tt.onclick(start)
    time.sleep(0.1)

vida = 10

ini01 = tt.Turtle()
ini01.hideturtle()
ini01.penup()
ini01.pencolor("blue")

ini02 = tt.Turtle()
ini02.hideturtle()
ini02.penup()
ini02.pencolor("yellow")

ini03 = tt.Turtle()
ini03.hideturtle()
ini03.penup()
ini03.pencolor("red")

ini04 = tt.Turtle()
ini04.hideturtle()
ini04.penup()
ini04.pencolor("white")

ini05 = tt.Turtle()
ini05.hideturtle()
ini05.penup()
ini05.pencolor("purple")

###################################
## definições do inicio do round ##
###################################

def init01(tipo01):
    ini01.setx(-650)
    ini01.sety(random.randint(-235, 65))
    ini01.setheading(0)
    ini01.pendown()
    if tipo01 == 0:
        ini01.shape("knight.gif")
    elif tipo01 == 1:
        ini01.shape("spartan.gif")
    elif tipo01 == 2:
        ini01.shape("roman.gif")
    else:
        ini01.shape("ninja.gif")
    ini01.showturtle()


def init02(tipo02):
    ini02.setx(-650)
    ini02.sety(random.randint(-235, 65))
    ini02.setheading(0)
    ini02.pendown()
    if tipo02 == 0:
        ini02.shape("knight.gif")
    elif tipo02 == 1:
        ini02.shape("spartan.gif")
    elif tipo02 == 2:
        ini02.shape("roman.gif")
    else:
        ini02.shape("ninja.gif")
    ini02.showturtle()


def init03(tipo03):
    ini03.setx(-650)
    ini03.sety(random.randint(-235, 65))
    ini03.setheading(0)
    ini03.pendown()
    if tipo03 == 0:
        ini03.shape("knight.gif")
    elif tipo03 == 1:
        ini03.shape("spartan.gif")
    elif tipo03 == 2:
        ini03.shape("roman.gif")
    else:
        ini03.shape("ninja.gif")
    ini03.showturtle()


def init04(tipo04):
    ini04.setx(-650)
    ini04.sety(random.randint(-235, 65))
    ini04.setheading(0)
    ini04.pendown()
    if tipo04 == 0:
        ini04.shape("knight.gif")
    elif tipo04 == 1:
        ini04.shape("spartan.gif")
    elif tipo04 == 2:
        ini04.shape("roman.gif")
    else:
        ini04.shape("ninja.gif")
    ini04.showturtle()


def init05(tipo05):
    ini05.setx(-650)
    ini05.sety(random.randint(-235, 65))
    ini05.setheading(0)
    ini05.pendown()
    if tipo05 == 0:
        ini05.shape("knight.gif")
    elif tipo05 == 1:
        ini05.shape("spartan.gif")
    elif tipo05 == 2:
        ini05.shape("roman.gif")
    else:
        ini05.shape("ninja.gif")
    ini05.showturtle()

###############################
## As definições dos cliques ##
###############################


def kill01(x, y):
    global pontos
    pontos += 10
    ini01.hideturtle()
    ini01.setheading(180)
    ini01.penup()

def kill02(x, y):
    global pontos
    pontos += 10
    ini02.hideturtle()
    ini02.setheading(180)
    ini02.penup()

def kill03(x, y):
    global pontos
    pontos += 10
    ini03.hideturtle()
    ini03.setheading(180)
    ini03.penup()

def kill04(x, y):
    global pontos
    pontos += 10
    ini04.hideturtle()
    ini04.setheading(180)
    ini04.penup()

def kill05(x, y):
    global pontos
    pontos += 10
    ini05.hideturtle()
    ini05.setheading(180)
    ini05.penup()

#############################
## definições de movimento ##
#############################

def inicio():
    x = random.randint(0,1)
    if x == 0:
        return random.randint(-44,-20)
    else:
        return random.randint(20,44)

       #EM CONSTRUÇÃO#

def mov01(tipo = 0,fase = 1):
    if tipo == 0:
        ## faz o personagem virar aleatoriamente no começo
        if fase == 0:
            ini01.setheading(inicio())
            ini01.forward(distancia(ini01.heading()))
        else :
            ## se estiver no meio, anda
            if -170 <= ini01.ycor() <= 0 :
                ini01.forward(distancia(ini01.heading()))
            elif 1 <= ini01.ycor() :
                ## se estiver em cima virar pra baixo
                if -45 <= ini01.heading():
                    ini01.right(1)
                    ini01.forward(distancia(ini01.heading()))
                else:
                    ini01.forward(distancia(ini01.heading()))
            else:
                ## se estiver em baixo, subir
                if 200  >= ini01.heading() >= 45:
                    ini01.forward(distancia(ini01.heading()))
                else:
                    ini01.left(1)
                    ini01.forward(distancia(ini01.heading()))
                    
            
    elif tipo == 1:
        if fase == 0:
            ini01.setheading(inicio())
            ini01.forward(distancia(ini01.heading()))
        else :
            ## se estiver no meio, anda
            if -170 <= ini01.ycor() <= -20 :
                chance = random.randint(0,180)
                if chance == 0:
                    ini01.setheading(360 - ini01.heading())
                    ini01.forward(distancia(ini01.heading()))
                else:
                    ini01.forward(distancia(ini01.heading()))
            elif -19 <= ini01.ycor() :
                ## se estiver em cima virar pra baixo
                if ini01.heading() <= 180: 
                    chance = random.randint(0,40)
                    if chance == 0:
                        ini01.setheading(360 - ini01.heading())
                        ini01.forward(distancia(ini01.heading()))
                    else:
                        ini01.forward(distancia(ini01.heading()))
                else:
                    ini01.forward(distancia(ini01.heading()))
                    
            else:
                ## se estiver em baixo, subir
                if ini01.heading() >= 180: 
                    chance = random.randint(0,40)
                    if chance == 0:
                        ini01.setheading(360 - ini01.heading())
                        ini01.forward(distancia(ini01.heading()))
                    else:
                        ini01.forward(distancia(ini01.heading()))
                else:
                    ini01.forward(distancia(ini01.heading()))
                    
    elif tipo == 2:
        if -150 <= ini01.ycor() <= -20 :
            ini01.setheading(random.randint(-60, 60))
            ini01.forward(distancia(ini01.heading()))
        elif -19 <= ini01.ycor() :
        ## se estiver em cima virar pra baixo
            ini01.setheading(random.randint(-80, 20))
            ini01.forward(distancia(ini01.heading()))
        else:
            ini01.setheading(random.randint(-20, 80))
            ini01.forward(distancia(ini01.heading()))
                
    else:
        if fase%100 != 0:
                ini01.forward(1)
        else:
                if -150 <= ini01.ycor() <= -20 :
                    ini01.sety(random.uniform(ini01.ycor()-80,ini01.ycor()+80))
                    ini01.forward(1)
                elif -19 <= ini01.ycor() :
                    ## se estiver em cima virar pra baixo
                    ini01.sety(random.uniform(ini01.ycor()-100,ini01.ycor()+20))
                    ini01.forward(1)
                else:
                    ini01.sety(random.uniform(ini01.ycor()-40,ini01.ycor()+120))
                    ini01.forward(1)
        
def mov02(tipo = 0,fase = 1):
    if tipo == 0:
        ## faz o personagem virar aleatoriamente no começo
        if fase == 0:
            ini02.setheading(inicio())
            ini02.forward(distancia(ini02.heading()))
        else :
            ## se estiver no meio, anda
            if -170 <= ini02.ycor() <= 0 :
                ini02.forward(distancia(ini02.heading()))
            elif 1 <= ini02.ycor() :
                ## se estiver em cima virar pra baixo
                if -45 <= ini02.heading():
                    ini02.right(1)
                    ini02.forward(distancia(ini02.heading()))
                else:
                    ini02.forward(distancia(ini02.heading()))
            else:
                ## se estiver em baixo, subir
                if 200  >= ini02.heading() >= 45:
                    ini02.forward(distancia(ini02.heading()))
                else:
                    ini02.left(1)
                    ini02.forward(distancia(ini02.heading()))
                    
            
    elif tipo == 1:
        if fase == 0:
            ini02.setheading(inicio())
            ini02.forward(distancia(ini02.heading()))
        else :
            ## se estiver no meio, anda
            if -170 <= ini02.ycor() <= -20 :
                chance = random.randint(0,180)
                if chance == 0:
                    ini02.setheading(360 - ini02.heading())
                    ini02.forward(distancia(ini02.heading()))
                else:
                    ini02.forward(distancia(ini02.heading()))
            elif -19 <= ini02.ycor() :
                ## se estiver em cima virar pra baixo
                if ini02.heading() <= 180: 
                    chance = random.randint(0,40)
                    if chance == 0:
                        ini02.setheading(360 - ini02.heading())
                        ini02.forward(distancia(ini02.heading()))
                    else:
                        ini02.forward(distancia(ini02.heading()))
                else:
                    ini02.forward(distancia(ini02.heading()))
                    
            else:
                ## se estiver em baixo, subir
                if ini02.heading() >= 180: 
                    chance = random.randint(0,40)
                    if chance == 0:
                        ini02.setheading(360 - ini02.heading())
                        ini02.forward(distancia(ini02.heading()))
                    else:
                        ini02.forward(distancia(ini02.heading()))
                else:
                    ini02.forward(distancia(ini02.heading()))
                    
                
    elif tipo == 2:
        if -150 <= ini02.ycor() <= -20 :
            ini02.setheading(random.randint(-60, 60))
            ini02.forward(distancia(ini02.heading()))
        elif -19 <= ini02.ycor() :
        ## se estiver em cima virar pra baixo
            ini02.setheading(random.randint(-80, 20))
            ini02.forward(distancia(ini02.heading()))
        else:
            ini02.setheading(random.randint(-20, 80))
            ini02.forward(distancia(ini02.heading()))
                
    else:
        if fase%100 != 0:
                ini02.forward(1)
        else:
                if -150 <= ini02.ycor() <= -20 :
                    ini02.sety(random.uniform(ini02.ycor()-80,ini02.ycor()+80))
                    ini02.forward(1)
                elif -19 <= ini02.ycor() :
                    ## se estiver em cima virar pra baixo
                    ini02.sety(random.uniform(ini02.ycor()-100,ini02.ycor()+20))
                    ini02.forward(1)
                else:
                    ini02.sety(random.uniform(ini02.ycor()-40,ini02.ycor()+120))
                    ini02.forward(1)

def mov03(tipo = 0,fase = 1):
    if tipo == 0:
        ## faz o personagem virar aleatoriamente no começo
        if fase == 0:
            ini03.setheading(inicio())
            ini03.forward(distancia(ini03.heading()))
        else :
            ## se estiver no meio, anda
            if -170 <= ini03.ycor() <= 0 :
                ini03.forward(distancia(ini03.heading()))
            elif 1 <= ini03.ycor() :
                ## se estiver em cima virar pra baixo
                if -45 <= ini03.heading():
                    ini03.right(1)
                    ini03.forward(distancia(ini03.heading()))
                else:
                    ini03.forward(distancia(ini03.heading()))
            else:
                ## se estiver em baixo, subir
                if 200  >= ini03.heading() >= 45:
                    ini03.forward(distancia(ini03.heading()))
                else:
                    ini03.left(1)
                    ini03.forward(distancia(ini03.heading()))
                    
            
    elif tipo == 1:
        if fase == 0:
            ini03.setheading(inicio())
            ini03.forward(distancia(ini03.heading()))
        else :
            ## se estiver no meio, anda
            if -170 <= ini03.ycor() <= -20 :
                chance = random.randint(0,180)
                if chance == 0:
                    ini03.setheading(360 - ini03.heading())
                    ini03.forward(distancia(ini03.heading()))
                else:
                    ini03.forward(distancia(ini03.heading()))
            elif -19 <= ini03.ycor() :
                ## se estiver em cima virar pra baixo
                if ini03.heading() <= 180: 
                    chance = random.randint(0,40)
                    if chance == 0:
                        ini03.setheading(360 - ini03.heading())
                        ini03.forward(distancia(ini03.heading()))
                    else:
                        ini03.forward(distancia(ini03.heading()))
                else:
                    ini03.forward(distancia(ini03.heading()))
                    
            else:
                ## se estiver em baixo, subir
                if ini03.heading() >= 180: 
                    chance = random.randint(0,40)
                    if chance == 0:
                        ini03.setheading(360 - ini03.heading())
                        ini03.forward(distancia(ini03.heading()))
                    else:
                        ini03.forward(distancia(ini03.heading()))
                else:
                    ini03.forward(distancia(ini03.heading()))
                
    elif tipo == 2:
        if -150 <= ini03.ycor() <= -20 :
            ini03.setheading(random.randint(-60, 60))
            ini03.forward(distancia(ini03.heading()))
        elif -19 <= ini03.ycor() :
        ## se estiver em cima virar pra baixo
            ini03.setheading(random.randint(-80, 20))
            ini03.forward(distancia(ini03.heading()))
        else:
            ini03.setheading(random.randint(-20, 80))
            ini03.forward(distancia(ini03.heading()))
                
    else:
        if fase%100 != 0:
                ini03.forward(1)
        else:
                if -150 <= ini03.ycor() <= -20 :
                    ini03.sety(random.uniform(ini03.ycor()-80,ini03.ycor()+80))
                    ini03.forward(1)
                elif -19 <= ini03.ycor() :
                    ## se estiver em cima virar pra baixo
                    ini03.sety(random.uniform(ini03.ycor()-100,ini03.ycor()+20))
                    ini03.forward(1)
                else:
                    ini03.sety(random.uniform(ini03.ycor()-40,ini03.ycor()+120))
                    ini03.forward(1)

def mov04(tipo = 0,fase = 1):
    if tipo == 0:
        ## faz o personagem virar aleatoriamente no começo
        if fase == 0:
            ini04.setheading(inicio())
            ini04.forward(distancia(ini04.heading()))
        else :
            ## se estiver no meio, anda
            if -170 <= ini04.ycor() <= 0 :
                ini04.forward(distancia(ini04.heading()))
            elif 1 <= ini04.ycor() :
                ## se estiver em cima virar pra baixo
                if -45 <= ini04.heading():
                    ini04.right(1)
                    ini04.forward(distancia(ini04.heading()))
                else:
                    ini04.forward(distancia(ini04.heading()))
            else:
                ## se estiver em baixo, subir
                if 200  >= ini04.heading() >= 45:
                    ini04.forward(distancia(ini04.heading()))
                else:
                    ini04.left(1)
                    ini04.forward(distancia(ini04.heading()))
                    
            
    elif tipo == 1:
        if fase == 0:
            ini04.setheading(inicio())
            ini04.forward(distancia(ini04.heading()))
        else :
            ## se estiver no meio, anda
            if -170 <= ini04.ycor() <= -20 :
                chance = random.randint(0,180)
                if chance == 0:
                    ini04.setheading(360 - ini04.heading())
                    ini04.forward(distancia(ini04.heading()))
                else:
                    ini04.forward(distancia(ini04.heading()))
            elif -19 <= ini04.ycor() :
                ## se estiver em cima virar pra baixo
                if ini04.heading() <= 180: 
                    chance = random.randint(0,40)
                    if chance == 0:
                        ini04.setheading(360 - ini04.heading())
                        ini04.forward(distancia(ini04.heading()))
                    else:
                        ini04.forward(distancia(ini04.heading()))
                else:
                    ini04.forward(distancia(ini04.heading()))
                    
            else:
                ## se estiver em baixo, subir
                if ini04.heading() >= 180: 
                    chance = random.randint(0,40)
                    if chance == 0:
                        ini04.setheading(360 - ini04.heading())
                        ini04.forward(distancia(ini04.heading()))
                    else:
                        ini04.forward(distancia(ini04.heading()))
                else:
                    ini04.forward(distancia(ini04.heading()))
                
    elif tipo == 2:
        if -150 <= ini04.ycor() <= -20 :
            ini04.setheading(random.randint(-60, 60))
            ini04.forward(distancia(ini04.heading()))
        elif -19 <= ini04.ycor() :
        ## se estiver em cima virar pra baixo
            ini04.setheading(random.randint(-80, 20))
            ini04.forward(distancia(ini04.heading()))
        else:
            ini04.setheading(random.randint(-20, 80))
            ini04.forward(distancia(ini04.heading()))
                
    else:
        if fase%100 != 0:
                ini04.forward(1)
        else:
                if -150 <= ini04.ycor() <= -20 :
                    ini04.sety(random.uniform(ini04.ycor()-80,ini04.ycor()+80))
                    ini04.forward(1)
                elif -19 <= ini04.ycor() :
                    ## se estiver em cima virar pra baixo
                    ini04.sety(random.uniform(ini04.ycor()-100,ini04.ycor()+20))
                    ini04.forward(1)
                else:
                    ini04.sety(random.uniform(ini04.ycor()-40,ini04.ycor()+120))
                    ini04.forward(1)

def mov05(tipo = 0,fase = 1):
    if tipo == 0:
        ## faz o personagem virar aleatoriamente no começo
        if fase == 0:
            ini05.setheading(inicio())
            ini05.forward(distancia(ini05.heading()))
        else :
            ## se estiver no meio, anda
            if -170 <= ini05.ycor() <= 0 :
                ini05.forward(distancia(ini05.heading()))
            elif 1 <= ini05.ycor() :
                ## se estiver em cima virar pra baixo
                if -45 <= ini05.heading():
                    ini05.right(1)
                    ini05.forward(distancia(ini05.heading()))
                else:
                    ini05.forward(distancia(ini05.heading()))
            else:
                ## se estiver em baixo, subir
                if 200  >= ini05.heading() >= 45:
                    ini05.forward(distancia(ini05.heading()))
                else:
                    ini05.left(1)
                    ini05.forward(distancia(ini05.heading()))
                    
            
    elif tipo == 1:
        if fase == 0:
            ini05.setheading(inicio())
            ini05.forward(distancia(ini05.heading()))
        else :
            ## se estiver no meio, anda
            if -170 <= ini05.ycor() <= -20 :
                chance = random.randint(0,180)
                if chance == 0:
                    ini05.setheading(360 - ini05.heading())
                    ini05.forward(distancia(ini05.heading()))
                else:
                    ini05.forward(distancia(ini05.heading()))
            elif -19 <= ini05.ycor() :
                ## se estiver em cima virar pra baixo
                if ini05.heading() <= 180: 
                    chance = random.randint(0,40)
                    if chance == 0:
                        ini05.setheading(360 - ini05.heading())
                        ini05.forward(distancia(ini05.heading()))
                    else:
                        ini05.forward(distancia(ini05.heading()))
                else:
                    ini05.forward(distancia(ini05.heading()))
                    
            else:
                ## se estiver em baixo, subir
                if ini05.heading() >= 180: 
                    chance = random.randint(0,40)
                    if chance == 0:
                        ini05.setheading(360 - ini05.heading())
                        ini05.forward(distancia(ini05.heading()))
                    else:
                        ini05.forward(distancia(ini05.heading()))
                else:
                    ini05.forward(distancia(ini05.heading()))
                
    elif tipo == 2:
        if -150 <= ini05.ycor() <= -20 :
            ini05.setheading(random.randint(-60, 60))
            ini05.forward(distancia(ini05.heading()))
        elif -19 <= ini05.ycor() :
        ## se estiver em cima virar pra baixo
            ini05.setheading(random.randint(-80, 20))
            ini05.forward(distancia(ini05.heading()))
        else:
            ini05.setheading(random.randint(-20, 80))
            ini05.forward(distancia(ini05.heading()))
                
    else:
        if fase%100 != 0:
                ini05.forward(1)
        else:
                if -150 <= ini05.ycor() <= -20 :
                    ini05.sety(random.uniform(ini05.ycor()-80,ini05.ycor()+80))
                    ini05.forward(1)
                elif -19 <= ini05.ycor() :
                    ## se estiver em cima virar pra baixo
                    ini05.sety(random.uniform(ini05.ycor()-100,ini05.ycor()+20))
                    ini05.forward(1)
                else:
                    ini05.sety(random.uniform(ini05.ycor()-40,ini05.ycor()+120))
                    ini05.forward(1)



######################################
############ JOGO PRINCIPAL ##########
######################################

                    
def levels(n):
    if n <= 5:
        return 0
    elif n <= 10:
        return random.randint(0, 1)
    elif n <= 25:
        return random.randint(0, 2)
    else:
        return random.randint(0, 3)

def speed(n):
    if n <= 30:
        return 0.1 - (((n/2)+80)/1000)
    elif 35 > n > 30 :
        return 0.1 - (((n/3)+ 85)/1000)
    else :
        return 0.1 - (((n/4)+ 90)/1000)

for n in range(25,41):
    tt.tracer(0,0)
    if vida <= 0:
        print('fim de jogo, você perdeu no round',n)
        tt.shape("gameover.gif")
        tt.showturtle()
        tt.update()
        break
        
    ini01.clear()
    ini02.clear()
    ini03.clear()
    ini04.clear()
    ini05.clear()
    tipo01 = random.randint(0, 3)
    tipo02 = random.randint(0, 3)
    tipo03 = random.randint(0, 3)
    tipo04 = random.randint(0, 3)
    tipo05 = random.randint(0, 3)
    init01(tipo01)
    init02(tipo02)
    init03(tipo03)
    init04(tipo04)
    init05(tipo05)
    ini01.onclick(kill01)
    ini02.onclick(kill02)
    ini03.onclick(kill03)
    ini04.onclick(kill04)
    ini05.onclick(kill05)
    velocidade = speed(n) 
    print('round :',n)
    print('o tempo entre cada passo sera:', '%.4f' % velocidade ,"segundos")
    print('você tem ',pontos,"pontos")
    print('Vidas :',vida)
    
    
    for i in range(1200):
        if  180 == ini01.heading() == ini02.heading() == ini03.heading() == ini04.heading() == ini05.heading():
            break
        
        if ini01.heading() != 180:
            if 300 >= ini01.xcor():
                mov01(tipo01,i)
            elif 340 >= ini01.xcor():
                ini01.setheading(ini01.towards(340,-50))
                ini01.forward(distancia(ini01.heading()))
            
            elif 450 > ini01.xcor():
                ini01.setheading(ini01.towards(450,-30))
                ini01.forward(1)
            else:
                vida -= 1
                ini01.hideturtle()
                ini01.setheading(180)
                ini01.penup()
                

        if ini02.heading() != 180:
            if 300 >= ini02.xcor():
                mov02(tipo02,i)
            elif 340 >= ini02.xcor():
                ini02.setheading(ini02.towards(340,-50))
                ini02.forward(distancia(ini02.heading()))
            
            elif 450 > ini02.xcor():
                ini02.setheading(ini02.towards(450,-30))
                ini02.forward(1)
            else:
                vida -= 1
                ini02.hideturtle()
                ini02.setheading(180)
                ini02.penup()

        if ini03.heading() != 180:
            if 300 >= ini03.xcor():
                mov03(tipo03,i)
            elif 340 >= ini03.xcor():
                ini03.setheading(ini03.towards(340,-50))
                ini03.forward(distancia(ini03.heading()))
            
            elif 450 > ini03.xcor():
                ini03.setheading(ini03.towards(450,-30))
                ini03.forward(1)
            else:
                vida -= 1
                ini03.hideturtle()
                ini03.setheading(180)
                ini03.penup()
                

        if ini04.heading() != 180:
            if 300 >= ini04.xcor():
                mov04(tipo04,i)
            elif 340 >= ini04.xcor():
                ini04.setheading(ini04.towards(340,-50))
                ini04.forward(distancia(ini04.heading()))
            
            elif 450 > ini04.xcor():
                ini04.setheading(ini04.towards(450,-30))
                ini04.forward(1)
            else:
                vida -= 1
                ini04.hideturtle()
                ini04.setheading(180)
                ini04.penup()

        if ini05.heading() != 180:
            if 300 >= ini05.xcor():
                mov05(tipo05,i)
            elif 340 >= ini05.xcor():
                ini05.setheading(ini05.towards(340,-50))
                ini05.forward(distancia(ini05.heading()))
            
            elif 450 > ini05.xcor():
                ini05.setheading(ini05.towards(450,-30))
                ini05.forward(1)
            else:
                vida -= 1
                ini05.hideturtle()
                ini05.setheading(180)
                ini05.penup()
            
        time.sleep(velocidade)
        tt.update()

if vida > 0:
    print("VOCÊ DEFENDEU O CASTELO E GANHOU, PARABENS")
print("Sua pontuação foi:" , pontos)
print("clique para sair")
time.sleep(8)
tt.exitonclick()
