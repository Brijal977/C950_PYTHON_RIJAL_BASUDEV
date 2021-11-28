##Lab Activity 3.7.1
import math


class Point:
    def __init__(self):
        self.x = 0
        self.y = 0


p = Point()
print('Start: (%d,%d)' % (p.x, p.y))
p.x = int(input())
p.y = int(input())

x_steps = int(input())
y_steps = int(input())
z_steps = int(input())

init_distance = math.sqrt(p.x ** 2 + p.y ** 2)
min_distance = init_distance
num_steps = 0
current_loc = Point()
prev_loc = Point()

while min_distance <= init_distance:
    current_loc.x += x_steps
    current_loc.y += y_steps

    num_steps += 1

    if num_steps % 3 == 0:
        current_loc.x -= z_steps
        current_loc.y -= z_steps

    d = math.sqrt(math.pow((p.x - current_loc.x), 2) + math.pow((p.y - current_loc.y), 2))

    if d == 0:
        min_distance = d
        break
    elif d > min_distance:
        current_loc = prev_loc
        num_steps -= 1
        break
    elif d < min_distance:
        min_distance = d
        prev_loc.x = current_loc.x
        prev_loc.y = current_loc.y

print('Point P: (%d,%d)' % (p.x, p.y))
print('Arrival point: (%d,%d)' % (current_loc.x, current_loc.y))
print('Distance between P and arrival: %f' % min_distance)
print('Number of iterations: %d' % num_steps)