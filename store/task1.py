customers = ['brad','jolie','johny','sooronbai','sooronbai','sadyr','sadyr','emma','sooronbai',
         'brad','almazbek','roza','roza','kurmanbek','toby','tony','robert','askar','robert','chris','chris']

print(len(set(customers)))


import random

list1 = random.sample(range(1,1000000),600000)
list1_max = list1.index(max(list1))
list1_min = list1.index(min(list1))


print(list1)