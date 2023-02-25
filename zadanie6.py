def remove_comments(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    in_comment = False
    out = []

    for line in content.split('\n'):
        if in_comment:
            if '*/' in line:
                in_comment = False
                line = line.split('*/', 1)[1].lstrip()
            else:
                continue

        if '//' in line:
            line = line.split('//', 1)[0].rstrip()

        if '/*' in line:
            in_comment = True
            line = line.split('/*', 1)[0].rstrip()

        if line:
            out.append(line)

    return '\n'.join(out)

input_file_path = r'C:\Users\Public\zadanie6\PlikC.cpp'
output_file_path = r'C:\Users\Public\zadanie6\PlikC_without_comments.cpp'

with open(output_file_path, 'w') as f:
    f.write(remove_comments(input_file_path))
