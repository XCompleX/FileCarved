import os
import pandas as pd
import sys

if not(os.path.exists("answer")):
    os.mkdir("answer")
else:
    for f in os.listdir("answer"):
        os.remove(os.path.join("answer", f))

if __name__ == "__main__":
    data = pd.read_excel(sys.argv[2])
    data.dropna(axis=1, inplace=True)

    with open(sys.argv[1], "rb") as f:
        for row in data.iterrows():
            startSector = int(row[1][2].replace(",",""))
            finishSector = int(row[1][3].replace(",",""))
            fileName = row[1][0]
            if not("Fill" in fileName):
                newFileName = fileName.split(" ")[0]                

                fn = None
                if (os.path.exists("answer/"+newFileName)):
                    fn = open("answer/"+newFileName, 'ab')
                else:
                    fn = open("answer/"+newFileName, "wb")
                fn.write(f.read((finishSector-startSector+1)*512))
                fn.close()
            else:
                f.read((finishSector-startSector+1)*512)