from flask import g, jsonify, request
from ..decorators import permission_required
from . import api
from app.models import Permission, User, Role
import json


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

@api.route('/users/', methods=['POST'])
@permission_required(Permission.ADMINISTER)
def new_user():
    user = User.from_json(request.json)
    db.session.add(user)
    db.session.commit()
    return json.dumps[user.to_json()], 201, \
            {'created': user.id}

@api.route('/users/<int:id>', methods=['PUT'])
@permission_required(Permission.ADMINISTER)
def edit_user(id):
    user = User.query.get_or_404(id)
    user.id = request.json.get('id',user.id)
    user.email = request.json.get('email', user.email)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_json()), 200, \
            {'update': id}

@api.route('/users/<int:id>', methods=['DELETE'])
@permission_required(Permission.ADMINISTER)
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify(user.to_json()), 200, \
            {'delete': id}
