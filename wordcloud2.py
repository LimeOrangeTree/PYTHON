# JPype1‑0.6.3‑cp36‑cp36m‑win_amd64.whl
from konlpy.corpus import kolaw
data=kolaw.open('constitution.txt').read()
print(data)
# 명사추출
# from konlpy.tag import Kkma
# kkma=Kkma()
# nouns=kkma.nouns(data)
# print(nouns)
from konlpy.tag import Hannanum
hannaum=Hannanum()
nouns=hannaum.nouns(data)
print(nouns)
# 텍스트변환
import nltk
text=nltk.Text(nouns)
print(text)
# 빈도수
data1=text.vocab()
data500=data1.most_common(500)
print(data500)
# 딕션어리 변환
dic=dict(data500)
# ------------------------------------
from wordcloud import WordCloud
import matplotlib.pyplot as plt
wc=WordCloud(font_path='malgun.ttf')
word=wc.generate_from_frequencies(dic)
plt.imshow(word)
plt.axis('off')
plt.show()

# https://mclearninglab.tistory.com/entry/Pytorch-%EC%84%A4%EC%B9%98-%EC%8B%9C-ImportError-DLL-load-failed-%ED%95%B4%EA%B2%B0%EB%B2%95


