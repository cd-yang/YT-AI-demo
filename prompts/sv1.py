from gpt import langchain_chat_openai_model
from langchain.schema import HumanMessage
from langchain.prompts import PromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser

template = '''
        Your task is to help a system engineer create a system model based on a technical fact sheet.
        Write all of the entities needed in the system model based on the information provided in the technical specifications delimited by triple backticks.
        
        Technical specifications:  ```{subject}```
        \n{format_instructions}
        '''


def get_sv_classes(description, debug=False):
    output_parser = CommaSeparatedListOutputParser()
    format_instructions = output_parser.get_format_instructions()
    prompt = PromptTemplate(
        template=template,
        input_variables=["subject"],
        partial_variables={"format_instructions": format_instructions}
    )

    _input = prompt.format(subject=description)
    if debug:
        print('*****_input: ' + _input)
    message = [HumanMessage(content=_input)]
    output = langchain_chat_openai_model(message)
    if debug:
        print('*****output: ')
    if debug:
        print(output)

    parsed_output = output_parser.parse(output.content)

    if debug:
        print(parsed_output)
    return parsed_output
