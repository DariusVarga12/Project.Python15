from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///programari.db'
db = SQLAlchemy(app)

class Programare(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nume_client = db.Column(db.String(50), nullable=False)
    data = db.Column(db.String(20), nullable=False)
    ora = db.Column(db.String(10), nullable=False)
    notificare_trimisa = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"Programare('{self.nume_client}', '{self.data}', '{self.ora}')"

with app.app_context():
    db.create_all()  # Crează tabelele în baza de date

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nume_client = request.form['nume_client']
        data = request.form['data']
        ora = request.form['ora']

        if is_slot_available(data, ora):
            programare = Programare(nume_client=nume_client, data=data, ora=ora)
            db.session.add(programare)
            db.session.commit()

            # Aici poți adăuga logica pentru trimiterea notificărilor către tine sau client

            return 'Programarea a fost efectuată cu succes!'
        else:
            return 'Această oră și dată nu sunt disponibile! Te rugăm să selectezi altă oră sau dată.'
    else:
        programari = Programare.query.all()
        return render_template('index.html', programari=programari)

@app.route('/sterge_programare/<int:programare_id>', methods=['POST'])
def sterge_programare(programare_id):
    programare = Programare.query.get(programare_id)
    if programare:
        db.session.delete(programare)
        db.session.commit()
        return 'Programarea a fost ștearsă cu succes!'
    else:
        return 'Programarea nu există!'

def is_slot_available(data, ora):
    existing_programari = Programare.query.filter_by(data=data).all()

    for programare in existing_programari:
        if programare.ora == ora:
            return False

    return True

if __name__ == '__main__':
    app.run(debug=True)
