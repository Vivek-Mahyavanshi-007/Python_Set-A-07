fh=open('Output.txt','w')

word=input("Enter a word to check for palindrome :")

if(word==word[::-1]):  
      print("The letter is a palindrome")  
      fh.write("The letter " + (word) + " is a palindrome")

else:  
      print("The letter is not a palindrome")
      fh.write(f"The letter " + (word) + " not a palindrome")
fh.close()
   
