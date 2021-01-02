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

    def set_cost(self, new_cost):
        self.__cost = new_cost

    def set_image_filename(self, new_image):
        self.__image = new_image


class Shelf:
    def __init__(self, position):
        self.__position = position
        self.__array = [""] * 10
        self.__free_pointer = 0

    def add_tool(self, tool_obj):
        self.__array[self.__free_pointer] = tool_obj
        self.__free_pointer += 1

    def get_array(self):
        return self.__array


def out_tool(shelf_obj):
    arr = shelf_obj.get_array
    for i in range(len(arr)):
        if arr[i] != "":
            print("Name of the book: %s" % arr[i].get_name())
            print("Cost of the book: %s" % arr[i].get_cost())



