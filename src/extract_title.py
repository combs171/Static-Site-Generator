def extract_title(markdown):
	for line in markdown.split("\n"):
		if line.startswith("# "):
			return line[2:].strip()
	raise ValueError("No h1 header found in markdown.")

