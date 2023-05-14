from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')
carrinho=[]
total = 0.00

# Main Page
@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('pages/index.html',titulo_pagina='Sales Clothes')

# Produtos
@app.route('/products')
def products():
    return render_template('/pages/products.html', titulo_pagina='Produtos')

# Rotas que envolvem Carrinho, Adicionar ao carrinho
@app.route('/addCart/<product>')
def addCart(product):
    global total
    carrinho.append(product)
    return render_template('/pages/products.html', titulo_pagina='Produtos', aviso='Produto Adicionado com Sucesso')

# Visualizar o carrinho
@app.route('/cart')
def card():
    return render_template('pages/cart.html', titulo_pagina='Carrinho', carrinho=carrinho)

# Finalizar o carrinho
@app.route('/endCart')
def endCart():
    return render_template('pages/endCart.html', titulo_pagina='Compra', carrinho=carrinho, total=total)

# Rotas para Produtos
@app.route('/infoProducts/<produto>')
def infoProducts(produto):
    global total,carrinho
    if produto == 'camisa':
        total += 50.0
        return render_template('/pages/infoProducts.html',\
        product='camisa',\
        desc='Camiseta de cor preta com estampas diversas',\
        tam='M',\
        price="R$ 50.00")
    
    elif produto == 'blusa':
        total += 45.00
        return render_template('/pages/infoProducts.html',\
        product=produto,\
        desc='Blusa de cor preta com estampas diversas',\
        tam='M',\
        price="R$ 45.00")
    
    elif produto == 'touca':
        total += 13.00
        return render_template('/pages/infoProducts.html',\
        product=produto,\
        desc='Touca nas cores cinza ou preto',\
        tam='P,M',\
        price='R$ 13.00')
    
    elif produto == 'calca':
        total += 100.00
        return render_template('/pages/infoProducts.html',\
        product=produto,\
        desc='Calças nas cores preto, cinza ou azul',\
        tam='M,G',\
        price='R$ 100.00')
    
    elif produto == 'mochila':
        total += 150.00
        return render_template('/pages/infoProducts.html',\
        product=produto,\
        desc='Mochilas cinzas perfeitas para guardar notebook e material escolar',\
        tam='M,G',\
        price='R$ 150.00')

if __name__ == '__main__':
    app.run(debug=True)