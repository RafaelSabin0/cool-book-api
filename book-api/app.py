from flask import Flask, request, jsonify
from routes.book_routes import book_routes


app =  Flask(__name__)


#get data
app.register_blueprint(book_routes)


app.run(port=5000, host='localhost', debug=True)