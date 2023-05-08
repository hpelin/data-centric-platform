import sys
from PyQt5.QtWidgets import QApplication

from dcp_client import settings
from dcp_client.fsimagestorage import FilesystemImageStorage
from dcp_client.bentoml_model import BentomlModel
from dcp_client.sync_src_dst import DataRSync
from dcp_client.app import Application
from dcp_client.welcome_window import WelcomeWindow

import warnings
warnings.simplefilter('ignore')


def main():
    settings.init()
    image_storage = FilesystemImageStorage()
    ml_model = BentomlModel()
    data_sync = DataRSync()
    '''
    data_sync = DataRSync(user_name="ubuntu",
                          host_name="jusuf-vm2",
                          server_repo_path="/home/ubuntu/data-centric-platform/data-sync/")
    '''
    welcome_app = Application(ml_model=ml_model, 
                              syncer=data_sync,
                              image_storage=image_storage,
                              server_ip='0.0.0.0',
                              server_port=7010)
    app = QApplication(sys.argv)
    window = WelcomeWindow(welcome_app)
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
