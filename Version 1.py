'''
Version 1
'''
class countrydata(object):
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

class Countriesdata(object):
'''this Represents a list of the Countries data '''

    def __init__(self):
        '''opens up the file and stores it in a list'''
        self.countrylist=[]
        mynewhandle = open("countries.csv", "r")
        theline = mynewhandle.readline() #skip first line with column headings
        somedata=Countrydata() #goes to the Countrydata class to create an object
        self.countrylist.append(somedata) # blank data to overtake index[0]
        count=0 #to count how many sets of data are read
        while True:
            theline=mynewhandle.readline()
            count +=1
            if len(theline) == 0:              # If there are no more lines
                break                          #     leave the loop
            else:
                alist = theline.split(",")
                #make sure the data is read in properly with the proper data types
                somedata= Countrydata(alist[0],float(alist[1]),float(alist[2]))
                self.countrylist.append(somedata)
        mynewhandle.close()
        self.numData=count
        
        self.countryDict = {}
        for i in range(len(self.countrylist)):
            self.countryDict[i] = 
class Point:
'''this Point class represent the point of each country(x,y) '''

    def __init__(self, x=0, y=0):
''' Create a new point at the origin'''
        self.x = x#latitude
        self.y = y#longtitude
        
    def __str__(self):    
            return "({0}, {1})".format(self.x, self.y)
        
    def midpoint(p1, p2):
        """ Return the midpoint of points of two countries """
        mx = (p1.x + p2.x)/2 #it takes two x points and finds the mid of the two x
        my = (p1.y + p2.y)/2 # it takes two y and find the mid of two y
        return Point(mx, my)#this is the mid point cooridinate
    
   def sortbyCountryName(self):
        #supply the code
        for i in range(1,self.numData-1):
            for j in range(1,self.numData-1):
                if self.countrylist[j].name > self.countrylist[j+1].name:
                    tmp = self.countrylist[j]
                    self.countrylist[j] = self.countrylist[j+1]
                    self.countrylist[j+1]=tmp
        return self

    def sortbylatitude(self):
        #supply the code
        def merge(left, right):
        #the numbers would be stored in this list from smallest to biggest
            result = []
            while left and right:
                if left[0]<=right[0]:
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
                return self
        mergeSort(self.countrylist.latitude)

    def searchbyatomicNumber(self,symbol):
        def BinarySearchR(thelist, symbol):
            mid=len(thelist)//2
            if thelist[mid]==symbol:
                return True
            elif mid<=0:
                return False
            elif num>thelist[mid]:
                #recalls the function with half the list
                return BinarySearchR(thelist[mid:],num)
            else:
                return BinarySearchR(thelist[:mid],num)
        BinarySearchR(self.countrylist,symbol)
# draw map
print(Countries.data(countrieslist))