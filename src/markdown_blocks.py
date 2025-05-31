def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")

    cleaned_blocks = []
    for block in blocks:
        if block == "":
            continue

        stripped_block = block.strip()
        cleaned_blocks.append(stripped_block)

    return cleaned_blocks
