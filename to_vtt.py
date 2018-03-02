"""
This module converts subtitles to .vtt format
For now it converts only .srt subs

This shitty code writed by je09
Github repository: https://github.com/je09/2VTT

2018
"""
#import logging

class srt_parser:
    """
    Parsing of .srt content
    Returns dictionary with structured sub's information
    """
    def __init__(self):
        self._sub_metadata = {'counter': [], 'time': [], 'text': []}

    def parse_time(self, time):
        """
        Parsing time
        Input is a list with unparsed
        values of subtitle's time
        Returns list with 2 lists with time in 4 variables
        """
        parsed_time = []

        for i in time:
            hours, minutes, seconds = i.split(':', 2)
            seconds, microseconds = seconds.split(',', 1)
            parsed_time.append([int(hours), int(minutes), int(seconds), int(microseconds)])

        return parsed_time

    def parse_text(self, sub_text):
        """
        Parsing the whole text of the subtitle
        Input is a list with lines
        just from the .srt file
        Maybe I should add it in __init__?
        """

        # TODO: Rewrite this in beatiful way
        single_replica = []
        full_replicas = []

        for i in enumerate(sub_text):
            # String shouldn't be empty
            if bool(i[1].strip()):
                single_replica.append(i[1])
            # String should be empty, but previous line shouldn't
            # Also it works if it's end of the list
            # TODO: Simplify this statement
            if (bool(i[1].strip()) == False and (len(single_replica)) != 0) or (i[0] == len(sub_text) - 1):
                full_replicas.append(single_replica)
                single_replica = []

        for replica_groups in full_replicas:
            if replica_groups:
                self.parse_lines(replica_groups)

        return self._sub_metadata

    def parse_lines(self, line_text):
        # print(line_text)
        self._sub_metadata['counter'].append(int(line_text[0].strip().strip('\ufeff')))
        self._sub_metadata['time'].append(self.parse_time(line_text[1].strip().split(' --> ', 1)))
        self._sub_metadata['text'].append(line_text[2:len(line_text)])


class vtt_builder:
    """
    Build a .vtt file from the dictionary

    Result stores in the 'vtt_lines' after initialisation
    """

    # List with converted subtitle lines
    vtt_lines = []
    # Dicitionary of the subtitle
    _metadata = {}

    def __init__(self, subtitle_dictionary):
        """
        Input: dictionary from parser
        """
        # Initialisation of the metada dictionary and starting of the building
        self._metadata = subtitle_dictionary
        self._build_lines()

    def _build_time(self, time):
        """
        Building time section according to the pattern
        Input: time list from dictionary
        Output: string with time formated for vtt
        Example: 00:00:26.720
        """
        return '{:02d}:{:02d}:{:02d}.{:03d}'.format(time[0], time[1],
                                                    time[2], time[3])

    def _build_lines(self):
        """
        Building dialog lines from metada
        """
        amount_of_lines = len(self._metadata['counter'])
        lines = []

        for i in range(0, amount_of_lines):
            text = ''
            # Building time section
            start_time, end_time = self._metadata['time'][i]
            time = '{0} --> {1}'.format(self._build_time(start_time),
                                        self._build_time(end_time))
            # Building text section
            for j in (self._metadata['text'])[i]:
                text += j + '\n'

            # Building line itself and adding it into the list
            lines.append('{0}\n{1}\n'.format(time, text))

        self._build_vtt(lines)

    def _build_vtt(self, lines):
        """
        Build .vtt formated subtitle content
        Input: list of lines of the subtitle
        """
        self.vtt_lines = 'WEBVTT\n\n'

        for i in lines:
            self.vtt_lines += i