import os

# Function to create an index of a folder and its subfolders
def create_index(path, depth=0):
    if depth >= 3: # stop recursion if the current depth is more than 3
        return []
    # Get all the subfolders in the current path
    subfolders = [f.name for f in os.scandir(path) if f.is_dir()]
    subfolders.sort() # sort the subfolders in alphabetical order
    index = []
    for subfolder in subfolders:
        subpath = os.path.join(path, subfolder) # create the path for the subfolder
        if depth == 0:
            index.append(subfolder) # add the subfolder name to the index
        elif depth == 1:
            index.append('  ' + subfolder) # add the subfolder name to the index
        elif depth == 2:
            index.append('    ' + subfolder) # add the subfolder name to the index
        index += create_index(subpath, depth+1) # recursively call the function for the subfolder and increase the depth by 1
    return index

# Main function
if __name__ == '__main__':
    path = input("Please enter the path of the root directory: ")
    index = create_index(path)
    # Open the file with 'w' mode to write the data
    with open(os.path.join(path, 'index.txt'), 'w') as f:
        for item in index:
            f.write(item + '\n')
    print("Index file created in the top-level folder.")
