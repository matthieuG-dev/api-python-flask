from flask import Flask, request, jsonify

from app import *
from models import User

# USER ROUTES
@app.route('/user', methods=['POST'])
def ceate_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')

    user_schema = UserSchema()

    new_user = User(user_id=str(uuid.uuid4()) ,username=data['username'], pseudo=data['pseudo'], email=data['email'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    user_schema.dump(new_user).data

    return jsonify({'message': 'New user created !'})

@app.route('/user', methods=['GET'])
def get_all_user():
    users = User.query.all()

    output = []

    for user in users:
        user_data = {}
        user_data['user_id'] = user.user_id
        user_data['username'] = user.username
        user_data['email'] = user.email
        user_data['password'] = user.password
        output.append(user_data)

    return jsonify({
        'message:' : 'OK',
        'users' : output
        })

@app.route('/user/<user_id>', methods=['GET'])
def get_one_user(user_id):
    # user = UserSchema.query.filter_by(user_id=user_id).first()

    if not user:
        return jsonify({'message': 'User not found!'})
    
    # user_data = {}
    # user_data['user_id'] = user.user_id
    # user_data['username'] = user.username
    # user_data['email'] = user.email
    # user_data['password'] = user.password
    result = user_schema.dump(user)

    return jsonify({
        'message : ' : 'OK',
        'date : ' : result.data
        })

@app.route('/user/<user_id>', methods=['PUT'])
def remove_user(user_id):

    user_to_update = User.query.filter_by(user_id=user_id).first()

    if not user_to_update:
        return jsonify({'message': 'User not found!'})

    data = request.get_json()

    user_schema = UserSchema.load()

    user_to_update.password = data['password']
    db.session.commit()
    user_schema.dump(user_to_update).data


    return jsonify({
        'message : ' : 'OK',
        'updated user : ' : user_to_update
    })

