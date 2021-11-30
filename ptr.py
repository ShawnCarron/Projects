def getPTR(ip):
    """Takes an IP and converts it to its reversed form to insert into DNS as a PTR"""
    
    ipSplit = ip.split(".")
    oct1, oct2, oct3, oct4  = list(reversed(ipSplit))
    return(f"{oct1}.{oct2}.{oct3}.{oct4}.in-addr.arpa")
