from gpt import langchain_chat_openai_model
from langchain.schema import HumanMessage
from langchain.prompts import PromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser


def get_sv_classes(description):
    output_parser = CommaSeparatedListOutputParser()
    format_instructions = output_parser.get_format_instructions()
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
    output = langchain_chat_openai_model(message)
    print('*****output: ')
    print(output)

    parsed_output = output_parser.parse(output.content)

    print(parsed_output)
    return parsed_output
