[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/1jDm7-Ue)
# LAB-2: Data Scraping using Scrapy and Data Preprocessing

**Course:** DS605 Fundamentals of Machine Learning  
**Academic Year:** 2025-26 (Autumn)  

---

## 📌 Objective
This lab guides you through:
1. Extracting data from a website using the **Scrapy** framework.
2. Cleaning and preparing the scraped data for analysis using **pandas**.

---

## 📖 What is Scrapy?
**Scrapy** is a fast, powerful, and open-source Python framework for building web crawlers (spiders). It enables you to:
- Extract data from websites.
- Process and clean the data.
- Save it in formats like CSV, JSON, or databases.

Unlike simple libraries, Scrapy provides a **complete architecture** for crawling, following links, and processing data efficiently using an **asynchronous** workflow.

---

## 🏗 Scrapy Architecture
- **Scrapy Engine** – Controls data flow between components.
- **Scheduler** – Manages the queue of URLs to crawl.
- **Downloader** – Fetches web pages.
- **Spiders** – Your custom classes to define crawling and data extraction logic.
- **Item Pipelines** – Process, clean, validate, and store scraped data.

---

## ⚙️ Prerequisites
- Python 3.x installed.
- Basic understanding of Python and HTML.
- `pip` installed in your terminal/command prompt.

---

## 🔹 Setting Up the Environment
```bash

python3 -m venv venv

source venv/bin/activate      # On Linux/Mac

venv\Scripts\activate         # On Windows

pip install scrapy 