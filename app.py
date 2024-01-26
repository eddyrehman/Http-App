from flask import Flask, request, abort
import os

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    n = request.args.get('n')
    m = request.args.get('m')

    if not n:
        abort(400, "Parameter n is required.")

    file_path = os.path.join('/tmp/data', f"{n}.txt")

    try:
        if m:
            # Read specific line
            content = read_line(file_path, int(m))
        else:
            # Read entire file
            content = read_entire_file(file_path)

        return content
    except FileNotFoundError:
        abort(404, f"File {n}.txt not found.")
    except Exception as e:
        print(f"Error: {e}")
        abort(500, "Internal Server Error")

def read_line(file_path, line_number):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return lines[line_number - 1] if line_number <= len(lines) else ''

def read_entire_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

if __name__ == '__main__':
    app.run(port=8080)