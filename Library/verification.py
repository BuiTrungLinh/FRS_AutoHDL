class Verification:
    def __init__(self, sp):
        self.sp = sp

    def verify_config(self):
        # check all changed cfgs in .text file acording to IFs current, save intto dict file
        # check each command-value in scanner
        return

    def verify_iden(self):
        # add expected into dict, obser into dict, compare
        return

    def verify_eventlog(self):
        # sending sp command to get event log, make sure there are required events
        return

    def verify_combination(self):
        # verify .wav file, ule
        return


def compare_data(expected, obser):
    return False if expected != obser else True
