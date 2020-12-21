from flask import Flask,request,jsonify
from flask_api import status
from config import Config
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from utils import distance_diff_kms
import json

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
print(db)
migrate = Migrate(app, db)


class CompanyDetails(db.Model):
       __tablename__ = "CompanyDetails"
       id = db.Column(db.Integer(),primary_key = True)
       CompanyName = db.Column(db.String(255), nullable=False)
       Lat = db.Column(db.Float(), nullable=False)
       Long = db.Column(db.Float(), nullable=False)
       created_on = db.Column(db.DateTime(), default=datetime.utcnow)

       def __repr__(self):
              return '<CompanyName {}>'.format(self.CompanyName)

class ProductDetails(db.Model):
       __tablename__ = "ProductDetails"
       id = db.Column(db.Integer(), primary_key=True)
       CompanyName = db.Column(db.String(255), nullable=False)
       Lat = db.Column(db.Float(), nullable=False)
       Long = db.Column(db.Float(), nullable=False)
       productname = db.Column(db.String(255), nullable=False)
       productprice = db.Column(db.Float(), nullable=False)
       productdescription = db.Column(db.Text(), nullable=False)
       created_on = db.Column(db.DateTime(), default=datetime.utcnow)
       def __repr__(self):
              return '<Product_id {}>'.format(self.id)



@app.route('/productIntegrate',methods=["POST"])
def ProductIntegrateAPI():
    request_data = request.get_json()
    required_fields = ["CompanyName", "Location", "ProductList"]
    for key in required_fields:
        if key not in request_data:
            result = {"status": 400, "description": "%s is a mandatory field." % key}
            return jsonify(result),status.HTTP_404_NOT_FOUND
    try:
        print(request_data["Location"])
        company = CompanyDetails(CompanyName=request_data["CompanyName"],Lat=float(request_data["Location"]["lat"]),Long=float(request_data["Location"]["long"]))
        db.session.add(company)
        db.session.commit()
        for product in request_data["ProductList"]:
            product_list = ProductDetails(CompanyName=request_data["CompanyName"], Lat=float(request_data["Location"]["lat"]),
                                     Long=float(request_data["Location"]["long"]),productname=product["productname"],
                                    productprice = float(product["productprice"]),productdescription=product["productdescription"])
            db.session.add(product_list)
            db.session.commit()
        response = {"status": 200, "message": "Product Integrated  Successfully "}
        return response, status.HTTP_200_OK
    except Exception as e:
        print(e)
        return {"status": 500, "message": "Technical Error occurred Try again After some time"}

@app.route('/productList',methods=["GET"])
def GetProductList():
    request_data = request.get_json()
    required_fields = ["current_lat","current_long","product_name"]
    product_price = request_data.get("product_price")
    for key in required_fields:
        if key not in request_data:
            result = {"status": 400, "description": "%s is a mandatory field." % key}
            return jsonify(result),status.HTTP_404_NOT_FOUND
    try:
        product_List = []
        products = ProductDetails.query.all()
        for product in products:
            distance_diff = distance_diff_kms(request_data["current_lat"],request_data["current_long"],product.Lat,product.Long)
            print(distance_diff)
            if distance_diff < 40.0:
                if request_data["product_name"] == product.productname and product_price and product.productprice <= float(product_price):
                    product_List.append({"Company_Name": product.CompanyName, "productname": product.productname,
                                         "productprice": product.productprice,
                                         "productdescription": product.productdescription,"distance_diff":distance_diff})
                elif request_data["product_name"] == product.productname:
                    product_List.append({"Company_Name": product.CompanyName, "productname": product.productname,
                                         "productprice": product.productprice,
                                         "productdescription": product.productdescription,"distance_diff":distance_diff})
            else:
                continue
        if product_List:
            return jsonify({"result":product_List})
        else:
            return jsonify({"result": "No Product Found in nearest Locality"})
    except Exception as e:
        print(e)
        return {"status": 500, "message": "Technical Error occurred Try again After some time"}




if "__name__" == "__main__":
    app.run()