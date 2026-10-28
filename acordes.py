# MIR-Experiments-with-Music21
# Copyright (C) 2026 Pablo López-Rocamora
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from music21 import *
import matplotlib.pyplot as plt
from melodia_general import get_finalis
import re
from base import OrderedCounter

def chords(s):
    finalis = get_finalis(s)
    chord_ordered = list()
    schords = s.chordify()

    for c in schords.recurse().getElementsByClass('Chord'):
        if c.isIncompleteMajorTriad() == True:
            chord_ordered.append(c.getChordStep(1).name + ' - PMInc')
        elif c.isIncompleteMinorTriad() == True:
            chord_ordered.append(c.getChordStep(1).name + ' - PmInc')
        elif c.isMajorTriad() == True:
            chord_ordered.append(c.getChordStep(1).name + ' - PM')
        elif c.isMinorTriad() == True:
            chord_ordered.append(c.getChordStep(1).name + ' - Pm')
        elif c.isAugmentedTriad() == True:
            chord_ordered.append(c.getChordStep(1).name + ' - TriadaAum')
        elif c.isDiminishedTriad() == True:
            chord_ordered.append(c.getChordStep(1).name + ' - TriadaDism')
        elif c.isGermanAugmentedSixth() == True:
            chord_ordered.append(c.getChordStep(1).name + ' - 6Al')
        elif c.isFrenchAugmentedSixth() == True:
            chord_ordered.appendc(c.getChordStep(1).name + ' - 6Fr')
        elif c.isItalianAugmentedSixth() == True:
            chord_ordered.append(c.getChordStep(1).name + ' - 6It')
        elif c.isSwissAugmentedSixth() == True:
            chord_ordered.append(c.getChordStep(1).name + ' - 6Sui')
        elif c.isAugmentedSixth() == True:
            chord_ordered.append(c.getChordStep(1).name + ' - 6Aum')
        elif c.isDominantSeventh() == True:
            chord_ordered.append(c.getChordStep(1).name + ' - 7Dom')
        elif c.isDiminishedSeventh() == True:
            chord_ordered.append(c.getChordStep(1).name + ' - 7Dism')
        elif c.isHalfDiminishedSeventh() == True:
            chord_ordered.append(c.getChordStep(1).name + ' - HalfDim7')
        elif c.isFalseDiminishedSeventh() == True:
            chord_ordered.append(c.getChordStep(1).name + ' - FalseDim7')
        elif c.isSeventh() == True:
            chord_ordered.append(c.getChordStep(1).name + ' - 7Diat')
        else:
            continue
        
    chord_ordered = sorted(chord_ordered)
    index = None
    for n, i in enumerate(chord_ordered):
        
        if bool(re.search(f'{finalis.name}\s\-\s.+', i)) == True:
            index = n
            break
    lst2 = chord_ordered[index:-1]
    lst1 = chord_ordered[:index]
    chord_sorted = lst2 + lst1
    chord_dict = OrderedCounter(chord_sorted)
    return chord_dict

