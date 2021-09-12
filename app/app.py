# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model_temp = pickle.load(open('app/delhi_house.pkl', 'rb'))


@app.route('/', methods = ["GET", "POST"])
def hello():
    request_type = request.method
    if(request_type=="GET"):
        return render_template("app/interface.html")
    else:
        input_list = []
        size = request.form["size"]
        input_list.append(size)
        location = request.form["location"]
        input_list.append(location)
        bedrooms = request.form["bedrooms"]
        input_list.append(bedrooms)
        resale = request.form["resale"]
        input_list.append(resale)
        if(request.form.get("staff")):
            input_list.append(1)
        else:
            input_list.append(0)
        if(request.form.get("gym")):
            input_list.append(1)
        else:
            input_list.append(0)
        if(request.form.get("pool")):
            input_list.append(1)
        else:
            input_list.append(0)
        if(request.form.get("garden")):
            input_list.append(1)
        else:
            input_list.append(0)
        if(request.form.get("harvesting")):
            input_list.append(1)
        else:
            input_list.append(0)
        if(request.form.get("games")):
            input_list.append(1)
        else:
            input_list.append(0)
        if(request.form.get("intercom")):
            input_list.append(1)
        else:
            input_list.append(0)
        if(request.form.get("security")):
            input_list.append(1)
        else:
            input_list.append(0)
        if(request.form.get("backup")):
            input_list.append(1)
        else:
            input_list.append(0)
        if(request.form.get("parking")):
            input_list.append(1)
        else:
            input_list.append(0)
        if(request.form.get("quarter")):
            input_list.append(1)
        else:
            input_list.append(0)
        if(request.form.get("utility")):
            input_list.append(1)
        else:
            input_list.append(0)
        if(request.form.get("play")):
            input_list.append(1)
        else:
            input_list.append(0)
        if(request.form.get("lift")):
            input_list.append(1)
        else:
            input_list.append(0)
        if(request.form.get("bed")):
            input_list.append(1)
        else:
            input_list.append(0)
        if(request.form.get("dining")):
            input_list.append(1)
        else:
            input_list.append(0)
        if(request.form.get("sofa")):
            input_list.append(1)
        else:
            input_list.append(0)
        if(request.form.get("wardrobe")):
            input_list.append(1)
        else:
            input_list.append(0)
        if(request.form.get("fridge")):
            input_list.append(1)
        else:
            input_list.append(0)

        input_1 = np.array([input_list])

       
        pred= model_temp.predict(input_1)
        price2 = str("₹{:,.2f}".format(round(pred[0])))
        return render_template("app/interface.html", price1 = price2)

if __name__ == "__main__":
    app.run(debug=False)
        
