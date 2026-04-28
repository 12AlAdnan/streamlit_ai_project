import streamlit as st
from api_calling import note_generator,audio_transcription,quiz_generation
from PIL import Image

st.title("Note Sumary and Quiz Generator")
st.markdown("Upload upto 3 images to generate Note summary and Quizes")
st.divider()

with st.sidebar:
    st.header("Controls")

    #work with images

    images = st.file_uploader(
        "uplode the photos of your notes",
        type=['jpg','jpge','png'],
        accept_multiple_files=True
    )

    pil_images = []

    for img in images:
     pil_img = Image.open(img)
     pil_images.append(pil_img)

    if images:
        if len(images)>3:
            st.error("Upload at max 3 images")
        else:

            st.subheader("Uploaded images")

            col = st.columns(len(images))

            for i, img in enumerate(images):
                with col[i]:
                    st.image(img)

    #difficulty
    selected_option = st.selectbox(
        "Enter The Difficulty Of Your Quiz",
        ("Eassy","Medium","Heard"),
        index = None
    )

    pressed = st.button("Click The Button To Intiate AI",type="primary")


if pressed:
    if not images:
        st.error("You must uplode 1 image")
    if not selected_option:
        st.error("You must select a Difficulty")

    if images and selected_option:
        # note

        with st.container(border=True):
            st.subheader("Your Note")

            with st.spinner("Generating Notes for you"):
                generated_notes = note_generator(pil_images)
                st.markdown(generated_notes)

        # Audio transcipt

        with st.container(border=True):
            st.subheader("Audio Transciption")


        with st.spinner("Generating Audio for you"):

            # clearing some mark down
            generated_notes = generated_notes.replace("#","")
            generated_notes = generated_notes.replace("*","")
            generated_notes = generated_notes.replace("-","")
            generated_notes = generated_notes.replace("`","")


            audio_transcript = audio_transcription(generated_notes)
            st.audio(audio_transcript)
        
        # the protion below will be replaced by API Call

        with st.container(border=True):
            st.subheader(f"Quiz {selected_option}")

        with st.spinner("Generating Quizzes for you"):
            quizzes = quiz_generation(pil_images,selected_option)

            st.markdown(quizzes)