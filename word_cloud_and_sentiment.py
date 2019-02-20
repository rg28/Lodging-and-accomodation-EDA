from nltk import ngrams
import pandas as pd
import re
import itertools
# cleans the input string , removes email addresses, links and unwanted characters
def clean(msg_content):
    if msg_content!=None:
        msg_clean = ''.join([ch for ch in str(msg_content) if ord(ch)<= 128])
        msg_clean = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', msg_clean)
        msg_clean = re.sub(r'\S+@\S+','', msg_clean)
        for r in ['\\n', '\n', '\r', '\t', '\\t', 'None', 'none']: msg_clean = msg_clean.replace(r, ' ')
        msg_clean = re.sub(r' +', ' ', re.sub("[/\\\:?\"]", '', msg_clean))
        msg_clean = ' '.join(w.strip() for w in msg_clean.lstrip().split(" ") if w!=" ")
    return " ".join(msg_clean.split())

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
len(stop_words)
stopwords=set(stopwords.words('english'))
df=pd.read_csv("reviews.csv")
df=df.astype(str)
df=df.groupby(['listing_id','id','date','reviewer_id'])['comments'].apply(','.join).reset_index()
sentence = ' '.join(str(i) for i in df['comments'])
sentence=clean(sentence)
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
wcloud = WordCloud(stopwords=stop_words,
                   background_color='black', normalize_plurals=True,
                  repeat=False,collocations=False).generate(str(sentence))

plt.imshow(wcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
##########SENTIMENT
from textblob import TextBlob
def sentiment(message):
    # create TextBlob object of passed tweet text
    analysis = TextBlob(message)
    # set sentiment
    return (analysis.sentiment.polarity)
#assigning sentiment score to rewiews

df=df.assign(sentiment_score=0)
df['sentiment_score']=df['sentiment_score'].astype(str)
df['sentiment_score']=df['comments'].apply(sentiment)
df=df.groupby(['listing_id'])['sentiment_score'].mean().reset_index()
import matplotlib.pyplot as plt

##blox plot of sentiment
plt.boxplot(df['sentiment_score'])
plt.ylabel('sentiment score')
plt.title('Box plot of sentiment score')
plt.show()

