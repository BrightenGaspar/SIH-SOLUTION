# 🚀 SIH Telemetry Command Center v3.5

Real-time Smart India Hackathon (SIH) Problem Statement Tracker, Analytics HUD, and Telemetry Command Center with **340+ Official Problem Statements**, 0.5s WebSocket feeds, high-contrast capacity status indicators, and multi-faceted filtering.

---

## 🌟 Key Features

- **340+ Official Problem Statements:** Complete dataset covering all SIH categories (Software & Hardware), Ministries (MoRTH, DRDO, MoA&FW, MeitY, MoHFW, ISRO, NDMA, etc.), and official themes.
- **High-Visibility Color System:**
  - 🔴 **Completed / Frozen (500/500):** Crimson Red + Locked Badge (Closed).
  - ⚠️ **Warning: Closing Soon (400–499):** Flashing Glowing Amber + Live Remaining Slots countdown.
  - 🟢 **Open / Accepting (<400):** Emerald Green + Available slots indicator.
- **Fast Interactive Filtering:** Search by PS ID, Title, Ministry, Domain, or Tech Stacks (e.g. PyTorch, ROS, ESP32, Flutter).
- **Interactive Telemetry HUD:** Deep-dive into problem scope, technical stacks, capacity meters, and surge alerts.
- **Shortlist & Bookmarks:** Star problem statements with persistent local storage.
- **CSV Data Export:** 1-click export of the entire filtered or full catalog.
- **0.5s Real-Time WebSocket Telemetry:** Live stream from FastAPI backend.

---

## ⚡ Quick Start (1-Command Run)

### Method 1: Double-Click Launcher (Windows)
Double-click `run.bat` in the root folder.

### Method 2: Command Line / Antigravity Terminal
1. Clone the repository in Antigravity or any terminal:
   ```bash
   git clone https://github.com/BrightenGaspar/SIH-SOLUTION.git
   cd SIH-SOLUTION/"SIH SOLUTION"
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Launch the server:
   ```bash
   python server.py
   ```

4. Open your browser at:
   **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 📁 Repository Structure

```
SIH SOLUTION/
├── index.html                   # Holographic Cyberpunk Frontend Dashboard
├── server.py                    # FastAPI Real-time WebSocket Backend & API
├── problem_statements.json      # 340+ Official Problem Statements Dataset
├── build_authentic_sih_data.py  # Dataset Generator & Updater Script
├── requirements.txt             # Python Dependencies
├── run.bat                      # Windows One-Click Launcher
└── README.md                    # Documentation & Instructions
```
