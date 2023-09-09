from flask import Flask , request , render_template,jsonify
from src.pipeline.predication_pipeline import CustomData , PredictionPipeline
import pandas as pd



app = Flask(__name__)


@app.route('/')

def home_page():
    return render_template('home.html')

@app.route('/predict' , methods = ["GET" , "POST"])

def predict_datapoint():
    if request.method =='GET':
        return render_template('home.html')
        
    else:
       
        data = CustomData(
        Day=str(request.form.get('Day')),
        Vix = float(request.form.get('Vix')),
        Remaining_day = int(request.form.get('Remaining_day')),
        Moment_in_vix = float(request.form.get('Moment_in_vix')),
        Moment_in_price = float(request.form.get('Moment_in_price')),
        Option_type=str(request.form.get('Option_type'))
        
        )
        
      
        final_new_data = data.get_data_as_dataframe()
        predict_pipeline = PredictionPipeline()
        pred = predict_pipeline.predict(final_new_data)

        results = round(pred[0],2)

        return render_template('home.html' , final_result =(f"Spread:- {results}"))
    




if __name__ == '__main__':
    app.run(host = '0.0.0.0' , debug = True , port = 5000)