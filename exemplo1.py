class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Bistrô'  # Corrigido para 'Bistrô'
restaurante_praca.categoria = 'Italiana'  # Corrigido para 'Italiana'

if restaurante_praca.ativo:
    print('Restaurante ativo!')
else:
    print('Restaurante inativo!')

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'  # Adicionei um nome para a nova instância
restaurante_pizza.categoria = 'Fast Food'
restaurante_praca.ativo = True

print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')
