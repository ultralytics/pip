import importlib, os  # To import YOLOv5 as module

if not os.path.isdir('./yolov5'):
    from git import Repo

    print('YOLOv5 is not found, attempting clone')

    try:
        Repo.clone_from('https://github.com/ultralytics/yolov5.git', 'yolov5')
        print('YOLOv5 cloned!')
    except Exception as e:
        print('Failed to clone YOLOv5 repo.' + str(e))

class YOLOv5:

    def export(**kwargs):
        _export = importlib.import_module("yolov5.export")
        _export.run(**kwargs)

    def detect(**kwargs):
        _detect = importlib.import_module("yolov5.detect")
        _detect.run(**kwargs)

    def train(**kwargs):
        _train = importlib.import_module("yolov5.train")
        _train.run(**kwargs)