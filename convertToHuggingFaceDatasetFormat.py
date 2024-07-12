"""
1. Parsing data to huggingface dataset format:
 [
    {
        "bam" : "sentence1", "fr" : "sentence1Translation
    },
    
    {
        "bam" : "sentence2", "fr" : "sentence2Translation"
    }. 
    ......
 ]

2. Arguments : 

arg 1 : bambara file path
arg 2 : french file path 
arg 3 : target name 
 
"""


import json, sys, os


def argumentValidation():
    if (len(sys.argv[1:])!=3): 
        print("Usage: python convertToHuggingFaceDatasetFormat.py <bam_file_path> <fr_file_path> <target_name>")
        sys.exit(1)

    for path in sys.argv[1:-1] :
        if not os.path.isfile(path):
            print(f"{path}: file not find")
            sys.exit(1)
        
if __name__ == '__main__':
    argumentValidation()

    files_path = sys.argv[1:]

    bm       = []
    fr       = []
    pairs    = {}
    data     = []


    with open(files_path[0], "r") as file: 
        bam = list(file)
        file.close 

    with open(files_path[1], "r") as file : 
        fr = list(file)
        file.close()

    for index in range(len(bam)): 
        pairs[bam[index]] = fr[index]

    pairs = list(pairs.items())

    for pair in pairs :

        data.append({
                    "bm" : (pair[0]).replace("\n", ""),
                    "fr" : (pair[1]).replace("\n", "")
                    })
    with open(f"{files_path[2]}.json", "w") as file : 
        json.dump(data,file)
        file.close()
