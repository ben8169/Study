import nltk
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
import pickle

f = open('myname.txt','r')
st = f.read()
st = st.lower()
my_dic = dict()


lemmatizer = WordNetLemmatizer()
pos_tags = pos_tag(st.split())

for word, tag in pos_tags:
    if word == "cloud":
        word = "cloud computing"
    elif word == "computing":
        continue
    else:
        pass
    base_form = lemmatizer.lemmatize(word)
    my_dic[word] = [base_form, tag]


cnt = 0
while cnt<5:
    new_word = input()
    if new_word in my_dic:
        print(my_dic[new_word])
    else:
        my_dic[new_word] = [lemmatizer.lemmatize(new_word),pos_tag([new_word])[0][1]]
        cnt += 1
        print(f"new_word:{cnt}")

with open('my_dic.json', 'wb') as f:
    pickle.dump(my_dic, f)


    
with open('my_dic.json', 'rb') as f:
    my_dic_read = pickle.load(f)