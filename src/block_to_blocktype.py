from blocktype import BlockType

def block_to_block_type(block):

	lines = block.splitlines()

	if len(block) > 1 and block[0] == "#" and " " in block[:7]:
		counter = 0
		for x in block:
			if x == "#":
				counter +=1
			else:
				break
		if 1 <= counter <= 6 and block[counter] == " ":
			return BlockType.HEADING

	if block.startswith("```") and block.endswith("```"):
		return BlockType.CODE

	if all(line.startswith(">") for line in lines):
		return BlockType.QUOTE

	if all(line.startswith("- ") for line in lines):
		return BlockType.UNORDERED_LIST

	expected_number = 1
	ordered_list = True
	for line in lines:
		x = line.split(". ", 1)
		if len(x) == 2 and x[0].isdigit():
			if int(x[0]) != expected_number:
				ordered_list = False
				break
			expected_number += 1
		else:
			ordered_list = False
			break

	if ordered_list:
		return BlockType.ORDERED_LIST

	else:
		return BlockType.PARAGRAPH

