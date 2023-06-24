from flask import Flask, render_template, request
import solution

app = Flask(__name__)
app.config['SECRET_KEY'] = 'FANCY'

@app.route('/')
def index():
    return render_template('task.html', author = 'Jennie')

@app.route('/wordsearch', methods=['GET', 'POST'])
def matrix_form():
    if request.method == 'POST':
        matrix = []
        for i in range(3):
            row = []
            for j in range(4):
                value = str(request.form.get(f'matrix[{i}][{j}]'))
                row.append(value)
            matrix.append(row)
        
        s = solution.Solution()
        board = [[matrix[0][0],matrix[0][1],matrix[0][2],matrix[0][3]] , [matrix[1][0],matrix[1][1],matrix[1][2],matrix[1][3]] , [matrix[2][0],matrix[2][1],matrix[2][2],matrix[2][3]] ]
        word = str(request.form.get(f'word'))
        result = s.exist(board, word)

        return render_template('result.html', matrix=matrix, word_res=word, result_res=result)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)