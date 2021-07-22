from xml.etree import ElementTree
def indent(elem,level=0):
    i="\n"+"  "*level      #줄바꿈
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text=i+"  "
        if not elem.tail or not elem.tail.strip():
            elem.tail=i
        for e in elem:
            indent(e,level+1)
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail=i

#<a><b>test1</b>3<c>1</c></a>
# 엘리먼트 생성
note=ElementTree.Element('note')
# 속성추가
note.attrib['date']='20151231'

to=ElementTree.Element('to')
# 엘리먼드 값 지정
to.text="Tove"
# 엘리먼트 붙이기
note.append(to)
# 서브엘리먼트 생성
ElementTree.SubElement(note,'from').text='Jani'
ElementTree.SubElement(note,'heading').text='Reminder'
ElementTree.SubElement(note,'body').text="Don't forget me this weekend"
# 엘리먼트 삭제
# note.remove(to)
# 들여쓰기
# print(len(note))
indent(note)
#확인
ElementTree.dump(note)
# 저장
ElementTree.ElementTree(note).write("out1.xml",encoding='utf-8',xml_declaration=True)


