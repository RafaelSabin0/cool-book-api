from flask import jsonify, Blueprint, request
from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()

book_routes = Blueprint('book_routes', __name__)


db = mysql.connector.connect(
    host=os.environ.get('DB_HOST'),
    port=os.environ.get('DB_PORT'),
    user=os.environ.get('DB_USER'),
    password=os.environ.get('DB_PASSWORD'),
    database=os.environ.get('DB_NAME')
)

cursor = db.cursor()


@book_routes.route('/book', methods=['GET'])
def get_book():
    try:
        cursor.execute("Select * From books")
        columns = [col[0] for col in cursor.description]
        books = [dict(zip(columns, row)) for row in cursor.fetchall()]
        db.commit()
        return jsonify(books)
    except Exception as e:
        print("🚨 Error 🚨: ", e)
        return jsonify({'🚨 Oops 🚨': 'Internal Server Error',}), 500



@book_routes.route('/book/<int:id>', methods=['GET'])
def get_book_by_id(id):
    try:
        cursor.execute(f"Select * From books where id = {id}")
        columns = [col[0] for col in cursor.description]
        book = [dict(zip(columns, row)) for row in cursor.fetchall()]
        db.commit()
        return jsonify(book)
    
    except Exception as e:
       print("🚨 Error 🚨: ", e)
       return jsonify({'🚨 Oops 🚨': 'Internal Server Error',}), 500 

@book_routes.route('/book/create', methods=['POST'])
def add_book():
    request_data = request.json
  
    if not request_data:
        return jsonify({"🚨 Oops 🚨": "Check if the request body is valid and try again"}), 400
    
    title = request_data.get('title')
    author = request_data.get('author')
    price = request_data.get('price')
    
    try:
        cursor.execute(f'INSERT INTO `books` (`id`, `title`, `author`, `price`) VALUES (NULL, "{title}", "{author}", "{price}");')
        db.commit()

        response_data = {
            '✅ Success ✅': 'New Book Added!',
            'Book Info':{
            'title': title,
            'author': author,
            'price': price
            }
        }

        return jsonify(response_data)
    
    except Exception as e:
        print("🚨 Error 🚨: ", e)
        return jsonify({'🚨 Error 🚨': 'Internal Server Error'}), 500  
    

@book_routes.route('/book/update', methods=['PUT'])
def update_book():
    request_data = request.json

    book_id = request_data.get('id')
    title = request_data.get('title')
    author = request_data.get('author')
    price = request_data.get('price')

    if not request_data:
        return jsonify({'🚨 Oops 🚨': 'Check if the request body is valid and try again'}), 400
    
    if not book_id or not title or not author or not price:
            return jsonify({'🚨 Oops 🚨': 'Check that all fields are included in the request and try again!'}), 400
    if len(title) <0 or len(author) <0 or len(price) <0:
            return jsonify({'🚨 Oops 🚨': 'Check that all fields are filled in correctly and try again!'}), 400
        
    try:
        cursor.execute(f'UPDATE `books` SET `title` = "{title}", `author` = "{author}", `price` = "{price}" WHERE `books`.`id` = {book_id};')
        db.commit()

        response_data = {
            '✅ Success ✅': 'Book Updated!',
            'Book':{
            '_id': book_id,
            'title': title,
            'author': author,
            'price': price
            }
        }

        return jsonify(response_data) 
    
    except Exception as e:
        print("🚨 Error 🚨: ", e)
        return jsonify({'🚨 Error 🚨': 'Internal Server Error'}), 500
    
@book_routes.route('/book/update_price', methods=['PUT'])
def update_book_price():
     request_data = request.json

     try:
        if not request_data:
             return jsonify({'🚨 Oops 🚨': "The requested information can't be empty"})
     
        book_id = request_data.get('id')
        price = request_data.get('price')

        if not book_id:
             return jsonify({'🚨 Oops 🚨': "It's necessary to inform the book ID!"})

        cursor.execute(f'UPDATE `books` SET `price` = "{price}" WHERE `books`.`id` = {book_id};')
        db.commit()

        #Consulting book information to show as result
        cursor.execute(f"Select * From `books` where id = {book_id}")
        columns = [col[0] for col in cursor.description]
        book_info = [dict(zip(columns, row)) for row in cursor.fetchall()]
        db.commit()

        return jsonify({'✅ Price Updated Successfully! ✅': book_info})
    
     except Exception as e:
        print("🚨 Error 🚨: ", e)
        return jsonify({'🚨 Error 🚨': 'Internal Server Error'}), 500

     
@book_routes.route('/book/delete/<int:id>', methods=['DELETE'])
def delete_book_by_id(id):
    try:
        if not id:
            return jsonify({'🚨 Oops 🚨': "It's necessary to inform the book ID"})
        
        #Getting the book info to show the information deleted in the end
        cursor.execute(f"Select * From `books` where id = {id}")
        columns = [col[0] for col in cursor.description]
        book_info = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        #Removing item by id:
        cursor.execute(f"DELETE FROM books WHERE `books`.`id` = {id};")
        db.commit()

        return jsonify({'🗑️ Book Deleted 🗑️': book_info})
    
    except Exception as e:
        print("🚨 Error 🚨: ", e)
        return jsonify({'🚨 Error 🚨': 'Internal Server Error'}), 500


