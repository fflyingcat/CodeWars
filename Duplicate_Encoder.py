def duplicate_encode(word):
    n = (len(word))
    str = ""
    word = word.lower()
    for i in range(0,n):
        if(word.find(word[i],0,n)==word.rfind(word[i],0,n)):
            str+="("
        else:
            str+=")"
    return str
#https://www.codewars.com/kata/54b42f9314d9229fd6000d9c