from flask import Flask
from flask import request, jsonify
app=Flask(__name__)


comptes_telephoniques=[
    {'phone_id':1,
     'title':u'0890138857 ',
     'description': u'Chu Nhat Tan',
     'done': False
     },
     {'phone_id':2,
     'title':u'0840559771',
     'description': u'Monsieur Partrick',
     'done': False
     },
     {'phone_id':3,
     'title':u'0890138789 ',
     'description': u'Carolin',
     'done': False
     },
     {'phone_id':4,
     'title':u'0840559888',
     'description': u'Monsieur Emmanuel',
     'done': False
     }
]

@app.route('/api/v1/comptes_telephoniques', methods=['GET'])
def get_tasks():
    return jsonify({'comptes_telephoniques':comptes_telephoniques})

@app.route('/api/v1/somme/,<int:a>/<int:b>', methods=['GET'])
def somme(a,b):
    s=a + b
    return jsonify({'somme':s})


def get_phone(phone_id):
    if phone_id not in comptes_telephoniques:
        abort(404)
    return comptes_telephoniques[phone_id]

# Routes
@app.route('/phones', methods=['GET'])
def get_phones():
    return jsonify(comptes_telephoniques)

@app.route('/phones/<string:phone_id>', methods=['GET'])
def get_phone_by_id(phone_id):
    phone = get_phone(phone_id)
    return jsonify(phone)


@app.route('/phones', methods=['POST'])
def add_phone():
    new_phone = {
        'id': request.json['id'],
        'model': request.json['model'],
        'quantity': request.json['quantity']
    }
    comptes_telephoniques[new_phone['id']] = new_phone
    return jsonify(new_phone), 201

@app.route('/phones/<string:phone_id>', methods=['PUT'])
def update_phone(phone_id):
    phone = get_phone(phone_id)
    phone.update(request.json)
    return jsonify(phone)

@app.route('/phones/<string:phone_id>', methods=['DELETE'])
def delete_phone(phone_id):
    del comptes_telephoniques[phone_id]
    return '', 204


if __name__=="__main__":
    app.run(debug=True)