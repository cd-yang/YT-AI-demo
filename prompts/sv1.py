import os
from langchain.schema import HumanMessage
from langchain.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.chat_models import AzureChatOpenAI
from langchain.output_parsers import PydanticOutputParser, CommaSeparatedListOutputParser
from pydantic import BaseModel, Field, validator
from typing import List
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())  # read local .env file

# model_name = 'text-davinci-003'
model_name = 'gpt-35'
temperature = 0.0
model = AzureChatOpenAI(model_name=model_name, temperature=temperature,
                    openai_api_key=os.environ['OPENAI_API_KEY'],
                    openai_api_base=os.environ['API_BASE'],
                    openai_api_type=os.environ['API_TYPE'],
                    openai_api_version=os.environ['API_VERSION'],
                    deployment_name=os.environ['DEPLOYMENT_NAME'])


def getSvClasses(description):

    output_parser = CommaSeparatedListOutputParser()
    format_instructions = output_parser.get_format_instructions()

    # prompt = f'''
    # Your task is to help a system engineer create a system model based on a technical fact sheet.

    # Write all of the entities needed in the system model based on the information provided in the technical specifications delimited by triple backticks.
    # 只需要输出Output JSON 的内容，别的都不用输出，并且要用原文不能进行翻译和修改

    # Technical specifications:  ```{description}```
    # '''

    prompt = PromptTemplate(
        template='''
        Your task is to help a system engineer create a system model based on a technical fact sheet.
        Write all of the entities needed in the system model based on the information provided in the technical specifications delimited by triple backticks.
        
        Technical specifications:  ```{subject}```
        \n{format_instructions}
        ''',
        # "List five {subject}.\n{format_instructions}",
        input_variables=["subject"],
        partial_variables={"format_instructions": format_instructions}
    )

    _input = prompt.format(subject=description)
    print('*****_input: ' + _input)
    message = [HumanMessage(content=_input)]
    output = model(message)
    print('*****output: ')
    print(output)

    parsed_output = output_parser.parse(output.content)

    print(parsed_output)
    return parsed_output
