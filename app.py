from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = []
    if request.method == 'POST':
        names = [n.strip() for n in request.form['names'].split('\n') if n.strip()]
        num_groups = int(request.form['num_groups'])
        random.shuffle(names)

        grouped = [[] for _ in range(num_groups)]
        for i, name in enumerate(names):
            grouped[i % num_groups].append(name)

        result = []
        for group in grouped:
            numbers = list(range(1, len(group) + 1))
            random.shuffle(numbers)
            numbered_group = list(zip(group, numbers))
            result.append(numbered_group)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
