import streamlit as st
import replicate
import os

st.set_page_config(page_title="AI Video Maker", layout="wide")
st.title("🎬 محرك صناعة الفيديوهات بالذكاء الاصطناعي")

# هنا نضع مفتاح الـ API (سأعلمك كيف تحصل عليه مجاناً)
api_key = st.sidebar.text_input("Enter Replicate API Token:", type="password")
os.environ["REPLICATE_API_TOKEN"] = api_key

prompt = st.text_area("صف الفيديو الذي تريده بدقة (باللغة الإنجليزية):", "A majestic dragon flying over a volcanic landscape, cinematic style, 4k")

if st.button("بدء التصميم 🚀"):
    if not api_key:
        st.error("من فضلك أدخل مفتاح الـ API أولاً في القائمة الجانبية")
    else:
        with st.spinner("جاري إنشاء الفيديو... انتظر قليلاً"):
            try:
                output = replicate.run(
                    "stability-ai/stable-video-diffusion:3f0457d9",
                    input={"prompt": prompt}
                )
                st.video(output[0])
                st.success("تم الانتهاء!")
            except Exception as e:
                st.error(f"حدث خطأ: {e}")
