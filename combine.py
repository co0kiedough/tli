import csv
import glob
class combine:
    
    def __init__(self):
        
        self.files = glob.glob('*heet*.csv')
        skuf = self.files[0]
        locf = self.files[1]
        
        self.skuc = csv.DictReader(open(skuf, 'r', newline=''))
        self.locc = csv.DictReader(open(locf, 'r', newline=''))
        
    def combiner(self):
        
        self.locd = {}
        i = 0
        for rows in self.locc:
            self.locd[i] = rows
            i +=1
        
        i = 0
        self.skud = {}
        for rows in self.skuc:
            self.skud[i] = rows
            i+=1
        i = 0
        self.prod = {}
        
        for rows in self.locd:
            print(self.locd[rows].keys())
            item = str(self.locd[rows]['item']).lower().strip()
            color = str(self.locd[rows]['color']).lower().strip()
            size = str(self.locd[rows]['size']).lower().strip()
            
            for row in self.skud:
                if str(self.skud[row]['Item#']).lower().strip() == str(item).lower().strip() and str(self.skud[row]['Color']).lower().strip() == str(color).lower().strip():
                    print(str(item) +' ' + color + ' ' + size)
                    print(str(self.skud[row]['ProductID']).lower())
                    if str(self.skud[row]['Size']).lower().strip() == str(size).lower().strip():
                        print(str(self.skud[row]['ProductID']).lower())
                        self.skud[row]['location'] = self.locd[rows]['location']
                    else:
                        self.skud[row]['location'] = ''
        
        outfields = ['Item#', 'Description', 'Qty', 'Color', 'Size', 'Pack/Box', 'Price', 'WAREHOUSE', 'ProductID', 'location']
        # cout = csv.DictWriter(open('location_sheets.csv', 'w', newline=''), outfields)
        # cout.writeheader()
        # for r in self.skud:
        #     # print(self.skud[rows])
        #     thisrow = self.skud[r]
        #     
        #     try:
        #         cout.writerows(thisrow)
        #     except Exception:
        #         print(thisrow)
            # cout.writerows(self.skud[r])
            
        
                    
                    
                    
                
                
            
        
        
    
    #code
