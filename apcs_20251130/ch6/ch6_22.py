def readCsv(csvName):
    result = []
    try:
        with open(csvName,"r") as f:
            line = f.readline()
            while line:
                #print(line)
               dataList = line.split(",")
               dataList = list(map(lambda v:v.replace('"',""),dataList)) 
               result.append(dataList)
               line = f.readline()
        return  result      
    except Exception as ex:
        print(ex)
    
csvList =  readCsv("data2.csv")
for csvData in csvList:
    print(csvData)
