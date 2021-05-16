
from TelemetryGenerator.Utils.Logger import InitLogger
from TelemetryGenerator.Utils.Config import Config
from TelemetryGenerator.Utils.Validator import directory_validator
from TelemetryGenerator.Utils.Runner import Runner


if __name__ == "__main__":
    logger = InitLogger()
    basic_logger = logger.basic_logger()

    basic_logger.info(msg="Started TelemetryGenerator Successfully...")
    basic_logger.info(msg="Initialized logger object...")

    directory_validator(logger=basic_logger, directories=Config.DIRECTORIES_TO_VALIDATE)

    logger = logger.rotating_logger(basic_logger)

    runner = Runner(logger=logger, timeout=Config.TIMEOUT_BETWEEN_RUNS)
    runner.run()

