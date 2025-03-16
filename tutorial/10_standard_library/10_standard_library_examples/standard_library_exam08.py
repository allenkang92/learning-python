

import re


re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
# ['foot', 'fell', 'fastest']

re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))
# cat in the hat

'tea for too'.replace('too', 'two')
print('tea for too'.replace('too', 'two'))
# tea for two
