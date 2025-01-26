from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    plot_area = data.get('plot_area', 0)
    permissible_fsi = data.get('permissible_fsi', 0)
    tdr = data.get('tdr', 0)
    ancillary_fsi = data.get('ancillary_fsi', 0)

    # Perform calculations
    total_fsi = permissible_fsi + tdr + ancillary_fsi
    built_up_area = total_fsi * plot_area
    carpet_area = built_up_area * 0.8  # Assuming 80% efficiency

    return jsonify({
        "total_fsi": total_fsi,
        "built_up_area": built_up_area,
        "carpet_area": carpet_area
    })

if __name__ == '__main__':
    app.run(debug=True)
