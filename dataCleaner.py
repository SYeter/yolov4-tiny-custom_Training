import os
import shutil

folderdir = "../augmented_jpg_data/obj_raw"
destination_folder = "../augmented_jpg_data/obj"

isFolderExists = os.path.exists(folderdir)


if isFolderExists:
    dirs = os.listdir(folderdir)
    for i in dirs:
        print("i",i)
        if i.endswith(".txt") and str(i.split(".txt")[0]) != "classes":
            print("aaaaa :",str(i.split(".txt")[0]))
            txt = i
            jpg = str(i.split(".txt")[0]) + ".jpg"
            png = str(i.split(".txt")[0]) + ".png"
            jpeg = str(i.split(".txt")[0]) + ".jpeg"
            try:
                shutil.move(folderdir + "/" + jpg, destination_folder)
                shutil.move(folderdir + "/" + txt, destination_folder)

            except:
                try:
                    shutil.move(folderdir + "/" + png, destination_folder)
                    shutil.move(folderdir + "/" + txt, destination_folder)
                except:
                    shutil.move(folderdir + "/" + jpeg, destination_folder)
                    shutil.move(folderdir + "/" + txt, destination_folder)

    print("DONE")

else:
    print("Folder path doesnt exists")