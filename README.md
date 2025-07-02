# Excel Filter App

A simple Flask web application that allows users to upload an Excel file, filters the data into "VA" and "Non-VA" sheets (with an optional "Local" sheet), and returns a filtered Excel file for download.

## Features
- Upload `.xls` or `.xlsx` Excel files via a web interface
- Automatically filters rows into "VA" and "Non-VA" sheets based on the first column
- Download the filtered Excel file with separate sheets
- Easy to deploy (Heroku/Render/other platforms)

## How It Works
1. User uploads an Excel file through the web form
2. The app processes the file and filters rows:
    - Rows where the first cell is `FLUVFL` (optional, currently commented out)
    - Rows where the fourth character of the first cell is `V` go to the "VA" sheet
    - All other rows go to the "Non-VA" sheet
3. The user downloads the filtered Excel file

## Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd excelFilter
   ```
2. **Create a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the app locally:**
   ```bash
   python onlineDoclineFilter.py
   ```
   The app will be available at [http://localhost:5000](http://localhost:5000)

2. **Upload an Excel file:**
   - Open your browser and go to [http://localhost:5000](http://localhost:5000)
   - Use the form to upload your Excel file
   - Download the filtered file returned by the app

## Example
- Upload an Excel file with your data
- The app will return a file with two sheets: `VA` and `Non-VA`

## Deployment

This app can be deployed to platforms like Heroku or Render. The included `Procfile` is suitable for such deployments:

```
web: python onlineDoclineFilter.py
```

## Requirements
See `requirements.txt` for the full list of dependencies.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change. 