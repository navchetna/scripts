from groq import Groq
import os
from dotenv import load_dotenv, dotenv_values
from table import Table

def get_table_description(item: Table):
    load_dotenv() 
    client = Groq(
        api_key=os.getenv("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": """
                    <s>[INST] <<SYS>>\n You are a helpful, respectful, and honest assistant. Your task is to generate a detailed and descriptive summary of the provided table data in Markdown format, based strictly on the table and its heading. <</SYS>> 
                    [INST] Your job is to create a clear, specific, and **factual** textual description. **Do not add any external information** or provide an abstract summary. Only base the description on the data from the table and its heading.
                    
                    1. Link the **columns** with the corresponding **values** in the rows, referencing the exact terms and terminology from the table. 
                    2. For each row, explain how each column's data relates to the corresponding values. Ensure the description is **step-by-step** and follows the structure of the table in a natural order.
                    3. **Do not return the table itself.** Provide only the descriptive summary, written in **paragraphs**.
                    4. The description should be precise, direct, and **avoid interpretation** or generalization. Stay true to the exact data given.
                    
                    Think carefully and make sure to describe every column and its respective values in detail. 
                """
            },
            {
                "role": "user",
                "content": f"{item.heading}\n{item.markdown_content}",
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    return chat_completion.choices[0].message.content