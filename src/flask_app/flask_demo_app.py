import json

import pandas as pd
import plotly.express as px
from flask import Flask, render_template
from plotly.utils import PlotlyJSONEncoder

app = Flask(__name__)


@app.route("/")
def index():
    DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
                'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
    df = pd.read_csv(DATA_URL, compression='gzip')
    df['Date/Time'] = pd.to_datetime(df['Date/Time'])
    df['hour'] = df['Date/Time'].dt.hour

    fig = px.histogram(df, x='hour', nbins=24, title='Uber rides by hour (Sep 2014)')
    plot_json = json.dumps(fig, cls=PlotlyJSONEncoder)
    plot_html = fig.to_html(include_plotlyjs='cdn', full_html=False)

    return render_template('index.html', plot_json=plot_json, plot_html=plot_html)


# Run the Flask app
# Runs by default on http://127.0.0.1:5000
if __name__ == '__main__':
    app.run(debug=True)