from typing import Tuple

import pandas as pd


class FilterDisk:
    def apply(self, data: pd.DataFrame) -> pd.DataFrame:
        disk_data, remaining_data = self.__identify_disks(data)
        selected_disk = disk_data.sort_values('n_om').iloc[0]

        output_data = remaining_data.append(selected_disk)
        output_data.sort_index(inplace=True)
        output_data.reset_index(inplace=True)
        
        return output_data

    def __identify_disks(self, data: pd.DataFrame) -> Tuple[pd.DataFrame]:
        find_disk = lambda x: 1 if 'FI' in x else 0

        data['aux_col'] = data['equipment'].apply(find_disk)
        disk_data = data[data['aux_col']==1].copy()
        disk_data.drop(columns='aux_col', inplace=True)

        remaining_data = data[data['aux_col']==0].copy()
        remaining_data.drop(columns='aux_col', inplace=True)

        return disk_data, remaining_data
