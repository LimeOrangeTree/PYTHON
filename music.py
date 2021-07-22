# S_PAGENUMBER: 5
# S_MB_CD: W0726200
# S_HNAB_GBN: I
# hanmb_nm: G-DRAGON
# sort_field: SORT_PBCTN_DAY
import requests
import re
url="https://www.komca.or.kr/srch2/srch_01_popup_mem_right.jsp"
for page in range(1,19):
    params={'S_PAGENUMBER':page,'S_MB_CD':'W0726200'}
    result=requests.post(url,data=params)
    # print(result)
    # 저작물명 가수명 작사 작곡 편곡
    tbody=re.findall(r'<tbody>(.+?)</tbody>',result.text,re.DOTALL)
    # 이미지지우기
    # <img src="/images/common/control.gif"  alt="" />
    tbody[1]=re.sub('<img.+?/>','',tbody[1])
    # <br/> 삭제
    tbody[1]=re.sub('<br/>','',tbody[1])
    # print(len(tbody))
    # print(tbody)
    # print(tbody[1])
    trs=re.findall(r'<tr>(.+?)</tr>',tbody[1],re.DOTALL)
    # print(len(trs))
    for tr in trs:
        tds=re.findall(r'<td>(.+?)</td>',tr,re.DOTALL)
        # print(tds)
        # print(len(tds))
        print(','.join(tds))



