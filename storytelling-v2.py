import streamlit as st
from gtts import gTTS
import os
import time
from datetime import datetime
import tempfile
import base64
import streamlit.components.v1 as components

# Streamlit page configuration
st.set_page_config(
    page_title="Story Teller for Kids",
    page_icon="📖",
    layout="centered"
)

# Title and description
st.title("📖 Story Teller for Kids")
st.write("Write a fun story and let me read it aloud for your kids!")

# Store generated audio files for cleanup
if 'generated_files' not in st.session_state:
    st.session_state.generated_files = []

# Language selection
language = st.selectbox("Select Language / เลือกภาษา", ["English / อังกฤษ", "Thai / ไทย"])
lang_code = 'en' if language == "English / อังกฤษ" else 'th'

# Text area for story input
story_text = st.text_area(
    "Tell your story here / เขียนเรื่องราวของคุณที่นี่:",
    placeholder="Once upon a time... / กาลครั้งหนึ่งนานมาแล้ว...",
    height=300
)

# Flag to control cleanup button visibility
if 'show_cleanup' not in st.session_state:
    st.session_state.show_cleanup = False

# Button to generate speech
if st.button("Read Story Aloud! / อ่านเรื่องราวออกเสียง!"):
    if story_text.strip() == "":
        st.warning("Please write a story first! / กรุณาเขียนเรื่องราวก่อน!")
    else:
        with st.spinner("Generating story audio... / กำลังสร้างเสียงเรื่องราว..."):
            try:
                # Use temp directory for file
                temp_dir = tempfile.gettempdir()
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                audio_file = os.path.join(temp_dir, f"story_{timestamp}.mp3")
                
                # Generate audio with gTTS using selected language
                tts = gTTS(text=story_text, lang=lang_code, slow=False)
                tts.save(audio_file)
                
                # Increased delay to ensure file is fully written
                time.sleep(3)
                
                # Check if file exists and has content
                if os.path.exists(audio_file):
                    file_size = os.path.getsize(audio_file)
                    st.write(f"Audio file created at: {audio_file}")
                    st.write(f"File size: {file_size} bytes")
                    
                    if file_size > 1000:  # Ensure it’s not empty
                        st.success("Story audio generated! / เสียงเรื่องราวถูกสร้างแล้ว!")
                        
                        # Read the audio file
                        with open(audio_file, 'rb') as f:
                            audio_bytes = f.read()
                        
                        # HTML audio player
                        st.write("Playing with HTML audio player... / กำลังเล่นด้วยเครื่องเล่นเสียง HTML...")
                        audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')
                        audio_html = f"""
                        <audio controls>
                            <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
                            Your browser does not support the audio element.
                        </audio>
                        """
                        components.html(audio_html, height=50)
                        
                        # Download button
                        st.download_button(
                            label="Download and Play MP3 / ดาวน์โหลดและเล่น MP3",
                            data=audio_bytes,
                            file_name=f"story_{timestamp}.mp3",
                            mime="audio/mp3"
                        )
                        
                        # Store file for cleanup and show cleanup button
                        st.session_state.generated_files.append(audio_file)
                        st.session_state.show_cleanup = True
                    else:
                        st.error("Audio file is too small or empty. Generation failed. / ไฟล์เสียงเล็กเกินไปหรือว่างเปล่า ล้มเหลวในการสร้าง.")
                else:
                    st.error("Audio file wasn’t created. Check internet or permissions. / ไม่สามารถสร้างไฟล์เสียงได้ กรุณาตรวจสอบอินเทอร์เน็ตหรือการอนุญาต.")
                
            except Exception as e:
                st.error(f"Oops! Something went wrong: {str(e)} / ขออภัย! เกิดข้อผิดพลาด: {str(e)}")

# Cleanup button (only shown after audio generation)
if st.session_state.show_cleanup and st.session_state.generated_files:
    if st.button("Cleanup Temporary Files / ล้างไฟล์ชั่วคราว"):
        deleted_count = 0
        for file_path in st.session_state.generated_files:
            if os.path.exists(file_path):
                os.remove(file_path)
                deleted_count += 1
        if deleted_count > 0:
            st.success(f"Deleted {deleted_count} temporary file(s). / ลบไฟล์ชั่วคราว {deleted_count} ไฟล์เรียบร้อยแล้ว")
            st.session_state.generated_files.clear()  # Clear the list
            st.session_state.show_cleanup = False  # Hide the cleanup button
        else:
            st.info("No temporary files to delete. / ไม่มีไฟล์ชั่วคราวให้ลบ")
            st.session_state.show_cleanup = False  # Hide if no files

# Kid-friendly styling with Thai font support
st.markdown("""
    <style>
    .stTextArea textarea {
        font-family: 'Noto Sans Thai', 'Comic Sans MS', cursive, sans-serif;
        font-size: 16px;
        background-color: #f0f8ff;
        border-radius: 10px;
    }
    .stButton button {
        background-color: #ff69b4;
        color: white;
        border-radius: 10px;
        font-family: 'Noto Sans Thai', 'Comic Sans MS', cursive, sans-serif;
        font-size: 18px;
    }
    .stButton button:hover {
        background-color: #ff1493;
    }
    .stSelectbox {
        font-family: 'Noto Sans Thai', sans-serif;
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@400;700&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

# Footer
st.write("---")
st.write("Created with ❤️ for kids and parents / สร้างด้วย ❤️ สำหรับเด็กและผู้ปกครอง")