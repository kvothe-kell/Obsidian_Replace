import os

# Path to the Obsidian Vault
VAULT_PATH = "/Users/husband/Obsidian/Vault 111/Resources/Market Notes/Macro"


def process_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.readlines()

    # Check if the file has a frontmatter block
    if not content or content[0].strip() != "---":
        return

    # Extract frontmatter
    end_index = 1
    while end_index < len(content) and content[end_index].strip() != "---":
        end_index += 1

    if end_index == len(content):  # If no closing frontmatter block, exit
        return

    frontmatter = content[1:end_index]  # Extract frontmatter (excluding "---")
    body = content[end_index + 1:]  # Extract body (content after frontmatter)

    # Search for 'Topic: Finance' in frontmatter
    updated_frontmatter = []
    topic_updated = False

    for line in frontmatter:
        if line.startswith("Topic:") and "Finance" in line:
            updated_frontmatter.append(line.replace("Finance", "Economics"))
            topic_updated = True
        else:
            updated_frontmatter.append(line)

    # If no change was made, exit
    if not topic_updated:
        return

    # Reconstruct the file with the updated frontmatter
    new_content = ["---\n"] + updated_frontmatter + ["---\n"] + body

    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(new_content)

    print(f"Updated: {file_path}")


def scan_vault():
    for root, _, files in os.walk(VAULT_PATH):
        for file in files:
            if file.endswith(".md"):
                process_file(os.path.join(root, file))


if __name__ == "__main__":
    scan_vault()
