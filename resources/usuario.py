from flask_restful import Resource,reqparse
from models.usuario import UserModel
from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt
from werkzeug.security import safe_str_cmp
from blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('login',type=str, required=True, help="O campo login, não pode ficar vazio!")
atributos.add_argument('senha',type=str, required=True, help="O campo senha, não pode ficar vazio!")
# atributos.add_argument('tipo',type=str, required=True, help="O campo tipo, não pode ficar vazio!")
# atributos.add_argument('nome',type=str, required=True, help="O campo nome, não pode ficar vazio!")
# atributos.add_argument('cpf',type=str, required=True, help="O campo cpf, não pode ficar vazio!")
# atributos.add_argument('end',type=str, required=True, help="O campo endereço, não pode ficar vazio!")
# atributos.add_argument('tel',type=str, required=True, help="O campo telefone, não pode ficar vazio!")


class User (Resource):

    def get(self, user_id):
        user  = UserModel.encontra_user(user_id)
        if user :
            return user.json()
        return {'message': 'usuario não existe'}, 404
    @jwt_required
    def delete(self, user_id):
        user = UserModel.encontra_user(user_id)
        if user:
            user.delete_user()
            return {'message': 'usuario apagado'}
        return {'message': 'Usuario não encontrado'}, 404

class UserRegister(Resource):
    def post (self):
        dados =  atributos.parse_args()

        if UserModel.encontra_por_login(dados['login']):
            return {'message': 'esse login ja existe'}

        user = UserModel(**dados)
        user.save_user()
        return {'message': 'Usuario cadastrado com sucesso!'},201

class UserLogin (Resource):

    @classmethod
    def post(cls):
        dados = atributos.parse_args()

        user  = UserModel.encontra_por_login(dados['login'])

        if user and safe_str_cmp(user.senha, dados['senha']):
            token_de_acesso =  create_access_token(identity=user.user_id)
            return {'access_token': token_de_acesso}, 201
        return {'message': 'the username or password is incorrect'}, 401

class UserLogout (Resource):

    @jwt_required
    def post(self):
        jwt_id = get_raw_jwt()['jti'] #JWT Token Identifier
        BLACKLIST.add(jwt_id)
        return {'message': 'Logged out sucessfully!'},200














