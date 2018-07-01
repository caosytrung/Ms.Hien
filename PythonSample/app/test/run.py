from  app.helper.csv_helper import  CsvHelper
from  app.config import  app_config
from Tkinter import  *

def callback():
    master.destroy()

master = Tk()
master.maxsize(300,100)
master.minsize(300,100)
w = master.winfo_screenwidth()
h = master.winfo_screenheight()
size = tuple(int(pos) for pos in master.geometry().split('+')[0].split('x'))
x = w/2 - 300/2
y = h/2 - 100/2
master.geometry("%dx%d+%d+%d" % (size + (x, y)))

btn_text = StringVar()
loadingButton = Button(master,textvariable = btn_text, height=100, width=100)
loadingButton.pack()
doneButton = Button(master,text = 'Done', command=callback, height=100, width=100)


def ShowDoneDialog():

   loadingButton.text= 'a'

csvHelper = CsvHelper()

if not csvHelper.IsFileExist(app_config.SOURCE_DATA):
    csvHelper.AutomateTestDataGeneration(app_config.SOURCE_DATA)

specificColumnsToRead = [app_config.CITY_COLUMN,app_config.AGE_COLUMN]
sourceDatas = csvHelper.ReadingDataFromFile(app_config.SOURCE_DATA,specificColumnsToRead)

targetDatas = sourceDatas.groupby([app_config.CITY_COLUMN]).mean().reset_index([app_config.CITY_COLUMN])
targetDatas = targetDatas.rename(columns={app_config.AGE_COLUMN:  app_config.AVERAGE_AGE})
csvHelper.SavingDataToFile(targetDatas,app_config.DES_DATA)
print(targetDatas)

btn_text.set("Done")
master.mainloop()
print(targetDatas)




