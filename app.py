from flask import Flask, request, jsonify
from models import User
from database import Base, session, engine
from schemas import UserOut

app = Flask(__name__)

@app.route('/user_info/<int:user_id>', methods=['GET'])
def user_info(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        user_data = user.formatted_data
        return jsonify(user_data)
    else:
        return jsonify({'error': 'User not found'}), 404


@app.route('/user_info', methods=['POST'])
def user_info_new():
    user_id = request.form.get('id')
    user = session.query(User).filter_by(id=user_id).first()
    user_data = user.formatted_data
    user_out = UserOut(**user_data)
    return jsonify(user_out.dict())



if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.run(debug=True)
