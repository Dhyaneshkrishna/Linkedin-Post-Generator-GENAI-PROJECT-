GenAI Post Generator

GenAI Post Generator is a tool designed to analyze the LinkedIn posts of an influencer and help them generate new posts that align with their unique writing style. This tool extracts key topics, writing tone, length preferences, and language from the influencer's previous posts to assist in crafting future content.

1. Features:
   1. Analyze Past Posts: Extracts key topics, language, and length from the influencer's previous posts.
   2. Generate New Posts: Uses topics, language, and length to create new posts that match the influencer's writing style.
   3. Few-shot Learning: Employs examples from past posts to guide a large language model (LLM) in generating tailored content.

2. Use Case:
   Example Scenario:
   Sidd Ahmed is a LinkedIn influencer who wants help in creating future posts. By feeding his past LinkedIn posts into this tool, it extracts key topics, writing style, and preferences. Sidd Ahmed can then select a topic, length, and language to generate a post tailored to his writing style.

3. Technical Architecture:
   1. Stage 1: Post Analysis:
      - Collect LinkedIn posts.
      - Extract key attributes such as topic, language, and length.
   2. Stage 2: Post Generation:
      - Use the extracted attributes (topic, language, length) to generate a new post.
      - Leverage few-shot learning with related past posts to guide the LLM in mimicking the user's writing style.

4. Setup and Installation:
   Prerequisites:
      - Python 3.8 or above
      - API Key from Groq Console (https://console.groq.com/keys)

   Steps:
      1. Clone the Repository:
         ```bash
         git clone https://github.com/your-username/project-genai-post-generator.git
         cd project-genai-post-generator
         ```
      2. Install Dependencies:
         ```bash
         pip install -r requirements.txt
         ```
      3. Set Up API Key:
         - Obtain your API Key from Groq Console (https://console.groq.com/keys).
         - Create a .env file in the root directory and update it with:
           ```env
           GROQ_API_KEY=your_api_key_here
           ```
      4. Run the Application:
         ```bash
         streamlit run main.py
         ```

5. Usage:
   1. Open the Streamlit app in your browser (default: http://localhost:8501).
   2. Upload your LinkedIn posts (text or JSON format).
   3. Select a topic, preferred length, and language.
   4. Click the Generate button to create a new LinkedIn post.
