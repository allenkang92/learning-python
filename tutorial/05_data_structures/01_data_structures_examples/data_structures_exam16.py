



knights  = {'gallahad' : 'the pure',
            'robin' : 'the brave'}

for k, v in knights.items():
    print(k, v)
# gallahad the pure
# robin the brave


for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
# 0 tic
# 1 tac
# 2 toe

questions = ['name', 'quest', 'favorit color']
answer = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answer):
    print('What is your {0}? It is {1}'.format(q, a))
    # What is your name? It is lancelot
    # What is your quest? It is the holy grail
    # What is your favorit color? It is blue

