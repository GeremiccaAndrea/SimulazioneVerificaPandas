from flask import Flask, request, render_template
app = Flask(__name__)

import pandas as pd 
df = pd.read_excel("https://github.com/tommella90/milano-housing-price/blob/main/milano_housing_02_2_23.xlsx?raw=true")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Es1')
def Es1():
    quartiere = request.args.get('quartiere')
    appartamentiQuartiere = df[df["neighborhood"] == quartiere].sort_values(by= 'date')[['neighborhood', 'price', 'date']].to_html()
    return render_template('risultato.html', tabella = appartamentiQuartiere)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)