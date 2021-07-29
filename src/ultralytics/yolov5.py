import importlib, os  # To import YOLOv5 as module

if not os.path.isdir('./yolov5'):
    from git import Repo

    print('YOLOv5 is not found, attempting clone')

    try:
        #Repo.clone_from('https://github.com/ultralytics/yolov5.git', 'yolov5')
        Repo.clone_from('https://github.com/KalenMike/yolov5.git', 'yolov5')
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

    def train(log_handler, **kwargs):
        _train = importlib.import_module("yolov5.train")
        opt =_train.parse_opt(True)
        for k, v in kwargs.items():
            setattr(opt, k, v)

        #_train.run(**kwargs)
        _train.main(opt)

    def newCallbackHandler():
        _callback_handler = importlib.import_module("yolov5.utils.callbacks")
        return _callback_handler.Callbacks()