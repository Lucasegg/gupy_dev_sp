def inverter_string(string):
  # Primeiro, criamos uma lista com cada caractere da string
  lista_caracteres = list(string)
  # Em seguida, inverte a lista usando slicing
  lista_caracteres_invertida = lista_caracteres[::-1]
  # Finalmente, juntamos todos os caracteres da lista invertida em uma nova string
  string_invertida = "".join(lista_caracteres_invertida)
  # Retornamos a string invertida
  return string_invertida

# Testamos a função com algumas strings
print(inverter_string("oi")) # deve imprimir "io"
print(inverter_string("bom dia")) # deve imprimir "aid mob"
print(inverter_string("Python")) # deve imprimir "nohtyP"
