from functools import reduce

#http://book.pythontips.com/en/latest/map_filter.html
#https://stackoverflow.com/questions/10666163/how-to-check-if-all-elements-of-a-list-matches-a-condition
#https://pyeda.readthedocs.io/en/latest/boolalg.html

#necesitamos instanciar nuestras variables globales
#en este caso van a ser los conjuntos que nos definen en la tarea
V = ["a","b"]
C = ["1", "2"]
vc = V + C
op = ["+","*","=="]
algebra = ["+","*","=", "(", ")"]
sigma = V + C + op

'''
######################################################
Pregunta 2
parte 2
######################################################
'''

# lo que se piensa cmabiar es que busque el primer numero respecto
# a una tupla, y que retorne un conjunto de tuplas encontradas

#RETURN: tupla(a,b)
def search(mat, x, pr,col=0):
	n= len(mat[0]) - 1
	i = 0 
	j = n
	arr=[]
	# se comienza en el punto (0,n-1)
	while ( i <= n and j >= col ):
		v = mat[i][j]
		if (v[0] == x):
			if pr==3:
				v[1]*=2
			arr.append(v)
		if (v[0] > x ): 
			j -= 1
		# if v[0] < x 
		else:  
			i += 1
	return arr

def binversa(mat, x, pr, col):
	n= len(mat[0]) - 1
	i = 0 
	j = col
	arr=[]
	while(i<=n and j<=n):
		fila = mat[i]
		b = all(elem[0]>x for elem in fila)
		if not b:
			bol = any(elem[0]==x for elem in fila)
			if bol:
				lista = [elem for elem in fila if elem[0]==x]
				arr+=lista
			else:
				i+=1
				if j==i:
					j+=1
		elif mat[i+1][0][0]<=x:
			i+=1
			if j==i:
				j+=1
		else:
			return arr
	return arr

# lo que se quiere cambiar es que cree una triangular superior con tuplas
# en vez de numeros
def triSup(lista):
	# crear matriz
	# Menos intuitiva pero mas eficiente
	#matriz = [None] * numero_filas
	#for i in range(numero_filas):
	#    matriz[i] = [None] * numero_columnas
	# Variación de la anterior
	m = len(lista)
	#lista = np.array(lista)
	mat = [ [[0,0]] * m for i in range(m)]
	#mat = np.array(mat)
	i=0
	j=0
	while(i<len(lista)):
		while(j<len(lista)):
			#print(mat[i][j][0])
			if i==j:
				mat[i][j]=[lista[i][0]+lista[j][0],lista[i][1]*lista[j][1]]
			else:
				mat[i][j]=[lista[i][0]+lista[j][0],lista[i][1]*lista[j][1]*2]
			j+=1
		i+=1
		j=i
	return mat

def sortSecond(val):
	return val[0]

#funcion que dadas dos listas retorna la lista de repeticiones de la lista
# va ser necesario pero con tuplas 
def union(lista1,lista2):
	# list merge without dupe
	l1 = lista1[:]
	l2 = lista2[:]
	l2.sort(key=sortSecond)
	#l1.extend([element for element in l2 if element not in l1])
	l1.extend([element for element in l2])
	#print("Union: " + str(l1))
	return l1

def agrandar(m, pr,col):
	mat = m[:]
	l1 = []
	if pr==3:
		# por cada fila de mat
		for i in range(len(mat)):
			#l1 lista que contiene los elementos de mat +3
			fila = mat[i][col:]
			#print(fila)
			j=0
			while(j<len(fila)):
				largo = fila[j][0]
				combi = fila[j][1]
				largo+=3
				combi*=2
				l1+=[[largo,combi]]
				j+=1
			if i==col:
				col+=1
	if pr==4:
		for i in range(len(mat)):
			#l1 lista que contiene los elementos de mat +4
			fila = mat[i][col:]
			j=0
			while(j<len(fila)):
				largo = fila[j][0]
				combi = fila[j][1]
				largo+=4
				l1+=[[largo,combi]]
				j+=1
			if i==col:
				col+=1
	#print(l1)
	return l1

def verificar(ls,x):
	b=any(i[-1][0]<x for i in ls)
	#print(b)
	return b

def validar(ls,x):
	#print("antes de verificar" + str(ls))
	#print("verificar: " + str([i[0] for i in ls if i[0][0]<x]))
	#print("largo de lista que viene: " + str([len(i) for i in ls if i[-1][0]<x]))
	for i in range(len(ls)):
		lista = ls[i]
		#print("esta es la lista que estamos evaluando: " + str(lista))
		v = lista[0][0]
		if v<x:
			return True
		else:pass
	return False
	#b=any(i[-1][0]<x for i in ls)
	#print(b)
	#return b

def contiene(sol):
	b=any(i!=[] for i in sol)
	#print(b)
	return b

def mayorN(mtotal,x):
	b=any(x>mt[-1][-1][0] for mt in mtotal)
	#print([mt[-1][-1][0] for mt in mtotal if x>mt[-1][-1][0]])
	return b

def supMat(mt,lar,col):
	ppal=[]
	lx=[]
	ls = lar[:]
	for j in range(len(mt)):
		#print("valor de J en sup MAT:" + str(j))
		sx1 = agrandar(mt[j],3,col)
		sx2 = union(ls[j],sx1)
		mm1 = triSup(sx2)
		lx.append(sx2)
		ppal.append(mm1)
		l1 = agrandar(mt[j],4,col)
		l2 = union(ls[j],l1)
		m2 = triSup(l2)
		lx.append(l2)
		ppal.append(m2)

	lar=lx[:]
	mt=ppal[:]
	#print("largo mat con mat in function: " + str(len(mt)))
	#print("matriz despues in function:" + str([elem[0] for elem in mt]))
	return [mt,lar]

#funcion para calcular an
def ctd(n, st,last=[[1,4],[5,4**2*2],[6,4**2*1]]):
	if n==1:
		return last[0][1]
	elif n==5:
		return last[1][1]
	elif n==6:
		return last[2][1]
	#n>1
	else:
		assert st==3 or st==4
		#tenemos dos casos para averiguar si el numero n está en la secuencia,
		#en el primer caso, hay que ver si a está en la tabla 
		if st==3:
			x=n-3
		elif st==4:
			x=n-4
		last_1 = [last[:]]
		mat1 = [triSup(last_1[0])]
		lbus1 = 1
		ncond = 1
		while(mayorN(mat1,x)):
			facc = supMat(mat1,last_1,ncond)
			ncond = min([len(m[0]) for m in mat1])
			mat1 = facc[0]
			last_1 = facc[1]
		#print("matriz antes:" + str([elem[0] for elem in mat1]))
		#print("ncond1: " + str(ncond))
		e1=[]
		for i in range(len(mat1)):
			e1+=search(mat1[i],x,st,lbus1)
		#no esta en la matriz el numero
		# si e1 esta en la matriz
		ans=0
		#print("resultadon1: " + str(e1))
		if contiene(e1):
			f=0
			ans=[]
			ans += [elem[1] for elem in e1 if elem!=[]]
			princ=len(mat1)
			lbus1=min([len(m[0]) for m in mat1])
			#lbus1 = min([len(m[0]) for m in mat1])
			#print("largo de matriz que cont matrices ANTES: " +  str(len(mat1)))
			sol1=[]
			#print(ncond)
			nuevos = [elem[ncond:] for elem in last_1]
			#print(nuevos)
			#print(verificar(nuevos,n-1))
			#print(last_1)
			f=0
			while(verificar(last_1,n-1)):
				#print(last_1)
				facc = supMat(mat1,last_1,ncond)
				ncond = min([len(m[0]) for m in mat1])
				last_1 = facc[1]
				#print("last_1" + str(last_1))
				nuevos = [elem[ncond:] for elem in last_1]
				#print("NCOND Y NUEVOS: " + str(ncond) + "__-__" + str(nuevos))
				mat1 = facc[0]
				for i in range(len(mat1)):
					solve = search(mat1[i],x,st,ncond) 
					sol1+= solve
				#ncond = min([len(m[0]) for m in mat1])
				#print(nuevos)
				princ = len(mat1)
				f+=1
				
				#print("largo de matriz que cont matrices: DPS " +  str(len(mat1[0])))
			#si la matriz de matrices crece
			#print("largo de matriz que cont matrices: " +  str(len(mat1)))
			#print("matriz despues:" + str([elem[0] for elem in mat1]))
			

					#print(sol1)
			#print(sol1)
			#por cada tupla en expresion 1, vamos a sumar la segunda componente
			if contiene(sol1):
				ans += [elem[1] for elem in sol1 if elem!=[]]
			return reduce((lambda x,y: x+y), ans)
		# no esta ni e1 ni e2
		else:
			return ans

'''
######################################################
Pregunta 2
parte 3
######################################################
'''
class Tree:
	def __init__(self,data=None, left=None, right=None):
		self.data=data
		self.left=left
		self.right=right

def toLista(st):
	L = []
	char=0
	while(char<len(st)):
		if st[char]=="=":
			L.append(st[char]+st[char+1])
			char+=2
		else:
			L.append(st[char])
			char+=1
	return L

s1 = "((a==b)+1)"
l1=["(", "(", "a", "==", "b", ")", "+", "1", ")"]
assert toLista(s1)==l1

#print(toLista(s1))
#print(l1)

# ver si el nodo esta en V o C
def enNum(st):
	assert type(st)==str
	if st in vc: return True
	else: return False
# ver si el nodo es un operador valido
def enOp(st):
	assert type(st)==str
	if st in op: return True
	else: return False

def isTree(arbol):
	assert (isinstance(arbol,Tree))
	if enNum(arbol.data): return True
	elif enOp(arbol.data):
		izq = isTree(arbol.left)
		der = isTree(arbol.right)
		return  izq and der
	else: return False

def repet(st):
	if "(" in st:
		s1 = len(list(filter(lambda x: x=="(", st)))
		s2 = len(list(filter(lambda x: x==")", st)))
		if s1==s2:
			return True
		else:
			return False
	else:
		return False


#CASOS
#(a+(a+b))
#((a+b)+a)
def constructor(st):		
	# Vamos a contar el numero de parentesis que hay para 
	# analizar la profundidad de la expresion dada
	t = Tree("false")
	if len(st)==1:
		if enNum(st):
			t.data = st
			return t
		return t
	else:
		lista = toLista(st)
		# si tiene parentesis, debe tener misma cantidad de "(" como de ")"
		if repet(st):
			# debe tener los operadores binarios
			if "+" or "*" or "==" in lista:
				# una lista de largo 5 tiene grandes oportunidades de ser exp
				if len(lista)==5:
					t.data = lista[2]
					t.left = constructor(lista[1])
					t.right = constructor(lista[3])
				# len(lista) > 5
				elif 5<len(lista):
					lvl = 0
					j=0
					i=1
					while(i<len(lista)-1):
						#si es el primero y es un elemento de V union C
						if i==1 and enNum(lista[i]):
							# El siguiente debe ser un operador, si no lo es
							# isTree lo va a revelar
							j=i+1
							t.data = lista[j]
							#print(t.data)
							t.left = constructor(st[1])
							#print(t.left.data)
							st2 = "".join(lista[j+1:len(lista)-1])
							#print(st2)
							t.right = constructor(st2)
							return t
						if lista[i]=="(":
							lvl+=1
						elif lista[i]==")":
							lvl-=1
							if lvl==0:
								j=i+1
								t.data = lista[j]
								#print(t.data)
								st1 = "".join(lista[1:j])
								#print(st1)
								t.left = constructor(st1)
								st2 = "".join(lista[j+1:len(lista)-1])
								#print(st2)
								t.right = constructor(st2)
								#print(t.left)
								return t
						i+=1
					return t
				return t
			else: return t
		else: return t

def esExp(s):
	t = constructor(s)
	b = isTree(t)
	return b

def cantidad(c):
	if c in [1,5,6]:
		return ctd(c,3)
	else:
		return ctd(c,3) + ctd(c,4)

'''
######################################################
Pregunta 2
parte 4
######################################################
'''

def printAns():
	s = input()
	lar = len(s)
	b = esExp(s)
	if b:
		c = cantidad(lar)
		print("1 " + str(c))
	else:
		c = cantidad(lar)
		print("0 " + str(c))

def ppt():
	s = input()
	c = int(s)
	if c in [1,5,6]:
		print(ctd(c,3))
	else:
		print(ctd(c,3) + ctd(c,4))

if __name__ == "__main__":
	printAns()
	#ppt()