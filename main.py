import os
import re

# Path to the Obsidian Vault
vault_path = input("Please Enter the Vault Path: ")

VAULT_PATH = "/Users/husband/Obsidian/Vault 111/Resources/Market Notes/Macro"


def process_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.readlines()

    # Check if the file has frontmatter block
    if not content or content[0].strip() != "---":
        return

    # Extract frontmatter
    end_index = 1
    while end_index < len(content) and content[end_index].strip() != "---":
        end_index += 1

    frontmatter = content[1:end_index]
    body = content[end_index + 1:]

    # Check if 'Topic' contains 'Economics'
    topic_match = re.search(r"^Topic:\s*(.*)", "\n".join(frontmatter), re.MULTILINE)
    if not topic_match or "Finance" not in topic_match.group(1):
        return

    # # Check if "#economics" already exists
    # if "#finance" in "".join(body):
    #     return

    # Append the tag
    with open(file_path, "a", encoding="utf-8") as f:
        f.write("\n\n#finance\n")

    print(f"Updated: {file_path}")


def scan_vault():
    for root, _, files in os.walk(VAULT_PATH):
        for file in files:
            if file.endswith(".md"):
                process_file(os.path.join(root, file))


if __name__ == "__main__":
    scan_vault()
