# TODO: 生成的结果不稳定，需使用 langchain 优化
def getSvClasses(description):
    prompt = f'''
    Your task is to help a system engineer create a system model based on a technical fact sheet.

    Write all of the entities needed in the system model based on the information provided in the technical specifications delimited by triple backticks.
    只需要输出Output JSON 的内容，别的都不用输出，并且要用原文不能进行翻译和修改
    
    Technical specifications:  ```{description}```
    '''
    return prompt

# {
# "entities": [
# {
# "name": "北京",
# "type": "location"
# },
# {
# "name": "台北",
# "type": "location"
# },
# {
# "name": "世界",
# "type": "location"
# },
# {
# "name": "井冈山号综合登陆舰（999舰）",
# "type": "vehicle"
# },
# }