from factorizar import factorizar, divisores

# divisores y factorizar -> se ocupan para verificar que un numero es generador de otro

def buscar_generadores(p, limite):
	# estoy asumiendo que p es primo... quizas debo checar validar eso?
	considerar_limite = True
	if limite < 0:
		limite = 1
	elif limite == 0:
		considerar_limite = False
	generadores = []
	factores = factorizar(p - 1)
	divisor = divisores(factores)
	for i in xrange(2, p - 1):
		esgenerador = validar_generador(i, divisor, p)
		if esgenerador: # es generador i de p
			generadores.append(i)
		if considerar_limite:
			if len(generadores) == limite:
				break
	return generadores

def validar_generador(g, divisores, m): # g es generador, m es el modulo
	esgenerador =  True
	for i in xrange(1, len(divisores) - 1): # no hay que evaluar el primer y ultimo divisor
		auxiliar = pow(g, divisores[i], m)
		if auxiliar == 1: # si al menos una de las evaluaciones es igual a 1, no es generador
			esgenerador = False
			break
	return esgenerador
