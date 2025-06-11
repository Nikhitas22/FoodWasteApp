
# 🍽️ Food Waste Management System

This Streamlit web application helps manage and reduce food wastage by connecting **food providers** (like restaurants, caterers) with **receivers** (like NGOs, orphanages). It provides real-time data filtering, visualizations, SQL insights, and full CRUD operations on food donations.

---

## 🚀 Features

- 📊 **Data Overview** — Charts and filters by location, provider type, and food type
- 📈 **SQL Insights** — 24 pre-defined SQL queries for powerful analytics
- 🧾 **CRUD Operations** — Add, view, update, and delete data from 4 core tables:
  - `providers`
  - `receivers`
  - `foodlistings`
  - `claims`
- 📍 Filter food donations by city and category
- 🖼️ Interactive UI with banner, layout-wide view, and charts

---

## 🏗️ Tech Stack

- `Python`
- `Streamlit`
- `PostgreSQL`
- `psycopg2`
- `pandas`, `matplotlib`, `plotly`

---

## 📁 Project Structure

```
FoodWasteApp_FinalDeploy/
│
├── app.py                         # Main app entry point
├── utils.py                       # Database utility functions
├── fwm.png                        # Banner image
├── requirements.txt               # Python dependencies
├── README.md                      # This file
├── pages/
│   ├── 1_Project_Introduction.py
│   ├── 2_Data_Overview.py
│   ├── 3_SQL_Insights.py
│   ├── 4_Contact_Information.py
│   ├── 5_CRUD_Operations.py
│   └── 6_Creator_Information.py
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository or download ZIP:

```bash
git clone https://github.com/Nikhitas22/FoodWasteApp_FinalDeploy.git
cd FoodWasteApp_FinalDeploy
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Make sure PostgreSQL is running and update your DB credentials inside `utils.py`:

```python
def get_connection():
    return psycopg2.connect(
        dbname="foodmws",
        user="postgres",
        password="Nikhita@22",
        host="localhost",
        port="5432"
    )
```

### 4. Run the app:

```bash
streamlit run app.py
```

---

## 📬 Contact

- 👩 Developer: Nikhita
- 🌐 GitHub: [Nikhitas22](https://github.com/Nikhitas22)

---

## ✅ License

This project is open-source and free to use.
