import logging
import os

from file_age import is_aged_file


class FileInfos:

    LOG = logging.getLogger(__name__)

    def __init__(self, folder):
        self._folder = folder
        self._files = []
        for root, dirs, files in os.walk(folder):
            for file in files:
                fn = os.path.join(root, file)
                self._files.append(
                    (fn, os.path.getmtime(fn), os.path.getsize(fn)))
        self._files.sort(key=lambda x: x[1])

    def get_files(self):
        return self._files

    def processing_files(self, rules):
        keep = []
        processing = []
        if rules.max_file_count > 0 and\
                len(self._files) > rules.max_file_count:
            keep = self._files[-rules.max_file_count:]
            processing = self._files[0:len(self._files)-rules.max_file_count]
        else:
            keep = self._files

        if rules.max_folder_size > 0:
            folder_size = 0
            keep0 = []
            while keep:
                file = keep.pop(0)
                if folder_size+file[2] < rules.max_folder_size:
                    keep0.append(file)
                    folder_size += file[2]
                else:
                    processing.append(file)
            keep = keep0

        if rules.max_file_age.seconds > 0:
            keep0 = []
            while keep:
                file = keep.pop(0)
                if not is_aged_file(file[1], rules.max_file_age):
                    keep0.append(file)
                else:
                    processing.append(file)
            keep = keep0

        if processing:
            size_processing = 0
            for file in processing:
                size_processing += file[2]
            self.LOG.info('Processing %s files (%s bytes) in folder %s', len(
                processing), size_processing, self._folder)

        return processing, keep
