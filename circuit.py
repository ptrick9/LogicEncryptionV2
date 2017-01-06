

class Circuit:

    inputs = []
    outputs = []
    gates = []
    comments = []

    def __init__(self):
        self.inputs = []
        self.outputs = []
        self.gates = []
        self.comments = []

    def addLine(self, line):
        if 'INPUT' in line:
            self.inputs.append(line.rstrip())
        elif 'OUTPUT' in line:
            self.outputs.append(line.rstrip())
        elif line[0] == '#':
            self.comments.append(line.rstrip())
        elif '=' in line and ('NOT' in line or 'AND' in line or 'OR' in line):
            self.gates.append(line.rstrip())
        elif len(line) < 3:
            pass
        else:
            print("unable to add line correctly")

    def dump(self):
        c = ""
        for line in self.comments:
            c = c + line + "\n"
        for line in self.inputs:
            c = c + line + "\n"
        for line in self.outputs:
            c = c + line + "\n"
        for line in self.gates:
            c = c + line + "\n"
        return c

    def __str__(self):
        s = "There are %i inputs, %i outputs, %i gates, and %i comments" % (len(self.inputs), len(self.outputs), len(self.gates), len(self.comments))
        return s