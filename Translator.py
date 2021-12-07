
def translate(search):
    translate = " "
    for letter in search:
        if letter in "AEUIOaeuio":
         translate = translate + "b"
        else:
            translate = translate + letter
    return translate

translated = translate(input("search: "))
print (translated)
