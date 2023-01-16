'''
Version 2
'''
class Countrydata(object): #makes a object for each country
    '''
    this represents a single country with
    its attributes of
    1.symbol
    2.latitude
    3.longtitude
    4.name of country
    '''
    def __init__(self, symbol='', latitude=0.0, longtitude=0.0, name=''):
        self.symbol = symbol#string
        self.latitude = latitude#float
        self.longtitude = longtitude#float
        self.name = name#string


    def __str__(self):
        return "Symbol: {0:12}\n\
latitude: {1:5}\n\
longtitude: {2:5}\n\
name:{3:5}".format(self.symbol, self.latitude, self.longtitude, self.name)
    
    def __repr__(self):
        return "Symbol: {0:12}\n\
latitude: {1:5}\n\
longtitude: {2:5}\n\
name:{3:5}".format(self.symbol, self.latitude, self.longtitude, self.name)

class Countriesdata(object):
    '''this Represents a list of the Countries data '''

    def __init__(self):
        '''opens up the file and stores it in a list'''
        self.countrylist=[]
        mynewhandle = open("countries.csv", "r")
        theline = mynewhandle.readline() #skip first line with column headings
        count=0 #to count how many sets of data are read
        while True:
            theline=mynewhandle.readline()
            theline=theline.rstrip()#takes away the \n 
            if len(theline) == 0:              # If there are no more lines
                break                          #     leave the loop
            else:
                count +=1
                alist = theline.split(",")
                #make sure the data is read in properly with the proper data types
                somedata= Countrydata(alist[0],float(alist[1]),float(alist[2]),alist[3])
                self.countrylist.append(somedata)
        mynewhandle.close()
        self.numData=count
        
        #create a dictionary to store items which would help us for an easy sort
        self.countryDict = {country.name:country for country in self.countrylist}
        print(self.countryDict)
        #https://www.geeksforgeeks.org/python-convert-a-list-to-dictionary/
        
    def searchbyName(self):# searches for object using the dictionary
        #using the dictionary is so much more convient than using a linear or binary search
        Name = input("what is the Name you are finding? ")#user input the country name 
        print(self.countryDict[Name])
        
    def sortbyName(self):# a merge sort using Name
        def merge(left, right):#merge function works with mergesort funciton to compare the words
            result = []
            while left and right:
                if left[0].name<=right[0].name:#sort by object attribute name
                    result.append(left[0])
                    left = left[1:]
                else:
                    result.append(right[0])
                    right = right[1:]
            while left:
                result.append(left[0])
                left = left[1:]
            while right:
                result.append(right[0])
                right = right[1:]
            #returns the solved list
            return result
        #mergeSort function breaks the list into halves and halves of halves and so on
        def mergeSort(thelist):
            if len(thelist)<=1:
                return thelist
            else:
                mid = len(thelist)//2
                lefthalf = mergeSort(thelist[:mid])
                righthalf = mergeSort(thelist[mid:])
            return merge(lefthalf, righthalf)
        
        return mergeSort(self.countrylist)#call functions using countrylist as parameter 
    
    def sortbysymbol(self):
        for i in range(self.numData-1):
            for j in range(self.numData-1):
                if self.countrylist[j].symbol > self.countrylist[j+1].symbol:
                    tmp = self.countrylist[j]
                    self.countrylist[j] = self.countrylist[j+1]
                    self.countrylist[j+1]=tmp
        return self.countrylist
    
    def searchbySymbol(self,symbol):
        def BinarySearchR(thelist, symbol):
            mid=len(thelist)//2
            if thelist[mid].symbol==symbol:
                return thelist[mid]
            elif mid<=0:
                return "No such Symbol"
            elif symbol>thelist[mid].symbol:
                #recalls the function with half the list
                return BinarySearchR(thelist[mid:],symbol)
            else:
                return BinarySearchR(thelist[:mid],symbol)
        print(BinarySearchR(self.countrylist,symbol))



    def drawMap(self):
        import drawmap
        drawmap.drawmap(self.countrylist)
    
        
class Point(Countriesdata):
    '''this Point class represent the point of each country(x,y) '''
    pass

    def __init__(self, x=0, y=0):
        ''' Create a new point at the origin'''
        self.x = x#latitude
        self.y = y#longtitude
        
    def __str__(self):    
            return "({0}, {1})".format(self.x, self.y)
        
    def midpoint(p1,p2):
        """ Return the midpoint of points of two countries """
        mx = (p1.x+ p2.x)/2#it takes two x points and finds the mid of the two x
        my = (p1.y + p2.y)/2# it takes two y and find the mid of two y
        return Point(mx, my)#this is the mid point cooridinate

#Main Code
countriesd = Countriesdata()
points = Point()
print("Welcome To EARTH Studies:")
methods = ["Draw Map","Search by Symbol","Search by Name","Midpoint between countries","Sort by Name","Sort by Symbol"]
while True:
    count = 1
    for item in methods:
        print(count, item)
        count += 1
    method = int(input("What method would you like see? "))
    if method == 1:
        countriesd.drawMap()
    elif method == 2:
        inpsymbol = input("what is the symbol? ")
        countriesd.searchbySymbol(inpsymbol)
    elif method == 3:
        countriesd.searchbyName()
   # elif method ==4:
        #points.midpoint()
    elif method == 5:
        print(countriesd.sortbyName())
    elif method ==6:
        print(countriesd.sortbysymbol())
    cont = input("Would you like to continue to a different method or stop? (Yes or No):" )
    if cont == "No":
        break
    
        

