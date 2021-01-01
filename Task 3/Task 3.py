# task 3.1
class Tool:
    def __init__(self, name, cost, image):
        self.__name = name
        self.__cost = cost
        self.__image = image

    def get_name(self):
        return self.__name

    def get_cost(self):
        return self.__cost

    def get_image_filename(self):
        return self.__image

    def set_name(self, new_name):
        self.__name = new_name
