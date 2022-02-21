from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logic.person import Person
from logic.document import Document


app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []
model2 = []


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/person', methods=['GET'])
def person():
    return render_template('person.html')


@app.route('/person_detail', methods=['POST'])
def person_detail():
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    p = Person(id_person=id_person, name=first_name, last_name=last_name)
    model.append(p)
    return render_template('person_detail.html', value=p)


@app.route('/people')
def people():
    data = [(i.id_person, i.name, i.last_name) for i in model]
    print(data)
    return render_template('people.html', value=data)


@app.route('/document', methods=['GET'])
def document():
    return render_template('document.html')


@app.route('/document_detail', methods=['POST'])
def document_detail():
    tittle = request.form['tittle']
    id_document = request.form['id_document']
    pub_date = request.form['pub_date']
    edition = request.form['edition']
    nro_pag = request.form['nro_pag']
    d = Document(tittle=tittle, id_document=id_document, pub_date=pub_date, edition=edition, nro_pag=nro_pag)
    model2.append(d)
    return render_template('document_detail.html', value=d)


@app.route('/documents')
def documents():
    data2 = [(i.tittle, i.pub_date, i.id_document, i.edition, i.nropag) for i in model2]
    print(data2)
    return render_template('documents.html', value=data2)


if __name__ == '__main__':
    app.run()
