
# coding: utf-8

# In[26]:

import nibabel as nib
import numpy as np
from nilearn import plotting as niplt


# # In[22]:

# l_hipp = nib.load('/Users/maus/Desktop/SCR/pattexp/masks/ROI_Masks/LeftHippocampus.nii')
# r_hipp = nib.load('/Users/maus/Desktop/SCR/pattexp/masks/ROI_Masks/RightHippocampus.nii')

# lhipp = l_hipp.get_data()
# rhipp = r_hipp.get_data()

# # In[24]:

# lhipp[lhipp < 75] = 0
# lhipp[lhipp >= 75] = 1


# rhipp[rhipp < 75] = 0
# rhipp[rhipp >= 75] = 1


# # In[27]:

# niplt.plot_roi(l_hipp)
# niplt.plot_roi(r_hipp)


# # In[35]:

# nib.save(l_hipp, '/Users/maus/Desktop/SCR/analyses/Paper/hippo_Beta/l_hipp_25perc.nii.gz')
# nib.save(r_hipp, '/Users/maus/Desktop/SCR/analyses/Paper/hippo_Beta/r_hipp_25perc.nii.gz')


# ## Make bilateral mask

# In[36]:

l_hipp_1 = nib.load('/Users/maus/Desktop/SCR/pattexp/masks/ROI_Masks/LeftHippocampus.nii')
r_hipp_1 = nib.load('/Users/maus/Desktop/SCR/pattexp/masks/ROI_Masks/RightHippocampus.nii')


# In[37]:

l_data1 = l_hipp_1.get_data().copy()
r_data1 = r_hipp_1.get_data().copy()


# In[43]:

bilateral_data = ((l_data1) | (r_data1)).astype('int64')


# In[44]:

bilateral = nib.Nifti1Image(bilateral_data, l_hipp_1.get_affine(), l_hipp_1.get_header())


# In[45]:

niplt.plot_roi(bilateral)


# In[46]:

nib.save(bilateral, '/Users/maus/Desktop/SCR/analyses/Paper/hippo_Beta/bilateral_hipp_nothresh.nii.gz')


# In[ ]:



