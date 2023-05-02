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

@app.route('/Es2')
def Es2():
    quartieri = df[['neighborhood']].sort_values(by = 'neighborhood')
    senzaDuplicati = quartieri.drop_duplicates().to_html()
    return render_template('risultato.html', tabella = senzaDuplicati)

@app.route('/Es3')
def Es3():
    zona = request.args.get('zona')
    dfmedio = df[df['neighborhood'] == zona][['price']].mean()
    return render_template('risultato.html', tabella = dfmedio)

@app.route('/Es4')
def Es4():
    prezzoMedioQuartiere = df.groupby("neighborhood")[["price"]].mean().sort_values(by = 'price',ascending = False).to_html()
    return render_template('risultato.html', tabella = prezzoMedioQuartiere)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)