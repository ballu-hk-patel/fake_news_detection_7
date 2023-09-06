from flask import Flask, abort, jsonify, request, render_template
import joblib
from feature import *
import json

# Model = joblib.load('model.pkl')
Model = joblib.load('Logisticmodel.pkl')
data=Model['model']
media=Model['data']
print(media.media.unique())



PEOPLE_FOLDER = os.path.join('static')
file = os.path.join(PEOPLE_FOLDER, "indeximage.png")
fact = os.path.join(PEOPLE_FOLDER, "fake-news.png")


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER


@app.route('/')
def home():
    return render_template("index.html",media=media.media.unique())


@app.route('/api',methods=['POST'])
def get_delay():
    
    result=request.form
    query_title = result['title']
    query_text = result['maintext']
    query_media=result['media']
    print(query_text)
    query = get_all_query(query_title, query_text)
    print(query)
    print(type(query))

    user_input = {'query':query}
    print(user_input)
    print(type(user_input))
    
    pred = data.predict(query)
    pred = data.predict(query)

    print(pred)
    dic = {1:'real',0:'fake'}
    ccor=int(pred[0])
    print(ccor)
    # return f'<html><body><h1>{dic[pred[0]]}</h1> <form action="/"> <button type="submit">back </button> </form></body></html>'
    return render_template("results.html",image=file,result=dic[pred[0]],media=media.media.unique(),fact=fact ,ccor=ccor)


if __name__ == "__main__":
    # app.run(host = '0.0.0.0',port = '8080')

    app.run(debug = True)

