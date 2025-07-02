import os
import shutil
from datetime import datetime
import argparse
from colorama import Fore,init,Style

#logging function 
def log(message,log_file):
    timestamp= datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open(log_file, "a",encoding="utf-8") as f:
        f.write(f"{timestamp} {message}\n")
        print(message)


#file organizer
def organize_files(source_folder,extensions,log_file):
    target_folders={
        ext:os.path.join(source_folder,ext[1:]+"_folder")
        for ext in extensions
        
    }

#create folders 
    for folder in target_folders.values():
        os.makedirs(folder,exist_ok=True)

    #tracking stats
    Moved=0
    skipped=0
    errors=0
        

##file moving 
    for filename in os.listdir(source_folder):
        file_path=os.path.join(source_folder,filename)

        if os.path.isfile(file_path):
            matched=False
            for ext in extensions:
                if filename.lower().endswith(ext):
                    matched=True
                    target_path=os.path.join(target_folders[ext],filename)
                    try:
                        shutil.move(file_path,target_path)
                        log(f"Moved {filename} -> {target_folders[ext]}",log_file)
                        Moved+=1
                    except Exception as e:
                        log(f"Failed to move {filename}: {e}",log_file)
                        errors+=1
                        break #stop checking for more extensions once matched
                if not matched:
                    skipped+=1

    print(Fore.CYAN+"Summary Statement")
    print(Fore.GREEN+f"Moved files:{Moved}")
    print(Fore.YELLOW+f"Skipped files: {skipped}")
    print(Fore.RED+f"Errors: {errors}")
    print(Style.RESET_ALL)
#Cli parser
def parse_args():
    parser=argparse.ArgumentParser(
        description="Organize files by extension into folders"
    )
    parser.add_argument(
        "--source","-s",
        required=True,
        help="Source folder to scan"

    )
    parser.add_argument(
     "--extensions","-e",
     nargs="+",
     required=True, 
     help="file extensions to move e.g(.txt,.csv,.pdf)"
    )

    parser.add_argument(
        "--logfile","-l",
        default="organizer.log",
        help="Log file name(default : organizer.log)"

    )

    return parser.parse_args()
    

# Main 
def main():
    args=parse_args()
    organize_files(args.source,args.extensions,args.logfile)

if __name__ == "__main__":
    main()
