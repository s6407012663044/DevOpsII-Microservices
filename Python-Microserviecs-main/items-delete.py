from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_items as us

app = Flask(__name__)

@app.route('/delete', methods=['DELETE'])
def delete():
    # Get the user's login information from the request
    name = request.form.get('name')
        # passwd = request.form.get('password')
        # name = request.form.get('name')

    _user = us.find_itemsname(name)
    data = [x for x in _user if x["name"]==name]
    # return jsonify(_user)
    #Get Data
    if data:
        us.items_delete(name)
        return jsonify({'message': 'Delete successfully.'}), 200
    else:
        return jsonify({'message': 'Cannott Delete.'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True) #127.0.0.1