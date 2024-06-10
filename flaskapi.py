from flask import Flask, jsonify, request
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from flask_cors import CORS


app = Flask(__name__)
CORS(app, origins="http://localhost:3000")



@app.route('/generate_graph', methods=['POST'])
def generate_graph():
    # Get data from the request body
    # data = request.json.get('data')

    # if not data:
    #     return jsonify({'error': 'Data not provided in the request body'}), 400
    
    points = [
    { 'x': 21, 'y': 63550.54945809429 },
    { 'x': 22, 'y': 63101.58062960831 },
    { 'x': 23, 'y': 62592.86768150468},
    { 'x': 24, 'y': 62064.937849835915 },
    { 'x': 25, 'y':  61540.09870230193},
    { 'x': 26, 'y': 61016.55730059251 },
    { 'x': 27, 'y':   60490.12329174257},
    { 'x': 28, 'y':  59958.36852501197},
    { 'x': 29, 'y': 59421.08467804466 },
    { 'x': 30, 'y':  58880.89456345447},
    { 'x': 1, 'y':  58335.40076658658},
    { 'x': 2, 'y': 57787.51297018444 },
    { 'x': 3, 'y': 57235.516783711435 },
   
    ]

    x = [21,22,23]
    y = [63800,64900,67000]
    response_data = {'xpoints': x, 'ypoints': y}
    return jsonify(response_data)

#     # Create a bar graph
#     plt.bar(range(len(data)), data)
#     plt.xlabel('X-axis Label')
#     plt.ylabel('Y-axis Label')
#     plt.title('Sample Graph')

#     # Save the plot to a BytesIO object
#     buffer = BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)

#     # Convert the plot to base64 string
#     base64_image = base64.b64encode(buffer.getvalue()).decode('utf-8')

#     # Close the plot to free up memory
#     plt.close()

   

if __name__ == '__main__':
    app.run(debug=True)
