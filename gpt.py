import os
import requests
import json
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())  # read local .env file

openai.api_key = os.environ['OPENAI_API_KEY']
openai.api_base = os.environ['API_BASE']
openai.api_type = os.environ['API_TYPE']
openai.api_version = os.environ['API_VERSION']
deployment_name = os.environ['DEPLOYMENT_NAME']


def get_completion(prompt, temperature=0.0, model="gpt-35"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        engine=deployment_name
    )
    return response.choices[0].message["content"]


def GetJson(description):
    prompt = f'''
    Your task is to help a system engineer create a 
    system model based 
    on a technical fact sheet.

    Write all of the entities needed in the system model based on the information 
    provided in the technical specifications delimited by 
    triple backticks.

    Use the following format:
    ENTITIES: <text to summarize>
    ACTIONS: <summary>
    Output JSON: <json with summary and num_names>
    
    Technical specifications:  ```{description}```
    只需要输出Output JSON 的内容，别的都不用输出，并且要用原文不能进行翻译和修改
    '''
    # print(prompt)
    return get_completion(prompt)
