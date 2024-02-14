from flask import Flask,render_template,send_file
import json
import os
path = os.getcwd()

app = Flask(__name__,template_folder='public')

@app.route('/')
def index():
    return render_template('index.html')




#router to check status of certificate
@app.route('/api/cer')
def status():
    #read status.json file
    json_file = open(f'{path}/status.json')
    data = json.load(json_file)
    return data



#create a route to download certificate
@app.route('/api/download/<name>')
def download(name):
    return send_file(f'{path}/Cert/{name}.zip', as_attachment=True)
if __name__ == '__main__':
    app.run(debug=True)
