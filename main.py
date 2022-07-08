import wikipedia

wikipedia.set_lang("pt")
#print(wikipedia.summary('Doctor Who'))

wiki = wikipedia.page('Décimo primeiro Doutor')

text = wiki.content
print(text)