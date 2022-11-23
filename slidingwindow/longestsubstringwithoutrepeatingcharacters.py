class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #using the array to store all the ascii values
        harray=[False] *128
        maximum = 0

        start = 0
        for end in range(len(s)):
            #storing the ascii value at each index of the array
            if harray[ord(s[end])] == False:
                #if the array is false change it to true
                harray[ord(s[end])] = True
                maximum = max(maximum,end-start+1)

            else: # if end ch in hashset
                while s[start]!=s[end]:
                    #if the array is true then change it to false and return the maximum by incrementing the sequence
                    harray[ord(s[start])]=False
                    start+=1
                start+=1

        return maximum
        
        