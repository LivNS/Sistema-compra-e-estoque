# RM 97819 - Lívia Namba Seraphim 
# RM 98384 - Victor Maciel
# RM 550412 - Débora Amaral

# Sistema para controle de compras e estoque 

# Menu Principal
print("***Bem-vindo(a) à Vinheria Agnello!!***")
print("1 - Comprar produtos")
print("2 - Ver estoque")
print("3 - Cadastro para Pessoa Jurídica")
print("0 - Sair")

# Produtos do estoque
estoque = {
    "Fasano Brunello di Montalcino 2017": {"quantidade": 5, "preco": 899.00},
    "Casa Ferreirinha Vinha Grande Douro Tinto 2019": {"quantidade": 45, "preco": 189.90},
    "Vinho Canção Tinto Suave 750": {"quantidade": 20, "preco": 20.00},
    "Casa Santos Lima Confidencial Branco 2019": {"quantidade": 30, "preco": 90.00},
    "Premier Rendez-Vous Cinsault Rosé 2020": {"quantidade": 10, "preco": 109.00},
}

# Catálogo de vinhos
catalogo_vinhos = {
    "Fasano Brunello di Montalcino 2017": 899.00, 
    "Casa Ferreirinha Vinha Grande Douro Tinto 2019": 189.90,
    "Vinho Canção Tinto Suave 750": 20.00,
    "Casa Santos Lima Confidencial Branco 2019": 90.00,
    "Premier Rendez-Vous Cinsault Rosé 2020": 109.00,
}

# Definindo o menu de compra
def menu_compra():
    print("Veja as nossas opções de vinhos: ")
    for chave, valor in catalogo_vinhos.items():
        print(f"{chave}: R${valor:.2f}")
    produto = input("Qual produto deseja comprar? ")
    quantidade = int(input("Digite a quantidade que deseja adicionar ao carrinho: "))
   
    # Se a quantidade ou produto não existirem no estoque uma mensagem de "não encontrado" será mostrada
    if produto not in estoque:
        print("Este produto não foi encontrado!")
        
    # Se existir, a quantidade em estoque sera atualizada e a compra pode ser finalizada
    else:
       quantidade_estoque = estoque[produto]["quantidade"]
    if quantidade_estoque < quantidade:
            print("Quantidade insuficiente em estoque!")
    else:
        estoque[produto]["quantidade"] -= quantidade
        preco_produto = estoque[produto]["preco"]  
        total = preco_produto * quantidade
        print(f"Compra realizada com sucesso! Total: R${total:.2f}")

        # resumo da compra
        print("\n Resumo final da compra:")
        preco_total = 0
        print(f"{produto} - {quantidade} unidades - R${preco_produto * quantidade:.2f}")
        preco_total += preco_produto * quantidade
        print("Total da compra: R$ {:.2f}".format(preco_total))

# Definindo o menu do estoque
def menu_estoque():
    print("** Estoque **")
    for produto, dados in estoque.items():
        print(produto)
        print(f"Quantidade: {dados['quantidade']}")
        print(f"Preço: R${dados['preco']:.2f}")

def menu_cadastro():
    cnpj = input("Digite o CNPJ da empresa: ")
    nome = input("Digite o nome da empresa: ")
    email = input("Digite o e-mail da empresa: ")
    telefone = input("Digite o telefone da empresa: ")
    print(f"Empresa cadastrada com sucesso!\nCNPJ: {cnpj}\nNome: {nome}\nE-mail: {email}\nTelefone: {telefone}")

opcao = input("Escolha uma opção: ")
while opcao != "0":
    if opcao == "1":
        menu_compra()
    elif opcao == "2":
        menu_estoque()
    elif opcao == "3":
        menu_cadastro()
    else:
        print("Opção inválida!")
    
    opcao = input("Escolha uma opção: ")

print("Até logo!")



