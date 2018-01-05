# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 20:08:10 2016

@author: culi
"""

import numpy as np
from matplotlib import pyplot as plt
try:
    print('1')
except Exception as e:
    print(e)
theta=np.arange(0,2*np.pi,0.02)
plt.subplot(121,polar=True)
plt.plot(theta,2*np.ones_like(theta),lw=2)
plt.plot(theta,theta/6,'--',lw=2)
plt.subplot(122,polar=True)
plt.plot(theta,np.cos(5*theta),'--',lw=2)
plt.plot(theta,2*np.cos(4*theta),lw=2)
plt.rgrids(np.arange(0.5,2,0.5),angle=45)
plt.thetagrids([0,45,90])
plt.show()
