import streamlit as st
from PIL import Image
from model import generate_caption_with_hashtags

st.set_page_config(page_title="AI-Based Image Caption Generator", layout="centered")
st.title("🖼️ AI-Based Image Caption Generator")

option = st.radio("Choose Input Type:", ("Upload Image", "Enter Description"))

if option == "Upload Image":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        if st.button("Generate Caption"):
            caption, hashtags = generate_caption_with_hashtags(image=image)
            if isinstance(caption, list):
                st.success("Generated Captions:")
                for idx, cap in enumerate(caption, 1):
                    st.markdown(f'**{idx}.** {cap}')
            else:
                st.success("Generated Caption:")
                st.write(caption)

            
            if hashtags:
                st.markdown(f"**Hashtags:** {hashtags}")

elif option == "Enter Description":
    description = st.text_area("Enter a short description:")
    if st.button("Generate Caption") and description:
        caption, hashtags = generate_caption_with_hashtags(description=description)
        if isinstance(caption, list):
            st.success("Generated Captions:")
            for idx, cap in enumerate(caption, 1):
                st.markdown(f'**{idx}.** {cap}')
        else:
            st.success("Generated Caption:")
            st.write(caption)

            
        if hashtags:
            st.markdown(f"**Hashtags:** {hashtags}")
        