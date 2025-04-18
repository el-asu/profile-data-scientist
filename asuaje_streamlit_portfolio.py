# SREAMLIT PROFILE written by ChatGPT on 16/10/2024

import streamlit as st
from PIL import Image

# Basic setup
st.set_page_config(page_title="Personal Profile", layout="wide")

# Sidebar
st.sidebar.title("Navigation")
pages = st.sidebar.radio("Go to", ["Introduction", "Projects", "Services", "CV", "References", "Meet me"])

# Placeholder function for chatbot (Llama LLM)
def chatbot_placeholder():
    st.write("Chatbot placeholder: This will be the custom Llama LLM trained on your CV, projects, and publications.")

# Introduction Section
if pages == "Introduction":
    st.title("Welcome to My Personal Profile")
    
    st.write("""
        In this app, you can explore my projects, the services I offer, and my experience. You can also chat with a chatbot that has been trained to understand my career and help answer your questions.
    """)
    
    st.subheader("About me!")

    st.write("""
        I’m a Data Scientist and Pharmacist (PhD), my professional journey has been shaped by diverse experiences that aim to enhance business value and contribute to the scientific community through making Data Science more accessible to the non-trained community.

Currently, I serve as a Professor in the Data Science program at the University of the City of Buenos Aires, where I train IT professionals in the fundamentals of Artificial Intelligence, with an emphasis on Symbolic AI (e.g., Expert Systems).

As a Project Manager at Talento Científico, I support SMEs in finding top-tier scientists for their projects, specializing in the Data Science field. My goal is to match the right talent with each science-based business.

Before this role, I was privileged to be a part of the esteemed Francis Crick Institute in London. My time there involved a postdoctoral position at the Cancer Metabolism Lab, delving into the link between glucose metabolism and tumour growth as well as liver physiology. Subsequently, as a Project Manager within the Academic Training Team, I orchestrated diverse initiatives aimed at enhancing postdocs’ career progression.

My scientific journey commenced in Argentina, where I earned my PhD at the Immunological and Physiopathological Studies Institute (IIFP). My doctoral research focused on deciphering the role of ion channels in regulating pH within tumoral cells. 

    """)

    st.subheader("Chat with me!")
    chatbot_placeholder()
    st.write("""
    There is a chatbot coming soon, but not ready yet!
    """)

# Projects Section
elif pages == "Projects":
    st.title("My Projects")
    
    # Placeholder for projects
    projects = [
        {"title": "Dr.Mapp", "description": "This Streamlit app allows users to identify the nearest healthcare facilities on a map based on their location (in Argentina).", "link": " https://drmapp.streamlit.app/", "image": "project1_placeholder.jpg"},
        {"title": "Project 2", "description": "Brief intro to Project 2", "link": "https://github.com/project2", "image": "project2_placeholder.jpg"},
        {"title": "Project 3", "description": "Brief intro to Project 3", "link": "https://github.com/project3", "image": "project3_placeholder.jpg"}
    ]
    
    for project in projects:
        st.subheader(project["title"])
        img = Image.open(project["image"])
        st.image(img, width=300, caption=project["title"])
        st.write(project["description"])
        st.write(f"[View Project]({project['link']})")

# Services Section
elif pages == "Services":
    st.title("Services I Offer")
    services = [
        "Data Visualization",
        "Infographics",
        "Business Intelligence",
        "Biomedical Data Analysis",
        "Machine Learning Model Development",
        "LLM Model Training"
    ]
    
    for service in services:
        st.write(f"- {service}")

# CV Section
elif pages == "CV":
    st.title("Curriculum Vitae")
    st.subheader("Name: Placeholder Name")
    st.image("profile_picture_placeholder.jpg", width=150)
    st.write("Personal Details: [Placeholder for contact information]")
    
    st.subheader("Summary")
    st.write("This is a placeholder summary of my career.")
    
    st.subheader("Education")
    st.write("""
    - PhD in Biomedical Research – Placeholder University
    - MSc in Data Science – Placeholder University (currently enrolled)
    - BSc in Pharmacy – Placeholder University
    """)
    
    st.subheader("Work Experience")
    st.write("""
    - Data Scientist, Placeholder Company, 2024-present
    - Postdoctoral Researcher, Placeholder Institute, 2020-2024
    - Project Manager, Placeholder Organization, 2016-2020
    """)
    
    st.subheader("Skills")
    st.write("""
    - Machine Learning
    - Data Visualization
    - Python, R
    - Project Management
    """)
    
    st.subheader("Additional Training")
    st.write("Placeholder for additional training")
    
    st.subheader("Publications")
    st.write("""
    - Publication 1: Placeholder Title
    - Publication 2: Placeholder Title
    """)
    
    st.download_button(label="Download CV", data="cv_placeholder.pdf", file_name="CV.pdf")

# References Section
elif pages == "References":
    st.title("References")
    st.write("Available upon request.")

# Meet Me Section
elif pages == "Meet me":
    st.title("Get in Touch")
    st.write("Feel free to reach out to me via email:")
    st.write("Email: placeholder.email@example.com")
    
    st.write("You can also book a meeting with me through Calendly:")
    st.write("[Book a Meeting](https://calendly.com/placeholder)")

# Footer
st.sidebar.write("---")
st.sidebar.write("Powered by Streamlit")
