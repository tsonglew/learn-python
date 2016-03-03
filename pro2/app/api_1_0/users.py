from flask import g, jsonify, request
from flask.ext.httpauth import HTTPBasicAuth
from ..decorators import permission_required, admin_required
from . import api
from app.models import Permission, User, Role
import json


auth = HTTPBasicAuth()


@api.route('/users/')
def get_users():
    page = request.args.get('page', 1, type=int)
    pagination = User.query.paginate(
            page, per_page=10, error_out=False)
    users = pagination.items
    return json.dumps(
        [user.to_json() for user in users ],
        indent = 1
    ), 200

@api.route('/users/<int:id>')
def get_user(id):
    user = User.query.get_or_404(id)
    return json.dumps(
        [user.to_json()],
        indent = 1
    ), 200

@api.route('/users/', methods=['GET', 'POST'])
@admin_required
def new_user():
    user = User.from_json(request.json)
    db.session.add(user)
    db.session.commit()
    return jsonify( user.to_json() ),201


@api.route('/users/<int:id>', methods=['GET', 'PUT'])
@admin_required
def edit_user(id):
    user = User.query.get_or_404(id)
    if request.method == 'PUT':
        data_dict = eval(request.data)
        user.username = data_dict.get('username', user.username)
        user.email = data_dict.get('email', user.email)
        if data_dict.get('password'):
            user.password_hash = generate_password_hash(data_dict.get('password'))
        db.session.add(user)
        db.session.commit()
    return jsonify(user.to_json()), 200

@api.route('/users/<int:id>', methods=['GET', 'DELETE'])
@admin_required
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({
        'delete': id
        }), 200
