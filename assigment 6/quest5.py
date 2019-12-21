# # Question 5:
# # Write a code in python in which create a class named it Car which
# # have 5 attributes such like (model, color and name etc.) and 3
# # methods. And create 5 object instance from that class.


class Car:
    def _init_(self, model, colour, name, company, registration):
        self.model = model
        self.colour = colour
        self.name = name
        self.company = company
        self.registration = registration
    def descriptionCar(self):
        print("the make of car is {self.model}")
        print("the make of car is {self.colour}")
        print("the make of car is {self.name}")
        print("the make of car is {self.company}")
        print("the make of car is {self.registration}")

    # def move(self):
    #     print("{self.company} is move with very high speed")

    # def breaks(self):
    #     print("{self.name} is disc breaks")
car1 = Car(2014,"Black","Civic","Honda",2018)
car2 =Car(2013,"Blue","Suzuki","Mehran",2019)
car3 = Car(2015,"White","Suzuki","Cultus",2017)
car4=Car(2017,"Red","Suzuki","Vitz",2019)
car5=Car(2018,"Golden","Suzuki","waganor",2019)


