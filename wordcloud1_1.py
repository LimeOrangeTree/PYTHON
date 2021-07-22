# from WordCloud import WordCloud
# # import WordCloud
# import matplotlib.pyplot as plt
# import numpy as np
#
# text=open('data\\dream.txt',encoding='utf-8').read()
# # print(text)
# wc=WordCloud(max_font_size=50,min_font_size=10,background_color="white")
# word=wc.generate(text)
# plt.imshow(word)
# plt.axis('off')
# plt.show()

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import STOPWORDS
sw=set(STOPWORDS)
print(sw)
# sw.add('')
img=Image.open('img\\mask-word-cloud.jpg')
mask=np.array(img)
text=open('data\\dream.txt',encoding='utf-8').read()
wc=WordCloud(mask-mask,stopwords=sw)
word=wc.generate(text)
plt.imshow(word)
plt.axis('off')
plt.axit('off')
plt.show()