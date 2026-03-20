import re
result=re.match(r'\d+', '123456ab56c') 
print(result.group())

result=re.match(r'\D+', 'abc16ab56c')
print(result.group())

result=re.search(r'\d+', 'abcre567')
print(result.group())

result=re.findall(r'\d+','abc456edf555')
print(result)

result = re.sub(r'\d+','55','123ebctrr')
print(result)

result= re.split(r'\d+','abc123efg567')
print(result)