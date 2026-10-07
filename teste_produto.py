from produto import Produto

p1 = Produto()

p1.nome = "Brilhantte"
p1.codigo = 123456
p1.preco = 12.50
p1.tipo = "Sabão em pó"
p1.quantidade = 250

p2 = Produto()
p2.nome = "Omo"
p2.codigo = 123456
p2.preco = 12.50
p2.tipo = "Sabão em pó"
p2.quantidade = 250

print(p1.listar_produtos())
print(p2.listar_produtos())