from random import choice


print "Choose one side bellow to shoot!"
print "left,center,right"
your_choice = raw_input(">")

print "You kicked %s."%your_choice
direction = ['left','center','right']
com = choice(direction)

print 'Computer saved %s.'%com

if your_choice != com:
    print "GOALLLLLLLL!!!!!!!"
else:
    print "Oops..."
