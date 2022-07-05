from data import *
import json
import random
for string import Template
list = [1,2,3]

d_json = json.dumps(list)
print(d_json)

#dd = json.loads(client)

#for key, value in dd.items():
#    print(key)
#    print(value)

#inte = random.randint(1, 20)
inte = random.randrange(1, 20000, 20)
flow = random.random()

names = ['aa', 'bb', 'cc', 'dd']
s = random.choice(names)

print(s)



print(inte, flow)

with open('index.html', 'r') as html:
    template = Template(html.read())
    body = template.safe_substitute(name = 'AA')
