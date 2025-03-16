


table = {'Sjoerd' : 4127,
         'Jack' : 4098,
         'Dcab' : 8637678}

print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))
# Jack: 4098; Sjoerd: 4127; Dcab: 8637678



table = {'Sjoerd' : 4127,
         'Jack' : 4098,
         'Dcab' : 8637678}

print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
# Jack: 4098; Sjoerd: 4127; Dcab: 8637678