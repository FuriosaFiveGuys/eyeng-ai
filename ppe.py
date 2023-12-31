import openai

def ppe(prompt):
    OPENAI_API_KEY = ""
    openai.api_key = OPENAI_API_KEY

    def get_completion(prompt, model="gpt-4-1106-preview"):#"gpt-3.5-turbo"):
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0.1,
        )
        return response.choices[0].message["content"]

    response = get_completion(prompt)
    return response