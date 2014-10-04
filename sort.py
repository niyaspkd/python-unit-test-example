class ElementTypeError(Exception):pass
class TypeError(Exception):pass
def sort(l):
	if type(l) != list: raise TypeError,"Input must be list"
	for i in l:
		if type(i) != int: raise ElementTypeError,"Invalid list element"
	for i in range(len(l)):
		for j in range(i,len(l)):
			if l[i]>l[j]:
				l[i],l[j]=l[j],l[i]
	return l

