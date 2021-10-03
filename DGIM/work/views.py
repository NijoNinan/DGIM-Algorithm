# dgim logic


l = ""
storage = []
index = -1



class Bucket:
	
	def __init__(self , index):
		self.size = 1
		self.time = index+1
		self.startIndex = self.endIndex = index
		self.value = "1"

	def __str__(self):
		global l
		res = [self.size, self.value]
		return str(res)


	# combining logic
	def combine(self,b):
		self.size += b.size
		self.time = b.time
		self.endIndex = b.endIndex
		self.value = l[self.startIndex:self.endIndex+1]


# this function is called to check whether there is more that 2 buckets of same size
# if there is it will combine
def reshape():
	global storage
	
	# if only 2 elements are there
	if len(storage)<3:
		return

	
	# if 3 buckets have same size 
	if storage[-1].size == storage[-2].size and storage[-2].size == storage[-3].size:

		# if true then combine the 2nd last and 3rd last element

		# last element
		a = storage.pop()

		# 2nd last element
		b = storage.pop()

		# combining 2nd last element with 3rd last element
		storage[-1].combine(b)

		# checking again
		reshape()

		# append the last element back
		storage.append(a)




# ===========================================================================

# main views part

from django.shortcuts import render,redirect


def home(request):
	global storage

	context = {}
	context["l"] = l
	context["storage"] = storage
	return render(request, "home.html",context)


def button0(request):
	global l, index
	l += "0"
	index += 1
	return redirect(home)



def button1(request):
	global l, storage, index
	l += "1"
	index += 1
	storage.append( Bucket(index) )
	reshape()
	return redirect(home)
