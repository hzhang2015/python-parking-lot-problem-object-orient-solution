'''
Created on 2014-11-29

@author: ouyangsiqi
'''

class Level:
    '''
    The class is the levels of the parking lot
    '''
    __spaces = []
    __spaceCount = len(__spaces)

    def __init__(self, spacesOfEachLevel):
        '''
        Constructor
        '''
        self.__spaces = spacesOfEachLevel
        self.__spaceCount = len(spacesOfEachLevel)
    
    def getSpaces(self):
        '''
        The method to get the spacesOfEachLevel in the level
        '''
        return self.__spaces
        
    def getSpaceCount(self):
        '''
        The method to get the space count of the level
        '''
        return self.__spaceCount;

    def showLevelParkingStatus(self):
        '''
        The method to show the parking status of the level
        '''
        emptySpaceCount = 0
        for i in range(self.__spaceCount):
            if not self.__spaces[i].checkIfCarParked():
                emptySpaceCount += 1
        print "    total spaces count: " + str(self.__spaceCount)
        print "    empty spaces count: " + str(emptySpaceCount)
        print "    parked spaces count: " + str(self.__spaceCount - emptySpaceCount)