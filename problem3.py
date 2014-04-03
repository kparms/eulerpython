a=list(range(2,114))
for x in a:
	comp=[]
	for y in range(a.index(x),len(a)):
		q=x*a[y]
		if q<=max(a):
			comp.append(q)
		else:
			break
	for z in comp:
		a.remove(z)

	

for p in a:
	print(str(p) + ' mod: ' + str(13195%p))