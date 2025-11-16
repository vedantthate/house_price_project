# House Price Prediction Project

This project is a **Flask-based machine learning web application** that
predicts house prices using simplified inputs derived from the **Boston
Housing Dataset**.\
The model is trained using **Linear Regression** with four key features:

-   **DIS** -- Distance to Employment Centers\
-   **RM** -- Average Number of Rooms\
-   **RAD** -- Accessibility to Highways\
-   **NOX** -- Air Pollution Levels

The UI provides a beautiful, user-friendly interface with auto-fill
examples to help users understand input ranges.

------------------------------------------------------------------------

## 🚀 Project Features

### 🔹 Machine Learning

-   Linear Regression model
-   Trained on selected features from the Boston Housing Dataset
-   Prediction output originally in
    \*\*$1000 units**, later converted to: - Actual USD ($)
    -   Indian Rupees (₹)

### 🔹 Backend --- Flask

-   `/predict` API endpoint for ML inference
-   Serves the main UI page
-   JSON-based communication between frontend & backend

### 🔹 Frontend --- HTML, CSS, JavaScript

-   Fully responsive card-based UI
-   Auto-fill example buttons:
    -   City
    -   Suburban
    -   Rural
-   Input validation with helpful hints
-   Clean and modern layout

------------------------------------------------------------------------

## 📁 Project Structure

    house_price_project/
    │── model.pkl               # Trained ML model
    │── app.py                  # Flask backend
    │── templates/
    │     └── index.html        # Main frontend UI
    │── requirements.txt        # Required dependencies
    └── README.md               # Project documentation

------------------------------------------------------------------------

## 🔧 Installation & Setup

### 1️⃣ Clone the project

    git clone <your-repo-link>
    cd house_price_project

### 2️⃣ Create virtual environment

    python -m venv venv

### 3️⃣ Activate virtual environment

Windows:

    venv\Scripts\activate

Linux / Mac:

    source venv/bin/activate

### 4️⃣ Install dependencies

    pip install -r requirements.txt

### 5️⃣ Run Flask app

    python app.py

The project now runs at:\
👉 **http://127.0.0.1:5000**

------------------------------------------------------------------------

## 🧠 How the Prediction Works

The app uses only **4 features** from the dataset:

  Feature   Meaning                     Higher Value Effect
  --------- --------------------------- ---------------------
  DIS       Distance from job centers   ↓ Price
  RM        Number of rooms             ↑ Price
  RAD       Highway accessibility       ↑ Price
  NOX       Pollution level             ↓ Price

The model outputs price in **\$1000 units**, so:

    final_price = predicted_value * 1000
    price_in_inr = final_price * 85

------------------------------------------------------------------------

## 🌐 UI Auto-Fill Examples

### 🏙 City Example

-   DIS: 1.8\
-   RM: 6.0\
-   RAD: 12\
-   NOX: 0.60

### 🏡 Suburban Example

-   DIS: 4.8\
-   RM: 5.0\
-   RAD: 6\
-   NOX: 0.48

### 🌾 Rural Example

-   DIS: 10.2\
-   RM: 4.0\
-   RAD: 2\
-   NOX: 0.32

These help guide users to input realistic values.

------------------------------------------------------------------------

## 📦 Requirements

    Flask==3.0.3
    pandas==2.2.2
    numpy==1.26.4
    scikit-learn==1.4.2
    joblib==1.4.2

------------------------------------------------------------------------

## 📝 Author

**Damini Gudape**

------------------------------------------------------------------------

## 📣 Notes

-   Prices are approximate and **not real market prices**.
-   Prediction is for learning/demo purposes only.
