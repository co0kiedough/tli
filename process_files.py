import csv, re
import pandas as pd
import numpy as np
import glob
import datetime
from operator import itemgetter
from operator import attrgetter
import requests

def sortrow(self, row, rownum):
    filedict = {}
    
    rowfields = ['STATEMENT_DATE','TRANSACTION_DATE','AS_OF_DATE','QUANTITY_AMOUNT','TRANSACTION_PRICE','TRANSACTION_AMOUNT','REC_TYPE_DESC','DESC_LINE1_TEXT','DESC_LINE2_TEXT','DESC_LINE3_TEXT','CMNT_LINE1_TEXT','CMNT_LINE2_TEXT','CMNT_LINE3_TEXT','INVST_PROD_ID','CUSIP_NO','CHECK_NUMBER','PAYEE_DESC','ACCRUED_INTEREST_AMOUNT','NET_COST_AMOUNT','RLZD_GNLOSS_AMOUNT','NET_PROCEEDS_AMOUNT']
    
    #code


class cleanFile:
    
    def __init__(self):
        
        self.tfiles = glob.glob('*.xl*')
        self.preserve = {}
        self.cusipre = re.compile(' {2,}\S{4,}')
        
        self.cusipf = pd.read_excel(self.tfiles[1], na_filter=False, header=0)
        self.zfile = pd.read_excel(self.tfiles[0], na_filter=False, header=0)
        self.rawfile = pd.read_excel(self.tfiles[2], na_filter=False, header=0)
        cd = {}
        zd = {}
        self.cusipd = self.cusipf.to_dict(orient='index', into=cd)
        self.zdict = self.zfile.to_dict(orient='index', into=zd)
    
    def matchdesc(self):
        
        
        for rows in self.zdict:
            if self.zdict[rows]['CUSIP_NO'] == '':
                 skip = 'this'
        else:
            cus = str(self.zdict[rows]['CUSIP_NO'])
            cusf = cus[len(str(cus))-4:]
            for row in self.cusipd:
                zcus = self.cusipd[row]['Security Description']
                zcusf = zcus[len(zcus)-4:]
                if cusf == zcusf:
                    self.zdict[rows]['Matched Description'] = zcus
                    
        headers = [*self.zdict[0].keys()]
        headers.append('Matched Description')
        ffile = open('finished.csv', 'w', newline='')
        fcsv = csv.DictWriter(ffile, headers)
        fcsv.writeheader()
        
        for rows in self.zdict:
            # try:
            #     x = self.zdict[rows]['Matched Description']
            # except Exception:
            #     self.zdict[rows]['Matched Description'] = ''
            
            fcsv.writerow(self.zdict[rows])
        
        ffile.close()
        
    
    
    def uploadfile(self):
        rf = self.rawfile
        rfd = {}
        rawd = rf.to_dict(orient='index', into=rfd)
        rawlist = []
        jand = {'cashd':{},'excr':{},'excd':{},'rop':{},'cashw':{},'int':{},'div':{},'dist':{},'mint':{},'buy':{},'sell':{}}
        febd = {'cashd':{},'excr':{},'excd':{},'rop':{},'cashw':{},'int':{},'div':{},'dist':{},'mint':{},'buy':{},'sell':{}}
        mard = {'cashd':{},'excr':{},'excd':{},'rop':{},'cashw':{},'int':{},'div':{},'dist':{},'mint':{},'buy':{},'sell':{}}
        aprd = {'cashd':{},'excr':{},'excd':{},'rop':{},'cashw':{},'int':{},'div':{},'dist':{},'mint':{},'buy':{},'sell':{}}
        mayd = {'cashd':{},'excr':{},'excd':{},'rop':{},'cashw':{},'int':{},'div':{},'dist':{},'mint':{},'buy':{},'sell':{}}
        jund = {'cashd':{},'excr':{},'excd':{},'rop':{},'cashw':{},'int':{},'div':{},'dist':{},'mint':{},'buy':{},'sell':{}}
        juld = {'cashd':{},'excr':{},'excd':{},'rop':{},'cashw':{},'int':{},'div':{},'dist':{},'mint':{},'buy':{},'sell':{}}
        augd = {'cashd':{},'excr':{},'excd':{},'rop':{},'cashw':{},'int':{},'div':{},'dist':{},'mint':{},'buy':{},'sell':{}}
        sepd = {'cashd':{},'excr':{},'excd':{},'rop':{},'cashw':{},'int':{},'div':{},'dist':{},'mint':{},'buy':{},'sell':{}}
        octd = {'cashd':{},'excr':{},'excd':{},'rop':{},'cashw':{},'int':{},'div':{},'dist':{},'mint':{},'buy':{},'sell':{}}
        novd = {'cashd':{},'excr':{},'excd':{},'rop':{},'cashw':{},'int':{},'div':{},'dist':{},'mint':{},'buy':{},'sell':{}}
        decd = {'cashd':{},'excr':{},'excd':{},'rop':{},'cashw':{},'int':{},'div':{},'dist':{},'mint':{},'buy':{},'sell':{}}
        
        months = {1:jand,2:febd,3:mard,4:aprd,5:mayd,6:jund,7:juld,8:augd,9:sepd,10:octd,11:novd,12:decd}
        finald = {}
        finall = []
        
        i=0
        mnames = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
        for rows in rawd:
            i+=1
            rawd[rows]['rownumber'] = str(i)
            rawlist.append(rawd[rows])
            
        transmonth = '0'
        infilefields = ['FIRM_ID', 'RR_CD', 'ACCOUNT_NUMBER', 'STATEMENT_DATE', 'TRANSACTION_DATE',
                        'AS_OF_DATE', 'QUANTITY_AMOUNT', 'TRANSACTION_PRICE', 'TRANSACTION_AMOUNT',
                        'REC_TYPE_DESC', 'DESC_LINE1_TEXT', 'DESC_LINE2_TEXT', 'DESC_LINE3_TEXT',
                        'CMNT_LINE1_TEXT', 'CMNT_LINE2_TEXT', 'CMNT_LINE3_TEXT', 'INVST_PROD_ID',
                        'CUSIP_NO', 'CHECK_NUMBER', 'PAYEE_DESC', 'ACCRUED_INTEREST_AMOUNT',
                        'NET_COST_AMOUNT', 'RLZD_GNLOSS_AMOUNT', 'NET_PROCEEDS_AMOUNT']
        
        outfilefields = ['JDAccount','Account','Transaction','StatementMonth','StatementYear','TransactionDate','Transaction',
                         'Inn','Out','SecurityCategory','SecurityDescription','Price','Debit','Credit','Comment',
                         'Commission','CommissionPercent','CommissionComments','HoldingPeriod','Status']
        
        fieldmap = {'Cash Withdrawals':'Cash Withdrawal', 'Cash Deposits':'Cash Deposit', 'Taxable interest':'Int', 'Tax-exempt interest':'Int', 'Regular Securities Purchase':'Buy', 'Return of principal':'Rop', 'Securities Sales':'Sell', 'Taxable dividends':'Div','Taxable capital gains distributions':'Div'}      
        
        for row in rawlist:
            t = row
            dstr = str(t['TRANSACTION_DATE'])
            sstr = str(t['STATEMENT_DATE'])
            sm = int(sstr.split('-')[1])
            sy = sstr.split('-')[0]
            inout = fieldmap[t['REC_TYPE_DESC']]
            if inout == 'Securities Sales':
                isin = '0'
                isout = int(t['QUANTITY_AMOUNT'])
                if isout < 0:
                    isout = isout * -1
                    isout = isout - int(t['ACCRUED_INTEREST_AMOUNT'])
                    isout = str(isout)
            elif inout == fieldmap[t['Regular Securities Purchase']]:
                isin = int(t['QUANTITY_AMOUNT'])
                if isin < 0:
                    isin = isin * -1
                    isin = isin - int(t['ACCRUED_INTEREST_AMOUNT'])
                    isin = str(isin)
                isout = '0'
            else:
                isin = 0
                isout = 0
                
            comment = str(t['CMNT_LINE1_TEXT']) + str(t['cCMNT_LINE2_TEXT']) + str(t['CMNT_LINE3_TEXT'])
            frow = {'Transaction':str(fieldmap[t['REC_TYPE_DESC']]),
                    'StatementMonth':mnames[sm],
                    'StatementYear':sy,
                    'Inn': isin,
                    'Out': isout,
                    'Transaction Date':dstr,
                    'Transaction':'tbd',
                    'Security Category':'tbd',
                    'Security Description':'tbd',
                    'Price':str(t['TRANSACTION_PRICE']),
                    'Debit':'tbd',
                    'Credit':'tbd',
                    'Comment':comment
                    
                    
                    
                    }
            
            dm = dstr.split('-')[1]
            curtype = row['REC_TYPE_DESC']
            
            if curtype == 'Cash Withdrawals':
                finall.append(frow)
                finald[sy][months[sm]]['cashw'][t['rownumber']] = frow
            elif curtype == 'Cash Deposits':
                finall.append(frow)
                finald[sy][months[sm]]['cashd'][t['rownumber']] = frow
            elif curtype == 'Taxable interest':
                finall.append(frow)
                finald[sy][months[sm]]['int'][t['rownumber']] = frow
            elif curtype == 'Regular Securities Purchase':
                finall.append(frow)
                finald[sy][months[sm]]['buy'][t['rownumber']] = frow
            elif curtype == 'Return of principal':
                finall.append(frow)
                finald[sy][months[sm]]['rop'][t['rownumber']] = frow
            elif curtype == 'Securities Sales':
                finall.append(frow)
                finald[sy][months[sm]]['sell'][t['rownumber']] = frow
            elif curtype == 'Tax-exempt interest':
                finall.append(frow)
                finald[sy][months[sm]]['int'][t['rownumber']] = frow
            elif curtype == 'Taxable dividends':
                finall.append(frow)
                finald[sy][months[sm]]['div'][t['rownumber']] = frow                
            elif curtype == 'Taxable capital gains distributions':
                finall.append(frow)
                finald[sy][months[sm]]['dist'][t['rownumber']] = frow
            else:
                finall.append(frow)
                finald[sy][months[sm]]['missingtype'][t['rownumber']] = frow 
            


            
            
                

        infilefields = ['FIRM_ID', 'RR_CD', 'ACCOUNT_NUMBER', 'STATEMENT_DATE', 'TRANSACTION_DATE', 'AS_OF_DATE', 'QUANTITY_AMOUNT', 'TRANSACTION_PRICE', 'TRANSACTION_AMOUNT', 'REC_TYPE_DESC', 'DESC_LINE1_TEXT', 'DESC_LINE2_TEXT', 'DESC_LINE3_TEXT', 'CMNT_LINE1_TEXT', 'CMNT_LINE2_TEXT', 'CMNT_LINE3_TEXT', 'INVST_PROD_ID', 'CUSIP_NO', 'CHECK_NUMBER', 'PAYEE_DESC', 'ACCRUED_INTEREST_AMOUNT', 'NET_COST_AMOUNT', 'RLZD_GNLOSS_AMOUNT', 'NET_PROCEEDS_AMOUNT']
        outfilefields = ['JDAccount','Account','Transaction','StatementMonth','StatementYear','TransactionDate','Transaction','Inn','Out','SecurityCategory','SecurityDescription','Price','Debit','Credit','Comment','Commission','CommissionPercent','CommissionComments','HoldingPeriod','Status']
        
        
        
        
        
        
        
    #code
