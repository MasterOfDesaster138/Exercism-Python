"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    coordinate = record[1]
    return coordinate 


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """

    return tuple([coordinate[0], coordinate[1]])


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    #if azara_record[0] == rui_record[1][0] and azara_record[1] == rui_record[1][1]:
    #    return True
    #return False

    return tuple(azara_record[1]) == rui_record[1]


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    new_record = 'not a match'

    if compare_records(azara_record, rui_record):
        new_record = azara_record + rui_record
    
    return new_record
        


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.
    """

    report = ""

    for record in combined_record_group:
        cleaned_record = list(record)
        cleaned_record.pop(1)  # Entfernt das Koordinatentuple aus dem Datensatz
        report += str(tuple(cleaned_record)) + "\n"  # Fügt den bereinigten Datensatz dem Bericht hinzu

    return report

