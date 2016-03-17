import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pistagesHelper
import picoscopeHelper


# Parameters for Ultrasound Sanning
nAveraging = 16;
nAScans = 500;
stepSize = 100e-6;
trigDelay=0;
nDataPoints = 1024;
nSamplingRate = 0.8e-9;
representativeVelocity = 1500;

# calculated parameters
totalScanSize = (nAScans * stepSize)/1e-3;
scanDepth = ((nDataPoints * nSamplingRate)*representativeVelocity)/1e-3;
dataBufferSize = nDataPoints * nAveraging;
imageData = np.zeros((nAScans,nDataPoints));
plotWindow=plt.imshow(imageData, extent=[0,scanDepth,0,totalScanSize], aspect='auto');
plt.show();
#initialise hardware

#initialise picoscope
ps = picoscopeHelper.picoscope(nDataPoints,nAveraging,nSamplingRate);


#initialise stages
stage1=pistagesHelper.piStages();
stage1.initialise();

#start scan
scanID = range(1,nAScans);

for i in scanID:
    #grab current stage position and update stage position
    # move stages
    curPos = stage1.getPos();
    newPos = curPos+stepSize;
    stage1.setPos(newPos);
    
    
    #grab picoscope data
    ps.grabData();
    data=ps.collectData();
  
    imageData[i,:]=data;
    plotWindow.set_data(imageData);
    plt.draw();