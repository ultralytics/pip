import os  # To import YOLOv5 as module
from .authentication import verifyAndFetch
from .yolov5 import YOLOv5

from . import hub_logger as HUBLogger

from pick import pick


def loadModels():
    email = input('Enter your email:')
    api_key = input('Enter your API key:')
    # email = 'kalen.michael@ultralytics.com'
    # api_key = '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4'
    return verifyAndFetch(email, api_key)

def listModelNames(models):
    modelList = []
    for model in models:
        modelList.append(model['name'])
    return modelList

def registerLogger():
    callback_handler = YOLOv5.newCallbackHandler()
    hub_logger = HUBLogger.HUBLogger()
    callback_handler.regsiterAction('on_train_batch_end', 'HUB', hub_logger.on_train_batch_end)
    callback_handler.regsiterAction('on_train_epoch_end', 'HUB', hub_logger.on_train_epoch_end)
    callback_handler.regsiterAction('on_val_end', 'HUB', hub_logger.on_val_end)
    callback_handler.regsiterAction('on_val_end', 'HUB', hub_logger.on_train_val_end)
    callback_handler.regsiterAction('on_model_save', 'HUB', hub_logger.on_model_save)
    callback_handler.regsiterAction('on_train_end', 'HUB', hub_logger.on_train_end)

    return callback_handler

def trainModel(model):
    print('Starting Training for' + model['name'])
    print(f"Configuration applied, Image Size = {model['options']['imageSize']}, Batch Size = {model['options']['batchSize']}")
    #print(f"Configuration applied, Image Size = {model['options']['imageSize']}, Batch Size = {model['options']['batchSize']}")

    hook_handler = registerLogger()


    print('Running command:')
    print(f"YOLOv5.train(imgsz={model['options']['imageSize']},batch={model['options']['batchSize']},data='{model['dataset']['url']}', epochs={model['options']['epochs']}, weights={model['parent']['url']},nosave=True,cache=True)")
    YOLOv5.train(hook_handler, imgsz=model['options']['imageSize'],batch=model['options']['batchSize'],data=f"{model['dataset']['url']}",epochs=model['options']['epochs'],weights=f"{model['parent']['url']}",nosave=True,cache=True)


def main():
    models = loadModels()

    if models:
        if len(models) > 1:
            # User to select which model
            options = listModelNames(models)
            title = 'You have multiple models pending connection. Please select the model you would like to train now: '
            option, index = pick(options, title)
            print('Loading model configuration for ' + option)
            trainModel(models[index])
        else:
            # Start training only model
            return
        # Load models pending training from DB via cloud function api request
        # List options to user