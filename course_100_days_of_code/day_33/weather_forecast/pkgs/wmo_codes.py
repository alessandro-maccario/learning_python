import os
import sys
import pandas as pd

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pkgs.constants import WMO_CODES


class WMOProcessing:
    def __init__(self) -> None:
        pass

    def wmo_json_2_pandas(self) -> pd.DataFrame:
        # read the wmo_codes.json data in
        data = pd.read_json(WMO_CODES)
        # hold all the "day" values inside the list_wmo_code
        list_wmo_code = []
        for key_wmo_code, value in data.items():
            # add the wmo code to the "day" dictionary to easy the conversion to a DataFrame
            value["day"].update({"wmo_code": key_wmo_code})
            list_wmo_code.append(value["day"])

        # convert dictionary to pd.DataFrame to be used in conjunction with the weather data and add the wmo_code
        df = pd.DataFrame.from_records(list_wmo_code)

        return df
