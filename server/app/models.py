from app import db

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length = 30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)

class CoinMetaData(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length = 30), nullable=False, unique=True)
    ticker = db.Column(db.String(length = 20), nullable=False, unique=True)

class UserCoins(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    coin_id = db.Column(db.Integer(), db.ForeignKey('coin.id'), nullable=False)

class CoinPrices(db.Model):
    id = db.Colum(db.Integer(), primary_key=True)
    coin_id = db.Column(db.Integer(), db.ForeignKey('coin.id'))
    price = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())