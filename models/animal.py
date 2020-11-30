from sql_alchemy import banco

class AnimalModel(banco.Model):
    __tablename__ = 'tabela_info_animais'

    animal_nome = banco.Column(banco.String, primary_key = True)
    idade = banco.Column(banco.String(30)) # deixei como str porque a pessoa pode passar idade assim (1 ano, ou 4 meses)
    dono = banco.Column(banco.String(20))
    tipo = banco.Column(banco.String(20))
    sexo = banco.Column(banco.String(20))
    cor = banco.Column(banco.String(20))
    end = banco.Column(banco.String(80))
    foto = banco.Column(banco.String(80))
    


    def __init__(self,animal_nome,idade,dono,tipo,sexo,cor,end,foto):
        self.animal_nome = animal_nome
        self.idade = idade
        self.dono = dono
        self.tipo = tipo
        self.sexo = sexo
        self.cor = cor
        self.end = end
        self.foto = foto
        
        #tipo, sexo, cor, end,foto

    def json(self):
        return {
        'animal_nome': self.animal_nome,
        'idade': self.idade,
        'dono': self.dono,
        'tipo': self.tipo,
        'sexo': self.sexo,
        'cor': self.cor,
        'end': self.end,
        'foto': self.foto
        }

    #metodo de classe
    @classmethod
    def encontra_animal(cls, animal_nome):
        animal = cls.query.filter_by(animal_nome=animal_nome).first()
        # *select *from animais where animal_nome=$animal_nome
        if animal:
            return animal
        return None

    def save_animal(self):
        banco.session.add(self)
        banco.session.commit()

    def update_animal(self, idade, dono,tipo,sexo,cor,end,foto):
        self.idade = idade
        self.dono = dono
        self.tipo = tipo
        self.sexo = sexo
        self.cor = cor
        self.end = end
        self.foto = foto

    def delete_animal(self):
        banco.session.delete(self)
        banco.session.commit()
