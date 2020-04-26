
class CommonUsed(object):

    @classmethod
    def dfToArrayOfJson(self,df):
        tempArr = []
        for idx, row in df.iterrows():
            tempDict = {}
            tempInsideDict = {}
            for columnName in list(df):
                tempInsideDict[columnName] = str(row[columnName])
            tempDict[idx] = tempInsideDict
            tempArr.append(tempDict)
        return tempArr

    @classmethod
    def sthToJson(self,name,something):
        tempDict = {
            name: something
        }
        tempDict = json.dumps(tempDict) # note i gave it a different name
        loaded_r = json.loads(tempDict)
        return loaded_r

    @classmethod
    def rowToJson(self,row_df):
        tempInsideDict = {}
        for columnName in list(row_df):
            tempInsideDict[columnName] = str(row_df[columnName].iloc[0])
        return tempInsideDict

    @classmethod
    def dfToArrayOfJsonWithoutIdx(self,df):
        tempArr = []
        for idx, row in df.iterrows():
            tempInsideDict = {}
            for columnName in list(df):
                tempInsideDict[columnName] = row[columnName]
            tempArr.append(tempInsideDict)
        return tempArr