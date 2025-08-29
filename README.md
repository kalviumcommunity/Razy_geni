# Car AI Agent

A complete CLI-based Car Intelligence Automation System that combines Prompting, RAG (Retrieval-Augmented Generation), Structured Output, and Function Calling to assist with car maintenance, trip planning, performance optimization, and driving analytics.

---

## 🚀 Features

### 🛠️ Smart Maintenance Planner

* Generates **Now-Next-Later maintenance schedules** as structured JSON
* Recommends optimal servicing windows based on mileage, time, and usage patterns
* Balances urgent fixes with preventive maintenance

### 🏎️ Trip Optimizer

* Uses RAG to retrieve **past trip data** for context
* Suggests optimal routes, refueling stops, and driving tips
* Generates structured trip plans with distance, cost, and estimated time
* Considers fuel efficiency, weather, and traffic data

### ⛽ Fuel & Cost Tracker

* Tracks **fuel consumption and expenses** from CSV logs
* Analyzes efficiency trends by driving style, road type, and speed
* Updates recommendations to save money and maximize mileage

### ⏰ Smart Scheduler

* Assigns trips and maintenance to **optimal time slots**
* Prevents conflicts with pre-planned trips
* Validates schedules against driver availability

### 📊 Driving Analytics Ingester

* Reads trip/fuel/maintenance logs from CSV
* Analyzes performance trends: mileage, service cost, breakdown frequency
* Generates structured reports and insights

### 💬 Driving Coach (Framework)

* Suggests safe driving practices based on past data
* Identifies high-risk patterns (speeding, harsh braking, etc.)
* Helps improve fuel economy and driving behavior

---

## 🏗️ Architecture

```
car-agent/
├── cli/               # Command handlers
│   ├── plan.py        # Maintenance & trip planning
│   ├── optimize.py    # Trip optimization
│   ├── schedule.py    # Task scheduling
│   └── metrics.py     # Driving analytics
├── core/              # Business logic
│   ├── scheduler.py   # Time & task optimization
│   ├── prompting.py   # AI-driven recommendations
│   ├── retrieval.py   # RAG system for past data
│   └── schemas.py     # JSON validation
├── data/              # Persistent storage
│   ├── trips/         # Historical trip data
│   ├── fuel/          # Fuel & expense logs
│   ├── maintenance/   # Service & repair logs
│   └── schedules/     # Trip & maintenance plans
└── config.json        # Configuration
```

---

## 🛠️ Installation

```bash
# Clone and setup
git clone <repository>
cd car-agent

# Install dependencies
pip install -r requirements.txt

# Initialize workspace
python car.py init
```

---

## 📖 Usage Examples

### 1. Generate Maintenance Plan

```bash
# Create a Now-Next-Later maintenance plan
python car.py plan --accept  

# Include performance-based suggestions
python car.py plan --suggest  

# Plan for specific mileage
python car.py plan --mileage 25000
```

### 2. Optimize Trip

```bash
# Optimize a city trip
python car.py optimize "Bangalore to Mysore" --mode city  

# Plan a highway trip
python car.py optimize "Delhi to Jaipur" --mode highway  

# Preview without saving
python car.py optimize "Weekend trip" --preview
```

### 3. Schedule Tasks

```bash
# Queue trip for optimal time
python car.py schedule trip.json  

# Override driving time
python car.py schedule trip.json --time "Sat 07"  

# Preview scheduling
python car.py schedule trip.json --preview
```

### 4. Analyze Performance

```bash
# Import fuel metrics from CSV
python car.py metrics --import fuel.csv  

# Show performance summary
python car.py metrics --since 30d --summary  

# Export analysis
python car.py metrics --export report.json
```

### 5. Driving Insights

```bash
# Get safety recommendations
python car.py coach trip.json  

# Process driving analytics
python car.py coach --schedule schedule.json
```

---

## 📁 Data Formats

### CSV Fuel/Trip Format

```
trip_id,distance_km,fuel_liters,cost,in_city,avg_speed,started_at
trip_001,350,25,2300,false,80,2025-08-10T06:00:00Z
trip_002,45,3.5,310,true,25,2025-08-12T09:00:00Z
```

### Generated Trip Plan Structure

```json
{
  "id": "trip_abc123",
  "route": "Bangalore → Mysore",
  "distance_km": 150,
  "fuel_estimate": 10,
  "cost_estimate": 900,
  "target_window": {"day": "Sat", "hour": 7},
  "source_snippets": [
    {"trip_id": "trip_001", "reason": "similar distance & terrain"}
  ]
}
```

### Weekly Maintenance Plan Structure

```json
{
  "week_of": "2025-08-25",
  "now": [
    {
      "task": "Oil change",
      "priority": "high",
      "target_window": {"day": "Tue", "hour": 9}
    }
  ],
  "next": [...],
  "later": [...]
}
```

---

## ⚙️ Configuration

Edit `config.json` to customize:

```json
{
  "car_model": "Toyota Fortuner 2022",
  "fuel_type": "Diesel",
  "topics": ["maintenance", "fuel", "driving"],
  "tone": "practical, concise, safe",
  "windows": [
    {"day": "Sat", "hour": 7},
    {"day": "Sun", "hour": 8}
  ],
  "experiment_spread_hours": 2,
  "manual_mode": true
}
```

---

## 🔄 Workflow

* **Plan:** `car plan --accept` → Generate weekly trip & maintenance strategy
* **Optimize:** `car optimize "trip"` → Create optimized routes & plans using RAG
* **Schedule:** `car schedule trip.json` → Assign tasks to best time slots
* **Coach:** `car coach trip.json` → AI-generated safe driving tips
* **Analyze:** `car metrics --import data.csv` → Learn from fuel & trip data

---

## 🎯 Key Design Principles

* **Manual-first:** Operates on local data, outputs copy-paste ready plans
* **RAG-grounded:** Every recommendation references similar past trips/logs
* **Schema-validated:** All outputs comply with defined JSON schemas
* **Performance-informed:** Recommendations improve based on real metrics
* **Modular:** Clean separation between CLI, core logic, and data

---

## 🔮 Future Enhancements

* Direct integration with **car OBD-II data**
* Real-time **fuel price API** integration
* **A/B testing** of trip routes for fuel efficiency
* Automated **service reminders** via notifications
* Integration with **navigation apps** (Google Maps, Waze)

---

## 📊 Analytics Features

The system tracks and analyzes:

* Fuel efficiency by trip type (city vs highway)
* Maintenance cost trends
* Best time windows for long drives
* High-risk driving patterns for safer recommendations

This creates a **self-improving system** that gets smarter with every trip logged.

---

## 🎥 Video Demonstration

A video walkthrough of the project will cover:

1. **Project Overview**: Explaining the purpose and features of the Car AI Agent.
2. **Technical Implementation**: Demonstrating the CLI commands and their outputs.
3. **Use Cases**: Showcasing real-world scenarios like trip optimization and driving analytics.
4. **Future Enhancements**: Discussing planned features like OBD-II integration and fuel price APIs.