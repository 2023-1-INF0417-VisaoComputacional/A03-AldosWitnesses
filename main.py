from flask import Flask, request
import uuid, os, requests

from Katna.video import Video
from Katna.writer import KeyFrameDiskWriter	

app = Flask(__name__)
ROOT = r"./videos"
caption_ip = os.environ["CAPTIONING_SERVER"]

@app.route('/keyframe-extractor', methods=["POST"])
def request_handler():
    data = request.data
    for filename in request.files:
        file = request.files[filename]
        if file:
            save_filename = os.path.join(ROOT, str(uuid.uuid4()) + ".avi")
            file.save(save_filename)
            print(f"Received file {save_filename}.")
    if os.path.isfile(save_filename):
        dirpath = keyframe_gen(save_filename)
        success = send_images(dirpath)
        text = "Success!\n"
    else:
        text = "An internal error ocurred, please try again later.\n"
    return text
    #return translate_caption(text)

def keyframe_gen(filepath):
    vd = Video()
    path_segments = os.path.split(filepath)
    tail = path_segments[-1].split(".")[0]
    path_segments = list(path_segments[ : -1]) + [tail]
    frames_path = os.path.join("", *path_segments )
    no_of_frames_to_return = 12
    diskwriter = KeyFrameDiskWriter(location=f"/{frames_path}")
    print(f"Saving frames of {filepath} to {frames_path}.")
    vd.extract_video_keyframes(no_of_frames=no_of_frames_to_return, file_path=filepath, writer=diskwriter)
    print("Frames saved!")
    return frames_path

def send_images(dirpath):
    success = False
    captions = []
    for file in os.listdir(dirpath):
        if file.endswith(".jpeg"):
            print(f"Sending frame {os.path.join(dirpath, file)}...")
            with open(os.path.join(dirpath, file), 'rb') as f:
                res = requests.post(f"http://{caption_ip}/python-backend", files={"data" : f})
                captions.append([file, res.text])
                print(f"Request response\n{res.text}\n")
                success = True
    text = ""
    for file, caption in captions:
        text += f"{file} - {caption}\n"
    if success:
        with open(os.path.join(dirpath, "captions.txt"), "w") as file:
            file.write(text)
    return success

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1882)
