class back():
    def cat(self):
        print("cat sound")
        
#obj = back()
#obj.cat()

class back2(back):
    def dog(self):
        print("dog sound")
        
obj = back2()
obj.cat()
obj.dog()