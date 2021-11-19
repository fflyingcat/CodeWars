def ips_between(start, end):
    startIP = start.split('.')
    endIP = end.split('.')
    count = (int(endIP[0])-int(startIP[0])) * pow(256,3)
    count += ((int(endIP[1]) - int(startIP[1])) * pow(256,2) if int(endIP[1]) >= int(startIP[1]) else (int(endIP[1]) - int(startIP[1])) * 256*256)
    count += ((int(endIP[2]) - int(startIP[2])) * 256 if int(endIP[2]) >= int(startIP[2]) else (int(endIP[2]) - int(startIP[2])) * 256)
    count += (int(endIP[3]) - int(startIP[3]) if int(endIP[2]) >= int(startIP[2]) else (int(endIP[3]) - int(startIP[3])))
    return count
#https://www.codewars.com/kata/526989a41034285187000de4