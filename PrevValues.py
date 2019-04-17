class PrevValues:
    def __init__(self, window, st_val):
        self.window = window
        self.__arr = [st_val for i in range(window)]
    def append(self, x):
        self.__arr.append(x)
        self.__arr = self.__arr[-self.window: ]
    def getVal(self, i):
        return self.__arr[i]
