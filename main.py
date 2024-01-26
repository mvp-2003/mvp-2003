import os
from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def count_views():
    count = int(os.getenv("VIEW_COUNT", 0))
    os.environ["VIEW_COUNT"] = str(count + 1)
    return Response(f'<svg><text x="0" y="15">{count}</text></svg>', mimetype='image/svg+xml')

if __name__ == "__main__":
    app.run()