from gpt import langchain_chat_openai_model
from langchain.schema import HumanMessage
from langchain.prompts import (
    PromptTemplate,
)
# Your are a system engineer create.
template = '''
        
        Based on a technical fact sheet, 尽可能详细地用 mermaidjs 回答时序图

        Technical specifications:  ```{subject}```

        '''


def get_sv_sequence_diagrams(description: str, debug=False) -> str:
    print('正在生成时序图')

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
    return output.content
