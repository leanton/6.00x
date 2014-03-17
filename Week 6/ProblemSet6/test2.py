def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """

    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#': # Discard lines with None and 'Comment lines'
            continue
        lines.append(line)

    print lines

    triggers = []
    triggerMap = {}

    # Be sure you understand this code - we've written it for you,
    # but it's code you should be able to write yourself
    for line in lines:

        linesplit = line.split(" ")

        # Making a new trigger
        if linesplit[0] != "ADD":
            trigger = makeTrigger(triggerMap, linesplit[1],
                                  linesplit[2:], linesplit[0])

        # Add the triggers to the list
        else:
            for name in linesplit[1:]:
                triggers.append(triggerMap[name])

    return triggers

def makeTrigger(triggerMap, triggerType, params, name):

    if triggerType == 'SUBJECT':
        triggerMap[name] = params[0]
    if triggerType == 'TITLE':
        triggerMap[name] = params[0]
    if triggerType == 'SUMMARY':
        triggerMap[name] = params[0]
    if triggerType == 'PHRASE':
        triggerMap[name] = str(' '.join(params))
    if triggerType == 'NOT':
        triggerMap[name] = params[0]
    if triggerType == 'AND':
        triggerMap[name] = params
    if triggerType == 'OR':
        triggerMap[name] = params
    print triggerMap
    # TODO: Problem 11


print readTriggerConfig('triggers.txt')