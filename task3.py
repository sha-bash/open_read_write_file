import os

folder_path = 'D:/python/open_read_write_file/sorted'
file_names = os.listdir(folder_path)

file_names_sorted = sorted(file_names, key=lambda f: len(open(os.path.join(folder_path, f), encoding='utf-8').readlines()))

merged_file_path = 'D:/python/open_read_write_file/merged_file.txt'
with open(merged_file_path, 'w', encoding='utf-8') as merged_file:
    for file_name in file_names_sorted:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, encoding='utf-8') as file:
            lines = file.readlines()
            line_count = len(lines)
        
        merged_file.write(f'{file_name}\n')
        merged_file.write(f'{line_count}\n')
        merged_file.write(''.join(lines))
