class JustCounter:
    __privateCount = 0 # the double underscore makes it private
    def count(self):
        self.__privateCount += 1
        print(self.__privateCount)


counter = JustCounter()
counter.count()
