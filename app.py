from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>DevOps Project</h1>
    <h2>Hello from Kubernetes + Docker + Jenkins</h2>
    """

@app.route("/health")
def health():
    return {
        "status": "UP"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)