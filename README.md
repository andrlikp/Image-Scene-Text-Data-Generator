# Image-Scene-Text-Data-Generator
This code generates text into images and creates annotation.txt file for neural networks end-to-end training. It also creates trainMLT.txt file with names of all training images.

## Step for correct working:

1. Install all packages from requirements.txt
2. You need text files for generating texts. Example files are in folder text_files. Code for fast extraction Wikipedia dumps is in folder Wiki_Dumps_Extraction.
3. You need folder with images in which the text will be generated. Code for downloading image database is in the folder Image_data_download.
4. Specify paths in to_train_AITGM.py. Description is in the code as comment. Variables are: <b>src_path</b>; <b>end_path</b>; <b>train_file_path</b>
5. Adjust or make your own yaml file for setting text generator. Example but fully set file is <b>ct.yml</b>
6. Specify path where annotation files will be save in yaml file. Variable is annotation: path:
7. Choose a font you want and get it in folder fonts. Then update font names in yaml file. Preset type is <b><i>.otf</b></i>
8. Execute <b>to_train_AITGM.py</b> without any parameters. All is set now, happy generating.
