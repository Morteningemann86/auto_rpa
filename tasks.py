import requests
import subprocess
import io
from resources.key import api_key

# Function to get code from OpenAI API based on user prompt
def get_code_from_openai(prompt):
    # OpenAI API URL for code generation
    url = 'https://api.openai.com/v1/engines/davinci-codex/completions'
    # Headers for the API request
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + api_key
    }
    # JSON payload for the API request, modify temperature, max_tokens as needed
    data = {
        'prompt': prompt,
        'temperature': 0.7,
        'max_tokens': 2048
    }
    # POST request to the OpenAI API
    response = requests.post(url, json=data, headers=headers)
    # Extracting generated code from the response
    generated_code = response.json()['choices'][0]['text']
    return generated_code

# Main function
def main():
    # Get task description from user
    task_description = input("Describe the task for automation: ")
    # Get Python code for the task from OpenAI API
    python_code = get_code_from_openai(task_description)
    
    # Create a new Python file with the generated code
    filename = 'generated_code.py'
    with open(filename, 'w') as file:
        file.write(python_code)
    
    # Run the generated Python script and catch exceptions
    try:
        # Execute the generated Python file
        output = subprocess.check_output(['python', filename], stderr=subprocess.STDOUT, universal_newlines=True)
        print("Execution Output:\n", output)
    except subprocess.CalledProcessError as e:
        print("An error occurred during execution:\n", e.output)

# Execute the main function
if __name__ == '__main__':
    main()
