import os

root_dir = '/cv_project/datasets/add_fight' # replace with your directory
mp4_files = os.listdir(root_dir)
for mp4_file in mp4_files:
    if mp4_file.endswith('.mp4'):
        print(f'processing file:{os.path.join(root_dir, mp4_file)}')
        os.system(f'python3 transnetv2.py {os.path.join(root_dir, mp4_file)}')