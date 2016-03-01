from flask import g, jsonify, request
from . import api


@api.route('/users/')
def get_users():
    user = request.args.get('page', 1, type=int)
    pagination = User.query.paginate(
            page, per_page=10, error_out=False)
    users = pagination.items
    return jsonify(
            for user in users:
                {
                'id': user.to_json(),
                'username': user.to_json(),
                'email': user.to_json()
                }
            )

@api.route('/users/<int:id>')
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify({
        'id': user.id.to_json(),
        'username': user.name.to_json(),
        'email': user.email.to_json()
    })

@api.route('/users/', methods=['POST'])
@permission_required(Permission.ADMINISTER)
def new_user():
    user = User.from_json(request.json)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_json()), 201, \
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
