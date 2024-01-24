from constans import VALUES, SUITES, OK_MESSAGE

class Card:
    def __init__(self, suit, value):
        
        validationResult = self.validateInputValues(suit,value)
        if validationResult != OK_MESSAGE:
            raise Exception(validationResult)

        self.suit = suit
        self.value = value

    def getSuit():
        return self.suit
    
    def getValue():
        return self.value
    
    def validateInputValues(self, suit, value):
        
        if not suit or not isinstance(suit,str) or suit.lower().capitalize() not in SUITES:
            return "Invalid suit"
        
        if not value or not isinstance(value,str) or value not in VALUES:
            return "Invalid value"
        
        return OK_MESSAGE