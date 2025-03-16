


from string import Template

t = Template('${village}folk send $$10 to $cause.')
print(t.substitute(village='Nottingham', cause='the ditch fund'))
# Nottinghamfolk send $10 to the ditch fund.


t = Template('Return the $item to $owner.')

d = dict(item='unladen swallow')
print(t.substitute(d))
# Traceback (most recent call last):
#   File "../../learning-python/practice-python/tutorial/10_standard_library/10_standard_library_examples/standard_library_exam19.py", line 14, in <module>
#     print(t.substitute(d))
#   File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/string.py", line 121, in substitute
#     return self.pattern.sub(convert, self.template)
#   File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/string.py", line 114, in convert
#     return str(mapping[named])
# KeyError: 'owner'