#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.
import zipfile, os
def backupToZip(folder):
    folder = os.path.abspath('C:\\Users\\username\\Practice-Python')
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        backupZip.write(foldername)
    for filename in filenames:
        newBase / os.path.basename(folder) + '_'
        if filename.startswith(newBase) and filename.endswith('.zip'):
            continue
        backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')
backupToZip('C:\\Users\\username\\Python-backup')