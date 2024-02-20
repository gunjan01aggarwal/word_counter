from string import punctuation
# Initialise count =0
ch_count=0
word_count=0
sentence_count=0

#Count character with spaces
def count_char_with_space(Data):
    total_count=len(Data)
    return print(f"Total charcter count with spaces is {total_count}.")


#count character without spaces
def count_char_without_space(Data,ch_count):
  words=Data.split()
  for word in words:
    count=len(word)
    ch_count+=count
  return print(f"Total character count without space is {ch_count}.")
   

##count  words
def count_words(Data,word_count):
   words=Data.split()
   for word in words:
      word=word.strip(punctuation)
      if "." in word:
         wordss=word.split(".")
         for w in wordss:
            if  w=="":
               continue
            word_count=word_count+1
      elif "," in word:
         Words=word.split(",") 
         for ww in Words:
            if ww=="":
               continue
            word_count=word_count+1
      elif "?" in word:
         Wordss=word.split(",") 
         for www in Wordss:
            if www=="":
               continue
            word_count=word_count+1
      elif ";" in word:
         Wordss=word.split(",") 
         for www in Wordss:
            if www=="":
               continue
            word_count=word_count+1

      else:
         word_count+=1      

   return print(f"Total word count is {word_count}")
   



#count sentences .
def count_sentences(Data,sentence_count):
   sentences=Data.split('.')
   for sentence in sentences:
    if (sentence=='')|(sentence=="  ")|(sentence=="   "):
      continue
    sentence_count+=1
   return print(f"Count the sentences is {sentence_count}")




def main():
   print("Do you want to count the characters with space? Press1")
   print("Do you want to count the characters without space? Press2")
   print("Do you want to count the words? Press3")
   print("Do you want to count the sentences? Press4")
   try:
      user_input=int(input())
      if user_input==1:
         data=input("Enter the data:\n")
         count_char_with_space(data)
      elif user_input==2:
         data=input("Enter the data\n")   
         count_char_without_space(data,ch_count) 
      elif user_input==3:
         data=input("Enter the data\n")
         count_words(data,word_count)
      else:
         data=input("Enter the data\n")
         count_sentences(data,sentence_count)   
   except:
      print("Sorry,user does not select any option.")






main()
