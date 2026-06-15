import os
import time

while True:
    print('File Metadata Viewer.')

    choice = input('1.Print File Metadata\n2.Exit\nChoice: ').strip()

    if choice == '1':
        filename = input('Enter Filename: ')
        try:
            with open(filename, 'r') as file:
                data = file.read()

                filesize = os.path.getsize(filename)
                absolute_path = os.path.abspath(filename)
                file_extention = os.path.splitext(filename)
                created = os.path.getctime(filename)
                modified = os.path.getmtime(filename)
                accessed = os.path.getatime(filename)

                print(f'Filename:{filename} ')
                print(f'Filesize:{filesize} ')
                print(f'Absolute path:{absolute_path} ')
                print(f'Extension:{file_extention[1]}')
                print(f'Created:{time.ctime(created)} ')
                print(f'Modified:{time.ctime(modified)} ')
                print(f'Accessed:{time.ctime(accessed)} ')
                print('')

        except FileNotFoundError:
            print('File do not exist.\n')

    elif choice == '2':
        print('Program Closed.')
        break
    else:
        print('Invalid choice.\n')