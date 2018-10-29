'''Solution to Matt Enlow's Brainteaser:

If you were to travel on the surface of the Earth
1000 miles in one direction, turn 90° to the right,
then 1000 more miles, another 90° right turn, another
1000 miles, another 90° to the right, then a final
1000 miles, how far from your starting point do you
think you'd be?

October 29, 2018'''

from math import cos, degrees, radians,sqrt

#starting Location:
SanFran = (37.7749,122.4194) #remember (y, x) not (x,y)

def degreesLongitude(distance,degreesLatitude,radius = 3959):
    '''returns how many degrees in longitude are represented
    by a given distance East or West at a given latitude.

    since arc_l = radius * angle * cos(latitude) '''
    return degrees(distance / (radius*cos(radians(degreesLatitude))))


def degreesLatitude(distance,degreesLatitude,radius = 3959):
    '''returns how many degrees in latitude are represented
    by a given distance South at a given latitude.'''
    return degrees(distance / (radius))#*cos(radians(degreesLatitude))))

def distance(p1,p2):
    '''Returns the 2D distance from p1 to p2
    distance((0,5),(12,0)) --> 13.0'''
    diff_longitude = p1[1] - p2[1]
    diff_latitude = p1[0] - p2[0]
    return sqrt((diff_longitude*53)**2 + (diff_latitude*69)**2)

eastDegrees = degreesLongitude(1000,SanFran[0]) #around 18.3 degrees

loc2 = (SanFran[0],SanFran[1] - eastDegrees)

southDegrees = degreesLatitude(1000,loc2[0])

loc3 = (loc2[0] - southDegrees,loc2[1])

westDegrees = degreesLongitude(1000,loc3[0])

loc4 = (loc3[0],loc3[1] + westDegrees)

northDegrees = degreesLatitude(1000,loc4[1])

endLoc = (loc4[0] + abs(northDegrees),loc4[1])

#print(distance((0,5),(12,0)))
print(loc2)
print(loc3)
print(loc4)
print("End Location =", endLoc)
print("Distance:",distance(SanFran,endLoc))

#End: 37.7749° N, 122.4194° W to 48.9° N, 119.45° W
