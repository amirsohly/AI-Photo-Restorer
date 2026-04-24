---
title: My Photo Restorer
emoji: 📸
colorFrom: indigo
colorTo: green
sdk: gradio
sdk_version: 6.13.0
app_file: app.py
pinned: false
license: mit
python_version: 3.10.13
---

# 📸 AI Photo Restorer

A powerful, Deep Learning-based web application designed to restore, upscale, and reconstruct faces in old, blurry, and damaged photographs. This project leverages state-of-the-art Generative Adversarial Networks (GANs) to bring your vintage memories back to life.

## 🌟 Key Features

* **Face Restoration:** Accurate reconstruction of facial features (eyes, lips, skin texture) in heavily degraded images using the advanced `GFPGAN` model.
* **Background Upscaling:** Enhances the overall image resolution and clarity, removing digital noise using `Real-ESRGAN`.
* **User-Friendly Interface:** Built with `Gradio` to provide a seamless, intuitive experience requiring zero technical knowledge.
* **End-to-End Pipeline:** Fully automated processing—just upload an image and let the AI do the rest with a single click.

---

## 🛠 Tech Stack

This project is built using the following tools and architectures:

* **Programming Language:** Python 3.10+
* **Deep Learning Framework:** PyTorch
* **Core AI Models:** GFPGAN (Tencent ARC) & Real-ESRGAN
* **Computer Vision:** OpenCV (cv2)
* **Web UI Framework:** Gradio
* **Deployment:** Hugging Face Spaces & Docker

---

## 🚀 Local Installation

If you wish to run this application locally on your own machine, follow these steps:

**1. Clone the repository:**
```bash
git clone [https://github.com/your-username/AI-Photo-Restorer.git](https://github.com/your-username/AI-Photo-Restorer.git)
cd AI-Photo-Restorer
```

**2. Install dependencies:**
*(It is highly recommended to use a Virtual Environment)*
```bash
pip install -r requirements.txt
```

**3. Run the application:**
```bash
python app.py
```
Open your web browser and navigate to `http://127.0.0.1:7860`. *(Note: The required pre-trained model weights will be downloaded automatically upon the first run).*

---

## 💡 How it Works (Architecture)

This system utilizes a multi-stage processing pipeline:
1. The user uploads an image, which is pre-processed into a neural-network-friendly tensor format.
2. The `Real-ESRGAN` model processes the background, upscaling the overall resolution by 2x while aggressively reducing compression artifacts and noise.
3. The `GFPGAN` model detects bounding boxes for faces within the image. It uses rich generative priors (learned from millions of high-quality human faces) to restore missing or corrupted details while strictly preserving the person's identity.
4. The restored faces are seamlessly blended back into the upscaled background, and the final output is returned to the user.

---

## 🙏 Acknowledgements

This project builds upon the incredible open-source research provided by the AI community:
* [Tencent ARC GFPGAN](https://github.com/TencentARC/GFPGAN)
* [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN)
* [Gradio UI Framework](https://gradio.app)

---
*Developed with ❤️ by [Amirreza](https://www.linkedin.com/in/amirsohly/)*
```
