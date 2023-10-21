from flask import Flask , request
import json

app = Flask(__name__)

count = 0

@app.route('/')
def Index():
    return open("Index.html").read()

@app.route('/log', methods=['POST'])
def log_count():
    global count
    data = json.loads(request.data)
    count = data['count']
    
    with open('count_log.txt', 'a') as log_file:
        log_file.write(f'Count - {count}\n')

    return 'Logged'

if __name__ == '__main__':
    app.run(debug=True)
