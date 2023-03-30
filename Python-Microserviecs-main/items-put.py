from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_items as us

app = Flask(__name__)

@app.route('/update', methods=['PUT'])
def update():
    # Get the user's login information from the request
        name = request.form.get('name')
        category = request.form.get('category')
        price = request.form.get('price')
        instock = request.form.get('instock')

        _user = us.items_name()
        data = [x for x in _user if x["name"]==name]
    # return jsonify(_user)
    #Get Data
        if data:
            us.items_update(name,category,price,instock)
            return jsonify({'message': 'Update successfully.'}), 200
        else:
            return jsonify({'message': 'Cannot update.'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True) #127.0.0.1