# Copyright (c) FRC 1076 PiHi Samurai
# You may use, distribute, and modify this software under the terms of
# the license found in the root directory of this project

from configuration import configsources
from network import ntmanager
import ntcore
import logging
from video import CameraManager
from pipeline import PipelineManager
from utils.misc import releaseGIL

from processes import rootsrv_client as rootsrv
import os
from dotenv import load_dotenv


load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.DEBUG if os.getenv("DEBUG") == "true" else logging.INFO, 
    format='[%(levelname)s] %(threadName)s(%(name)s): %(message)s' # stdout is being logged by journald, which already keeps timestamps
)

logger = logging.getLogger(__name__)


if __name__ == "__main__":

    logger.info("Launching SamuraiSight")

    
    inst: ntcore.NetworkTableInstance = ntcore.NetworkTableInstance.getDefault()
    inst.startServer(os.getenv("ROBORIO"))
    inst.startClient4(os.getenv("DEV_NAME"))
    ntmanager.initialize(os.getenv("DEV_NAME"),inst)
    rootsrv.initialize(os.getenv("ROOTSRV_SOCK"))

    configurator = configsources.ConfigParser("config.toml")

    configurator.loadFieldConfig()

    CameraManager.loadCameras(configurator.getCameraConfigs())
    PipelineManager.loadPipelines(configurator.getPipelineConfigs())
    PipelineManager.startAll()

    while True:
        #TODO: Manage webclient/NT client here
        releaseGIL()

    
    
    


    

    
    
    






    
