from flask_restful import Resource,reqparse
from models.animal import AnimalModel


class Animais (Resource):
    def get (self):
        return {'animais': [animal.json() for animal in AnimalModel.query.all()]}

class Animal (Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('idade')
    argumentos.add_argument('dono')
    argumentos.add_argument('tipo')
    argumentos.add_argument('sexo')
    argumentos.add_argument('cor')
    argumentos.add_argument('end')
    argumentos.add_argument('foto')

    def get(self, animal_nome):
        animal  = AnimalModel.encontra_animal(animal_nome)
        if animal :
            return animal.json()
        return {'message': 'animal não disponivel'}, 404

    def post(self,animal_nome):
        if AnimalModel.encontra_animal(animal_nome):
            return {"message": "Animal '{}' já cadastrado".format(animal_nome)}, 400

        dados = Animal.argumentos.parse_args()
        animal = AnimalModel(animal_nome, **dados)
        try:
            animal.save_animal()
        except:
            return {'message': 'Não foi possivel salvar o PET'}
        return animal.json(),201

    def put(self, animal_nome):
        dados = Animal.argumentos.parse_args()
        animal_encontrado =  AnimalModel.encontra_animal(animal_nome)

        if animal_encontrado:
            animal_encontrado.update_animal(**dados)
            animal_encontrado.save_animal()
            return animal_encontrado.json(), 200
        animal = AnimalModel(animal_nome, **dados)
        animal.save_animal()
        return animal.json(),201


    def delete(self, animal_nome):
        animal = AnimalModel.encontra_animal(animal_nome)
        if animal:
            animal.delete_animal()
            return {'message': 'Animal apagado'}
        return {'message': 'Pet não encontrado'}, 404
