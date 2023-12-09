import streamlit as st
import openai
from openai import OpenAI

###GPT API KEY
OPENAI_API_KEY = st.secrets["openai_api_key"]
openai.api_key = OPENAI_API_KEY
client = OpenAI(api_key=OPENAI_API_KEY)

####

#@st.cache_data
def openAI_content(system_act_as, user_prompt):
    response = client.chat.completions.create( 
        model="ft:gpt-3.5-turbo-1106:personal::8TtTGyWJ", #finetuned GPT model for this specific use case only
        messages=[
            {"role": "system", "content": system_act_as},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7
    )
    prompt_tokens = response.usage.prompt_tokens
    completion_tokens = response.usage.completion_tokens
    generated_content = response.choices[0].message.content
    gpt_version_used = response.model

    
    cost_per_token_input = 0.001
    cost_per_token_output = 0.002
    cost_prompt = prompt_tokens * (cost_per_token_input/1000)
    cost_completion = completion_tokens * (cost_per_token_output/1000)
    total_cost = cost_prompt + cost_completion
    total_cost = round(total_cost, 7)

    return generated_content, total_cost