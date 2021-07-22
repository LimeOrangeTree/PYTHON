# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# import numpy as np
# # https://www.lfd.uci.edu/~gohlke/pythonlibs
# # wordcloud‑1.5.0‑cp36‑cp36m‑win_amd64.whl
# # 마틴루터킹목사의 I have a dream 연설문을 검색해서 data\dream.txt 저장
# text=open('data\\dream.txt',encoding='utf-8').read()
# # print(text)
# # 워드클라우드 생성
# # wc=WordCloud()
# wc=WordCloud(max_font_size=50,min_font_size=10,background_color="white")
# word=wc.generate(text)
# # 그리기
# plt.imshow(word)
# plt.axis('off')
# plt.show()
# -----------------------------
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# import numpy as np
# from PIL import Image
# img=Image.open('img\\m1.png')
# mask=np.array(img)
# # print(mask)
# text=open('data\\dream.txt',encoding='utf-8').read()
# # wc=WordCloud()
# wc=WordCloud(mask=mask)
# word=wc.generate(text)
# # 그리기
# plt.imshow(word)
# plt.axis('off')
# plt.show()
# ----------------------
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import STOPWORDS
sw=set(STOPWORDS)
print(sw)
# stopword 추가
sw.add('will')
img=Image.open('img\\m1.png')
mask=np.array(img)
text=open('data\\dream.txt',encoding='utf-8').read()
wc=WordCloud(mask=mask,stopwords=sw)
word=wc.generate(text)
plt.imshow(word)
plt.axis('off')
plt.show()
#-----------타이타닉 주제곡을 다운받아 워드클라우드로 만들어보세요
