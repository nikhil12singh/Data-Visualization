import json
import pandas as pd

with open('Output5.json') as json_file:      
    data = json_file.readlines()
    # this line below may take at least 8-10 minutes of processing for 4-5 million rows. It converts all strings in list to actual json objects. 
    data = list(map(json.loads, data)) 
    str1 = str(data);
    #str1.write(str1);

    for obj in data:
    	text_file = open("final.json", "w")
	text_file.write(str1)
	print (str1)
	text_file.close()
	
