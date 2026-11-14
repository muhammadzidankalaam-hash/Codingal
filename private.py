class myHome:
    __privateVar = 27; 
    def __privMeth(self):
        print("I'm inside class MyHome")
    def hello(self):
        print("Private Variable value:",myHome.__privateVar)
foo = myHome()
foo.hello()
foo.__privMeth


