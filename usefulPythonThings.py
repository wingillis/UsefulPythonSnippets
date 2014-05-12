#!/Users/wgillis/envs/dataAnalysis/bin/python
# Created by: Winthrop Gillis

# This file will contain a conglomeration of useful python idioms

# Print out strings using the local variable names:
speed = 'slow'
color= 'blue'

print('The {speed} {color} fox'.format(**locals()))

# Class attributes that I thought you could only do in javascript
class Modifiable():
	pass

mod = Modifiable()
mod.name = 'New Mod'
mod.version = 1.0

# You can actually store named args in a dictionary and unpack them for an argument
def func(a, b, c):
    print('{a}\n{b}\n{c}'.format(a=a,b=b,c=c))
# OR
def fun(**kwargs):
    print('{a}\n{b}\n{c}'.format(**kwargs))

keys = {'a': 'Lololol',
        'b': 'do dwopp',
        'c': 'helloooo'}

func(**keys)
fun(**keys)
