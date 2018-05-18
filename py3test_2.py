import re

address = """\
1237777 東京都千代田区 
1500036 東京都渋谷区  
3309111 埼玉県さいたま 
"""

postCode = re.sub(r'([0-9]{3})([0-9]{4})' ,r'\1-\2',address,flags=re.MULTILINE)#参照とか
name = address.find('埼玉県さいたま')#検索対象の先頭の位置が出る
postCode2 =re.findall('[0-9]{3}[0-9]{4}',address)#郵便番号だけを抜き出す。



print(postCode)
print(name)
print(postCode2)
