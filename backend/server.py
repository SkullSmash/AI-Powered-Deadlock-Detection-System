from flask import Flask, jsonify
from deadlock_detector import DeadlockDetector

app = Flask(__name__)

detector = DeadlockDetector()
# Simulating a deadlock scenario
detector.add_process("P1", "R1")
detector.add_resource("R1", "P2")
detector.add_process("P2", "R2")
detector.add_resource("R2", "P3")
detector.add_process("P3", "R3")
detector.add_resource("R3", "P1")  # Circular dependency

@app.route("/get-graph", methods=["GET"])
def get_graph():
    deadlock, cycle = detector.detect_deadlock()
    
    nodes = [{"id": node} for node in detector.graph.nodes()]
    links = [{"source": u, "target": v} for u, v in detector.graph.edges()]

    return jsonify({"graph": {"nodes": nodes, "links": links}, "deadlock": deadlock, "cycle": cycle})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
