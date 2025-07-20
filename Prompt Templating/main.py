from jinja2 import Environment, FileSystemLoader
import json

env = Environment(loader=FileSystemLoader("templates"))

def render_prompt(template_name, user_input, context="", task_type=""):
    template = env.get_template(template_name)
    return template.render(user_input=user_input, context=context, task_type=task_type)

if __name__ == "__main__":
    examples = [
        {
            "template_name": "qa_prompt.j2",
            "user_input": "What is the capital of France?",
            "context": "France is a country in Europe with Paris as its capital.",
            "task_type": ""
        },
        {
            "template_name": "summarization_prompt.j2",
            "user_input": "Artificial intelligence is a branch of computer science focused on building smart machines...",
            "context": "",
            "task_type": ""
        },
        {
            "template_name": "translation_prompt.j2",
            "user_input": "How are you?",
            "context": "",
            "task_type": "French"
        },
        {
            "template_name": "roleplay_prompt.j2",
            "user_input": "Explain the theory of relativity.",
            "context": "",
            "task_type": "Albert Einstein"
        },
        {
            "template_name": "json_prompt.j2",
            "user_input": "Name: John Doe, Age: 35, Occupation: Engineer",
            "context": "Extract person's details",
            "task_type": '{ "name": "", "age": 0, "occupation": "" }'
        }
    ]

    for example in examples:
        prompt = render_prompt(**example)
        print(f"\n--- {example['template_name']} ---\n{prompt}")
