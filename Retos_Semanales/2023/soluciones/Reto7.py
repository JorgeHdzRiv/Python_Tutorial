"""
/*
 * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */

"""
def preguntar(pregunta, opciones):
    print(pregunta)
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")
    seleccion = int(input("Selecciona una opción (1-4): "))
    return seleccion - 1

def main():
    print("¡Bienvenido al Sombrero Seleccionador de Hogwarts!")
    print("Responde las siguientes preguntas para que el sombrero te asigne a una casa.\n")

    preguntas = [
        "\n¿Qué cualidad valoras más?\n",
        "\n¿Qué tipo de actividad disfrutas más?\n",
        "\n¿Cuál es tu enfoque principal?\n",
        "\n¿Qué animal te representa mejor?\n",
        "\n¿Cuál es tu mayor aspiración?\n"
    ]

    opciones = [
        ["Coraje", "Inteligencia", "Lealtad", "Astucia"],
        ["Deportes", "Estudiar", "Cuidar de otros", "Investigar cosas nuevas"],
        ["Lograr metas", "Aprender constantemente", "Ayudar a los demás", "Alcanzar el éxito"],
        ["León", "Serpiente", "Tejón", "Águila"],
        ["Destacar en lo que hago", "Ser respetado y reconocido", "Crear lazos fuertes", "Descubrir la verdad"]
    ]

    puntuaciones = [0, 0, 0, 0]  # Gryffindor, Slytherin, Hufflepuff, Ravenclaw

    for i in range(len(preguntas)):
        respuesta = preguntar(preguntas[i], opciones[i])
        puntuaciones[respuesta] += 1

    casa_seleccionada = puntuaciones.index(max(puntuaciones))
    casas = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]

    print("\nEl Sombrero Seleccionador ha decidido que perteneces a la casa:", casas[casa_seleccionada])

if __name__ == "__main__":
    main()
