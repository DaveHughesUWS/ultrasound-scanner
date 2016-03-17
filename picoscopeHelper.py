import numpy as np

class picoscope:
    def __init__(self,nPoints, nAvg,nSRate):
        self.nDataPoints = nPoints;
        self.nAveraging = nAvg;
        self.nSampleRate =nSRate;
        self.dataBuffer = np.zeros(self.nDataPoints);
    
    
    def grabData(self):
        # collect data from hardward
        self.dataBuffer = self.dataBuffer+np.ones(self.nDataPoints);
    
    def collectData(self):
        # function to return data from scope
        return self.dataBuffer;