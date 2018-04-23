#Zip file backup
import zipfile
import os
import shutil

def backupToZip(folder):
    #Backup Entire contents of "folder" into a zip file
    folder = os.path.abspath(folder) #ensures folder is absolute path

    #Finds what number backup to assign to the zip file
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '-' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    #Create the zipfile
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename,'w')

    #Walk the 'folder' and compress the files in each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)
        #Add all the files in this folder
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue   # don't backup the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')
        
backupToZip('C:\\Users\\jackc\\Documents')
