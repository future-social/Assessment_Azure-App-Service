from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Read Table_Input.csv and process data
df = pd.read_csv('Table_Input.csv', delimiter=',')



@app.route('/')
def index():
    print(df.head())
    # Render Table 1
    table1_html = df.to_html(index=False, )

    # Calculate values for Table 2
    category_values = {
        'Alpha': df.loc[df['Index #'].isin(['A5', 'A20']), 'Value'].sum(),
        'Beta': df.loc[df['Index #'] == 'A15', 'Value'].values[0] / df.loc[df['Index #'] == 'A7', 'Value'].values[0],
        'Charlie': df.loc[df['Index #'] == 'A13', 'Value'].values[0] * df.loc[df['Index #'] == 'A12', 'Value'].values[0]
    }

    return render_template('index.html', table1=table1_html, category_values=category_values)

if __name__ == '__main__':
    app.run(debug=True)
