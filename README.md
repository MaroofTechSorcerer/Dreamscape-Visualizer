
# 🌌 Dreamscape Visualizer (HD)

A beginner-friendly **text-to-image dream generator** using **Stable Diffusion XL** and an interactive **Streamlit** UI — designed to turn your imagination into high-quality visuals.

---

## ✨ Features

- 🪄 Generate HD images with **Stable Diffusion XL (SDXL)**
- 🎨 Choose from 5 styles: *Fantasy*, *Sci-Fi*, *Mythical*, *Nightmare*, *Lucid*
- ⚡ Simple UI built using Streamlit
- ⬇️ Download generated images with a single click
- ☁️ Cloud-compatible: Run it on Google Colab or Hugging Face Spaces

---

## 📸 Screenshots

### Prompt Input Interface

![Prompt UI](screenshots/app_homepage.png)

### Generated Dream Output

![Dream Output](screenshots/generated_output.png)

> Add your screenshots in a folder called `screenshots/`.

---

## 💬 Example Prompt

"A city floating in the sky made of crystals and glowing neon trees, with robotic birds flying above."  
Style: Sci-Fi

Result: A stunning, dreamlike HD image

---

## 🗂️ Folder Structure

```
dreamscape-visualizer/
├── app.py               # Main Streamlit application
├── requirements.txt     # Required dependencies
├── README.md            # Documentation file
└── screenshots/         # UI screenshots (add manually)
```

---

## 🖥️ Local Setup

💡 Use Google Colab or Hugging Face Spaces if you don’t have a good GPU.

1. **Clone the repository**  
```bash
git clone https://github.com/yourusername/dreamscape-visualizer.git
cd dreamscape-visualizer
```

2. **Install dependencies**  
```bash
pip install -r requirements.txt
```

3. **Run the app**  
```bash
streamlit run app.py
```  
Then open in your browser: [http://localhost:8501](http://localhost:8501)

---

## ⚙️ Requirements

- Python 3.8+  
- PyTorch with CUDA support (if running locally)  
- `diffusers`, `transformers`, `accelerate`, `safetensors`  
- A GPU with 10GB+ VRAM (or run on cloud)

---

## 🧰 Technologies Used

| Tool         | Purpose                        |
|--------------|--------------------------------|
| Streamlit    | Frontend UI                    |
| SDXL         | Image generation engine        |
| Hugging Face | Model hosting and inference    |
| PyTorch      | Deep learning framework        |

---

## 🔮 Planned Features

- 🖼️ Image history/gallery  
- 🎛️ Style customization sliders  
- 🧠 Prompt templates & suggestions  
- 🎥 Prompt-to-video mode (experimental)

---

## 🙏 Acknowledgements

- Stability AI – creators of SDXL  
- Hugging Face – model & hosting  
- Streamlit – app UI framework

---

## 📜 License

This project is licensed under the MIT License — free to use and remix for personal & educational use.
