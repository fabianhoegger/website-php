import re
import numpy
def Average(lst):
    return sum(lst) / len(lst)

ip_list=[]
with open("2021_logs_3.gsd") as f :
    try:
        for line in f:
            string=line.split(" - - ")
            ip_list.append(string[0])
    except:
        print("ERROR==D")
x=numpy.array(ip_list)
ip,counts=numpy.unique(x,return_counts=True)
ip=list(ip)
counts=list(counts)
print("Total number of visitors (unique ips)",len(ip))
print("Average number of requests per visitor",Average(counts))
"""
2021
Jan 6 to jan 25
671 visitors,average requests 8
"""
"""
2020
may1 - jan6 2021
Total number of visitors (unique ips) 5599
Average number of requests per visitor 13.283264868726558
"""
"""
2019 2020
jul 27 - may 1 2020
Total number of visitors (unique ips) 6123
Average number of requests per visitor 11.883390494855464
"""
"""
2019
jan 6 to jul26
Total number of visitors (unique ips) 5535
Average number of requests per visitor 12.5497741644083

"""
