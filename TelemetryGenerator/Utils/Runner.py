import time
import sys
import random
import uuid
import datetime

from datetime import date

from proj.TelemetryGenerator.Procedures.TelemetryCreator import TelemetryCreator
from proj.TelemetryGenerator.Procedures.TelemetryInfo import TelemetryInfo
from proj.TelemetryGenerator.Utils.Config import Config


class Runner:
    def __init__(self, logger, timeout: int) -> None:
        self.logger = logger
        self.timeout = timeout

    def sleep(self) -> None:
        self.logger.info(msg=f'Sleeping for {self.timeout} until next run...')
        time.sleep(self.timeout)

    def run(self):
        while True:
            try:
                self.logger.info(msg=f"Running a new session of handler...")
                telemetry_creator = self._construct_telemetry_objects()
                telemetry_creator.handle()
                self.sleep()
                self.logger.info(msg=f"{self.timeout} seconds passed.")
            except Exception:
                self.logger.critical(msg=sys.exc_info())
                raise

    def _construct_telemetry_objects(self):
        telemetry_id = str(uuid.uuid4())
        timestamp = str(datetime.datetime.now())
        telemetry_name_object = TelemetryInfo(generated_number=random.random(),
                                              telemetry_id=telemetry_id,
                                              timestamp=timestamp,
                                              name=Config.TELEMETRY_NAME_FORMAT.format(telemetry_id, date.today()))
        telemetry_creator = TelemetryCreator(telem_info=telemetry_name_object,
                                             flushing_output=Config.OUTPUT_DIRECTORY,
                                             logger=self.logger,
                                             output_limitation=Config.TELEMETRY_AMOUNT_LIMITATION)
        return telemetry_creator
