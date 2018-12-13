import webbrowser as wb
import pyautogui as pg
import time as t

points = 0

show= pg.prompt("what is your favorite show?")

if show == "Hawaii Five-O":
    pg.alert("That is a really good show!")
    wb.open("https://www.youtube.com/watch?v=mjaayCARwro")
    t.sleep(10)
    points += 5
    
elif show == "Criminal Minds":
    pg.alert ("I love Derrick")
    wb.open("https://www.youtube.com/watch?v=sqyNqxbCfO8")
    t.sleep(10)
    points += 5
    
elif show == "Bubble Guppies":
    pg.alert("Great Show")
    wb.open("https://www.youtube.com/watch?v=TLs3xaUInB8")
    t.sleep(10)
    points += 5

elif show == "Bodyguard":
    pg.alert ("Dope Show")
    wb.open("https://www.youtube.com/watch?v=TLs3xaUInB8")
    t.sleep(10)
    points += 5

elif show == "NFL Network":
    pg.alert("Booger McFarland is a beast")
elif show == "Fox":
    pg.alert("Joe Buck is cool dude")
else:
    pg.alert("Your favorite show is " + show)

food= pg.prompt("What is your favorite food?")

if food == "dumplings":
    pg.alert("I love dumplings!")
    wb.open("https://www.youtube.com/watch?v=qu0CxX8GJj8")
    t.sleep(10)
    points += 5

elif food == "ice cream":
    pg.alert("I hate getting a brain freeze")
    wb.open("https://www.youtube.com/watch?v=5t-IKxx9ttU")
    t.sleep(10)
    points += 5

elif food == "hamburgers":
    pg.alert("Have you ever been to in and out burger")
    wb.open("https://www.youtube.com/watch?v=RDKgqH5X78I")
    t.sleep(10)
    points += 5

elif food == "Flamin' hot cheetos":
    pg.alert("Bianca and Angelica love those")
    wb.open("https://www.youtube.com/watch?v=bS1Nf0syICc")
    t.sleep(10)
    points += 5

elif food == "sushi":
    pg.alert("I just want some sushi from Japan")
elif food == "Salmon":
    pg.alert("I love salmon on a bagel")
else:
    pg.alert("Your favorite food is" + food)

game = pg.prompt("What is your favorite game? ")

if game == "fortnite":
    pg.alert("I heard James wants Leviathon")
    wb.open("https://www.youtube.com/watch?v=JgOPpoSB1Hw")
    t.sleep(10)
    points += 5

elif game == "clash royale":
    pg.alert("I heard Jackson buys")
    wb.open("https://www.youtube.com/watch?v=lDooxdR7DwA")
    t.sleep(10)
    points += 5

elif game == "call of duty":
    pg.alert("Black Ops 4 is dope")
    wb.open("https://www.youtube.com/watch?v=vfc42Pb5RA8")
    t.sleep(10)
    points += 5

elif game == "flappy golf":
    pg.alert("I completed all the levels")
    wb.open("https://www.youtube.com/watch?v=OpfNY2_6Cto")
    t.sleep(10)
    points += 5

elif game == "nhl":
    pg.alert("I'm dope at that game")
elif game == "Madden":
    pg.alert("I'm dope at that game")
else:
    pg.alert("You need to start playing better games like " + game)

subject = pg.prompt("What is your favorite class? ")

if subject == "Comp Sci":
    pg.alert("I heard Jurgis goes to Yale in the summer to study computers")
    wb.open("https://www.youtube.com/watch?v=mWUMzCpgtl8")
    t.sleep(10)
    points += 5

elif subject == "math":
    pg.alert("2+2=4")
    wb.open("https://www.youtube.com/watch?v=3M_5oYU-IsU")
    t.sleep(10)
    points += 5

elif subject == "history":
    pg.alert("George Washington is a liar")
    wb.open("https://www.youtube.com/watch?v=56akaRCW_tk")
    t.sleep(10)
    points += 5

elif subject == "spanish":
    pg.alert("Yo hablo espanol")
    wb.open("https://www.youtube.com/watch?v=JkiglO98YYo&t=46s")
    t.sleep(10)
    points += 5

elif subject == "science":
    pg.alert("You should join the outdoor adventure team")
elif subject == "english":
    pg.alert("I'm the bestest at grammer ")
else:
    pg.alert("That is a great  " + subject)

sport = pg.prompt("What is your favorite sport? ")

if sport == "Hockey":
    pg.alert("The capitals are the best team")
    wb.open ("https://www.youtube.com/watch?v=UtnCUQH94j0")
    t.sleep(10)
    points += 5
    
elif sport == "Football":
    pg.alert("The patriots suck")
    wb.open("https://www.youtube.com/watch?v=vnYWLZThFVk")
    t.sleep(10)
    points += 5
    
elif sport == "Basketball":
    pg.alert("Lebron James is the best player of all time")
    wb.open("https://www.youtube.com/watch?v=kF8pBeDXlOA")
    t.sleep(10)
    points += 5
    
elif sport == "Baseball":
    pg.alert("The Red Sox are going to win the World Series")
    wb.open("https://www.youtube.com/watch?v=yFCr1Zn73Ws")
    t.sleep(10)
    points += 5
    
elif sport == "Quiditch":
    pg.alert("Gryfindor is the best team")
elif sport == "Soccer":
    pg.alert("Croartia is the best team")
else:
    pg.alert("That is a great  " + sport)
          
