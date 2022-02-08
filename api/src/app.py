from os import getenv

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from db.base import Base
from models.real_estate import RealEstateProperty
from utils.directory_resolvers import get_db_uri


ENVIRONMENT = getenv('ENVIRONMENT', 'dev')

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = get_db_uri('real_estate.db')
db = SQLAlchemy(app, model_class=Base)


@app.get('/api/properties')
def get_properties():
    if selected := request.args.get('selected') is not None:
        properties = RealEstateProperty.query.filter_by(selected=selected).all()
    else:
        properties = RealEstateProperty.query.all()
    return jsonify(RealEstateProperty.serialize_list(properties))


@app.put('/api/properties/<property_id>')
def update_property(property_id):
    selected = request.args.get('selected')
    if selected is not None:
        re_property = _get_property(property_id)
        re_property.selected = True if selected.lower() == 'true' else False
        db.session.commit()
        return jsonify(re_property.serialize())
    else:
        return False


@app.get('/api/properties/<property_id>')
def get_property(property_id):
    re_property = _get_property(property_id)
    return jsonify(re_property.serialize())


def _get_property(property_id):
    """
    Internal method to resolve property for use by REST functions
    :param property_id: ID of the property to retrieve
    :return:
    """
    return RealEstateProperty.query.filter_by(
        property_id=property_id).first()

