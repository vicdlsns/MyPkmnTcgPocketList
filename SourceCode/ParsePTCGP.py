import urllib.request, json, glob

urlcards = "https://raw.githubusercontent.com/flibustier/pokemon-tcg-pocket-database/main/dist/cards.json"
urlsets = "https://raw.githubusercontent.com/flibustier/pokemon-tcg-pocket-database/main/dist/sets.json"
urlrarity = "https://raw.githubusercontent.com/flibustier/pokemon-tcg-pocket-database/main/dist/rarity.json"

filenamecards="cards.json"
filenamesets="sets.json"
filenamerarity="rarity.json"

def getCards(getFromUrl=False):
    if getFromUrl:

        with urllib.request.urlopen(urlcards) as url:
            cards = json.loads(url.read().decode())

            with open(filenamecards, 'w', encoding='utf-8') as f:
                json.dump(cards, f, ensure_ascii=False, indent=2)
            #print(cards)

        with urllib.request.urlopen(urlsets) as url:
            sets = json.loads(url.read().decode())

            with open(filenamesets, 'w', encoding='utf-8') as f:
                json.dump(sets, f, ensure_ascii=False, indent=2)
            #print(sets)

        with urllib.request.urlopen(urlrarity) as url:
            rarity = json.loads(url.read().decode())

            with open(filenamerarity, 'w', encoding='utf-8') as f:
                json.dump(rarity, f, ensure_ascii=False, indent=2)
            #print(rarity)

    else:
        with open(filenamecards) as f:
            cards = json.load(f)

        with open(filenamesets) as f:
            sets = json.load(f)

        with open(filenamerarity) as f:
            rarity = json.load(f)

    return cards, sets, rarity

def setNamesTup():
    setTup = [(s["code"],s["label"]["en"]) for s in sets]
    return setTup

def setNamesDict():
    setTup = setNamesTup()
    return dict(setTup)
    

def cardsFromSet(setCode):
    return [c for c in cards if c["set"] == setCode]

def saveMarkdown(setCode=None):
    idName = setNamesTup()
    
    if setCode==None:
        for code, name in idName:
            name=name.replace(":"," ")
            L = cardsFromSet(code)
            with open(f"..\\EmptyLists\\List_{code}-{name.replace(' ','-')}.md","w") as file:
                for card in L:
                    file.write(f"- [ ] {card['number']} - {card['label']['eng']} - {card['rarity']} \n")
    else:
        L = cardsFromSet(setCode)
        name = [tup for tup in idName if tup[0] == setCode][0][1]
        name=name.replace(":"," ")
        with open(f"..\\EmptyLists\\List_{setCode}-{name.replace(' ','-')}.md","w") as file:
            for card in L:
               file.write(f"- [ ] {card['number']} - {card['label']['eng']} - {card['rarity']} \n")

def genWishlist(filenameList=glob.glob("..\\_MyCards\\*.md"), outFilename="..\\_Wishlist.md"):
    saveList = []
    for filename in filenameList:
        with open(filename,"r") as file:
            cardList = file.readlines()
            notMarked = [line for line in cardList if "- [ ]" in line[:5]]
        if notMarked!=[]:
            saveList.append("# " + filename.split("\\")[-1] + "\n")
            saveList += notMarked
            saveList.append("\n")

    with open(outFilename,"w") as file:
        file.writelines(saveList)

def runFromUrl(setCode=None):
    cards, sets, rarity = getCards(getFromUrl=True)
    saveMarkdown(setCode)
                
