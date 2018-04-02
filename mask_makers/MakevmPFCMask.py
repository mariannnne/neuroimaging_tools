
# coding: utf-8

# In[26]:

import nibabel as nib
import numpy as np
from nilearn import plotting as niplt


# In[22]:

vmpfc = nib.load('/Users/maus/Desktop/SCR/analyses/ROI/FrontalMedialCortex.nii')
vdata = vmpfc.get_data()

vdata[vdata < 50] = 0
vdata[vdata >= 50] = 1

# In[27]:

niplt.plot_roi(vmpfc)



# In[35]:

nib.save(vmpfc, '/Users/maus/Desktop/SCR/analyses/ROI/vmpfc_50perc.nii.gz')




