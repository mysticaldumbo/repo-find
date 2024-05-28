import requests
import webbrowser
import random

def get_random_repo():
    url = 'https://api.github.com/repositories'

    response = requests.get(url)

    if response.status_code == 200:
        repositories = response.json()

        random_repo = random.choice(repositories)

        repo_url = random_repo['html_url']

        return repo_url
    else:
        print("Failed to fetch repositories. Status code:", response.status_code)
        return None

def open_random_repo_in_browser():
    repo_url = get_random_repo()

    if repo_url:
        webbrowser.open_new_tab(repo_url)
        print("Opened a random GitHub repository in your default browser.")
    else:
        print("Failed to open a random GitHub repository.")

if __name__ == "__main__":
    open_random_repo_in_browser()
