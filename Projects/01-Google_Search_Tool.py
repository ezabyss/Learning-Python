# pip install google (in terminal if you haven't installed google package already)

from googlesearch import search 
print("HI THERE!!! WELCOME TO GOOGLE SEARCH TOOL")

# take users query
query = input("Please enter your query to search:  ")

# start=0  means from top 
# stop=5 : upto 5th
# it fetches the top 5 links from google
for link in search(query,start=0,stop=5): 
    print(link)
