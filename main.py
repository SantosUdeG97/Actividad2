import os
import re
import random

# Replace numbers function
def replaceNumbers(filePath):
    # Opening the file in read mode.
    with open(filePath, 'r') as file:
        content = file.read()

    # Replacing numbers on file for random letters
    content = re.sub(r'(\d+)', lambda m: ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(len(m.group(1)))), content)
    # Replacing letter on file for random numbers
    content = re.sub(r'([A-Z])', lambda m: ''.join(random.choice('0123456789') for _ in range(len(m.group(1)))), content)

    # Rewriting the content on the file
    with open(filePath, 'w') as file:
        file.write(content)

# Traverse folder function
def traverseFolder(folderPath):
    # Scrolls through all files and subfolders within the folder.
    for root, dirs, files in os.walk(folderPath):
        for fileExtension in files:
            # Replaces only text files
            if fileExtension.endswith('.txt'):
                filePath = os.path.join(root, fileExtension)
                replaceNumbers(filePath)

# Indicating the path of the folder to work with
if __name__ == '__main__':
    folderPath = 'C:/Users/jlsan/Documents/CUCEI/Seminario de sistemas operativos/Practica2/data' # The path in my computer, this may be changed
    traverseFolder(folderPath)