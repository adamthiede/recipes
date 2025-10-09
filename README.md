# Recipes!

A recipe site and static content generator using [discount](https://www.pell.portland.or.us/~orc/Code/discount/) and python.

Markdown is easier to write for most people than HTML. So this converts recipes in markdown to HTML and deploys them to [my recipe site](https://recipes.thiedefamily.org).

## Adding a recipe

- make a new markdown file (`recipe_name.md`) in the `source` folder.
- Look at the `0.md.example` file for ideal formatting.
- The first line should have the title of the recipe that will be extracted to the main page. It should begin with `# ` (a single pound sign and a space). This is an "H1" in HTML (the biggest header size).
- After that, put ingredients and steps with two pound signs to denote "h2" fields in HTML. (Smaller headers.)
- Use `-` (minus, hyphen) for list items.
- Separate new paragraphs by multiple newlines.

## License

Python code is AGPL, recipes are CC0

## Forking

If you want to do this yourself, just edit the head and foot templates, and deploy to github or gitlab. I've included a CI workflow for both.
