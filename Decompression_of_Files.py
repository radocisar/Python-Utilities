### Needs patool installed (pip isntall patool)

import patoolib

# For a single file:
patoolib.extract_archive(r"C:\Raw_Data\Raw_1_sec_Bar_Data\US_Stocks\MSFT\MSFT_Bars_20180913.txt.gz", 
                          outdir=r"C:\Raw_Data\Raw_1_sec_Bar_Data\US_Stocks\MSFT\M\\")

# For all files in folder:
for files in os.listdir(r"C:\Raw_Data\Raw_1_sec_Bar_Data\US_Stocks\GOOGL\\"):
    #print(files)
    patoolib.extract_archive(r"C:\Raw_Data\Raw_1_sec_Bar_Data\US_Stocks\GOOGL\{}".format(files), 
                             outdir=r"C:\Raw_Data\Raw_1_sec_Bar_Data\US_Stocks\GOOGL\\")
    os.remove(r"C:\Raw_Data\Raw_1_sec_Bar_Data\US_Stocks\GOOGL\{}".format(files))
