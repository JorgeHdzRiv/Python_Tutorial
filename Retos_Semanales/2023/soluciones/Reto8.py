"""
/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */
"""

# Solución:
#   - Se utiliza el método de los cuadrados medios para generar números pseudoaleatorios.

#https://es.wikibooks.org/wiki/M%C3%A9todo_de_los_cuadrados_medios_para_la_generaci%C3%B3n_de_n%C3%BAmeros_pseudoaleatorios

# Descripcion del metodo de los cuadrados medios
#   - Se toma un numero de 4 digitos (semilla) y se eleva al cuadrado dando como resultado x0.
#   - Se toman los 4 digitos centrales del resultado y se toma como el nuevo numero pseudoaleatorio.
#   - Se repite el proceso n veces.

class CuadradosMedios:
    def __init__(self,semilla,n):
        self.semilla = semilla
        self.n = n
        self.num = semilla
    
    def generar(self):
        x0 = self.semilla ** 2
        x0_str = str(x0)
        x0_str = x0_str.zfill(2 * self.n)
        mitad = len(x0_str) // 4
        self.semilla = int(x0_str[mitad:3 * mitad])
        return self.semilla
    
# Parámetros del generador (puedes ajustar estos valores)
semilla_inicial = 4230
n = 4

# Crear el generador
generador = CuadradosMedios(semilla_inicial, n)


# Generar números pseudoaleatorios entre 0 y 100
numero_pseudoaleatorio = generador.generar() % 101
print(f"El numero aleatorio es: {numero_pseudoaleatorio}")

        
        



