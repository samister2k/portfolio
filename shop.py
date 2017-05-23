bag = ["ipad", "copies"]
print ("welcome to school")
print ("you need to buy a keyword journal for 1.50")
print ("this is what you have in your bag so far")
print (bag)


buy_choice=input("this is what is what you can get in the shop: keyword journal, copy, apple pen")

if buy_choice== "keyword journal":
	print("that will be €1.50")
	bag.append("keyword journal")
	print("Great choice. Thanks for shopping with us!. Let's see what's in your bag now..")
	print (bag) 
		
		
		
elif buy_choice== "copy":
	print("that will be 50c")
	bag.append("copy")
	print("Great choice. Thanks for shopping with us!. Let's see what's in your bag now..")
	print (bag)         
	
	
elif buy_choice== "apple pen":
	print("that will be €15")
	bag.append("apple pen")
	

else:
	print("We don't sell eh... "+ buy_choice + ", sorry!")
	

	'''welcome to school
you need to buy a keyword journal for 1.50
this is what you have in your bag so far
['ipad', 'copies']
this is what is what you can get in the shop: keyword journal, copy, apple penkeyword journal
that will be €1.50
Great choice. Thanks for shopping with us!. Let's see what's in your bag now..
['ipad', 'copies', 'keyword journal']'''
