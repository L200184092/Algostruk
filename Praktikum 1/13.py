import inflect
def katakan(x):
    y = inflect.engine().number_to_words(x)
    #z = y.number_to_words(x)
    print(y) 
 

