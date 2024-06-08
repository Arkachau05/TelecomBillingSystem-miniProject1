from flask import Flask, render_template, request

app = Flask(__name__)

class Customer:
    def __init__(self, name, phone_number, usage):
        self.name = name
        self.phone_number = phone_number
        self.usage = usage
        self.total_bill = usage * 0.15
customers = []

@app.route('/')
def index():
    return render_template('index.html', customers=customers)

@app.route('/add_record', methods=['POST'])
def add_record():
    name = request.form['name']
    phone_number = request.form['phone_number']
    usage = float(request.form['usage'])
    customer = Customer(name, phone_number, usage)
    customers.append(customer)
    return render_template('index.html', customers=customers)

@app.route('/modify_record', methods=['POST'])
def modify_record():
    phone_number = request.form['phone_number']
    for customer in customers:
        if customer.phone_number == phone_number:
            new_usage = float(request.form['new_usage'])
            customer.usage = new_usage
            customer.total_bill = new_usage * 0.1
            return render_template('index.html', customers=customers, message='Record modified successfully!')
    return render_template('index.html', customers=customers, message='Record not found!')

@app.route('/delete_record', methods=['POST'])
def delete_record():
    phone_number = request.form['phone_number']
    for customer in customers:
        if customer.phone_number == phone_number:
            customers.remove(customer)
            return render_template('index.html', customers=customers, message='Record deleted successfully!')
    return render_template('index.html', customers=customers, message='Record not found!')

if __name__ == '__main__':
    app.run(debug=True)
