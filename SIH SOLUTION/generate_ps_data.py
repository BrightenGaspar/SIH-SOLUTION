import json
import random

# SIH Real Problem Statement Templates & Themes
ministries_and_domains = [
    {
        "ministry": "Ministry of Agriculture & Farmers Welfare",
        "domain": "Agriculture & FoodTech",
        "templates": [
            ("AI-Driven Multi-Crop Disease Diagnosis from Drone & Smartphone Imagery", "Software", ["PyTorch", "OpenCV", "FastAPI", "Flutter", "Edge AI"]),
            ("IoT Soil Macronutrient (NPK) & pH Sensor Telemetry with Autonomous Irrigation", "Hardware", ["ESP32", "LoRaWAN", "Embedded C", "MQTT", "Grafana"]),
            ("Blockchain Farm-to-Fork Traceability & Fair Price Escrow System", "Software", ["Solidity", "Ethereum", "Node.js", "IPFS", "React"]),
            ("Autonomous Solar-Powered Agro-Rover for Selective Weed Eradication", "Hardware", ["ROS2", "Jetson Nano", "YOLOv8", "Motor Drivers", "LiDAR"]),
            ("Predictive Satellite Harvest Yield & Mandi Dynamic Price Forecasting", "Software", ["Python", "XGBoost", "Sentinel-2 API", "PostgreSQL", "Next.js"]),
            ("Smart Cold Storage Microclimate & Perishable Decay Predictor", "Hardware", ["Raspberry Pi", "DHT22", "Gas Sensors", "Python", "InfluxDB"]),
            ("Crowdsourced Pest Outbreak Early Warning System with Geospatial Clustering", "Software", ["GIS", "GeoPandas", "Django", "React Native", "Mapbox"]),
            ("Automated Grain Quality Assessment Scanner Using Hyperspectral Vision", "Hardware", ["Spectroscopy", "Raspberry Pi 4", "TensorFlow Lite", "Python"])
        ]
    },
    {
        "ministry": "Ministry of Road Transport and Highways (MoRTH)",
        "domain": "Transportation & Smart Vehicles",
        "templates": [
            ("Computer Vision Automated Pothole & Road Hazard Detection with GPS Geotagging", "Software", ["YOLOv10", "FastAPI", "React", "Leaflet", "Docker"]),
            ("V2X Intelligent Collision Warning & Blind Spot Radar Node for Highways", "Hardware", ["C-V2X", "ESP32", "CAN-Bus", "Ultrasonic", "C++"]),
            ("AI-Adaptive Traffic Light Signal Optimization via Real-time Camera Feeds", "Software", ["Python", "OpenCV", "Deep Reinforcement Learning", "FastAPI"]),
            ("Smart On-Board Driver Drowsiness & Distraction Alert System", "Hardware", ["Jetson Nano", "OpenCV", "dlib", "Buzzer/Vibration Module"]),
            ("Overload & Axle Weight Screening for Commercial Vehicles using Piezo Sensors", "Hardware", ["Load Cells", "Arduino Mega", "RF Transceivers", "C++"]),
            ("Emergency Vehicle Corridor Green Wave Automation using GPS & DSRC", "Software", ["Kafka", "WebSockets", "Go", "PostGIS", "React"]),
            ("Automated EV Fleet Battery Health Degradation & Thermal Runaway Predictor", "Software", ["Python", "LSTM", "Battery Management System", "Flask"])
        ]
    },
    {
        "ministry": "Ministry of Defence / DRDO",
        "domain": "Cybersecurity & Defense",
        "templates": [
            ("Anti-Rogue Drone Acoustic & RF Signal Fingerprinting Interception Hub", "Hardware", ["SDR (RTL-SDR)", "GNU Radio", "Raspberry Pi", "Machine Learning"]),
            ("Zero-Trust AI Threat Intelligence & Malware Sandboxing Platform", "Software", ["Rust", "FastAPI", "eBPF", "Suricata", "Elasticsearch"]),
            ("Secure Tactical Mesh Radio Ad-Hoc Network for GPS-Denied Environments", "Hardware", ["LoRa", "ESP32-S3", "ECDSA Cryptography", "C++"]),
            ("Deepfake Video & Audio Forensic Detection Engine for National Security", "Software", ["PyTorch", "FaceForensics++", "Flask", "React", "FFmpeg"]),
            ("Autonomous Soldier Biometric Telemetry & Dehydration Vitals Vest", "Hardware", ["MAX30102", "ECG Sensor", "LoRaWAN", "Embedded C"]),
            ("Quantum-Resistant Post-Quantum Cryptographic VPN & Tunneling Suite", "Software", ["Kyber", "Dilithium", "Go", "WireGuard API", "C"]),
            ("Automated Vulnerability Scanner & Exploit Mitigation Engine for SCADA", "Software", ["Python", "Scapy", "Nmap Engine", "Angular", "Docker"])
        ]
    },
    {
        "ministry": "Ministry of Health & Family Welfare (MoHFW)",
        "domain": "MedTech & HealthCare",
        "templates": [
            ("Portable Non-Invasive Anemia & Jaundice Screener using Optical Spectroscopy", "Hardware", ["Photodiode", "ARM Cortex-M4", "Bluetooth BLE", "Flutter"]),
            ("AI Radiology Companion for Chest X-Ray Pneumonia & TB Screening", "Software", ["DenseNet121", "PyTorch", "DICOM", "FastAPI", "React"]),
            ("Real-time Hospital ICU Bed & Oxygen Logistics Allocation Grid", "Software", ["Go", "Redis", "WebSockets", "Vue.js", "PostgreSQL"]),
            ("Smart Wearable Tremor Suppressor for Parkinson's Disease Patients", "Hardware", ["IMU MPU6050", "Micro-Actuators", "STM32", "C++"]),
            ("Automated Tele-Triage Chatbot in 12 Regional Indian Languages", "Software", ["LangChain", "Llama 3", "Whisper ASR", "FastAPI", "Next.js"]),
            ("Counterfeit Medicine Verification via Hologram Micro-Texture Vision", "Software", ["OpenCV", "TensorFlow", "React Native", "MongoDB"]),
            ("IoT Cold-Chain Vaccine Storage Temp & Power Interruption Guardian", "Hardware", ["DS18B20", "GSM Module", "ESP32", "Cloud MQTT"])
        ]
    },
    {
        "ministry": "Ministry of Jal Shakti / Water Resources",
        "domain": "Water Management & Clean Tech",
        "templates": [
            ("Autonomous Surface Drone for River Debris & Microplastic Harvesting", "Hardware", ["Pixhawk", "Solar MPPT", "Camera Vision", "ROS2"]),
            ("IoT Smart Water Distribution Telemetry with Acoustic Pipe Leak Detection", "Hardware", ["Piezo Vibration Sensors", "LoRaWAN", "ESP32", "Python"]),
            ("Groundwater Table Depletion Forecaster using Sentinel-1 Radar Imagery", "Software", ["Google Earth Engine", "Python", "Prophet", "MapLibre"]),
            ("Real-time Industrial Effluent Quality Compliance HUD with Alarm Alerts", "Software", ["FastAPI", "InfluxDB", "Grafana", "TimescaleDB", "React"]),
            ("Smart Rainwater Harvesting & Greywater Recycling Micro-Controller", "Hardware", ["Relay Matrix", "Flow Meters", "Arduino", "C++"]),
            ("AI Algal Bloom & Eutrophication Early Detection in Reservoirs", "Software", ["MODIS Imagery", "PyTorch", "GeoServer", "Next.js"])
        ]
    },
    {
        "ministry": "Ministry of Electronics and Information Technology (MeitY)",
        "domain": "AI/ML & GovTech",
        "templates": [
            ("AI Semantic Document Parsing & Fraud Detection for Govt Welfare Portals", "Software", ["LayoutLMv3", "Tesseract OCR", "FastAPI", "PostgreSQL"]),
            ("Multimodal Voice-First Public Grievance Redressal Assistant in Indic Dialects", "Software", ["Bhashini API", "Whisper", "LangGraph", "React"]),
            ("Decentralized Sovereign Identity (DID) & Zero-Knowledge Credential Issuer", "Software", ["Polygon ID", "ZKP-Snarks", "Ethers.js", "NestJS"]),
            ("Real-time Deep Packet Inspection for Cyber Threat & Botnet Mitigation", "Software", ["DPDK", "Rust", "C++", "Prometheus", "FastAPI"]),
            ("Crowdsourced High-Resolution Street Light & Civil Asset Mapping App", "Software", ["Flutter", "OpenStreetMap", "Python", "PostGIS"]),
            ("Edge AI Privacy-Preserving Facial Verification for Pension Distribution", "Hardware", ["K210 Edge AI", "ESP32-CAM", "Thermal Sensor", "C++"])
        ]
    },
    {
        "ministry": "Ministry of Education / AICTE",
        "domain": "EdTech & Smart Education",
        "templates": [
            ("Adaptive Gamified Coding & STEM Learning Platform for Rural Schools", "Software", ["React", "Python Sandbox", "WebAssembly", "Node.js"]),
            ("AI Proctoring System with Multi-Head Pose & Secondary Device Detection", "Software", ["MediaPipe", "YOLOv8", "WebRTC", "FastAPI", "React"]),
            ("Automated Assessment of Handwritten Student Answer Scripts using OCR", "Software", ["Vision Transformers", "TrOCR", "FastAPI", "PostgreSQL"]),
            ("Interactive 3D Virtual Science Lab Simulations in WebXR", "Software", ["Three.js", "WebGL", "WebXR", "React", "Blender"]),
            ("AI Career Counseling & Skill Gap Recommendation Engine for Graduates", "Software", ["Graph Neural Networks", "FastAPI", "Neo4j", "Next.js"])
        ]
    },
    {
        "ministry": "Ministry of Power & Renewable Energy (MNRE)",
        "domain": "Renewable Energy & Smart Grid",
        "templates": [
            ("Micro-Grid Rooftop Solar Power Trading Marketplace via Smart Contracts", "Software", ["Solidity", "Web3.js", "Node.js", "TimescaleDB"]),
            ("AI Thermal Hotspot Detection on Solar PV Arrays via Drone Thermography", "Software", ["Thermal YOLO", "OpenCV", "Python", "FastAPI"]),
            ("Smart Inverter IoT Controller for Grid Frequency Stabilization", "Hardware", ["STM32F4", "Current Transducers", "CAN", "Embedded C"]),
            ("Wind Turbine Blade Structural Vibration & Crack Prognostics System", "Hardware", ["MEMS Accelerometers", "ESP32-S3", "Edge ML", "LoRa"]),
            ("AI Battery Energy Storage System (BESS) Peak Shaving Optimization", "Software", ["MILP Optimization", "Python", "FastAPI", "Grafana"])
        ]
    },
    {
        "ministry": "Ministry of Housing and Urban Affairs (MoHUA)",
        "domain": "Smart Cities & Waste Management",
        "templates": [
            ("AI Smart Trash Sorting Bin with Auto Segregation of Wet/Dry/E-Waste", "Hardware", ["Raspberry Pi", "Servo Actuators", "MobileNetV3", "C++"]),
            ("Urban Heat Island Mapping & Green Roof Planning GIS Simulator", "Software", ["Landsat 8 LST", "GeoPandas", "FastAPI", "Deck.gl"]),
            ("Smart City Parking Space Allocator with Ultrasonic Array & App Booking", "Hardware", ["ESP8266", "Ultrasonic Sensors", "MQTT", "Flutter"]),
            ("Civic Garbage Overflow Predictor for Municipal Waste Compactor Trucks", "Software", ["Time Series Forecasting", "Python", "React", "Mapbox"]),
            ("Real-time Acoustic Noise Pollution Sensor Grid & Decibel Violation Map", "Hardware", ["I2S Mic Module", "ESP32", "ThingsBoard", "C++"])
        ]
    },
    {
        "ministry": "Indian Space Research Organisation (ISRO)",
        "domain": "Space Technology & Satellite Data",
        "templates": [
            ("AI Satellite SAR Imagery Deforestation & Illegal Mining Sentinel", "Software", ["PyTorch", "SAR Interferometry", "FastAPI", "PostGIS"]),
            ("CubeSat Low-Power Edge Object Tracker with Radiation-Hardened MCU", "Hardware", ["FPGA Zynq", "Verilog", "Vitis AI", "C++"]),
            ("Automated Near-Earth Orbital Debris Conjunction Warning Visualizer", "Software", ["SGP4 Orbit Propagator", "CesiumJS", "Python", "WebGL"]),
            ("Hyperspectral Ocean Chlorophyll & Cyclone Cloud Top Height Profiler", "Software", ["Python", "Xarray", "NetCDF4", "Dask", "Next.js"])
        ]
    },
    {
        "ministry": "National Disaster Management Authority (NDMA)",
        "domain": "Disaster Management & Emergency Response",
        "templates": [
            ("AI Flash Flood Inundation & Evacuation Route Simulator", "Software", ["HEC-RAS API", "DEM Analysis", "Python", "React Leaflet"]),
            ("Post-Earthquake Collapsed Building Survivor Localization Bioradar", "Hardware", ["UWB Radar 24GHz", "DSP Processor", "Python", "Bluetooth"]),
            ("Autonomous Forest Fire Detection Drone with Thermal Camera & Payload Drop", "Hardware", ["ArduPilot", "FLIR Thermal", "Jetson Orin", "ROS2"]),
            ("Emergency Mesh SOS Beacon with Offline SMS Gateway Relay", "Hardware", ["LoRa SX1262", "OLED Display", "ESP32", "Android App"]),
            ("Landslide Early Warning Inclinometer & Pore Pressure Telemetry Node", "Hardware", ["MEMS Inclinometer", "Solar Panel", "LoRaWAN", "C++"])
        ]
    },
    {
        "ministry": "Ministry of Tourism / Ministry of Culture",
        "domain": "Heritage & Tourism",
        "templates": [
            ("Interactive AR Historical Monument Restoration & Virtual Tour Guide", "Software", ["Unity", "ARKit/ARCore", "WebXR", "3D Gaussian Splatting"]),
            ("AI Heritage Temple Carving Epigraphy & Ancient Script Transliteration", "Software", ["Vision Transformers", "OCR", "FastAPI", "React"]),
            ("Smart Tourism Crowd Density & Queuing Management System", "Software", ["YOLOv8", "DeepSORT", "FastAPI", "Tailwind CSS"]),
            ("Audio-Guided Multilingual Geofenced Smart Museum Navigator", "Software", ["BLE Beacons", "Flutter", "Text-to-Speech", "Node.js"])
        ]
    }
]

# Generate over 320 distinct problem statements with realistic variations
problem_statements = []
ps_counter = 1001

# Distribute submission counts realistically:
# ~25% FROZEN (500), ~35% CRITICAL (350-499), ~40% OPEN/MODERATE (20-349)

prefixes = [
    "AI-Powered", "Next-Gen", "Autonomous", "Decentralized", "Cloud-Native",
    "Real-Time", "Edge-Computing", "Smart", "Intelligent", "Automated",
    "High-Precision", "Integrated", "Low-Cost", "Predictive", "Secure"
]

suffixes = [
    "for Tier-2 & Rural Deployments", "with Offline Edge Resilience",
    "for High-Density Urban Clusters", "for Industrial Compliance",
    "with Live Telemetry HUD", "with Multilingual Voice Assistant",
    "using Low-Power Mesh Nodes", "with Automated Alert Dispatch",
    "with Cryptographic Integrity Check", "for Micro-Enterprise Workflows"
]

categories_pool = ["Software", "Hardware"]

for cycle in range(5):
    for group in ministries_and_domains:
        ministry = group["ministry"]
        domain = group["domain"]
        templates = group["templates"]
        
        for title, default_cat, tech in templates:
            if ps_counter > 1350:
                break
                
            # Variations per cycle
            if cycle == 0:
                final_title = title
                cat = default_cat
            elif cycle == 1:
                prefix = prefixes[(ps_counter * 3) % len(prefixes)]
                final_title = f"{prefix} {title}"
                cat = "Hardware" if "Hardware" in default_cat or "Sensor" in title or "Drone" in title else default_cat
            elif cycle == 2:
                suffix = suffixes[(ps_counter * 7) % len(suffixes)]
                final_title = f"{title} {suffix}"
                cat = "Software" if cycle % 2 == 0 else "Hardware"
            elif cycle == 3:
                prefix = prefixes[(ps_counter * 5) % len(prefixes)]
                suffix = suffixes[(ps_counter * 2) % len(suffixes)]
                final_title = f"{prefix} {title} {suffix}"
                cat = default_cat
            else:
                final_title = f"Advanced {title} Framework v{cycle}.0"
                cat = default_cat

            # Assign count based on realistic brackets
            rand_val = (ps_counter * 37 + cycle * 19) % 100
            if rand_val < 22:
                count = 500  # FROZEN
            elif rand_val < 55:
                count = 380 + ((ps_counter * 13) % 119)  # CRITICAL (380-499)
            else:
                count = 45 + ((ps_counter * 17) % 325)   # MODERATE/OPEN (45-370)

            # Generate realistic description
            desc = (
                f"Problem Statement #{ps_counter}: Address the critical bottleneck in {domain} by designing a "
                f"production-grade {cat.lower()} solution for {ministry}. "
                f"The system must demonstrate sub-second latency, robust error-handling, intuitive telemetry visualization, "
                f"and full interoperability with standard government public APIs and legacy field infrastructure."
            )

            ps_obj = {
                "id": f"PS{ps_counter}",
                "title": final_title,
                "ministry": ministry,
                "domain": domain,
                "category": cat,
                "count": count,
                "max_cap": 500,
                "tech_stack": tech,
                "complexity": "Hard" if count > 450 else "Medium" if count > 200 else "Easy",
                "description": desc,
                "starred": (ps_counter % 7 == 0)
            }
            problem_statements.append(ps_obj)
            ps_counter += 1

print(f"Generated {len(problem_statements)} Problem Statements (PS1001 to PS{ps_counter-1})")

# Write to problem_statements.json
output_path = "c:/Users/gaspa/OneDrive/Desktop/SIH SOLUTION/problem_statements.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(problem_statements, f, indent=2)

print(f"Successfully saved to {output_path}")
