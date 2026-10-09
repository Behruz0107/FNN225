def reverse(string:list[str])->list[str]:
	result=[]
	for i in string:
		result.append(i[::-1])
	return result
if __name__=="__main__":
	matn=input("Matnni kiriting>>> ").split()
	res=reverse(matn)
	print(res)
