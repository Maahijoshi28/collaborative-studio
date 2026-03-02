Collaborative Studio: Real-Time Whiteboard
A high-performance, web-based collaborative studio that allows multiple users to sketch, brainstorm, and create on a shared digital whiteboard in real-time. Designed to solve the challenge of remote synchronization, this project utilizes Event-Driven Architecture and WebSockets to ensure zero-latency communication between connected clients.

🚀 Key Features
Real-Time Sync: Instantaneous drawing synchronization across all connected clients.

Customizable Workspace:

Color Palette selector for dynamic strokes.

Adjustable brush sizes for precision.

Emoji Stamp Tool (Sticker system).

Collaboration Tools:

Live canvas clearing.

Export-to-Image functionality for session saving.

Responsive Design: Built with Tailwind CSS for a modern, dark-themed professional interface.

🛠️ Technical Stack
Backend: Flask (Python) with flask-socketio.

Frontend: HTML5 Canvas, Tailwind CSS, JavaScript (ES6+).

Communication: WebSockets (Full-duplex, low-latency).

Deployment: Gunicorn / Eventlet (for production readiness).

⚙️ How to Run Locally
Clone the repository:

Bash
git clone <your-repo-link>
cd flaskwith-sqlite
Install dependencies:

Bash
pip install flask flask-socketio eventlet
Launch the Server:

Bash
python app.py
Access the Application:
Open http://127.0.0.1:5000 in multiple browser windows to test the real-time collaboration.

🧠 Architectural Justification
This project demonstrates Distributed State Synchronization. Unlike traditional REST APIs that rely on periodic polling, this application uses WebSocket Full-Duplex communication.

The server acts as a Message Broker, processing incoming events (coordinates, color data, emoji inputs) and broadcasting them to all clients, ensuring the system state remains consistent across all sessions in real-time.
