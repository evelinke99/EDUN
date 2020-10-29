class Exercises:
    def __init__(self,exercise,solution):
        self.__ex=exercise
        self.__sol=solution

    def setExercise(self,exercise):
        self.__ex=exercise

    def setSolution(self,solution):
        self.__sol=solution

    def getExercise(self):
        return self.__ex

    def getSolution(self):
        return self.__sol

class MissingAnswer(Exception):
    pass

class FinishedChallange(Exception):
    def __init__(self,value):
        self.__val=value

    def __str__(self):
        return 'Gratulálok sikeresen teljesítetted a(z) '+ self.__val+' témakört!'

class ClosingConfirmation(Exception):
    def __init__(self,value):
        self.__val=value

    def __str__(self):
        return 'Szeretné menteni a(z) '+ self.__val+' témakör eddig megoldott feladatait?'


