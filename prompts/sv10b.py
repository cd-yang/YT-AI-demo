from gpt import langchain_chat_openai_model
from langchain.schema import HumanMessage
from langchain.prompts import (
    PromptTemplate,
)

template = '''
        Your task is to help a system engineer create a system model based on a technical fact sheet.
        Write the state diagram of ```{sv_class}```

        Technical specifications:  ```{subject}```

        response in mermaidjs format
        '''


def get_sv_state_diagrams(description: str, sv_classes: [str] = [], debug=False) -> [str]:
    result = {}
    for sv_class in sv_classes:
        print('正在生成 【' + sv_class + '】 的状态图...')

        prompt = PromptTemplate(
            template=template,
            input_variables=["subject", "sv_class"],
            # partial_variables={"format_instructions": format_instructions}
        )

        _input = prompt.format(subject=description, sv_class=sv_class)
        if debug:
            print('*****_input: ' + _input)
        message = [HumanMessage(content=_input)]
        output = langchain_chat_openai_model(message)
        if debug:
            print('*****output: ')
        if debug:
            print(output.content)
        result[sv_class] = output.content

    return result
