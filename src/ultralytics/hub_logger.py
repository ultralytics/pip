class HUBLogger:

    def __init__(self):
        return

    def on_train_batch_end(self, *args):
        print('[HookFired] : on_train_batch_end')

    def on_train_epoch_end(self, *args):
         print('[HookFired] : on_train_epoch_end')

    def on_val_batch_end(self, *args):
         print('[HookFired] : on_val_batch_end')

    def on_val_end(self, *args):
         print('[HookFired] : on_val_end')

    def on_train_val_end(self, *args):
         print('[HookFired] : on_train_val_end')

    def on_model_save(self, *args):
         print('[HookFired] : on_model_save')

    def on_train_end(self, *args):
         print('[HookFired] : on_train_end')