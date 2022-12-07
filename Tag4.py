import random
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
Letters = 0
word = ''
name1 =''
name2 =''
gefunden = []
def inputfile():
    random_number = random.randint(1,239650)
    w = open("wortliste.txt", "r")
    for x in range(random_number):
        woerter = w.readline()
    return woerter
def spieler():
    global name1
    global name2
    global word
    Spieler = input('wie viele Spieler:')
    word = inputfile()
    Letters = 0
    for l in word:
        Letters =Letters+1
        gefunden.append('_')
    print('Buchstaben:',Letters)
    
    if Spieler == '1':
        print('Spieler:1')
        name1 = input('Name Spieler:')
        game(name1)
    if Spieler == '2':
        print('Spieler:2')
        name1 = input('Name Spieler 1:')
        name2 = input('Name Spieler 2:')
        game(name1)
        game(name2)

def game(spielername):
    global name1
    global name2
    global word
    
    punkte = 0
 #   for i in range(10):
    print(spielername)
    for x in range(10):
        random_number = random.randint(0,25)
        q = input('zum beenden q drücken')
        if q == 'z':
            print(random_number)
        if q == 'b':
            print(letters[random_number])
            cnt = 0
            if letters[random_number] in gefunden:
                continue
            for x in word:
                if letters[random_number] == x:  
                    gefunden[cnt] = x
                    punkte = punkte+10
                cnt = cnt+1
            print(gefunden)
        if q == 'q':
            break
    print('Punkte:',punkte)
    


spieler()