
import numpy as np
import re

def getKeysSurvey(client1):        
    key_record = []
    keys = np.array(client1.keys(),dtype=np.str)
    for x in np.nditer(keys):    #implemtn swithc for each type of records                    
        if (str(x).count(":")==2):#get all keys surveys
            key_record.append(x)        
    return np.array(key_record)

def Transform(db):#make a new Database for the records with the keys fix how is in the estudio.json              
    client1 = db.client1
    client2 = db.client2
    client3 = db.client3
    keys = getKeysSurvey(client1)
    for i in np.nditer(keys):              
        c =dict(client1.hgetall(str(i)))            
        tr = re.compile("Tr_1_")
        dr = re.compile("Dr_")
        doctor_col = list(filter(dr.match,c.keys()))   
        tr_col = list(filter(tr.match,c.keys()))
        newRecord = c.copy()
        try:
            newRecord['doctor_name'] = doctor_col[0]
            time_doctor = newRecord.get(doctor_col[0])
            newRecord['doctor_time'] = time_doctor 
            newRecord.pop(doctor_col[0])   
        
            print(i)    
            for j in range(len(tr_col)):#create a tr_1_# number ascending for each TR_1_## find
                idxkey = "Tr_1_"+str(j)
                newRecord[idxkey] = c.get(tr_col[j])
                newRecord.pop(tr_col[j])
            for items in newRecord.items():
                client2.hset(str(i),items[0],items[1])  
            print("completed")
            
        except:
            
            print("problem with this id:\t",i)
            recordProblem = c.copy()
            for items in recordProblem.items():
            
                client3.hset(str(i),items[0],items[1])  


