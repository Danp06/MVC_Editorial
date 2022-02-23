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


@app.route('/person_update/<id_person>', methods=['GET'])
def person_update(id_person):
    person_delete(id_person)
    return render_template('person_update.html', id_person=id_person)


@app.route('/person_delete/<id_person>')
def person_delete(id_person):
    for i in model:
        if i.id_person == id_person:
            temp = i
            print("La persona con Id: ", temp.id_person, " a sido borrado")
            model.remove(temp)

    return render_template('person_delete.html')


@app.route('/document', methods=['GET'])
def document():
    return render_template('document.html')


@app.route('/document_detail', methods=['POST'])
def document_detail():
    id_document = request.form['id_document']
    tittle = request.form['tittle']
    authors = request.form['authors']
    pub_date = request.form['pub_date']
    edition = request.form['edition']
    nropag = request.form['nropag']
    d = Document( id_document=id_document, tittle=tittle, authors=authors,
                  pub_date=pub_date, edition=edition, nropag=nropag)
    model2.append(d)
    return render_template('document_detail.html', value=d)


@app.route('/documents')
def documents():
    data2 = [(j.id_document, j.tittle, j.authors, j.pub_date, j.edition, j.nropag) for j in model2]
    print(data2)
    return render_template('documents.html', value=data2)


@app.route('/document_update/<id_document>', methods=['GET'])
def document_update(id_document):
    document_delete(id_document)
    return render_template('document_update.html', id_document=id_document)
    

@app.route('/document_delete/<id_document>')
def document_delete(id_document):
    for i in model2:
        if i.id_document == id_document:
            temp = i
            print("El documento con Id: ", temp.id_document, " a sido borrado")
            model2.remove(temp)

    return render_template('document_delete.html')


if __name__ == '__main__':
    app.run()
