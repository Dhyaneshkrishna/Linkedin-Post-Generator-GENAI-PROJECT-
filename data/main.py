import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

length_options = ["Short", "Medium", "Long"]
language_options = ["English"]

def main():
    st.subheader("LinkedIn Post Generator: ")

    col1, col2, col3 = st.columns(3)

    fs = FewShotPosts()
    tags = fs.get_tags()  
    
    with col1:
        
        selected_tag = st.selectbox("Topic", options=tags)

    with col2:
        
        selected_length = st.selectbox("Length", options=length_options)

    with col3:
        
        selected_language = st.selectbox("Language", options=language_options)

    
    st.write(f"Selected Tag: {selected_tag}, Length: {selected_length}, Language: {selected_language}")

    if st.button("Generate"):
        try:
            # Ensure that generate_post expects three parameters (length, language, and tag)
            post = generate_post(selected_length, selected_language, selected_tag)
            if post:
                st.write(post)
            else:
                st.write("Error generating post")
        except TypeError as e:
            st.write(f"Error: {e}")
            st.write("Ensure generate_post() accepts three parameters.")

if __name__ == "__main__":
    main()
