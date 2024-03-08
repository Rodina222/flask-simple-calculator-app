from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
        
        result = None
        number1 = int(request.form['num1'])
        number2 = int(request.form['num2']) 
        operation = request.form['operation']

        if operation == "add":
           result = number1 + number2

        elif operation == "subtract":
           result = number1 - number2
        
        elif operation == "multiply":
            result = number1 * number2

        elif operation == "divide":
            if number2 != 0:
              result = number1/number2
            else:
               result = "Error: Division by zero!"

        else:
            result = "Operation not supported or invalid"
        
        return render_template('index.html', result=result)
           
        
if __name__ == '__main__':
    app.run(debug=True)










