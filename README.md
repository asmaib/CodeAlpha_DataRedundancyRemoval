# Data Redundancy Checker

A simple Flask web application that allows users to input a value and check whether it already exists in the database (MongoDB Atlas) or not.
Built as part of the **CodeAlpha Internship Task 1**.

## 📌 Live Demo
🔗 [Visit the live site here](https://redundancy-checker.onrender.com)

---

## ✨ Features

- Add new data entries.
- Detect if data already exists in the database.
- Uses MongoDB Atlas for storage.
- Smooth button animation feedback based on status.
- Prevents duplicate entries.
- Shows success, warning, or error messages dynamically.
- Responsive and clean UI.
- Deployed on Render.
  
---

## 🛠️ Technologies Used

- **Python** 3.11
- **Flask** (Backend)
- **HTML/CSS** (Frontend)
- **MongoDB Atlas** (Database)
- **Render** (Deployment platform)

---

## 📁 Project Structure

CodeAlpha_DataRedundancyRemoval/
├── app.py # Flask application
├── requirements.txt # Python dependencies
├── render.yaml # Render deployment settings
├── templates/
│ └── index.html # HTML template
├── static/
│ └── style.css # Custom CSS

---

## ✅ How It Works

1. The user submits data using a form.
2. Flask checks MongoDB to see if the value exists.
3. Feedback is shown (success, warning, or error).
4. Button color animates from black → green/yellow/red based on the result.

---

## 📷 UI Preview
- Initial View  
The user is greeted with a minimal UI to enter data.

![Initial View](https://raw.githubusercontent.com/asmaib/CodeAlpha_DataRedundancyRemoval/main/assets/Screenshot 1.png)


- Data Added Successfully  
When a new unique value is entered.

![Success](https://raw.githubusercontent.com/asmaib/CodeAlpha_DataRedundancyRemoval/main/assets/Screenshot 2.png)

- Data Already Exists  
If the entered value is already present in the database.

![Warning](https://raw.githubusercontent.com/asmaib/CodeAlpha_DataRedundancyRemoval/main/assets/Screenshot 3.png)

- No Data Provided  
When the input field is left empty or only contains spaces.

![Error](https://raw.githubusercontent.com/asmaib/CodeAlpha_DataRedundancyRemoval/main/assets/Screenshot 4.png)

---

## 🧑‍💻 Author
Asma Alshilash
