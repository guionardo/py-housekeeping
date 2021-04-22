import datetime
import logging
import os
import time
import zipfile

from file_infos import FileInfos


class HouseKeeper:

    LOG = logging.getLogger(__name__)

    def __init__(self, configuration):
        self._configuration = configuration

    def run(self):
        total_processed_count = 0
        total_processed_size = 0
        total_keep_count = 0
        total_new_file_size = 0
        total_kept_file_size = 0
        t0 = time.time()
        for config in self._configuration.configs:
            file_infos = FileInfos(config.folder)
            processing_files, keep_files = file_infos.processing_files(
                config.rules)
            (processed_count,
             processed_size,
             new_file_size,
             kept_file_size) = self.process(config,
                                            processing_files,
                                            keep_files)
            total_processed_count += processed_count
            total_processed_size += processed_size
            total_new_file_size += new_file_size
            total_kept_file_size += kept_file_size
            total_keep_count += len(keep_files)
        resume = {
            "folders": len(self._configuration.configs),
            "processed files": total_processed_count,
            "kept files": total_keep_count,
            "kept files size": total_kept_file_size,
            "freed bytes": total_processed_size,
            "new file size": total_new_file_size,
            "running time": str(datetime.timedelta(seconds=time.time()-t0))
        }
        self.LOG.info('House keeping %s', resume)

    def process(self, config, processing_files, keep_files):
        self.LOG.info('Rule: %s', str(config))
        if not processing_files:
            self.LOG.info('No need to house keeping folder %s', config.folder)
            return 0, 0, 0, self._kept_files_size(keep_files)
        if config.action.action == 'delete':
            return self._process_delete(processing_files, keep_files)
        elif config.action.action == 'move':
            return self._process_move(processing_files, keep_files, config.action.action_destiny)
        elif config.action.action == 'compress':
            return self._process_compress(processing_files, keep_files, config.action.action_destiny)

    def _kept_files_size(self, keep_files):
        return sum([file[2] for file in keep_files])

    def _process_delete(self, processing_files, keep_files):
        processed_count = 0
        processed_size = 0
        try:
            for file in processing_files:
                os.unlink(file[0])
                processed_count += 1
                processed_size += file[2]
                self.LOG.info('DELETED FILE %s', file[0])
        except Exception as exc:
            self.LOG.error('EXCEPTION WHEN DELETING: %s', exc)

        return processed_count, processed_size, processed_size, self._kept_files_size(keep_files)

    def _process_move(self, processing_files, keep_files, action_destiny):
        processed_count = 0
        processed_size = 0
        try:
            for file in processing_files:
                new_file = os.path.join(
                    action_destiny, os.path.basename(file[0]))

                os.rename(file[0], new_file)
                processed_count += 1
                processed_size += file[2]
                self.LOG.info('MOVED FILE %s TO %s', file[0], new_file)
        except Exception as exc:
            self.LOG.error('EXCEPTION WHEN MOVING: %s', exc)

        return processed_count, processed_size, 0, self._kept_files_size(keep_files)

    def _process_compress(self, processing_files, keep_files, action_destiny):
        destiny_file = os.path.join(
            action_destiny, 'house_keep_'+datetime.datetime.now().strftime("%Y%m%d%H%M%S"+".zip"))
        processed_count = 0
        processed_size = 0
        new_file_size = 0
        try:
            with zipfile.ZipFile(destiny_file, 'w', compression=zipfile.ZIP_DEFLATED) as zip:
                comment = "House keep done in {0}".format(
                    datetime.datetime.now())
                zip.comment = bytes(comment)
                zip.debug = 1
                for file in processing_files:
                    zip.write(file[0])
                    processed_count += 1
                    processed_size += file[2]
                    self.LOG.info('COMPRESSED FILE %s', file[0])
            new_file_size = os.path.getsize(destiny_file)
            for file in processing_files:
                os.unlink(file[0])
            resume = {
                "processed files": processed_count,
                "freed size": processed_size,
                "zip file size": new_file_size,
                "zip file": destiny_file
            }
            self.LOG.info('ZIPPED %s', resume)

        except Exception as exc:
            self.LOG.error('EXCEPTION WHEN ZIPPING FILES: %s', exc)

        return processed_count, processed_size, new_file_size, self._kept_files_size(keep_files)
