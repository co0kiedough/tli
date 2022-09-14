import csv, glob, FuzzyWuzzy, re
import  MySQLdb
import MySQLdb.cursor
from pathlib import Path
from thefuzz import fuzz
from thefuzz import process



class assembleData:
    
    def __init__(self):
        csvs = [os.path.join(Path('bf').resolve(), i.name) for i in Path('bf').glob('**/*.csv')]
        cfiles = [os.path.join(Path('bf').resolve(), i.name) for i in Path('bf').glob('**/*.*') if os.path.join(Path('bf').resolve(), i.name) not in csvs]
        fcsvs = glob.glob('bf/**/*.csv', recursive = True)
        ffiles = glob.glob('bf/**/*.*', recursive = True)
        ffiles = [f for f in ffiles if f not in fcsvs]
        
        
        self.csvs = [os.path.join(Path('bf'), i.name) for i in Path('bf').rglob('**/**/*.csv')]
        self.noncsvs = [os.path.join(Path('bf'), i.name) for i in Path('bf').rglob('**/**/*.*') if i.name not in self.csvs]
                

        
        
        
    
    #code
