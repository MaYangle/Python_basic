class Restaurant():
    """模拟一个餐厅"""
    def __init__(self,name,cuisine_type):
        self.name = name
        self.type = cuisine_type
        self.number_served = 11
    def describe_restaurant(self):
        print("The name of the restaurant is " + self.name.title())
        print("The type of cuisine is " + self.type)
    def open_restaurant(self):
        print("The restaurant is opening")
    def set_number_served(self,number):
        self.number_served = number
    def increment_number_served(self,number):
        self.number_served += number