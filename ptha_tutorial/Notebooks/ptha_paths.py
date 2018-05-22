
"""
Set ptha_dir to the absolute path to the top level of this git repository.
Adjust if necessary below...
"""

from __future__ import print_function
import os,sys

#---------------------------------------------------------------------
# Adjust this line if needed to set path properly:
ptha_dir = os.path.abspath('..')
# Should be right when this module is imported from Notebooks subdirectory.
#---------------------------------------------------------------------

print("Assuming that top level of this repository is at: %s" % ptha_dir)

codes_dir = os.path.join(ptha_dir, 'PythonCode')
print("    Python codes can be found in codes_dir = %s"  % codes_dir)
sys.path.append(codes_dir)   # make python modules available

data_dir = os.path.join(ptha_dir, 'DataFiles')
print("    Data files can be found in data_dir = %s"  % data_dir)

events_dir = os.path.join(data_dir, 'Events')
print("    Results for each event can be found in events_dir = %s"  % events_dir)

#---------------------------------------------------------------------
# Added by Brian
#---------------------------------------------------------------------

# Path to the top level of the project respository (tsunami-inundation)
proj_dir = os.path.abspath('../..')
print("Assuming that top level of the CSE512 repository is at: %s" % proj_dir)

# Path to where JS data files are stored
js_data_dir = os.path.join(proj_dir, 'docs/data')
print("    JavaScript data files can be found in data_dir = %s"  % js_data_dir)