# 👕 Virtual Trial Room & Size Prediction System

A patent-published desktop application designed to simulate a **Virtual Fitting Room (VFR)** experience. This system predicts users’ apparel sizes and enables virtual garment try-ons using webcam images—enhancing accessibility, reducing trial room queues, and minimizing return rates in retail and e-commerce.

---

## 📌 Overview

This project leverages **pose estimation**, **image superimposition**, and **real-time processing** to deliver an interactive virtual try-on experience. By analyzing user body proportions via webcam or smartphone, the system predicts size and overlays garments virtually—eliminating the need for physical trials.

---

## 🎯 Motivation

Traditional apparel shopping poses several challenges:
- Long queues and limited changing room availability
- Size inconsistencies across brands
- Inaccessibility for differently-abled users
- High return rates in online retail

The VFR system addresses these by offering an efficient, digital, and inclusive alternative.

---

## ✨ Key Features

- **Size Prediction**: Calculates apparel size based on body geometry extracted from images.
- **Virtual Try-On**: Superimposes garments on the user’s image for visual assessment.
- **Brand-Agnostic Sizing**: Neutral to brand-specific size definitions.
- **Queue Reduction**: Reduces physical trial room congestion in retail.
- **Accessibility**: Offers independence to users with physical limitations.

---

## 🔄 System Workflow

1. The user stands in front of a camera at a predefined distance.
2. Pose estimation locates key body points (e.g., elbow joints).
3. The system calculates size based on joint distances.
4. The user selects garments from a menu.
5. The system overlays the garment on the user's image using superimposition.

---

## 📐 Size Prediction Logic

1. Capture image via webcam.
2. Apply pose estimation to detect elbow joints.
3. Measure distance between joints.
4. Map this value to a size label (S/M/L).
5. Output predicted size and preview try-on.

---

## 🛠 Tech Stack

- **Languages**: Python, MATLAB  
- **Libraries**: OpenCV, Tkinter  
- **Functionality**: Pose Estimation, Image Processing, GUI

---

## 📱 Applications

- **Retail Stores**: Reduce returns and fitting room congestion.
- **E-Commerce**: Enable try-before-you-buy online.
- **Fashion Industry**: Help designers test fit and aesthetics.
- **Accessibility**: Assist differently-abled shoppers.
- **Inventory Optimization**: Align sizes with real-time customer data.

---

## ⚠️ Constraints

- Requires user to maintain a fixed distance from the camera.
- Accurate operation needs a static, clutter-free background.
- Continuous power is necessary for real-time performance.

---

## 💻 Hardware Requirements

- Camera (Webcam or phone)
- Monitor for try-on preview
- Image processing-capable system
- Storage for images and logs

---

## 📄 Patent Info

This work is **patent-published** by the Government of India:  
**Application No.** 202121039172  
**Published in:** Indian Patent Journal (36/2021)  
**Date:** 3rd September 2021

---

## ✅ Conclusion

The Virtual Trial Room system bridges the gap between convenience and personalization in modern apparel shopping. It minimizes trial errors, streamlines customer journeys, and supports inclusive retail. Future enhancements could include garment recommendation engines and broader brand integration.

---

_For setup, usage instructions, or source files, refer to the codebase and scripts included in this repository._
