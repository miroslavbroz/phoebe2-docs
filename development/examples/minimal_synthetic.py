#!/usr/bin/env python
# coding: utf-8

# Minimal Example to Produce a Synthetic Light Curve
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.2 installed.  (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system('pip install -I "phoebe>=2.2,<2.3"')


# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# As always, let's do imports and initialize a logger and a new bundle.  See [Building a System](../tutorials/building_a_system.ipynb) for more details.

# In[1]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary()


# Adding Datasets
# ------------------
# 
# Now we'll create an empty lc dataset:

# In[2]:


b.add_dataset('lc', times=np.linspace(0,1,201), dataset='mylc')


# Running Compute
# ---------------------

# Now we'll compute synthetics at the times provided using the default options

# In[3]:


b.run_compute(irrad_method='none')


# Plotting
# --------------
# 
# Now we can simply plot the resulting synthetic light curve.

# In[4]:


afig, mplfig = b['mylc@model'].plot(show=True)


# In[5]:


afig, mplfig = b['mylc@model'].plot(x='phases', show=True)


# In[ ]:




