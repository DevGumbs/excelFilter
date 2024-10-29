from flask import Flask, request, render_template, send_file
import pandas as pd
import io
import os

app = Flask(__name__)

@app.route('/')
def upload_file():
    return '''
    <html><body>
    <h1>Excel Filter App</h1>
    <form action="/filter" method="post" enctype="multipart/form-data">
        <label for="file">Select Excel file:</label>
        <input type="file" name="file" accept=".xls,.xlsx"><br><br>
        <button type="submit">Submit</button>
    </form>
    </body></html>
    '''

@app.route('/filter', methods=['POST'])
def filter_data():
    file = request.files['file']
    df = pd.read_excel(file)

    # Apply filtering logic as in the previous code
    local, va, non_va = [], [], []
    for _, row in df.iterrows():
        first_item = str(row.iloc[0])
        if first_item == "FLUVFL":
            local.append(row.tolist())
        elif len(first_item) > 3 and first_item[3] == "V":
            va.append(row.tolist())
        else:
            non_va.append(row.tolist())

    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        #comment out local field
        # pd.DataFrame(local).to_excel(writer, sheet_name="Local", index=False) 
        pd.DataFrame(va).to_excel(writer, sheet_name="VA", index=False)
        pd.DataFrame(non_va).to_excel(writer, sheet_name="Non-VA", index=False)

    output.seek(0)
    return send_file(output, as_attachment=True, download_name="filtered_data.xlsx", mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Default to port 5000 if not specified
    app.run(host='0.0.0.0', port=port, debug=True)  # Use debug=True only for development
