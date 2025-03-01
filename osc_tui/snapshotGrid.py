import npyscreen
import pyperclip

import createVm
import main
import popup
import selectableGrid
import virtualMachine


class SnapshotGrid(selectableGrid.SelectableGrid):
    def __init__(self, screen, *args, **keywords):
        super().__init__(screen, *args, **keywords)
        self.col_titles = ["Id", "Description", "Size (Gb)", "Volume"]

        def on_selection(line):
            popup.editSnapshot(self.form, line)

        self.on_selection = on_selection

    def refresh(self, name_filter=None):
        groups = main.GATEWAY.ReadSnapshots(form=self.form)['Snapshots']
        values = list()
        for g in groups:
            vId = g['VolumeId'] if 'VolumeId' in g else "no volumes"
            vSize = g['VolumeSize'] if 'VolumeSize' in g else "unknow"
            values.append([g['SnapshotId'], g['Description'], vSize, vId])
        self.values = values
