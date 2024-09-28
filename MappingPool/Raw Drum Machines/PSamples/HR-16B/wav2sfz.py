import os

directory = os.getcwd()

wav_files = [f for f in os.listdir(directory) if f.endswith(".wav")]

#print(os.getcwd())
#print(wav_files)

for wav_file in wav_files:
    output_filename = os.path.splitext(wav_file)[0] + ".sfz"  # Remove .wav extension
    output_path = os.path.join(directory, output_filename)

    #print(output_path)

    with open(output_path, "w") as f:
        f.write(f"<region> sample={wav_file}")