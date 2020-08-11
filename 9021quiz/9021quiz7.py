# Defines two classes, Point() and Disk().
# The latter has an "area" attribute and three methods:
# - change_radius(r)
# - intersects(disk), that returns True or False depending on whether
#   the disk provided as argument intersects the disk object.
# - absorb(disk), that returns a new disk object that represents the smallest
#   disk that contains both the disk provided as argument and the disk object.
#
# Written by *** and Eric Martin for COMP9021


from math import pi, hypot


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x:.2f}, {self.y:.2f})'




class Disk:
    def __init__(self,*,centre = Point(0, 0),radius = 0):
        self.area=0
        self.Point=centre
        self.radius=radius
        self.caculate_area()

    def caculate_area(self):
        self.area=pi*self.radius*self.radius

    def intersects(self,other):
        x1=self.Point.x
        y1=self.Point.y
        #得到了第一个圆的圆心坐标
        x2=other.Point.x
        y2=other.Point.y
        #得到了第二个圆的圆心坐标
        centre_distance=((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)) **(1/2)
        #求出两个圆的圆心距
        sum_of_radiuses=self.radius+other.radius
        #两个圆的半径和
        if centre_distance<=sum_of_radiuses:
            return True
        else:
            return False

    def change_radius(self,target_radius):
        self.radius=target_radius
        self.caculate_area()

    def absorb(self,sec_cir):
        if self.radius>=sec_cir.radius:
            big_x=self.Point.x
            big_y=self.Point.y
            big_r=self.radius
            small_x=sec_cir.Point.x
            small_y=sec_cir.Point.y
            small_r=sec_cir.radius
        else:
            big_x=sec_cir.Point.x
            big_y=sec_cir.Point.y
            big_r=sec_cir.radius
            small_x=self.Point.x
            small_y=self.Point.y
            small_r=self.radius
        #大圆的圆心距是big小圆的是small
        center_distance=((big_x-small_x)*(big_x-small_x)+(big_y-small_y)*(big_y-small_y))**(1/2)
        #两个圆的圆心距
        q_r=(center_distance+big_r+small_r)/2
        #求出大圆的半径
        radius_sum=big_r+small_r
        #半径的和
        if center_distance <= big_r - small_r:
            disk_q=Disk(centre=Point(big_x,big_y),radius=big_r)
        #如果是相切或者是包含的关系 那么就只要把大圆作为结果即可
        else:
            q_y=(q_r-small_r)*(big_y-small_y)/center_distance+small_y
            q_x=(q_r-small_r)*(big_x-small_x)/center_distance+small_x
            #用相似比例来做
            disk_q=Disk(centre=Point(q_x,q_y),radius=q_r)
        return disk_q

    def __repr__(self):
        return f'Disk({self.Point}, {self.radius:.2f})'


disk_1 = Disk(centre = Point(0, 0), radius = 0)
disk_2 = Disk(centre = Point(3, 0), radius = 4)
disk_2.caculate_area()
disk_1.intersects(disk_2)
print(disk_2.area)
print(disk_1.intersects(disk_2))

disk_1.change_radius(2)      
print(disk_1.area)
disk_3 = disk_1.absorb(disk_2)
print(disk_1)
print(disk_2)
print(disk_3)
disk_4 = Disk(centre = Point(-4, 0), radius = 2)
print(disk_4.intersects(disk_1))
disk_5 = disk_4.absorb(disk_1)
print(disk_5)
disk_5.change_radius(5)
print(disk_5)
disk_6 = Disk(centre = Point(1, 2), radius = 6)
disk_7 = disk_5.absorb(disk_6)
print(disk_7)
a=disk_7.area
print(disk_7.area)
disk_8=Disk(centre = Point(1, 1), radius = 1)
disk_9=Disk(centre = Point(3, 1), radius = 1)
disk_10 = disk_8.absorb(disk_9)
print(disk_10)
disk_11=Disk(centre = Point(1, 1), radius = 1)
disk_12=Disk(centre = Point(1, 3), radius = 1)
disk_13 = disk_11.absorb(disk_12)
print(disk_13)



