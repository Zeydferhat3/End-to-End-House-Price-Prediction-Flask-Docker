from flask import Flask, request, render_template
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
from sklearn.preprocessing import StandardScaler, LabelEncoder

application = Flask(__name__)
app = application

# Route for a home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for predicting data
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            area=int(request.form.get('area')),
            bedrooms=int(request.form.get('bedrooms')),
            bathrooms=int(request.form.get('bathrooms')),
            stories=int(request.form.get('stories')),
            mainroad=request.form.get('mainroad'),
            guestroom=request.form.get('guestroom'),
            basement=request.form.get('basement'),
            hotwaterheating=request.form.get('hotwaterheating'),
            airconditioning=request.form.get('airconditioning'),
            parking=int(request.form.get('parking')),
            prefarea=request.form.get('prefarea'),
            furnishingstatus=request.form.get('furnishingstatus')
        )
        pred_df = data.get_data_as_data_frame()

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        return render_template('home.html', results=results[0])

if __name__ == "__main__":
    app.run(host="0.0.0.0")
