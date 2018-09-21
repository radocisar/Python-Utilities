import gzip
import shutil
import os

for files in os.listdir(r"C:\Raw_Data\Raw_1_sec_Bar_Data\US_Stocks\GOOGL\\"):
    file_in = open(r"C:\Raw_Data\Raw_1_sec_Bar_Data\US_Stocks\GOOGL\{}".format(files),"rb")
    file_out = gzip.open(r"C:\Raw_Data\Raw_1_sec_Bar_Data\US_Stocks\GOOGL\{}.gz".format(files),"wb")
    shutil.copyfileobj(file_in,file_out)
    file_in.close()
    file_out.close()
    os.remove(r"C:\Raw_Data\Raw_1_sec_Bar_Data\US_Stocks\GOOGL\{}".format(files))
