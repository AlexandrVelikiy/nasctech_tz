import os
from flask import Flask, jsonify
from flask_restplus import Resource,Api, reqparse
import utils

rule_fun_dict = utils.get_fun_dict()

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('data', type=float, action="split")
parser.add_argument('rule', type=str, action="split")

class Start(Resource):
    def get(self):
        args = parser.parse_args()
        data_list = args['data']
        rule_list = args['rule']
        if (not data_list) or (not rule_list):
            return {'result':[]}

        result_list = []
        for i, data in enumerate(data_list):
            try:
                rule_name = rule_list[i]
            except IndexError:
                break

            try:
                res = rule_fun_dict.get(rule_name)(data)
            except TypeError:
                continue
            result_list.append(res)

        return jsonify({'result': result_list})

api.add_resource(Start, '/start')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))
