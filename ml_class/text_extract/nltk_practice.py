import nltk
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
#nltk.download('punkt')



token = nltk.word_tokenize("At eight o'clock on Sunday morning")
#print(token)
#print(type(token))


with open ('myname.txt','r') as f:
	st = f.read()

st_token = nltk.sent_tokenize(st)
#print(st_token)


word_token = [nltk.word_tokenize(i) for i in st_token]
#print(word_token)


l = st_token[0]
entities = nltk.chunk.ne_chunk(word_token)
print(entities)
