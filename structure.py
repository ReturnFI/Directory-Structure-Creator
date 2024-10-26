import os

def create_structure_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        if not lines:
            print("Error: The tree.txt file is empty. Here's a default structure example:")
            print_default_structure()
            return

        base_path = ""
        
        for line in lines:
            level = line.count("    ")
            item = line.strip(" ├─└│ \n")

            if item.endswith('/'):
                base_path = os.path.join(base_path, item.strip('/'))
                os.makedirs(base_path, exist_ok=True)
            elif item:
                file_path = os.path.join(base_path, item)
                with open(file_path, 'w', encoding='utf-8') as fp:
                    fp.write("")
            else:
                print(f"Warning: Skipping invalid line: {line.strip()}")

            if lines.index(line) < len(lines) - 1:
                next_level = lines[lines.index(line) + 1].count("    ")
                if next_level < level:
                    base_path = "/".join(base_path.split('/')[:next_level])

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        print_default_structure()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def print_default_structure():
    default_structure = """\
dashboard/
├── index.html
├── style.css
├── script.js
├── pages/
│   ├── index.html
│   ├── users.html
│   └── settings.html
"""
    print(default_structure)

create_structure_from_file('tree.txt')
