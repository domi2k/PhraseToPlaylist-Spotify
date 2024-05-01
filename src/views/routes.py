from flask import Blueprint, render_template, request, jsonify, session

bp = Blueprint('routes', __name__)


@bp.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')
