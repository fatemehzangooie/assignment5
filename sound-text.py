text=input ("write your marked letter or word= ")
list_text=[]
list_sound=['o','i','u','a','e','O','I','U','A','E']
for letter in text:
    list_text.append(text)
    
for i in range (len(list_text)):
    
    if list_text[i] in list_sound:
        list_text[i]='what?'
        print(" ".join(text))    