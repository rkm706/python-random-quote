import random
def primary(): 
# Open quotes file and readlines into quotes array
    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()
    last = 18

# Print 2 random quotes
# The quotes file already has a newline so adding the "end" in print prevents print from inserting extra newline \n
    tmp = random.sample(quotes,2)
    for i in tmp:
      print(i,end="")

if __name__== "__main__":
  primary()