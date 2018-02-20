import os, to_vtt
from PyQt5.QtWidgets import QMessageBox
#import logging

class file_worker:
    _srt = to_vtt.srt_parser
    _vtt = to_vtt.vtt_builder


    def open_file(self, path, name):
        folder = os.path.dirname(path)
        text = self.decoder(path)

        try:
            dictionary = self._srt().parse_text(text)
            vtt_result = self._vtt(dictionary).vtt_lines

            self.write_file(vtt_result, name, folder)
        except ValueError:
            self.syntax_error(path)

    def write_file(self, text, name, folder):
        path = '{0}/{1}.vtt'.format(folder, name)
        with open(path, 'w', encoding='utf-8') as file:
            file.writelines(text)

    def decoder(self, path):
        """
        It isn't perfect way to get
        encoding of the file.
        But I don't have other ideas.
        """

        file = open(path, 'rb')
        file_in = file.read()

        try:
            text = file_in.decode('utf-8').splitlines()
        except UnicodeDecodeError:
            try:
                text = file_in.decode('cp1251').splitlines()
            except UnicodeDecodeError:
                text = file_in.decode('iso-8859-1').splitlines()

        if text != None:
            return text
        else:
            return 'Unknown encoding'

    # Show syntax error message
    def syntax_error(self, path):
        message = QMessageBox()
        message.setText('Syntax error in {0}'.format(path))
        message.exec()