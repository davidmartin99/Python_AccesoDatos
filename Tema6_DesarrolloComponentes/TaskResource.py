from flask_restful import Resource, Api, reqparse

from Tema6_DesarrolloComponentes.app import app

api = Api(app)

class TaskResource(Resource):
    def get(self, task_id):
        task = next((task for task in tasks if task["id"] == task_id), None)
        return task if task else ("", 404)

    def delete(self, task_id):
        global tasks
        tasks = [task for task in tasks if task["id"] != task_id]
        return "", 204

api.add_resource(TaskResource, "/tasks/<int:task_id>")
