"""一个可用来表示汽车的类"""
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #设置了一个里程 用来读数
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + " " +self.make + ' ' +self.model
        return long_name.title()
    def read_odometer(self):
        """打印出一条指向汽车里程的信息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self,mileage):
        """将里程表读数设置为指定的值"""
        #可对方法update进行扩展，防止有人将读书往回调
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back in odometer!")
    def increment_odometer(self,miles):
        """将里程表读数增加特定的值"""
        self.odometer_reading += miles

class Battery():  #定义了一个新类
    """模拟电动车汽车电瓶的简单尝试"""
    def __init__(self,battery=70):
        """初始化电瓶的属性"""
        self.battery_size = battery
    def describe_battery(self):
        """打印一条描述电瓶容量的信息"""
        print("This car has a " +str(self.battery_size) + "-kWh battery.")
    def get_range(self):
        """打印一条信息 指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = " This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
        
class ElectricalCar(Car):
    """电动车"""
    def __init__(self,make,model,year): #1
        """初始化父类的属性"""
        super().__init__(make,model,year) #2
        self.battery = Battery()  #创建了一个新的Battery实例 并且存储在属性self.battery中。
        
    def increment_odometer(self,miles):
        """修改一下"""
        self.odometer_reading += 0.98*miles