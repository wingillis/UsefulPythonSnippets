# Created by: Winthrop Gillis

# This file will contain a conglomeration of useful python idioms

# Print out strings using the local variable names:
speed = 'slow'
color= 'blue'

print('The {speed} {color} fox'.format(**locals()))

# Class attributes that I though you could only do in javascript
class Modifiable():
	pass

mod = Modifiable()
mod.name = 'New Mod'
mod.version = 1.0

