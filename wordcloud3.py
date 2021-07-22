from konlpy.corpus import kolaw
from konlpy.tag import Hannanum
import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
data=kolaw.open('constitution.txt').read()
hannaum=Hannanum()
nouns=hannaum.nouns(data)
# --한글자로된 명사 또는 제외할 문자지정
temp=[]
for n in nouns:
   if len(n)==1 or n=='제2장' or n=='제10조':
       continue
   temp.append(n)
text=nltk.Text(temp)
# ----------------------------
data1=text.vocab()
data500=data1.most_common(500)
# --빈도수가 1인것 제외
print(data500)  # [(값,value),(),...]
temp=[]
for i in data500:
    if i[1]==1:
        continue
    temp.append(i)
dic=dict(temp)
# -------------------------
print(dic)
# --이미지적용
img=Image.open('img\\m1.png')
mask=np.array(img)
wc=WordCloud(font_path='malgun.ttf',mask=mask)
word=wc.generate_from_frequencies(dic)
plt.imshow(word)
plt.axis('off')
plt.show()
# -------중앙일보의 기사를 가지고 워드클라우드로 구현하세요




