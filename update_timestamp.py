from datetime import datetime, timezone

readme_path = "README.md"

now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

start = "<!-- TIMESTAMP_START -->"
end = "<!-- TIMESTAMP_END -->"

new_section = f"{start}\n_Last updated: {now}_\n{end}"

with open(readme_path, "r", encoding="utf-8") as file:
    readme = file.read()

if start in readme and end in readme:
    before = readme.split(start)[0]
    after = readme.split(end)[1]
    readme = before + new_section + after
else:
    readme += f"\n\n## Last Updated\n\n{new_section}\n"

with open(readme_path, "w", encoding="utf-8") as file:
    file.write(readme)
