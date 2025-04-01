def markdown_to_blocks(markdown):

	split_blocks = markdown.split("\n\n")

	blocks = []

	for block in split_blocks:
		stripped_block = block.strip()

		if stripped_block:
			stripped_block = stripped_block.replace("\t", "")
			blocks.append(stripped_block)

	return blocks
