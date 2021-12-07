from flask import Blueprint
from flask_restplus import Api, Resource
from lutils.decorators import requires_fields_validation, requires_json

VERSION = '1.0'
DOC = 'swagger-doc'

blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(blueprint,
          version=VERSION,
          title='main-api',
          description=DOC,
          doc='/docs/swagger',
          authorizations={
              'x-api-key': {
                  'type': 'apiKey',
                  'in': 'header',
                  'name': 'x-api-key'
              },
              'Token': {
                  'type': 'apiKey',
                  'in': 'header',
                  'name': 'Authorization'
              }
          })

ns = api.namespace('', description='main-api endpoints')

@ns.route('/', doc=False)
class Index(Resource):
    def get(self):
        return dict(
            service='main-project API HealthCheck',
            version=VERSION)
