
# coding: utf-8

# In[26]:

import nibabel as nib
import numpy as np
from nilearn import plotting as niplt


# In[22]:

l_hipp = nib.load('/Volumes/sac/Projects/Imagination/Analysis/masks/auditory/STGpost.nii')
lhipp = l_hipp.get_data()

# In[24]:

lhipp[lhipp < 50] = 0



# In[27]:

niplt.plot_roi(l_hipp)



# In[35]:

nib.save(l_hipp, '/Users/maus/Desktop/SCR/analyses/Paper/hippo_Beta/STG_50perc.nii.gz')



