from flask import Flask, Response
import os

app = Flask(__name__)

@app.route("/")
def hello():
    count = int(os.getenv("VIEW_COUNT", 0))
    os.environ["VIEW_COUNT"] = str(count + 1)
    return Response(f'<svg><text x="0" y="15">{count}</text></svg>', mimetype='image/svg+xml')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)