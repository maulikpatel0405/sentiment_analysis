class objectIntegrator:

    aDict = {'neg': 0, 'neu': 0, 'pos': 0, 'compound': 0}
    count = 0

    def __init__(self):
        pass

    def objectCallCount(self):
        objectIntegrator.count = objectIntegrator.count + 1

    def integrator(self, obj):
        self.objectCallCount()
        objectIntegrator.aDict["neg"] = objectIntegrator.aDict["neg"] + obj["neg"]
        objectIntegrator.aDict["neu"] = objectIntegrator.aDict["neu"] + obj["neu"]
        objectIntegrator.aDict["pos"] = objectIntegrator.aDict["pos"] + obj["pos"]
        objectIntegrator.aDict["compound"] = objectIntegrator.aDict["compound"] + obj["compound"]





