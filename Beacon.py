class Beacon:
    def __init__(self, major: int, minor: int, avg_first_update_time: int, first_update_time_list, addition_time_list, avg_addition_time: float,
                 update_time_list, avg_update_time: float,
                 rssi_sma_list, rssi_sma: float):
        self.major = major
        self.minor = minor
        self.avg_first_update_time = avg_first_update_time
        self.first_update_time_list = first_update_time_list
        self.addition_time_list = addition_time_list
        self.avg_addition_time = avg_addition_time
        self.update_time_list = update_time_list
        self.avg_update_time = avg_update_time
        self.rssi_sma_list = rssi_sma_list
        self.rssi_sma = rssi_sma
        self.is_first_update_done = False

    # To initialise a new beacon from major, minor and addition time.
    # Called whenever a "Beacon_Added" command is received.
    @classmethod
    def from_maj_min_time(cls, major: int, minor: int, time: float):
        return cls(major, minor, time, [], [].append(time), 0, [], 0, [], 0)

    # To check whether the beacon object has the same major and minor as the passed parameters.
    def is_beacon(self, major: int, minor: int):
        if self.major == major & self.minor == minor:
            return True
        else:
            return False

    # Update the addition_time_list and the avg_addition_time.
    # Called whenever an "Updating_Beacon" command is received.
    def new_update_time(self, time: float):
        sum_ = self.avg_update_time * len(self.update_time_list)
        self.update_time_list.append(time)
        self.avg_update_time = (sum_ + time) / len(self.update_time_list)

    # Print the conclusions from the last scan cycle.
    # Print the Beacon details.
    # Print the addition_time for this cycle.
    # Print the first_update_time for this cycle.
    def print_scan_result(self):
        print("Beacon {" + self.major + "," + self.minor + "} result:")
        print("Addition Time")
