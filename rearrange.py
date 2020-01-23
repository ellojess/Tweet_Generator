import sys as sys 

#get the command line arguments with sys 
if __name__ == "__main__":
    args = sys.argv
    words = args[1:] #start with 1 to ignore first index 0
    print(words)