from flask import Flask, jsonify

app = Flask(__name__)

# Datos de ejemplo
tasks = [
    {"id": 1, "title": "Comprar víveres", "done": False},
    {"id": 2, "title": "Pasear al perro", "done": True},
    {"id": 3, "title": "Hacer ejercicio", "done": False}
]

# Endpoint para obtener todas las tareas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    return jsonify(task) if task else ("", 404)


from flask import request

@app.route('/tasks', methods=['POST'])
def add_task():
    new_task = {
        "id": len(tasks) + 1,
        "title": request.json.get("title", ""),
        "done": request.json.get("done", False)
    }
    tasks.append(new_task)
    return jsonify(new_task), 201


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task:
        task["title"] = request.json.get("title", task["title"])
        task["done"] = request.json.get("done", task["done"])
        return jsonify(task)
    return ("", 404)


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return ("", 204)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

