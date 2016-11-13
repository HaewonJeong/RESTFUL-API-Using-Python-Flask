from flask import Flask, jsonify, request, redirect,abort,make_response

app = Flask(__name__)

languages = [{'name' : 'JavaScript'}, {'name' : 'Python'}, {'name' : 'Ruby'}]
tasks = [
	{
	'id' : 1, 
	'title' : u'Buy groceries',
	'description' : u'Milk, Cheese, Pizza, Fruit, Tylenol',
	'done':False 
	},
	{
	'id' : 2,
	'title' : u'Learn Python',
	'description' : u'Need to find a good Python tutorial on the web',
	'done':False
	}
]
#GET
@app.route("/", methods=['GET'])
def test():
    return jsonify({'message' : 'This is Todo Webservice!'})

@app.route('/todo/tasks')
def get_tasks():
    return jsonify({'tasks':tasks})

@app.route('/todo/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) ==0 :
       abort(404)
    return jsonify({'task':task[0]})
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}),404)

@app.route('/todo/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
       abort(400)
    task = {
        'id': tasks[-1]['id']+1,
        'title' : request.json['title'],
        'description' : request.json.get('description', ""),
        'done': False 
    }
    tasks.append(task)
    return jsonify({'task':tasks})

@app.route('/todo/tasks/<int:task_id>', methods=['PUT'])
def edit_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
       abort(404)
    task[0]['title'] = request.json.get('title',task[0]['title'])
    task[0]['description'] = request.json.get('description',task[0]['description'])
    task[0]['done'] = request.json.get('done',task[0]['done'])
    return jsonify({'task' : task[0]})
@app.route('/todo/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id) :
    task = [task for task in tasks if task['id'] == task_id]
    if len(task)==0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result':True})

@app.route('/lang', methods=['GET'])
def returnAll():
    return jsonify({'languages' : languages})
   
@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
    langs = [language for language in languages if language['name'] == name]
    return jsonify({'language' : langs[0]})


#POST
@app.route('/lang', methods=['POST'])
def addOne():
    language = {'name' : request.json['name']}
    
    languages.append(language)
    return jsonify({'languages' : languages})
#PUT(Update)
@app.route('/lang/<string:name>', methods=['PUT'])
def editOne(name):
    langs = [language for language in languages if language['name'] == name] #find and return all the languages that match the name.
    langs[0]['name'] = request.json['name'] #update the name to whatever the name is in the jason
    return jsonify({'language' : langs[0]})
#DELETE
@app.route('/lang/<string:name>', methods=['DELETE']) #setup the route
def removeOne(name):
    langs = [language for language in languages if language['name'] == name]
    languages.remove(langs[0])
    return jsonify({'languages' : languages})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port =8080,debug=True)
