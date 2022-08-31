from pymongo import MongoClient
from flask import Flask, jsonify, request

app = Flask(__name__)

def mongoconnect():
    mongo_client = MongoClient('mongodb://127.0.0.1:27017')
    db = mongo_client.info
    col = db['carinfo']
    t = col.count_documents({})
    print(t)

@app.route(('/carinfo'), methods=['GET'])
def carinfo():
    mongo_client2 = MongoClient()
    db2 = mongo_client2.info
    col2 = db2["carinfo"]
    output = []
    for s in col2.find():
        output.append({'carmodel': s['carmodel'], 'color': s['color'],
                       'carowner': s['carowner']})

    return jsonify({'result': output})

@app.route(('/carownerretrieve'), methods=['POST'])
def retrievebycarowner():
    item = request.get_json()
    carowner_input = item['carowner']
    output = [carowner_input]
    mongo_client2 = MongoClient('mongodb-express-service', 27017)
    db2 = mongo_client2.info
    col2 = db2["carinfo"]
    for x in col2.find({}, {'carowner': 1, '_id': 0}):
        carowner = x['carowner']
        if carowner_input == carowner:
            output.append({'carowner':x['carowner']})

    query = {'carowner':carowner_input}
    allquery = {'_id': 0, 'carowner': 1, 'color': 1,'carmodel':1}

    rsp = list(col2.find(query, allquery))
    x = {'status': rsp}

    return x

@app.route(('/carmodelretrieve'), methods=['POST'])
def retrievebycarmodel():
    item = request.get_json()
    carmodel_input = item['carmodel']
    output = [carmodel_input]
    mongo_client2 = MongoClient('mongodb-express-service', 27017)
    db2 = mongo_client2.info
    col2 = db2["carinfo"]
    for x in col2.find({}, {'carmodel': 1, '_id': 0}):
        carmodel = x['carmodel']
        if carmodel_input == carmodel:
            output.append({'carmodel':x['carmodel']})

    query = {'carmodel':carmodel_input}
    allquery = {'_id': 0, 'carowner': 1, 'color': 1,'carmodel':1}

    rsp = list(col2.find(query, allquery))
    x = {'status': rsp}

    return x

@app.route(('/colorretrieve'), methods=['POST'])
def retrievebycolor():
    item = request.get_json()
    color_input = item['color']
    output = [color_input]
    mongo_client2 = MongoClient()
    db2 = mongo_client2.info
    col2 = db2["carinfo"]
    for x in col2.find({}, {'color': 1, '_id': 0}):
        color = x['color']
        if color_input == color:
            output.append({'color':x['color']})

    query = {'color':color_input}
    allquery = {'_id': 0, 'carowner': 1, 'color': 1,'carmodel':1}

    rsp = list(col2.find(query, allquery))
    x = {'status': rsp}

    return x

if __name__ == '__main__':
    app.run(debug=True)
