def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    lineLength: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    if len(text) <= lineLength or text.find(' ')==-1:
        return text
    elif text[lineLength-1] == ' ':
        return text[:lineLength] + '\n' + insertNewlines(text[lineLength:], lineLength)
    else:
        return text[:text.find(' ', lineLength)] + '\n' + insertNewlines(text[text.find(' ', lineLength)+1:], lineLength)

print insertNewlines('While I expect new intellectual adventures ahead, nothing will compare to the exhilaration of the world-changing accomplishments that we produced together.', 15)
print insertNewlines('Random text to wrap again.', 5)