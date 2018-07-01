import pandas as pd
from app.config import  app_config
import random
import os.path

class CsvHelper:
    def __init__(self):
        self.datas = pd.DataFrame(columns=[app_config.ID_COLUME,
                                           app_config.CITY_COLUMN,
                                           app_config.NAME_COLUMN,
                                           app_config.AGE_COLUMN])
        self.datas[[app_config.ID_COLUME, app_config.AGE_COLUMN]] =\
            self.datas[[app_config.ID_COLUME, app_config.AGE_COLUMN]].astype(int)
    def AutomateTestDataGeneration(self,file):
        for index in range(app_config.NUMBER_OF_ROWS):
            self.datas.loc[index] = [index * 100 + index,
                                     app_config.CAPITALS[random.randint(0,len(app_config.CAPITALS ) -1)],
                                     app_config.NAMES[random.randint(0,len(app_config.NAMES) - 1)],
                                     random.randint(app_config.MIN_AGE,app_config.MAX_AGE)]
        self.datas.to_csv(file, index=False)
    def IsFileExist(self,sourceFile):
        if os.path.isfile(sourceFile):
            return True
        return  False
    def ReadingDataFromFile(self,sourceFile,specificColumns):
        return pd.read_csv(sourceFile, skipinitialspace=True, usecols=specificColumns)

    def SavingDataToFile(self,datas,desFile):
        datas.to_csv(desFile, index=False)
