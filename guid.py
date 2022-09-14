import hashlib, uuid

def createguid(fromstr=None):
    
    if fromstr == None:
        return str(uuid.uuid4())
    else:
        bstr = str.encode(fromstr)
        
        hbstr = hashlib.md5(bstr)
        
        return str((uuid.UUID(hbstr.hexdigest())))
        
