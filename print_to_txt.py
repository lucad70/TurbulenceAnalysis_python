import os

def merge_python_files_to_text(directory, output_file):
    with open(output_file, 'w') as merged_file:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as f:
                        file_content = f.read()
                        merged_file.write(f"\n\n# File: {file_path}\n\n")
                        merged_file.write(file_content)

# Specify the directory of the cloned repository
repository_directory = '/home/lucadg911/TurbulenceAnalysis_python'
# Specify the path for the merged output file
output_file = '/home/lucadg911/TurbulenceAnalysis_python/print.txt'

merge_python_files_to_text(repository_directory, output_file)
