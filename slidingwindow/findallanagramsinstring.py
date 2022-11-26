#Time Complexity:: O(len(s)*len(p)) 
#Space Complexity:: O(len(s)*len(p))
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #base case if len of p is greater than s
        if len(p)>len(s):
            return []
        #empty resultant array
        result = [] 
        
        
        # create the pcount dictionary with all the character as zero
        pcount={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0} 
        # create the sscount dictionary with all the characters as zero 0
        ssCount={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0} 
        
        #frequency hashmap for every character in p
        for ch in p:
            if ch in pcount:
                # increment the ch value by 1
                pcount[ch]+=1 
            else:
                # setting the ch value by 1
                pcount[ch]=1 
    
    #intially startindex to zero
        start =0

    
    #iterate throught the lenght of p
        for end in range(len(p)): 
            #if string of end present in pcount increment sscount by one
            if s[end] in pcount:
                ssCount[s[end]]+=1
        # if pcount is equal to sscount then append the start value to the result array
        if pcount==ssCount: 
            result.append(start)


        #sliding window
        #iterate through the lenght of s from length of p
        for end in range(len(p),len(s)):
             #if string of end present in pcount increment sscount by one
            if s[end] in pcount:
                ssCount[s[end]]+=1
           #if string of start present sscount decrement sscount by one
            if s[start] in ssCount: 
                ssCount[s[start]]-=1
                #increment the start by one 
            start+=1
            # if pcount is equal to sscount the append the start value to the  result array
            if pcount==ssCount: 
                result.append(start)


        return result
        
