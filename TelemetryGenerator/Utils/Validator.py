import os


def directory_validator(logger, directories):
    for directory in directories:
        logger.info(msg=f"Started validating directory: {directory}")
        if not os.path.exists(directory):
            try:
                logger.error(msg=f"Can't find directory: {directory}... Creating.")
                os.makedirs(directory)
                logger.info(msg="Successfully created directory.")
            except Exception as error:
                logger.error(msg=f"An error occurred while trying to create directory: {directory}\r\n\t"
                                 f"Exception: {error}")
                return
        logger.info(msg="Successfully validated directories...")


def clean_old_files(logger, directory):
    for file in os.listdir(directory):
        try:
            os.remove(os.path.join(directory, file))
        except Exception as error:
            logger.error(msg=f"An error occurred while trying to remove file: {file} from {directory}\r\n\t"
                             f"Exception: {error}")
    logger.debug(msg=f"Successfully removed old files from directory: {directory}")


