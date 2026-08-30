from datetime import datetime, timezone
import random
import requests

fallback_quotes = [
    "The best way to get started is to quit talking and begin doing.",
    "Don’t let yesterday take up too much of today.",
    "It’s not whether you get knocked down, it’s whether you get up.",
    "If you are working on something exciting, it will keep you motivated.",
    "Success is the sum of small efforts repeated day in and day out."
]

def get_quote():
    try:
        response = requests.get("https://api.quotable.io/random", timeout=10)
        response.raise_for_status()
        data = response.json()
        return f"{data['content']} — {data['author']}"
    except Exception:
        return random.choice(fallback_quotes)

quote = get_quote()
now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

readme_path = "README.md"

with open(readme_path, "r", encoding="utf-8") as file:
    readme = file.read()

start = "<!-- QUOTE_START -->"
end = "<!-- QUOTE_END -->"

new_section = f"{start}\n> {quote}\n\n_Last updated: {now}_\n{end}"

if start in readme and end in readme:
    before = readme.split(start)[0]
    after = readme.split(end)[1]
    readme = before + new_section + after
else:
    readme += f"\n\n## Quote\n\n{new_section}\n"

with open(readme_path, "w", encoding="utf-8") as file:
    file.write(readme)
