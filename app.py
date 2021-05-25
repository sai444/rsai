from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import os
import datetime


app = Flask(__name__)




app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://iotmax:iotmax@localhost:5432/postgres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_SIZE'] = 5000


db = SQLAlchemy(app)

from models import projecttopic
cors = CORS(app, resources= {
    r"/*":{
        "origins":"*",
        "Access-Control-Allow-Origin":"*"
    }
})





@app.route("/")
def hello():
    return "Hello welcome to projecttopic API!"


@app.route('/projecttopic', methods=['POST', 'GET'])
def projecttopicpg():
    if request.method == 'POST':
        data = request.get_json()
        new_car = projecttopic(topic = data['topic'], project = data['project'], createdon = datetime.datetime.now())

        db.session.add(new_car)
        db.session.commit()

        data = {"message": f"name created successfully"}
        return jsonify(data), 200


    elif request.method == 'GET':
        things = projecttopic.query.all()
        results = [
            {
              "id" : thing.id,
                "topic" : thing.topic,
                "project" : thing.project,
                "createdon" : thing.createdon
                #  "compdatetime" : thing.compdatetime

            } for thing in things]

        return  jsonify(results)

@app.route('/projecttopic/<id>', methods=['GET', 'PUT', 'DELETE'])
def depts(id):
    car = projecttopic.query.get_or_404(id)

    if request.method == 'GET':
        response =   {
                "id" : car.id,
                "topic" : car.topic,
                "createdon" : car.createdon

        }
        return jsonify(response)

    elif request.method == 'PUT':
        data = request.get_json()
        car.topic = data['topic']
        # car.createdon = data['createdon']
        db.session.add(car)
        db.session.commit()
        data = {"message": f"name updated successfully"}
        return jsonify(data), 200

    elif request.method == 'DELETE':
        data = request.get_json()
        car.topic = data['topic']
        print('car ======================',car.topic)
        db.session.delete(car)

        db.session.commit()


        data = {"message": f"name deleted successfully"}
        return jsonify(data), 200

##################################################################################################################################################

##################################################################################################################################################

# 
if __name__ == '__main__':
    app.run()
