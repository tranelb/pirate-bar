questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

#def bartender ():
'''   
for item in questions:
    #raw_input = ("do you like % ?")%s(x)
    drink = []
    raw_input = ("do you like a %s drink?") % item
    if item == "yes":
        drink.append()

def pref(questions):
    likes = []
    raw_input("salty?")
    if "yes":
        likes.append(questions)
    raw_input("strong?")
    if "yes":
        likes.append(questions)
    raw_input("bitter?")
    if "yes":
        likes.append(questions)
    raw_input("sweet?")
    if "yes":
        likes.append(questions)
    raw_input("fruity?")
    if "yes":
        likes.append(questions)
    print likes
    return likes

pref(questions)
'''

def bartender():
    '''makes the drink profile'''    
    for key,value in questions:
        #raw_input("would you like your drink {}?".format(key,questions))
        drink = [t]
        t = raw_input("would you like your drink {}?".format(key,questions))
        if t == "yes":
            drink.append(value)
        print drink


bartender()
