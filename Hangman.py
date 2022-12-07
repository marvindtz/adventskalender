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
        woerter = w.readline()[:-1]
    return woerter.lower()
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
    print(gefunden)
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
    print(word)
def game(spielername):
    global name1
    global name2
    global word
    
    punkte = 0
 #   for i in range(10):
    print(spielername)
    for x in range(10):
        random_number = random.randint(0,25)
        q = input('zum beenden Q drücken jeder Kleinbuchstabe zum Raten')
        if q == 'Z':
            print(random_number)
        if q == 'Q':
            break
  #      if q == 'B':
        print(q)
        cnt = 0
        if q in gefunden:
            continue
        for x in word:
            if q == x:  
                gefunden[cnt] = x
                punkte = punkte+10
            cnt = cnt+1
        print(gefunden)
        
    print('Punkte:',punkte)
    


spieler()