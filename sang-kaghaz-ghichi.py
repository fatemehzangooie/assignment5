
import random
counter = 0
counter_1 = 0
counter_2=  0

for i in range(5):
    tedad_nafarat = input('1 person or 2 person?  :  ')
    
    if tedad_nafarat =='1'or tedad_nafarat =='2':

        break
    
    else:
        print('tedad nafarat eshtbah ast!!')
        continue



for i in range(5):
    
    tedad_bazi =  input('chand bar makhhid bazi konid :  1 or 3 or 5 :  ')

    if tedad_bazi =='1'or tedad_bazi =='3' or tedad_bazi =='5':
        
        tedad_bazi = int(tedad_bazi)
        break
    
    else:
        
        print('tedad bazi ra eshtbah vared kardid!!')
        continue



if  tedad_nafarat == '1' :
    
    while  counter < tedad_bazi :
    
        bazi_karbar = input('which one?! \n1.sang\n2.kaghaz \n3. ghichi\n')

        bazi_computer = random.randint( 1, 4)
    
               
        if bazi_karbar == '1' or 'sang':
            
            bazi_karbar= 1
        
            
        elif bazi_karbar == '2' or 'kaghaz':
            
            bazi_karbar= 2
            
        elif bazi_karbar == '3' or 'ghichi':
            
            bazi_karbar= 3
            
        else :
            
            print ('sorry! try again!!')
            
            counter -=1
            continue
            

        if bazi_karbar == bazi_computer :
            
            print ('mosavi ')
            
            counter -=1
        
        elif bazi_karbar== 1  and bazi_computer== 3  :
            
            counter_1+=1
            print ( 'bordi!!') 
             
        elif bazi_karbar== 2 and  bazi_computer== 1 :    
        
            counter_1+=1
            print ( 'bordi!!')
                         
        elif bazi_karbar== 3 and  bazi_computer== 2 : 
            counter_1+=1
            print ( 'bordi!!')
            
        elif (bazi_computer== 2 and bazi_karbar== 1):
            
            counter_2+=1
            print ( 'bahkti!!') 
             
        elif (bazi_computer== 3 and bazi_karbar== 2) :    
            
            counter_2+=1
            print ( 'baghyi!!')
                         
        elif (bazi_computer==1 and bazi_karbar== 3) : 
            counter_2+=1
            print ( 'bakhti!!')
            
        print('natije bazi \nshma:',counter_1,'\tcomputer :' ,counter_2)
            
        if counter == tedad_bazi-1:
            
            if counter_1 > counter_2:
                
                print('congragulation! you won!')
                
            else:
                
                if counter_1 != counter_2:
                
                   print('you lost!')
                
        counter +=1 
        

        
elif  tedad_nafarat == '2' :
    
     
    while  counter < tedad_bazi :
    
        for i in range(5):
    
          bazi_karbar_1 = input(' nafar 1 which one?! \n1.sang\n2.kaghaz \n3. ghichi\n')

          if bazi_karbar_1 =='1' :
              bazi_karbar_1 = int(bazi_karbar_1)
              break
    
          else:
        
             print('sorry! try again!!')
             
         
         
        for i in range(5):
    
          bazi_karbar_2 = input(' nafar 2 which one?! \n1.sang\n2.kaghaz \n3. ghichi\n')

          if bazi_karbar_2 =='1' or  bazi_karbar_2 =='2'  or  bazi_karbar_2 =='3':
        
             bazi_karbar_2 = int(bazi_karbar_2)
             break
    
          else:
             print('sorry! try again!!')
             
             continue

        
        if bazi_karbar_1 == bazi_karbar_2 :
            
            print ('mosavi ')
            
            counter -=1
        
        elif bazi_karbar_1== 1  and bazi_karbar_2== 3  :
            
            counter_1 +=1
            print ( ' (1) bordi!!') 
             
        elif bazi_karbar_1== 2 and  bazi_karbar_2== 1 :    
        
            counter_1 +=1
            print ( '(1) bordi!!')
                         
        elif bazi_karbar_1== 3 and  bazi_karbar_2== 2 : 
            counter_1 +=1
            print ( ' )(1) bordi!!')
            
        elif (bazi_karbar_2== 2 and bazi_karbar_1== 1):
            
            counter_2 +=1
            print (' (1) bordi!!') 
             
        elif (bazi_karbar_2== 3 and bazi_karbar_1== 2) :    
            
            counter_2 +=1
            print (' (2) bordi!!')
                         
        elif (bazi_karbar_2==1 and bazi_karbar_1== 3) :
             
            counter_2 +=1
            print (' (2) bordi!!')
            
        print('natije bazi: \nnafar 1:',counter_1,'\tnafar 2 :' ,counter_2)
            
        if counter == tedad_bazi-1:
            
            if counter_1 > counter_2:
                
                print('(1) you won! ')
                
            else:
                
                print('(2) you won! ')
                
        counter +=1    
     