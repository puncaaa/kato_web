# 🏥 KATO — Official Website of the Kazakhstan Association of Traumatology and Orthopaedics  
Django-based web platform for publishing medical news, scientific publications, and event information.

## 📌 Overview
This project is a full-featured website developed for **КАТО — Казахстанская Ассоциация Травматологии и Ортопедии**.  
The purpose of the platform is to provide a modern, professional online presence for the association, including:

- News and announcements  
- Conferences and medical events  
- Scientific publications and downloadable materials  
- Static informational pages (About, Membership, Contacts)  
- Contact form for inquiries  

The entire functionality is implemented **within a single Django app** for simplicity and maintainability.

---

## 🧱 Tech Stack

**Backend**
- Python 3.x  
- Django 4.x  
- SQLite (development) / PostgreSQL (production)

**Frontend**
- Django Templates  
- Bootstrap 5  
- Custom CSS  

**Other**
- Django Admin for full content management  
- Media storage for images & PDF files  

---

## 📂 Project Structure

project_root/
│
├── core/ # Django project settings and config
├── website/ # Main application containing all logic
│ ├── models.py # News, Events, Publications, Contact models
│ ├── views.py
│ ├── urls.py
│ ├── templates/ # HTML templates using base.html
│ ├── static/ # CSS, JS, images
│
├── media/ # Uploaded images and PDF files
├── manage.py
└── README.md



## 📰 Features

### **1. Home Page**
- Hero banner with association info  
- Latest news preview  
- Upcoming events section  
- Short "About Us" block  

---

### **2. News Module**
- List of all news with pagination  
- Category filtering  
- Detailed article page  
- Image support  
- Full CRUD in Django Admin  

**Models:**  
`News`, `NewsCategory`

---

### **3. Events & Conferences**
- Upcoming and past events separation  
- Detailed event page  
- Program PDF download  
- Optional event image  
- Managed through Django Admin  

**Model:**  
`Event`

---

### **4. Scientific Publications**
- List of all publications  
- Filtering by category and year  
- Detailed view with PDF download  
- Categories managed in admin  

**Models:**  
`Publication`, `PublicationCategory`

---

### **5. Static Pages**
- About  
- Membership  
- Contacts (with form)  
- Simple template-based pages  

---


📜 License
This project is private and developed specifically for КАТО.

👤 Author
Alen Pak
