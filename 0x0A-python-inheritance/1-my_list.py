#!/usr/bin/python3

class MyList(list):
    def print_sorted(self):
        print(MyList(sorted(self)))
