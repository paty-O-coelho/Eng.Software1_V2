from sql_alchemy import banco

class AnimalModel(banco.Model):
    __tablename__ = 'animais'

    animal_nome = banco.Column(banco.String, primary_key = True)
    idade = banco.Column(banco.String(20))
    dono = banco.Column(banco.String(20))

    def __init__(self,animal_nome,idade,dono):
        self.animal_nome = animal_nome
        self.idade = idade
        self.dono = dono

    def json(self):
        return {
        'animal_nome': self.animal_nome,
        'idade': self.idade,
        'dono': self.dono}

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

    def update_animal(self, idade, dono):
        self.idade = idade
        self.dono = dono

    def delete_animal(self):
        banco.session.delete(self)
        banco.session.commit()
