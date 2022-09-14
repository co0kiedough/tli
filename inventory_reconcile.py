import csv, os, re, os, win32api, glob


class inv:
    
    def __init__(self):
        self.warehouseQty = 0
        self.sincescanQty = 0
        self.warehouseDict = {}
        self.sincescanDict = {}
        
    def importCsvs(self):
        w = open
        wCsv = csv.DictReader(open('wh.csv'), 'wb')
        for items in wCsv:
            
            pass
        
        
    def mergeExcel(self):
        import pandas as pd
        import numpy as ny
        import os, collections, csv
        from os.path import basename
        import glob
        import datetime.datetime
        df = []
        g = glob.glob('**/*.xlsx', recursive=True)
        g1 = g[0]
        nos = input('number of sheets? ')
        numberOfSheets = nos
        for i in range(1, numberOfSheets+1):
            data = pd.read_excel(g1, sheet_name = str(i))
            df.append(data)
            
        x = datetime.datetime.now()
        
        final = 'merged'+x.strftime("%m_%d_%Y")+'.xlsx'
        df = pd.concat(df)
        df.to_excel(final)
        print 'Process Finished'
        input('Press Return to Exit')
        
    
    def compareSheets(self):
        #update later to pass csv objects to instantiation of function
        sizes = ['king', 'queen', 'full', 'twin']
        colors = ['white', 'black', 'brown', 'blue', 'green', 'gray', 'ivory', 'silver', 'aqua', 'navy', 'red', 'camel', 'canvas', 'sand', 'burgundy', 'beige', 'sage', 'cream', 'taupe', 'sky blue', 'wine', 'charcoal', 'linen', 'mint', 'pink', 'royal blue', 'gold', 'light gray', 'ocean blue']
        
        pass
    
    def name(self, ):
        pass
    
    
    
        
        
    
    
    
    #code
