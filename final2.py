# -*- coding: utf-8 -*-
import json
import ast
import pandas as pd
import os
import fnmatch

path = 'files/sw/'
listing = os.listdir(path)
i = 0;

for infile in listing:
    with open(infile) as json_file:  
        if fnmatch.fnmatch(infile, 'finale*'):    
            data = json_file.readlines()
            #print ("DATA")
            #print (data)
            # str1 = ''.join(data)
            # data3 = str1.replace('\"', '')
            # print ("DATA 3")
            # print(str1)
            # this line below may take at least 8-10 minutes of processing for 4-5 million rows. It converts all strings in list to actual json objects. 
            data2 = list(map(json.loads, data)) 
            # for obj in data2:
            #     strTemp = str(obj)
            #     index = strTemp.find('\'reviewTime\'')
            #     if strTemp[index+19] != ",":
            #         obj['date'] = strTemp[(index+18):(index+20)]
            #         obj['year'] = strTemp[(index+22):(index+26)]
            #         obj['month'] = strTemp[(index+15):(index+17)]
            #     else:
            #         obj['date'] = strTemp[(index+18):(index+19)]
            #         obj['year'] = strTemp[(index+21):(index+25)]
            #         obj['month'] = strTemp[(index+15):(index+17)]
            str1 = str(data2)
            data3 = str1.replace('u\'', '\'')
            data3 = data3.replace('u\"', '\"')
            data11 = eval(data3)
            #print (len(data11))
            #print (data11[0])
            counter = 0
            for obj in data11:
                strTemp = str(obj)
                #print (STRING)
                #print (strTemp)
                indexStart = strTemp.find('\'reviewText\'')
                indexEnd = strTemp.find('\'overall\'',indexStart)
                #index = strTemp.find('\'reviewTime\'')
                #obj['year'] = strTemp[(index+20):24]
                #obj['month'] = strTemp[(index+13):15]
                #obj['date'] = strTemp[(index+16):18]
                #idx = len(strTemp)
                #inserttxt = "\'year\' :\'"+strTemp[(index+20):24]+"\'"
                #strTemp = strTemp[:idx] + inserttxt + strTemp[idx:]
                #print (strTemp)
                #indexEnd2 = strTemp.find('\", \'',indexStart)
                #print indexStart
                #print indexEnd
                #print indexEnd2
                # indexEnd = indexEnd1
                # if indexEnd2 != -1 and indexEnd1<indexEnd2 :
                #     indexEnd = indexEnd1
                # else :
                #     indexEnd = indexEnd2
                #print indexStart
                #print indexEnd
                stringToRemove = strTemp[indexStart:indexEnd-1]
                #print "review Text String To remove"
                #print stringToRemove
                #index = strTemp.find(stringToRemove)
                #print "str index"
                #print index
                strTemp = strTemp.replace(stringToRemove,'')

                #removing summary

                indexStart = strTemp.find('\'summary\'')
                indexEnd1 = strTemp.find('\'',indexStart+13)
                indexEnd2 = strTemp.find('\"',indexStart+13)

                #indexEnd = strTemp.find()
                if indexEnd1 == -1 :
                    indexEnd = indexEnd2
                else :
                    indexEnd = indexEnd1

                indexEnd = strTemp.find('\'unixReviewTime\'',indexStart)

                print (indexStart)
                print (indexEnd)

                stringToRemove = strTemp[indexStart:indexEnd-1]
                print ("Review Summary String To remove")
                print (stringToRemove)

                strTemp = strTemp.replace(stringToRemove,'')



                #removing reviewer Name
                indexStart = strTemp.find('\'reviewerName\'')
                indexEnd = strTemp.find('\'helpful\'',indexStart)
                #print indexStart
                #print indexEnd

                stringToRemove = strTemp[indexStart:indexEnd-1]
                #print "Review Name String To remove"
                #print stringToRemove

                strTemp = strTemp.replace(stringToRemove,'')
                #print "STRING"
                #print strTemp

                #print (COUNTER)
                #print (counter)
                
                #print ("obj after removing string")
                #print (obj)

                obj = eval(strTemp)
                #print ("obj after removing string")
                #print (obj)
                #index = strTemp.find('\'reviewTime\'')
                dateVal = obj['reviewTime'];
                tempObj = dateVal.split(" ");
                obj['month'] = tempObj[0];
                obj['year'] = tempObj[2];
                if int(tempObj[0])>0 and int(tempObj[0])<4:
                    quater = "Q1"
                elif int(tempObj[0])>3 and int(tempObj[0])<7:
                    quater = "Q2"
                elif int(tempObj[0])>6 and int(tempObj[0])<10:
                    quater = "Q3"
                elif int(tempObj[0])>9 and int(tempObj[0])<13:
                    quater = "Q4"
                obj['quarter']= quater
                if len(tempObj[1]) == 2:
                    obj['date'] = tempObj[0] +"/" + tempObj[1][0:1] +"/" + tempObj[2]
                else:
                    obj['date'] = tempObj[0] +"/" + tempObj[1][0:2] +"/" + tempObj[2]

                # if strTemp[index+19] != ",":
                #     obj['date'] = strTemp[(index+18):(index+20)]
                #     obj['year'] = strTemp[(index+22):(index+26)]
                #     obj['month'] = strTemp[(index+15):(index+17)]
                # else:
                #     obj['date'] = strTemp[(index+18):(index+19)]
                #     obj['year'] = strTemp[(index+21):(index+25)]
                #     obj['month'] = strTemp[(index+15):(index+17)]

                #obj.reviewTime
                #print "str after removing string"
                #print strTemp
                print ("obj after adding date")
                print (obj)
                data11[counter]=obj
                counter=counter+1

            
            #print ("DATA after removing review text")
            #print(data11)
            #str1 = ''.join(data2)
            str1 = str(data11)
            data3=str1
            data3 = data3.replace('\'', '\"')
            #print ("DATA 3")
            #print(data)
            #data3 = data3.replace('\"\'', '\'')
            #data3 = data3.replace('u\'', '\'')
            #data3 = data3.replace('u\"', '\"')
            
            
            #data3 = data3.replace('\'s', '')
            #data3 = data3.replace('\"', '\'')
            #data3 = data3.replace('\",', '\',')
            

            #data3 = str1.replace('\"', '')
            #data4= data3.split();

            #removing reviewText
            #indexStart = 


            data4 = eval(data3)
            #data4 = json.loads(data3)
            #data4 = ast.literal_eval(data3)
            #print ("DATA 4")
            #print(data4)
        #print (data)
            file = open("files/yoo"+str(i)+".json", "w")
            i = i + 1
            file.write(str(data4))
            file.close() 