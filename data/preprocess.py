import sys
import os
import json
import re
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from data.llm_helper import llm

def clean_text(text):
    text = text.replace('�', '?').replace("Let�s", "Let's").replace("I�ve", "I've")
    text = text.replace("‘", "'").replace("’", "'").replace("“", '"').replace("”", '"')
    text = re.sub(r'[^a-zA-Z0-9\s.,!?\'"@#%&():;/-]', '', text)
    return text

def process_posts(raw_file_path, processed_file_path="data/processed_posts.json"):
    enriched_posts = []
    with open(raw_file_path, encoding="utf-8") as file:
        posts = json.load(file)
        for post in posts:
            post['text'] = clean_text(post['text'])
            metadata = extract_metadata(post['text'])
            post_with_metadata = {**post, **metadata}
            enriched_posts.append(post_with_metadata)

    unified_tags = get_unified_tags(enriched_posts)
    with open(processed_file_path, 'w', encoding='utf-8') as outfile:
        json.dump(enriched_posts, outfile, ensure_ascii=False, indent=4)
    logging.info(f"Processed {len(enriched_posts)} posts and saved to {processed_file_path}")

def get_unified_tags(posts_with_metadata):
    unique_tags = set()
    for post in posts_with_metadata:
        unique_tags.update(post['tags'])
    return list(unique_tags)

def extract_metadata(post):
    template = '''
    You are given a LinkedIn post. Extract the number of lines, language, and tags.
    1. Return valid JSON. No preamble.
    2. JSON object must have keys: line_count, language, tags (max 2 tags).
    3. Language: English.

    Here is the post: {post}
    '''
    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    try:
        response = chain.invoke(input={'post': post})
        json_parser = JsonOutputParser()
        return json_parser.parse(response.content)
    except OutputParserException as e:
        logging.error(f"Error parsing metadata for post: {post}")
        return {"line_count": 0, "language": "unknown", "tags": []}
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return {"line_count": 0, "language": "unknown", "tags": []}

if __name__ == '__main__':
    process_posts('data/raw_posts.json')