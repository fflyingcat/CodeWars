def queue_time(customers, n):
    tills = [0]*n
    for i in customers:
      tills[0] += i
      tills.sort()
    return max(tills)
#https://www.codewars.com/kata/57b06f90e298a7b53d000a86