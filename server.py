from flask import Flask, request, jsonify
import products_dao
import uom_dao
import orders_dao
import json
from sql_connection import get_sql_connection

app = Flask(__name__)

connection = get_sql_connection()
@app.route('/getproducts',methods=['GET'])

def get_products():
    products=products_dao.get_all_products(connection)
    response=jsonify(products)
    response.headers.add('Access-Control-Allow-origin','*')
    return response

@app.route('/getUOM',methods=['GET'])
def get_uom():
    response=uom_dao.get_uoms(connection)
    response=jsonify(response)
    response.headers.add('Access-Control-Allow-origin', '*')
    return response
@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = orders_dao.get_all_orders(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orders_dao.insert_order(connection, request_payload)
    response = jsonify({
        'order_id': order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/deleteproduct',methods=['POST'])

def delete_product():
    return_id=products_dao.delete_product(connection,request.form['product_id'])
    response=jsonify({'product_id':return_id})
    response.headers.add('Access-Control-Allow-origin','*')
    return response

@app.route('/insertproduct',methods=['POST'])

def insert_product():
    request_payload=json.loads(request.form['product_id'])
    product_id = products_dao.insert_new_product(connection,request_payload)
    response=jsonify({'product_id':product_id})
    response.headers.add('Access-Control-Allow-origin','*')
    return response


# main driver function
if __name__ == "__main__":
    print("Starting python flask server fot Grocery store management")
    app.run(port=5000)