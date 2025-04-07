from typing import List


class Stack:
    def __int__(self):
        self.__arr = []

    def push(self, element):
        self.__arr.append(element)

    def pop(self):
        if self.__arr:
            del self.__arr[-1]
            return self.__arr
        else:
            return -1


def stacks_using_arrays(arr):
    pass


if __name__ == "__main__":
    print(stacks_using_arrays([12, 45, 34, 465, 767, 67, 67]))
