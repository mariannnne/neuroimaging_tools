
# coding: utf-8

# In[26]:

import nibabel as nib
import numpy as np
from nilearn import plotting as niplt


# In[22]:
thr = 75
l_amyg = nib.load('/Volumes/sac/Projects/Imagination/Analysis/masks/amygdala/LeftAmygdala.nii')
r_amyg = nib.load('/Volumes/sac/Projects/Imagination/Analysis/masks/amygdala/RightAmygdala.nii')

ldata = l_amyg.get_data()
rdata = r_amyg.get_data()

# In[24]:

ldata[ldata < thr] = 0
ldata[ldata >= thr] = 1


rdata[rdata < thr] = 0
rdata[rdata >= thr] = 1


# In[27]:

niplt.plot_roi(l_amyg)
niplt.plot_roi(r_amyg)


# In[35]:

nib.save(l_amyg, '/Volumes/sac/Projects/Imagination/Analysis/masks/amygdala/l_amyg_30perc.nii.gz')
nib.save(r_amyg, '/Volumes/sac/Projects/Imagination/Analysis/masks/amygdala/r_amyg_30perc.nii.gz')


# ## Make bilateral mask

# In[36]:

l_amyg_1 = nib.load('/Volumes/sac/Projects/Imagination/Analysis/masks/amygdala/LeftAmygdala.nii')
r_amyg_1 = nib.load('/Volumes/sac/Projects/Imagination/Analysis/masks/amygdala/RightAmygdala.nii')


# In[37]:

l_data1 = l_amyg_1.get_data().copy()
r_data1 = r_amyg_1.get_data().copy()


# In[43]:

bilateral_data = ((l_data1 > thr) | (r_data1 > thr)).astype('int64')


# In[44]:

bilateral = nib.Nifti1Image(bilateral_data, l_amyg_1.get_affine(), l_amyg_1.get_header())


# In[45]:

niplt.plot_roi(bilateral)


# In[46]:

nib.save(bilateral, '/Volumes/sac/Projects/Imagination/Analysis/masks/amygdala/bilateral_amygdala_75.nii.gz')


# In[ ]:



