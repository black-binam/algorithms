class Produit:
    c =0
    def __init__(self,nom,prix,quantite,id=None):
        if id ==None:
            self.id = Produit.c
        else:
            self.id = Produit.c+1
            
        self.nom = nom
        self.prix = prix
        self.quantite = quantite
        Produit.c +=1
    
    def __repr__(self):
        return self.nom
    
    """def to_dict(self):
        return {'id':self.id,'nom':self.nom, 'prix':self.prix, 'quantite':self.quantite }"""

class Gestion_de_stock:
    def __init__(self):
        self.stock ={}
        
    
    def add_product(self,produit):
        assert type(produit) in [dict,Produit], "ErroType only accept dict type or Produit type"
        
        if type(produit) == Produit:
            produit = {'id':produit.id,'nom':produit.nom, 'prix':produit.prix, 'quantite':produit.quantite }
        
        id_produit = produit['id']
        
        if id_produit in self.stock:
            self.stock[id_produit].update(produit)
        else:
            self.stock[id_produit]=produit

    def search_product(self):
        id = input('Entrer un le numéro de produit: ')
        assert id.isdigit(), "Entrez une valeur numérique"
        assert int(id) in self.stock, 'No such product'
        return self.stock[int(id)]

    def delete_product(self,index):
        if index not in self.stock:
            print("!--There is no such product--!")
        del self.stock[index]
    
    def stock_value(self):
        return sum([dico['prix']*dico['quantite'] for dico in self.stock.values()])

    def out_of_stock(self):
        return [dico['id'] for dico in self.stock.values() if dico['quantite']==0]

    def all_products(self):
        return self.stock
    

