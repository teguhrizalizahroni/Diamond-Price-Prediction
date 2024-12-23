import streamlit as st
from predict import run_predict


def main():
    # Sidebar Menu with 'Home', 'Team List', and 'Price Prediction'
    menu = ['Home', 'Data Seedlings Team', 'Price Prediction']
    choice = st.sidebar.radio('Menu', menu)  # Using radio button for sidebar menu
    
    # Handle the menu choices based on the sidebar selection
    if choice == 'Home':
        st.subheader('Welcome to Data Seedlings!')
        st.write("At Data Seedlings, we believe that every dataset, no matter how small, has the potential to grow, evolve, and bloom into something truly transformative. Just like the first tender sprouts of a plant, data holds the power to spark innovation, guide decisions, and create meaningful change in the world.")
        st.write("Our mission is to nurture the growth of data-driven insights, from the early stages of data collection to the impactful discoveries that can shape the future. Whether you are a beginner learning the ropes of data analysis or an experienced professional seeking new ways to cultivate knowledge, Data Seedlings is your space to plant the seeds of discovery and watch them grow.")
        st.write("As part of our journey, we are excited to share our final project: Diamond Prediction. In this project, we’ve applied cutting-edge data science techniques to predict the value and characteristics of diamonds based on a variety of factors. By analyzing a wealth of data on diamond attributes, our goal is to provide accurate, actionable insights that can aid buyers, sellers, and anyone with an interest in the diamond industry.")
    elif choice == 'Data Seedlings Team':
        st.title("Data Seedlings Team")

        # Introduction
        st.write("Welcome to our team page! Here is a list of our team members:")

        # Team Members List
        team_members = ["Agnes Veronica Victoria (Captain)", "Muh Nur Aslam", "TeguhTeguh Rizali Zahroni", "Priyo Adi Nugroho", "Aditya Kama Nugrah", "Muhammad Bintang Pratama", "Alfi Nurzaman"]

        # Display the team members
        for member in team_members:
            st.write(f"- {member}")
    elif choice == 'Price Prediction':
        st.subheader('Diamond Price Prediction')
        run_predict()

    # Footer with Hyperlinks
    st.markdown(
        """
        <footer>
            <hr>
            <p style="text-align: left;">&copy; 2024 <a href="#" target="_blank">Digital Skola Batch 42 Kelompok - 1</a></p>
        </footer>
        """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
