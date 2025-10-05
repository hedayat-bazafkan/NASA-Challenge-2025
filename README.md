# 🌌 NASA Space Apps Challenge 2025 — A World Away: Hunting for Exoplanets with AI

**Project Name:** StarChain ExoDetector  
**Author:** Hedayat Bazafkan  
**Website:** [starchain.wiki](https://starchain.wiki)  
**Repository:** https://github.com/hedayat-bazafkan/NASA-Challenge-2025

---

## 🧭 Overview

This project was developed for the **NASA Space Apps Challenge 2025** under the theme  
**"A World Away: Hunting for Exoplanets with AI"**.

It leverages **machine learning** and **AI-assisted data processing** to detect potential **exoplanets** from NASA's open-source datasets (Kepler, K2, and TESS missions).  
The system is fully containerized using **Docker** and exposes a REST API that can be integrated into web platforms like WordPress for interactive analysis.

---

## 🚀 Features

- 🧠 **AI/ML Model** — Trained to classify exoplanets, candidates, and false positives  
- 🌍 **API Interface** — Exposes `/predict` endpoint for real-time predictions  
- ⚙️ **Dockerized Deployment** — Simple one-command setup  
- 🔗 **WordPress Integration** — Uses REST API plugin to connect with your web interface  
- 🧩 **Modular Design** — Easily extendable with new datasets or ML methods

---

## 📂 Project Structure


---

## 🧮 Algorithm Summary

### Step 1: Data Collection
NASA’s open datasets:
- [Kepler cumulative data](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=cumulative)
- [K2 candidates](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=k2pandc)
- [TESS Objects of Interest (TOI)](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=TOI)

### Step 2: Preprocessing
- Handle missing values  
- Normalize numeric features  
- Feature selection: orbital period, radius ratio, transit depth, etc.

### Step 3: Model Training
- ML Algorithm: **Random Forest Classifier**  
- Training split: 80% training / 20% validation  
- Evaluation: F1-score, precision, recall  

### Step 4: Prediction API
- Built with **FastAPI**  
- `/predict` endpoint accepts JSON input  
- Returns: `confirmed`, `candidate`, or `false positive`

---

## 🐳 Quick Start (Local Setup)

### 1. Clone the Repository
```bash
git clone https://github.com/hedayat-bazafkan/NASA-Challenge-2025.git
cd NASA-Challenge-2025


