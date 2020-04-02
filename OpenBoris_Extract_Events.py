# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 13:30:57 2020

@author: johnx
"""
FolderRoot = (r'  ')
import os
import json
import pandas as pd

# Creates a loop that will look through folder and any sub folders
for subdir, dirs, files in os.walk(FolderRoot):
    for filename in files:
        Borisfile = []
        filepath = subdir + os.sep + filename
        # If is used to check if file is a .boris
        if filepath.endswith(".boris"):        
            # Open Boris file using json format
            fileName = filename
            infile = open(filepath,"r")
            s = infile.read()
            project = json.loads(s)
            # Opens and extracts name of observations in file
            # The file has a hierarchical file structure
            observationlist = project["observations"]
            obkeys = observationlist.keys()
            p = 0
            for i in obkeys:
                current = observationlist[i]
                # Finds events within the Observation and writes to a lits
                Event_list = current["events"]
                # Some Event lists were empty - therefore filled with NAN/No value
                if not Event_list:
                    Event_list = [['nan','nan','nan','nan','nan'],['nan','nan','nan','nan','nan']]
                # Data was converted from list to a data frame / table
                newFrame = pd.DataFrame(Event_list)
                newFrame.columns = ['Time_seconds','Subject','Observation','','']
                findKey = observationlist.keys()
                keyList = list(findKey)
                # Creates a new folder for the data to export if it does not exist
                if not os.path.isdir(subdir + '\\Export\\'):
                    os.makedirs(subdir + '\\Export\\')
                # Create new file name and directory - Save as CSV
                fileExportName = subdir + '\\Export\\' + keyList[p] + '.csv' 
                newFrame.to_csv(fileExportName)
                p += 1
                
