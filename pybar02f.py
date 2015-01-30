import random

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

flavors = []

def bartender():
    '''makes the drink profile'''
    Q_and_A = questions.items()
    for key,value in Q_and_A:
        A = raw_input("{}".format(value,questions))
        if A == "yes":
            A = True
            flavors.append(key)
    print flavors
    return flavors




def mix_bot(flavors):
    '''takes the flavors list and combines random ingredients'''
    drink = []
    choices = ingredients.items()
    for thing in flavors:
        for answers,selections in choices:
            if thing == answers:
                drink.append(random.choice(selections))
    print drink
    return drink
        
        
            #if thing in flavors in answers.choices:
                
                
    
if __name__ == '__main__':
    bartender()

    mix_bot(flavors)
