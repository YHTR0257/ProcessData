import numpy as np
from pymatgen.io.vasp.outputs import Elfcar
from pymatgen.io.vasp import Poscar
import os

from ripser import Rips

class TDA:
    def __init__(self, data):
        self.data = data

    def compute_diagrams(self):
        rips = Rips()
        return rips.fit_transform(self.data)

class elf(TDA):
    def __init__(self, data, elf_path):
        super().__init__(data)
        self.elf_path = elf_path

    def _process_data(self):
        elfcar = Elfcar.from_file(self.elf_path)
    # ELFCARの概要を表示
    # print(dir(elfcar))
    # print(elfcar.structure)
        elf = elfcar.data["total"]
    # a軸の長さを取得
        lattice = elfcar.structure.lattice.as_dict()
        a = lattice['matrix'][0]
        b = lattice['matrix'][1]
        c = lattice['matrix'][2]

        xmax, ymax, zmax = elf.shape
        vmax, vmin = np.max(elf), np.min(elf)
        pmax, pmin = np.percentile(elf, 85), np.percentile(elf, 75)

    # pmax, pminの範囲でのみの値の座標を取得
        positions = np.where((elf < pmax) & (elf > pmin))
        positions = np.array(positions)
        positions = positions.T
    # 規格化を行う
        positions = positions / np.array([xmax, ymax, zmax])

        data = np.array([0, 0, 0])

        for item in positions:
            row = item * a + item * b + item * c
            data = np.vstack((data, row))
        data = data[1:]

        return data
    
    def compute_elf(self):
        return self.compute_diagrams()