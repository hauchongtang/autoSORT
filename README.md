# autoSORT
1. scraper.py scrapes for file extensions and its categories in target url and push results as an array saved to a csv or txt file
2. filefinder.py pulls data collected and uses it to create new folders to contain sorted files. Certain extensions will be paired to sorted folders
3. watchfolder.py uses watchdog module to monitor folder path for any insertions of files and then proceeds to execute filefinder.py to sort the files. The watchdog script will run indefinitely
