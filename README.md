<h1 align="center">
  Face-Rate
</h1>

<p align="center">
  Face-Rate is a web application that predicts a facial attractiveness score (1–5) for uploaded images using a custom-trained PyTorch model.  
</p>

---

## Overview
This project demonstrates end-to-end deployment of a deep learning model in a real-world web environment:  

- **Model Development**: Built and trained a convolutional neural network in **PyTorch** using the [SCUT-FBP500 V2 dataset](https://www.kaggle.com/datasets/pranavchandane/scut-fbp5500-v2-facial-beauty-scores). Training and experimentation were conducted in Google Colab (the notebook is included in this repository).  
- **Web Application**: Designed a lightweight frontend with **HTML**, **CSS**, and **JavaScript**.  
- **Deployment**: Containerized the application with **Docker** and deployed it on **AWS Elastic Container Service (ECS)** for scalable hosting.  

---

## Webpage Preview
<p align="center">
  <img width="390" height="500" alt="Face-Rate Screenshot" src="https://github.com/user-attachments/assets/66dd2188-47d1-439c-8b2b-164440fd9cc7" />
</p>

---

## Live Demo
🔗 Try it out here: [Face-Rate Web App](http://18.188.152.65/)  
*(Best viewed on desktop; currently not optimized for mobile.)*

---

## Repository Contents
- `model_training.ipynb` – Colab notebook for model training and evaluation  
- `frontend/` – Website files (HTML, CSS, JS)  
- `backend/` – FastAPI/Docker deployment logic  
