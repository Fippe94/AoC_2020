f = open("Day12/input.txt")
data = f.readlines()


class Ship:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.waypoint_x = 10
        self.waypoint_y = 1
        self.direction = 90

    def do_action(self, action, value):
        if action == 'N':
            self.y += value
        elif action == 'S':
            self.y -= value
        elif action == 'W':
            self.x -= value
        elif action == 'E':
            self.x += value
        elif action == 'R':
            self.direction += value
            self.direction %= 360
        elif action == 'L':
            self.direction -= value + 360
            self.direction %= 360
        elif action == 'F':
            if self.direction == 0:
                self.y += value
            elif self.direction == 90:
                self.x += value
            elif self.direction == 180:
                self.y -= value
            elif self.direction == 270:
                self.x -= value

    def rotate_waypoint(self, degrees):
        old_x = self.waypoint_x
        old_y = self.waypoint_y
        if degrees == 90:
            self.waypoint_x = old_y
            self.waypoint_y = -old_x
        elif degrees == 180:
            self.waypoint_x = -old_x
            self.waypoint_y = -old_y
        elif degrees == 270:
            self.waypoint_x = -old_y
            self.waypoint_y = old_x
        else:
            print('Wrong angle: ', degrees)

    def move_waypoint(self, action, value):
        if action == 'N':
            self.waypoint_y += value
        elif action == 'S':
            self.waypoint_y -= value
        elif action == 'W':
            self.waypoint_x -= value
        elif action == 'E':
            self.waypoint_x += value
        elif action == 'L':
            print(value)
            self.rotate_waypoint(360-value)
        elif action == 'R':
            print(value)
            self.rotate_waypoint(value)
        elif action == 'F':
            self.x += value*self.waypoint_x
            self.y += value*self.waypoint_y
            
    def get_location(self):
        return (self.x,self.y)


ship = Ship()

for line in data:
    action = line[0]
    value = int(line[1:])
    #ship.do_action(action, value)
    ship.move_waypoint(action, value)
    #print(line)
    #print(ship.get_location())
    #print(ship.waypoint_x, ship.waypoint_y)

x,y = ship.get_location()
print(x,y)
print(abs(x) + abs(y))

