from sql_alchemy import banco

class UserModel(banco.Model):
    __tablename__ = 'tabela_info_usuarios'

    user_id = banco.Column(banco.Integer, primary_key = True)
    login = banco.Column(banco.String(80))
    senha = banco.Column(banco.String(20))
    # tipo = banco.Column(banco.String(20))
    # nome = banco.Column(banco.String(20))
    # cpf = banco.Column(banco.Integer)
    # end = banco.Column(banco.String(80))
    # tel = banco.Column(banco.String(20))

    def __init__(self,login,senha):
        self.login = login
        self.senha = senha
        # self.tipo = tipo
        # self.nome = nome
        # self.cpf = cpf
        # self.end = end
        # self.tel = tel


    def json(self):
        return {
        'user_id': self.user_id,
        'login': self.login
        # 'tipo':self.tipo,
        # 'nome':self.nome,
        # 'cpf':self.cpf,
        # 'end':self.end,
        # 'tel':self.tel
        }

    #metodo de classe
    @classmethod
    def encontra_user(cls, user_id):
        user = cls.query.filter_by(user_id=user_id).first()
        # *select *from animais where animal_nome=$animal_nome
        if user:
            return user
        return None
    @classmethod
    def encontra_por_login(cls, login):
        user = cls.query.filter_by(login=login).first()
        # *select *from animais where animal_nome=$animal_nome
        if user:
            return user
        return None

    def save_user(self):
        banco.session.add(self)
        banco.session.commit()

    def delete_user(self):
        banco.session.delete(self)
        banco.session.commit()
