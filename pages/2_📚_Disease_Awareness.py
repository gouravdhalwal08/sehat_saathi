import streamlit as st
from core.language import TEXT

if 'lang' not in st.session_state:
    st.session_state.lang = 'en'

T = TEXT[st.session_state.lang]

st.header(T["disease_header"])
st.info(T["disease_intro"])

# --- ENGLISH CONTENT ---
if st.session_state.lang == 'en':
    with st.expander("🩺 Diabetes Mellitus"):
        st.markdown("""
        **What is it?** A chronic disease that occurs when the pancreas does not produce enough insulin or when the body cannot effectively use the insulin it produces.
        
        **Common Symptoms:** Frequent urination, increased thirst, unexplained weight loss, fatigue, blurred vision.
        
        **Prevention:**
        - Maintain a healthy body weight.
        - Engage in regular physical activity.
        - Eat a healthy, balanced diet.
        - Avoid tobacco use.
        """)
        
    with st.expander("🩸 Hypertension (High Blood Pressure)"):
        st.markdown("""
        **What is it?** A condition in which the force of the blood against the artery walls is too high.
        
        **Common Symptoms:** Often called the "silent killer" as it may have no symptoms. In some cases, it can cause headaches, shortness of breath, or nosebleeds.
        
        **Prevention:**
        - Reduce salt intake.
        - Eat more fruits and vegetables.
        - Be physically active regularly.
        - Avoid alcohol and tobacco.
        - Manage stress.
        """)
        
# --- HINDI CONTENT ---
elif st.session_state.lang == 'hi':
    with st.expander("🩺 मधुमेह (Diabetes)"):
        st.markdown("""
        **यह क्या है?** यह एक पुरानी बीमारी है जो तब होती है जब अग्न्याशय पर्याप्त इंसुलिन का उत्पादन नहीं करता है या जब शरीर अपने द्वारा उत्पादित इंसुलिन का प्रभावी ढंग से उपयोग नहीं कर पाता है।
        
        **सामान्य लक्षण:** बार-बार पेशाब आना, अधिक प्यास लगना, बिना किसी कारण के वजन कम होना, थकान, धुंधली दृष्टि।
        
        **रोकथाम:**
        - स्वस्थ शरीर का वजन बनाए रखें।
        - नियमित शारीरिक गतिविधि में संलग्न रहें।
        - स्वस्थ, संतुलित आहार लें।
        - तम्बाकू के सेवन से बचें।
        """)
        
    with st.expander("🩸 उच्च रक्तचाप (Hypertension)"):
        st.markdown("""
        **यह क्या है?** एक ऐसी स्थिति जिसमें धमनी की दीवारों के खिलाफ रक्त का बल बहुत अधिक होता है।
        
        **सामान्य लक्षण:** इसे अक्सर "साइलेंट किलर" कहा जाता है क्योंकि इसके कोई लक्षण नहीं हो सकते हैं। कुछ मामलों में, यह सिरदर्द, सांस की तकलीफ या नाक से खून बहने का कारण बन सकता है।
        
        **रोकथाम:**
        - नमक का सेवन कम करें।
        - अधिक फल और सब्जियां खाएं।
        - नियमित रूप से शारीरिक रूप से सक्रिय रहें।
        - शराब और तंबाकू से बचें।
        - तनाव का प्रबंधन करें।
        """)