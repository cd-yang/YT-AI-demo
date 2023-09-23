from gpt import langchain_chat_openai_model
from langchain.schema import HumanMessage
from langchain.prompts import (
    PromptTemplate,
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.output_parsers import StructuredOutputParser
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field, validator
from typing import List
import json

# 待测试： AV-1 中的各个字段，在一个请求中获取，还是单独获取，准确性高

template = '''
        Your task is to help a system engineer create a system model based on a technical fact sheet.
        Write all the information (operationalArea, operationalEnvironment, threatTarget, operationalBackground) based on the information provided in the technical specifications delimited by triple backticks.

        Technical specifications:  ```{subject}```

        response in Chinese, format in JSON
        '''
# \n{format_instructions}


def get_av1_fields(description, debug=False):
    # output_parser = StructuredOutputParser()
    # format_instructions = output_parser.get_format_instructions()
    prompt = PromptTemplate(
        template=template,
        input_variables=["subject"],
        # partial_variables={"format_instructions": format_instructions}
    )

    _input = prompt.format(subject=description)
    if debug:
        print('*****_input: ' + _input)
    message = [HumanMessage(content=_input)]
    output = langchain_chat_openai_model(message)
    if debug:
        print('*****output: ')
    if debug:
        print(output.content)

    # parsed_output = output_parser.parse(output.content)

    # if debug:
    #     print(parsed_output)
    # return parsed_output
    return json.loads(output.content)
    # return output.content

# # Define your desired data structure.
# class Joke(BaseModel):
#     setup: str = Field(description="question to set up a joke")
#     punchline: str = Field(description="answer to resolve the joke")

#     # You can add custom validation logic easily with Pydantic.
#     @validator("setup")
#     def question_ends_with_question_mark(cls, field):
#         if field[-1] != "?":
#             raise ValueError("Badly formed question!")
#         return field


# def get_av1_fields(description):
#     # And a query intented to prompt a language model to populate the data structure.
#     joke_query = "Tell me a joke."

#     # Set up a parser + inject instructions into the prompt template.
#     parser = PydanticOutputParser(pydantic_object=Joke)

#     prompt = PromptTemplate(
#         template="Answer the user query.\n{format_instructions}\n{query}\n",
#         input_variables=["query"],
#         partial_variables={
#             "format_instructions": parser.get_format_instructions()},
#     )

#     _input = prompt.format_prompt(query=joke_query)

#     print('_input: ' + _input.to_string())
#     # output = model(_input.to_string())
#     message = [HumanMessage(content=_input.to_string())]
#     output = langchain_chat_openai_model(message)
#     print('output: ')
#     print(output)

#     # return parser.parse(output)
#     print('parsed')
#     print(parser.parse(output))
#     return '66666666'
