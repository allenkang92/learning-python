


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

for i in sorted(basket):
    print(i)
# apple
# apple
# banana
# orange
# orange
# pear

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
# apple
# banana
# orange
# pear