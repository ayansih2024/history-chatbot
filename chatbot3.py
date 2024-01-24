import streamlit as st
import re
from streamlit_chat import message
import streamlit.components.v1 as components

# Set page title and layout
st.set_page_config(page_title="History Chatbot UI", layout="wide")

# Declare the history_responses dictionary with history-related questions and answers

history_responses = {
    "Indus Valley Civilization": "The Indus Valley Civilization, also known as the Harappan Civilization, was one of the world's oldest urban civilizations. It thrived around 2600–1900 BCE in the Indian subcontinent.",
    "Maurya Dynasty": "The Maurya Dynasty, founded by Chandragupta Maurya, was one of the largest empires in ancient India. Ashoka the Great, a prominent Mauryan ruler, is known for spreading Buddhism.",
    "Gupta Empire": "The Gupta Empire, from approximately 320 to 550 CE, is often referred to as the 'Golden Age of India.' It was known for significant achievements in art, science, and mathematics.",
    "Mughal Empire Architects": "The main architects of the Mughal Empire included Babur, Akbar, Jahangir, Shah Jahan, and Aurangzeb. They played key roles in shaping the empire's political and cultural landscape.",
    "British East India Company Impact": "The British East India Company had a profound impact on India. It played a key role in trade, governance, and territorial control. Over time, it led to British dominance and colonization.",
    "Independence from British Rule": "India gained independence from British rule on August 15, 1947. The Indian Independence Act of 1947 led to the partition of India into two independent nations, India and Pakistan.",
    "Indian Independence Movement Leaders": "Prominent leaders during the Indian independence movement included Mahatma Gandhi, Jawaharlal Nehru, Sardar Patel, Subhas Chandra Bose, and many others who played crucial roles in the struggle.",
    "Dandi March Significance": "The Dandi March, led by Mahatma Gandhi in 1930, was a nonviolent protest against the salt tax imposed by the British. It became a symbol of resistance and a turning point in the independence movement.",
    "Partition of India and Pakistan": "The partition of India and Pakistan took place on August 15, 1947, based on religious lines. It resulted in the creation of two independent nations, India (predominantly Hindu) and Pakistan (predominantly Muslim).",
    "First President of Independent India": "Dr. Rajendra Prasad was the first President of independent India. He served as the President from 1950 to 1962 and played a significant role in the early years of the republic.",
    "Mahatma Gandhi Role in Independence": "Mahatma Gandhi, also known as the Father of the Nation, played a central role in India's struggle for independence. His philosophy of nonviolence and civil disobedience inspired the masses.",
    "Emergency in India": "The Emergency in India was declared by then-Prime Minister Indira Gandhi in 1975. It lasted until 1977 and involved the suspension of civil liberties. It was a period of authoritarian rule.",
    "Battle of Plassey Importance": "The Battle of Plassey in 1757 was a pivotal moment in Indian history. It marked the beginning of British dominance in India, as the British East India Company gained control over Bengal.",
    "Indian Constitution Formation": "The key figures in the formation of the Indian Constitution included Dr. B.R. Ambedkar, Jawaharlal Nehru, Sardar Patel, and others. The Constituent Assembly drafted the constitution, which came into effect on January 26, 1950.",
    "India Became a Republic": "India became a republic on January 26, 1950, when the Constitution of India came into effect. This day is celebrated annually as Republic Day.",
    "Green Revolution Impact on Agriculture": "The Green Revolution, initiated in the 1960s, led to increased agricultural productivity in India. It introduced high-yielding varieties of crops, modern farming techniques, and improved irrigation.",
    "First Woman Prime Minister of India": "Indira Gandhi was the first woman Prime Minister of India. She served as the Prime Minister from 1966 to 1977 and later from 1980 until her assassination in 1984.",
    "First General Elections in India": "The first general elections in India were held in 1951-52, after gaining independence. The Indian National Congress, led by Jawaharlal Nehru, emerged as the dominant party.",
    "1857 Sepoy Mutiny Significance": "The 1857 Sepoy Mutiny, also known as the First War of Independence, had significant implications. It marked a turning point in Indian history and led to changes in British colonial policies.",
    "Classical Indian Art and Literature Contributors": "Major contributors to classical Indian art and literature include Kalidasa, Bhasa, Aryabhata, Varahamihira, and others. They made significant contributions in various fields during ancient times.",
    "Decline of Harappan Civilization": "The decline of the Harappan civilization is not conclusively known, but factors such as environmental changes, ecological issues, or migration have been suggested as possible causes.",
    "Ashoka the Great Contributions": "Ashoka the Great, a Mauryan ruler, is known for spreading Buddhism, promoting nonviolence, and implementing policies of social welfare. His edicts reflect a commitment to ethical governance.",
    "Bhakti Movement Prominence": "The Bhakti movement gained prominence in India from the 7th to the 17th centuries. It emphasized devotion to a personal god and transcended caste and religious barriers.",
    "Battle of Panipat Significance": "The Battle of Panipat, fought in 1526, marked the beginning of the Mughal Empire in India. Babur, the Mughal emperor, defeated Ibrahim Lodhi, the ruler of Delhi, in this decisive battle.",
    "Chola Dynasty Famous Rulers": "The Chola dynasty, known for its cultural achievements, had famous rulers such as Rajaraja Chola, Rajendra Chola, and others who contributed to art, architecture, and maritime trade.",
    "Spread of Buddhism in India": "Buddhism spread in India during the 6th century BCE. It was founded by Siddhartha Gautama (Buddha) and gained followers through his teachings and missionary activities.",
    "Silk Road Importance in Indian History": "The Silk Road, a network of trade routes, was crucial for India's economic and cultural interactions with other civilizations. It facilitated the exchange of goods, ideas, and cultures.",
    "Indian Ocean Trade Impact on India": "The Indian Ocean trade played a vital role in India's economic history. It connected India with regions like Africa, the Middle East, and Southeast Asia, fostering trade and cultural exchange.",
    "Sangam Literature Prominent Poets": "Prominent poets of Sangam literature include Thiruvalluvar, Avvaiyar, and others. Sangam literature is a collection of Tamil poetry from the ancient Sangam period.",
    "Rani Padmini Role in Indian History": "Rani Padmini, the queen of Mewar, is known for her role in the Rajput resistance against Alauddin Khilji. Her story is often associated with the Chittorgarh fort.",
    "Sufism Concept in Medieval India": "Sufism, a mystical Islamic tradition, gained popularity in medieval India. It emphasized a personal relationship with the divine and played a role in cultural and social integration.",
    "Marathas Influence and Leaders": "The Marathas were a powerful regional power in India. Leaders like Chhatrapati Shivaji and later leaders expanded Maratha influence in the 17th and 18th centuries.",
    "Vijayanagara Empire Architectural Achievements": "The Vijayanagara Empire, known for its architectural marvels, had achievements like the Virupaksha Temple and Hampi. These structures reflect the empire's cultural and artistic richness.",
    "Jallianwala Bagh Massacre Date": "The Jallianwala Bagh massacre occurred on April 13, 1919, in Amritsar. British troops, led by General Dyer, opened fire on a peaceful gathering, resulting in tragic loss of lives.",
    "Non-Cooperation Movement Key Figures": "The Non-Cooperation Movement had key figures like Mahatma Gandhi, Jawaharlal Nehru, and others who advocated for nonviolent resistance against British rule.",
    "Simon Commission Boycott Reason": "The Simon Commission, appointed in 1927, lacked Indian representation. It was boycotted in India as it was seen as an insult to Indian self-governance aspirations.",
    "Quit India Movement Significance": "The Quit India Movement, launched in 1942, was a mass protest against British rule. It demanded an end to British colonialism and played a role in India's journey to independence.",
    "Hyderabad Princely State Annexation": "The princely state of Hyderabad was annexed in 1948, following Operation Polo. It integrated Hyderabad into the Indian Union, resolving political and territorial issues.",
    "Khilafat Movement Notable Leaders": "The Khilafat Movement had notable leaders like Mahatma Gandhi, Ali Brothers, and Maulana Abul Kalam Azad. It aimed to support the Ottoman Caliphate and address Muslim grievances.",
    "Bengal Partition Causes and Consequences": "The Bengal Partition of 1905 had causes like administrative efficiency. Consequences included the annulment due to protests, leading to the creation of East and West Bengal.",
    "Netaji Subhas Chandra Bose Role in Independence": "Netaji Subhas Chandra Bose played a crucial role in India's struggle for independence. He led the Indian National Army (INA) and sought international support for India's cause.",
    "Goa Part of Independent India Date": "Goa became a part of independent India on December 19, 1961, after military action (Operation Vijay) against Portuguese colonial rule.",
    

}

# Title and container for chat history
st.title("History Chatbot")
chat_history = st.container()

# Markdown message to instruct users
st.markdown("Choose a topic from the dropdown, and I'll provide information about the history of India.")

# HTML style to right-align chat input
components.html("""
    <style>  
        <style>
    .stChatInput > div > input {
        text-align: right;
    }
        </style>
    </style>
    """,
    height=0  # Set height to 0 to hide the injected element
)

# Dropdown for selecting history-related questions
selected_question = st.selectbox("Select a History Topic", list(history_responses.keys()))

# Display user-selected question
if selected_question:
    st.markdown(f"You selected: {selected_question}")

# User input textbox
user_input = st.chat_input("Enter additional questions or comments here")

# Function to process user input and return responses
def history_bot(user_input):
    responses = []  # Store multiple responses
    
    if user_input and isinstance(user_input, str):
        for pattern, response in history_responses.items():
            if re.search(pattern, user_input, re.IGNORECASE):
                responses.append(response)

    if responses:
        return responses  # Return a list of responses
    return ["I'm sorry, I don't have information on that specific topic. Please consult official sources or books for accurate and up-to-date information."]

# Process user input and display responses
if user_input:  
    responses = history_bot(user_input) 
    for i, response in enumerate(responses):
        bot_history = f"Chatbot: {response}"
        message("You: " + user_input)  
        message(bot_history)
