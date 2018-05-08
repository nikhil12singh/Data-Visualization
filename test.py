import json
import pandas as pd
import os
import fnmatch

path = 'files/'
listing = os.listdir(path) 


for infile in listing:
    with open(infile) as json_file:  
        if fnmatch.fnmatch(infile, 'nikhil*'):
	        data = json_file.readlines()
	        # this line below may take at least 8-10 minutes of processing for 4-5 million rows. It converts all strings in list to actual json objects. 
	        data = list(map(json.loads, data)) 
	        str1 = str(data);
	        print (str1)
	        #str1.write(str1);
	        """text_file = open("Output5.json", "w")
            text_file.write(str1)
            text_file.close()"""






