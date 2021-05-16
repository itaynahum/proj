import json
import os

from proj.TelemetryGenerator.Utils.Validator import clean_old_files


class TelemetryCreator:
    def __init__(self, telem_info, flushing_output, logger, output_limitation):
        self.logger = logger
        self.telem_info = telem_info
        self.output = flushing_output
        self.output_limitation = output_limitation
        self._result = {}

    @property
    def result(self):
        return self._result

    def handle(self):
        self.logger.info(msg="Started generating telemetry...")
        self._constructor()

        if self.output_limitation is not None:
            if len(os.listdir(self.output)) > self.output_limitation:
                clean_old_files(directory=self.output, logger=self.logger)

        self.flusher(self.result)

    def _constructor(self):
        self.logger.info(msg="Started telemetry constructor...")
        for field in list(self.telem_info.__dict__.keys()):
            self.result[field] = dict(self.telem_info.__dict__.items())[field]
            self.logger.debug(msg=f"Successfully added {field} to final json object...")
        self.logger.info(msg=f"Successfully created {self.telem_info.name} content")
        return self.result

    def flusher(self, output_json):
        current_file_handled = os.path.join(self.output, f'{self.telem_info.name}.json')
        try:
            with open(current_file_handled, 'w') as output_file:
                json.dump(output_json, output_file)
                self.logger.info(msg=f"Successfully generated and flushed telemetry: {current_file_handled}")
        except Exception or IOError as error:
            self.logger.error(msg=f"An error occurred while trying to write telemetry data into "
                                  f"{self.telem_info.name}\r\n\tException: {error}")
            self._remove_file(current_file_handled)

    def _remove_file(self, filepath):
        try:
            self.logger.info("Removing unhandled telemetry from directory...")
            os.remove(filepath)
            self.logger.debug(msg=f"Removed {filepath} from output directory")
        except Exception as error:
            self.logger.error(msg=f'An error occurred while trying to remove {filepath} from directory\r\n\t'
                                  f'Exception: {error}')


