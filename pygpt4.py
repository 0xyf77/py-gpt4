import requests

def ask_gpt(api_key, prompt, max_tokens=50):
    api_url = 'https://api.openai.com/v1/engines/davinci-codex/completions'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    data = {
        'prompt': prompt,
        'max_tokens': max_tokens,
        'temperature': 0.7,
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 200:
        return response.json()['choices'][0]['text']
    else:
        raise Exception(f"ERROR: {response.status_code}, {response.json()['error']['message']}")
