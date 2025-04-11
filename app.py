import streamlit as st
from diffusers import AutoPipelineForText2Image
import torch
from io import BytesIO

st.set_page_config(page_title="Dreamscape Visualizer (Turbo)")
st.title("🌌 Dreamscape Visualizer")

@st.cache_resource
def load_pipeline():
    pipe = AutoPipelineForText2Image.from_pretrained(
        "stabilityai/sdxl-turbo",
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        variant="fp16" if torch.cuda.is_available() else None
    )
    pipe.to("cuda" if torch.cuda.is_available() else "cpu")
    return pipe

pipe = load_pipeline()

style_modifiers = {
    "Fantasy": "fantasy dream, ethereal, colorful",
    "Nightmare": "dark horror dream, creepy surreal",
    "Lucid": "hyperreal dream, bright, vivid",
    "Sci-Fi": "futuristic city, neon dream",
    "Mythical": "mythical world, god-like, celestial"
}

prompt = st.text_area("Describe your dream:")
style = st.selectbox("Choose a dream style:", list(style_modifiers.keys()))

if st.button("Generate Dream Image"):
    if not prompt.strip():
        st.warning("Please describe your dream first!")
    else:
        with st.spinner("Dreaming up your world..."):
            final_prompt = f"{prompt}, {style_modifiers[style]}"
            result = pipe(prompt=final_prompt, guidance_scale=0.0, num_inference_steps=2)
            image = result.images[0]
            st.image(image, caption="✨ Your Dream Visualized", use_column_width=True)

            # Convert image to bytes for download
            buf = BytesIO()
            image.save(buf, format="PNG")
            byte_im = buf.getvalue()

            st.download_button(
                label="📥 Download Dream Image",
                data=byte_im,
                file_name="dreamscape.png",
                mime="image/png"
            )
