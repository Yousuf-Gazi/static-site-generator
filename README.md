# 🧰 Static Site Generator

This is a lightweight static site generator written in Python. It converts Markdown files from the `content/` directory into styled HTML files using a custom `template.html`, and outputs them into the `docs/` directory. It also copies over static assets like images and CSS from the `static/` folder.

## 📁 Directory Structure

- `content/` — Source Markdown content  
- `static/` — Static assets (e.g., CSS, images)  
- `template.html` — HTML template with placeholders  
- `docs/` — Output folder for the generated site  
- `src/` — Source code and tests  

## 🚀 Usage

```bash
python3 src/main.py
```
To clean and rebuild:
```bash
./main.sh
```


### 4. Testing Block
```markdown
## 🧪 Running Tests

```bash
python3 -m unittest discover src/
```


### 5. Features List
```markdown
📌 Features:

- Recursive page generation from nested folders
- Supports headings, lists, blockquotes, and inline Markdown
- Simple templating for dynamic title and content insertion
- Asset copying for deployment-ready builds

This is a personal project built to better understand file I/O, recursion, and A simple Markdown to HTML parser and static site generator built using Python.
```

## 🛠️ Technologies Used

- Python 3
- Markdown (custom parser)
- HTML/CSS (for templating and styling)
- Shell scripts (for automation)

## 📷 Example

A Markdown file at:
```
content/blog/glorfindel/index.md
```
Will be converted into:
```
docs/blog/glorfindel/index.html
```
With all images and styles properly linked from the `static/` folder.

## 🎯 Last but not least

<div align="center">
✨ *From guided beginnings to independent creation* ✨  
🐍 *Powered by Python’s simplicity*  
🌱 *Rooted in curiosity, grown through code*
</div>
