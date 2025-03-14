
# 같은 컬렉션을 반복하는 동안에 해당 컬렉션을 수정하는 코드는 
# 올바르게 작성하기 어려울 수 있다.
# 일반적으로 컬렉션의 복사본을 반복하거나
# 새 컬렉션을 만드는 것이 더 간단하다.

users = {'Hans' : 'active', 
         'Eleonore' : 'inactive',
         'ddd' : 'active'}

# Strategy :  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
    

# Strategy : Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status