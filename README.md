## **AI-Powered Deadlock Detection System 🚀**  
A fully AI-automated backend for detecting deadlocks in real time using machine learning. This system analyzes process-resource allocation graphs and predicts potential deadlocks efficiently.  

---

### **📌 Features**  
✅ **Real-time Deadlock Detection** – Uses ML models to predict deadlocks from process-resource graphs.  
✅ **Graph-based Visualization** – (Future scope) Enhances understanding with 3D interactive graphs.  
✅ **REST API** – Allows external systems to interact with the deadlock detection engine.  
✅ **Logging & Monitoring** – Tracks API requests and responses for debugging & analytics.  

---

## **📦 Project Structure**  
```
AI-Powered-Deadlock-Detection-System/
│── backend/
│   ├── server.py           # Flask API for handling requests
│   ├── deadlock_detector.py # Core logic for deadlock detection
│── ML/
│   ├── synthetic_data.py   # Generates synthetic process-resource graphs
│   ├── train_model.py      # Trains ML model to predict deadlocks
│── README.md               # Documentation
│── requirements.txt        # Dependencies

 **⚡ Installation & Setup**  

 **🔹 Prerequisites**
- Python 3.10+
- Flask
- NumPy, Pandas, NetworkX
- Scikit-learn

### **🔹 Install Dependencies**
```bash
pip install -r requirements.txt
```

### **🔹 Run the API Server**
```bash
python backend/server.py
```
The API runs at `http://127.0.0.1:5000/`

### **🔹 Generate Dataset**
```bash
python ML/synthetic_data.py
```

### **🔹 Train ML Model**
```bash
python ML/train_model.py
```

---

## **🔗 API Endpoints**  

| Method | Endpoint           | Description |
|--------|--------------------|-------------|
| `GET`  | `/`                | Check if API is running |
| `POST` | `/add_process`     | Add a process requesting a resource |
| `POST` | `/add_resource`    | Allocate a resource to a process |
| `GET`  | `/detect_deadlock` | Check if a deadlock exists |
| `GET`  | `/get_graph`       | Get process-resource graph |

**Example API Request (cURL)**:
```bash
curl -X POST http://127.0.0.1:5000/add_process -H "Content-Type: application/json" -d '{"process_id": "P1", "resource_id": "R1"}'
```

---

## **📊 Future Improvements**  
🔹 **Real-time Deadlock Monitoring Dashboard**  
🔹 **Database Integration for Persistent Storage**  
🔹 **Advanced ML Models for Better Predictions**  
🔹 **Containerization (Docker, Kubernetes)**  

---

## **🛠 Contributors**  
- **Kashvi** – Developer & Architect
- **Yathartha** – Developer & Architect
- **Soumya Sewtangi** – Developer & Architect 

