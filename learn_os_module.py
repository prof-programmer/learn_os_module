import os
import csv
import shutil
from csv import reader

cwd = os.getcwd()
new_accounts = ''
banned_accounts = ''
ready_accounts = 'files'
session_reauth_accounts = ''


# TODO session fayllarni izlash

path = 'files'  # izlash papkasi
session_files = []
for rootdir, dirs, files in os.walk(path):
    for file in files:
        if (file.split('.')[-1]) == 'session':  # session formatdagi fayl topilsa
            # print (os.path.join(rootdir, file))       # bu qator papka adresi va faylni nomini qaytaradi
            print(os.path.join(file).split('.')[0])  # faylni formatini yashirib fayl nomini qaytaradi
            session_files.append(os.path.join(file).split('.')[0])
print(session_files)

# TODO session fayllarni csv faylga royxatini kiritish
# https://www.pythontutorial.net/python-basics/python-write-csv-file/
# https://www.geeksforgeeks.org/writing-data-from-a-python-list-to-csv-row-wise/


def write_to_csv(list_of_accounts):
    with open('accounts.csv', 'w') as f:
        # writer = csv.writer(f)
        for account in list_of_accounts:
            # write the data
            f.write(account, "\n")


# print(write_to_csv(session_files))

# TODO session fayllarni boshqa papkaga ko'chirish
# https://www.learndatasci.com/solutions/python-move-file/
# https://datagy.io/python-move-file/
# https://pynative.com/python-delete-files-and-directories/#h-remove-file-using-os-unlink-method

# def move_files(accounts_to_move, destination_directory):

# accounts_to_move = accounts_to_move
destination_directory = 'D:/GitHubRepos/os_module/banned_accounts/'
with open('accounts.csv', 'r') as f:
    # for file in os.listdir(f'{path}{f}'):
    #     file_path = os.path.join(dir, file)
    #     shutil.move(file_path, destination_directory)
    for file in f:
        print(file)

# TODO yangi csv fayl yaratish
