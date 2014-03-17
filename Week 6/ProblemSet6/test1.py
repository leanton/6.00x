import string

text = 'WordTrigger should be a subclass of Trigger. It has one new method, isWordIn, which takes in one string argument text. It returns True if the whole word word is present in text, False otherwise, as described in the above examples. This method should not be case-sensitive. Implement this method.'
text2 = 'Soft\'s the new pink!'
text3 = '\"Soft!\" he exclaimed as he threw the football.'

class WordTrigger(object):
    def __init__(self, word):
        self.word = str(word)

    def isWordIn(self, text):
        self.word = self.word.lower()
        text = text.lower()
        textInWords = text.split(' ')
        parsedText = []
        for word in textInWords:
        	if '\'' in word:
        		temp = word.split('\'')
        		for wtemp in temp:
        			textInWords.append(wtemp)
        	if '-' in word:
        		temp = word.split('-')
        		for wtemp in temp:
        			textInWords.append(wtemp)
        	edtword = word.strip(string.punctuation)
        	parsedText.append(edtword)
        del textInWords[:]
        if self.word in parsedText:
            return True
        else:
            return False

g1 = WordTrigger('soft')
print g1.isWordIn(text3)


class PhraseTrigger(Trigger): 
    def init(self, phrase): 
        self.phrase = phrase  
    def evaluate(self, story):  
        if self.phrase in story.getTitle():  
         return True  
    elif self.phrase in story.getSubject():  
         return True  
    elif self.phrase in story.getSummary(): 
         return True 
    else: 
         return False 

