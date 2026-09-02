# Entrada de dados: Coleta dos preços dos produtos
banana = float(input("Preço da banana: "))
maca = float(input("Preço da maçã: "))
uva = float(input("Preço da uva: "))
caju = float(input("Preço do caju: "))
morango = float(input("Preço do morango: "))
goiaba = float(input("Preço da goiaba: "))
laranja = float(input("Preço da laranja: "))
peixe = float(input("Preço do peixe: "))
arroz = float(input("Preço do arroz: "))
feijao = float(input("Preço do feijão: "))
oleo = float(input("Preço do óleo: "))

# Processamento: Cálculo da média dos 11 itens
media = (banana + maca + uva + caju + morango + goiaba + laranja + peixe + arroz + feijao + oleo) / 11

# Saída de dados: Tomada de decisão e exibição formatada (f-string)
if media >= 200:
    print(f"A média foi R$ {media:.2f} e a compra está cara!")
elif media >= 120:
    print(f"A média foi R$ {media:.2f} e a compra está comprável.")
else:
    print(f"A média foi R$ {media:.2f} e a compra está barata!")