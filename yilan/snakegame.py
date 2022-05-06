from asyncore import write
from cmath import polar
from re import A
import turtle # Turtle modülünü import ettik.
import time  #Programı yavaşlatmak için kullandık. sleep()
import random

SpeedTime = 0.15

window = turtle.Screen() #Pencere açmak için gerekli kodlar.
window.title("Snake Game") # Pencerenin Başlığı 
window.bgcolor("lightgreen") # Pencerenin arkaplanı
window.setup(width = 600, height=600) # Pencerenin Boyutları

window.tracer(0) #tracer() işlevi, otomatik ekran güncellemelerini açar veya kapatır. Default olarak açıktır. Bunu kapatıp işlemimizi update ile yapacağız.

HeadSnake=turtle.Turtle() #Nesne oluşturduk.
HeadSnake.speed=(0) # yılanın hızını  ayarlar.
HeadSnake.shape('square') #Yılanın kafasının şeklini ayarlar. “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
HeadSnake.color('red')# Renk
HeadSnake.penup()#Kafa haraket ettiğinde çizgi çizmez.
HeadSnake.goto(0,100)# kafayı haraket ettirdik ve konumlandırdık.
HeadSnake.direction = 'stop' #kafanın ilk yönü




food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color('blue')
food.penup()
food.shapesize(0.80,0.80)
food.goto(0,0)


#tails

tails = []
point = 0

write = turtle.Turtle()
write.speed(0)
write.shape("square")
write.color('white')
write.penup()
write.hideturtle()
write.goto(0,260)
write.write('Puan: {} '.format(point), align='center' , font=("Courier", 30, "normal"))         


def move():
    if HeadSnake.direction == "up":
        y = HeadSnake.ycor()
        HeadSnake.sety(y + 20)
    if HeadSnake.direction == "down":
        y = HeadSnake.ycor()
        HeadSnake.sety(y - 20)
    if HeadSnake.direction == "right":
        x = HeadSnake.xcor()
        HeadSnake.setx(x + 20)
    if HeadSnake.direction == "left":
        x = HeadSnake.xcor()
        HeadSnake.setx(x - 20)      
 

 


def goUp():
    if HeadSnake.direction != 'down':   # kafanın  yönünü yukarı yap, kafanın yönü aşağı değilse.
        HeadSnake.direction ='up'


def goDown():
    if HeadSnake.direction != 'up':   # kafanın  yönünü aşağı yap, kafanın yönü yukarı değilse .
        HeadSnake.direction ='down' 

def goRight():
    if HeadSnake.direction != 'left':  
        HeadSnake.direction ='right' 

def goLeft():
    if HeadSnake.direction != 'right':  
        HeadSnake.direction ='left'





window.listen()
window.onkey(goUp,'Up') #klavyeden up tuşuna basarsak go up fonksiyonu çalışacak.
window.onkey(goDown,'Down') 
window.onkey(goRight,'Right') 
window.onkey(goLeft,'Left') 









while True:
    window.update() #Penceremizin Ekranda kalması ve update alması için yaptık. Kodu Silerseniz göreceksiniz.
   
    if HeadSnake.xcor() > 300 or HeadSnake.xcor() < -300 or HeadSnake.ycor() >  300 or HeadSnake.ycor() < -300 :
        time.sleep(1)
        HeadSnake.goto(0,0)
        HeadSnake.direction ='stop'


        for tail in tails:
            tail.goto(1000,1000)
        


        tails= [] #kuyruklar listesi sıfırlandı
        point = 0 # kenara çarparsak puan sıfırlanır.
        write.clear()
        write.write('Puan: {} '.format(point), align='center' , font=("Courier", 30, "normal"))
        hiz = 0.15       


    if  HeadSnake.distance(food) < 20: # kafa ile yemek arasındaki mesafe 
        x = random.randint(-250,250)
        y= random.randint(-250,250)
        food.goto(x,y)  # kafa yemek üstünden geçerse  yemeği x ve y üzerinden random olarak atar.
        


        # yemeğin yeri değiştikce puan artar.
        point = point + 10
        write.clear()
        write.write('Puan: {} '.format(point), align='center' , font=("Courier", 30, "normal") )
    #  hiz = hiz - 0.001 # her yemek yediğinde hızı düşür.

        NewTail =turtle.Turtle()
        NewTail.speed(0)
        NewTail.shape('square')
        NewTail.color('green')
        NewTail.penup()
        tails.append(NewTail)


        
    for index in range(len(tails) - 1, 0, -1):
        x = tails[index - 1].xcor()
        y = tails[index - 1].ycor()
        tails[index].goto(x, y)
 
    if len(tails) > 0:   #  0 indeksteki kuyruğu  kafanın arkasına eklenir.
        x = HeadSnake.xcor()
        y = HeadSnake.ycor()
        tails[0].goto(x, y) 
     


    move() #Hareketler sürekli çalışacağı için döngüye aldık.
    time.sleep(SpeedTime) # Programı Yavaşlatmak için bu metohodu kullandık. Değişken üstte attadık. satr 4