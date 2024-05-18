from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask('Furniture store')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Part(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    part_name = db.Column(db.String(300))
    price = db.Column(db.Integer)
    used = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'Часть{self.id}. {self.part_name} - {self.price} rub.'


@app.route('/')
def main():
    parts = Part.query.all()
    return render_template('index.html', parts_list=parts)


@app.route('/used/<part_id>', methods=['PATCH'])
def modify_part(part_id):
    part = Part.query.get(part_id)
    part.used = request.json['used']
    db.session.commit()
    return 'Ok'

@app.route('/add', methods=['POST'])
def add_part():
    data = request.json
    part = Part(**data)
    db.session.add(part)
    db.session.commit()

    return 'OK'



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)