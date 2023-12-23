class Figure:
    unit = 'cm'
    def __init__(self):
        self.__perimeter = 0
    @property
    def perimeter(self):
        return self.__perimeter
    @perimeter.setter
    def perimeter(self,value):
             self.__perimeter = value
    def calculate_area(self):
        pass
    def info(self):
        pass
    def calculate_perimeter(self):
        pass
class Square(Figure):
    def __init__(self,side_length):
        super().__init__()
        self.__side_length = side_length
        self.__perimeter  = self.calculate_perimeter()


    def calculate_area(self):
        return self.__side_length ** 2
    def calculate_perimeter(self):
        return self.__side_length * 4

    def info(self):
        return (f'square side length : {self.__side_length}{self.unit}'
               f'\n perimeter : {self.__perimeter}{self.unit}'
               f'\n area: {self.calculate_area()}{self.unit}^2')
class Rectangle(Figure):
    def __init__(self,length,width):
        super().__init__()
        self.__length = length
        self.__width = width
        self.__perimeter = self.calculate_perimeter()

    def calculate_perimeter(self):
        return 2 * (self.__length + self.__width)

    def calculate_area(self):
        return self.__length * self.__width
    def info(self):
        return(f'rectangle length : {self.__length}{self.unit}'
              f'\n rectangle width: {self.__width}{self.unit}'
              f'\n perimeter : {self.__perimeter}{self.unit}'
              f'\n area: {self.calculate_area()}{self.unit}^2')

square = Square(12)
square2 = Square(23)
rec_1 = Rectangle(12,23)
rec_2 = Rectangle(23,34)
rec_3 = Rectangle(34,45)

list_with_figures = [square,square2,rec_1,rec_2,rec_3]
for figures in list_with_figures:
    print(figures.info())