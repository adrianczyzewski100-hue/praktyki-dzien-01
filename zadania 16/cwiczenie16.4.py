from flask import Flask

app = Flask(__name__)

@app.route('/tickets')
def tickets():
    ticket_list = [ 'ticket 1', 'ticket 2', 'ticket 3' ] 
    return ticket_list

if __name__ == '__main__':
    app.run(debug=True)