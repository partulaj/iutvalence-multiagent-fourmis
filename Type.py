class Type():
    def __init__(self, type):
        self.type = type
        if self.type=="Follower":
            self.alpha = 5
            self.beta = 2
        elif self.type=="Explorer":
            self.alpha = 1
            self.beta = 5

    def getAlpha(self):
        return self.alpha

    def getBeta(self):
        return self.beta

    def __str__(self):
        return self.type