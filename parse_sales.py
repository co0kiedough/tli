import sys, os, re, csv, pyodbc, glob
import pandas as pd
import numpy as np

class gather_sales:
    
    def __init__(self):
        self.excel_files = []
        self.csv_files = []
        self.sales_dict = {}
        self.temp_dict = {}
        self.temp_list = []
        
    def group_sales(self):
        
        the_files_xls = glob.glob("sales\*.xls")
        the_files_xlsx = glob.glob("sales\*.xlsx")
        the_files_csv = glob.glob("sales\*.csv")
        
        i=0
        if len(the_files_xls) > 0:
            xls_sales_dict = {}
            for f in the_files_xls:
                i+=1
                
                tmp_x = pd.read_excel(f, header=6)
                tmp_x_dict = tmp_x.to_dict('index')
                xls_sales_dict[f.split("\\")[1].split(".xls")[0]] = {'sales':tmp_x_dict,'dict_headers':[*tmp_x_dict[0].keys()]}

        if len(the_files_xlsx) > 0:
            # print(the_files_xlsx)
            xlsx_sales_dict = {}
            for f in the_files_xlsx:
                print(f)
                i+=1
                tmp_xx = pd.read_excel(f, header=11)
                tmp_xx_dict = tmp_xx.to_dict('index')
                xlsx_sales_dict[f.split("\\")[1].split(".xlsx")[0]] = {'sales':tmp_xx_dict,'dict_headers':[*tmp_xx_dict[0].keys()]}                
    
            return xlsx_sales_dict
        
    def add_qty(self, sales_dict):
        sd = sales_dict
        qty_dict = {}
        for f in sd:
            for sales in sd[f]:
                for orders in sd[f]['sales']:
                    sku = sd[f]['sales'][orders]['Vendor SKU']
                    prod = sd[f]['sales'][orders]['Product #']
                    if isinstance(sku, float):
                        print(orders, sku, prod)
                    else:
                        
                    
                        if len(sku) < 3:
                            sku_val = 'less than 3'
                        else:
                            if sku in qty_dict:
                                qty_dict[sku] = int(qty_dict[sku]) + int(sd[f]['sales'][orders]['Qty'])
                            else:
                                qty_dict[sku] = int(sd[f]['sales'][orders]['Qty'])
        return qty_dict
    
    def write_zulily_csv(self, qtydict):
        outf = open('zulily_sales_qty.csv', 'w', newline='')
        heads = ['SKU', 'Qty']
        outc = csv.DictWriter(outf, heads)
        outc.writeheader()
        for rows in qtydict:
            outc.writerow({'SKU':rows, 'Qty':qtydict[rows]})
            
        outf.close()
        
            
    
    
                    
                        
                
            
        
        
        
            
            
            
            
            
        
    
        
    
    
