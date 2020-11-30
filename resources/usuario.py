from flask_restful import Resource,reqparse
from models.usuario import UserModel


class User (Resource):

    def get(self, user_id):
        user  = UserModel.encontra_user(user_id)
        if user :
            return user.json()
        return {'message': 'usuario não existe'}, 404

    def delete(self, user_id):
        user = UserModel.encontra_user(user_id)
        if user:
            user.delete_user()
            return {'message': 'usuario apagado'}
        return {'message': 'Usuario não encontrado'}, 404

class UserRegister(Resource):
    def post (self):
        atributos = reqparse.RequestParser()

        atributos.add_argument('login',type=str, required=True, help="O campo login, não pode ficar vazio!")
        atributos.add_argument('senha',type=str, required=True, help="O campo senha, não pode ficar vazio!")
        atributos.add_argument('tipo',type=str, required=True, help="O campo tipo, não pode ficar vazio!")
        atributos.add_argument('nome',type=str, required=True, help="O campo nome, não pode ficar vazio!")
        atributos.add_argument('cpf',type=str, required=True, help="O campo cpf, não pode ficar vazio!")
        atributos.add_argument('end',type=str, required=True, help="O campo endereço, não pode ficar vazio!")
        atributos.add_argument('tel',type=str, required=True, help="O campo telefone, não pode ficar vazio!")

        dados =  atributos.parse_args()

        if UserModel.encontra_por_login(dados['login']):
            return {'message': 'esse login ja existe'}

        user = UserModel(**dados)
        user.save_user()
        return {'message': 'Usuario cadastrado com sucesso!'},201
