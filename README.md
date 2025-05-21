## Summary

We designed and implemented a simple user-friendly library management system.

This project was developed as part of a Data Science & AI bootcamp.

---

## Languages and Libraries Used

- **Frontend:** Streamlit
- **Backend:** Python with SQLAlchemy
- **Database:** MySQL with stored procedures
- **Development Tools:** VS Code, Git, MySQL Workbench

## Key Learnings

- Practice writing MySQL stored procedures for real-world logic
- Separate data access logic (via stored routines) from frontend code
- Use Git for version control and feature branching
- Create clean and minimal UI

## Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/lianes_simplest_library.git
cd lianes_simplest_library
```

### 2. Set Up Python Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure Environment

```ini
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=SimplestLib
```

### 4. Set Up Database

- Use schema.sql to create the schema and tables
- Use procedures.sql to define stored routines

### 5. Run the App

```bash
cd app
streamlit run app.py
```