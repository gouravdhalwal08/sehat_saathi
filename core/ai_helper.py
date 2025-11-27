import time

def get_gemini_response(question: str):
    """
    A simple, rule-based mock chatbot function.
    It simulates a response based on keywords. No API key needed.
    """
    question_lower = question.lower()
    
    # Simulate a "thinking" delay
    time.sleep(0.5)

    # --- Define Rules ---
    if "hello" in question_lower or "hi" in question_lower:
        return "Hello! I am Sehat Saathi. How can I help you today? (You can ask me about 'diabetes', 'fever', or 'headache')."
        
    elif "diabetes" in question_lower:
        return """
        Diabetes is a chronic condition affecting how your body processes sugar (glucose). 
        
        **General Info:**
        * **Type 1:** The body doesn't produce insulin.
        * **Type 2:** The body doesn't use insulin properly.
        
        **Prevention:** A healthy diet, regular exercise, and maintaining a healthy weight are key.
        
        ⚠️ **Disclaimer:** This is general information. Please consult a doctor for a proper diagnosis or medical advice.
        """
        
    elif "fever" in question_lower:
        return """
        A fever is a temporary increase in body temperature, often due to an illness.
        
        **General Info:**
        * It's a common sign of infection.
        * Rest and hydration are very important.
        
        ⚠️ **Disclaimer:** If a fever is very high or persists for more than a couple of days, it's crucial to see a healthcare professional.
        """
        
    elif "headache" in question_lower:
        return """
        Headaches are a common ailment and can have many causes, including stress, dehydration, or lack of sleep.
        
        **General Info:**
        * **Tension headaches:** Feel like a dull, aching pressure.
        * **Migraines:** Are often more intense, throbbing, and can have other symptoms like nausea.
        
        ⚠️ **Disclaimer:** For severe or frequent headaches, please consult a doctor to rule out any serious conditions.
        """

    elif "diagnosis" in question_lower or "treat" in question_lower or "cure" in question_lower:
        return "I am an AI assistant and cannot provide a medical diagnosis or treatment plan. It is very important to consult a qualified healthcare professional for any medical advice."

    else:
        return "I'm sorry, I can only provide general information on 'diabetes', 'fever', or 'headache'. For all other medical advice, please consult a qualified doctor."