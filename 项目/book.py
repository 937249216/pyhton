'''
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(160)
    if abs(pos()) < 1:
        break
end_fill()
done()
'''
'''
fullname= ["Alfred","Smoketoomuch"]
"mr{name[1]}".format(name=fullname)
import math
tmpl = "The {mod._name_} module define the value {mod.pi} for pi"
tmpl.format(mod=math)math.
'''
'''
header_fmt ='{{:{}}}  {{:{}}}'    .format(item_width,price_width)
fmt        ='{{:{}}}  {{:>{}.2f}}'.format(tiem_width,price_width)
'''

'''
Lables ={
    'phone':'phone nomber',
    'addr':'address'
}
name = input('Name:')
request =input ('Phone number (p) or address (a)? ')
ket = request
if request == 'p': key = 'phone'
if request == 'p': key = 'addr'
person = people.get(name,{})
lable = lables.get(key,key)
result = person.get(key,'not avaliable' )
print("{}'s{} is {}.".format(name,label,result))
'''
'''
girls = ['alice','bernice','clarice']
boys = ['cris','arnold','bob']
[b+'+'+g for b in boys for g in girls if b[0] == g[0]]
'''

def store (data,fullname):
    name  full_name.split()
    if len(names) == 2：names.insert(1,'')
    labels = 'first','middle','last'

    for labels, name in zip(labels,names):
        people = lookup(data,label,name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [fullname]    

