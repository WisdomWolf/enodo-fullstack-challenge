from os import getenv

from flask import Flask, jsonify
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
    properties = RealEstateProperty.query.all()
    return jsonify(RealEstateProperty.serialize_list(properties))


@app.put('/api/properties/select/<property_id>')
def select_property(property_id):
    re_property = _get_property(property_id)
    re_property.selected = True
    db.session.commit()
    return jsonify(re_property.serialize())


@app.delete('/api/properties/select/<property_id>')
def unselect_property(property_id):
    re_property = _get_property(property_id)
    re_property.selected = False
    db.session.commit()
    return jsonify(re_property.serialize())


@app.get('/api/properties/<property_id>')
def get_property(property_id):
    re_property = _get_property(property_id)
    return jsonify(re_property.serialize())


def _get_property(property_id):
    return RealEstateProperty.query.filter_by(
        property_id=property_id).first()

