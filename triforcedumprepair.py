#!/usr/bin/env python3
import argparse
import os
import bsdiff4
import hashlib as hash
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='+')
    args = parser.parse_args()
    for path in args.files:
        handle_path(Path(path))

def handle_path(path):
    if path.is_dir():
        for f in path.iterdir():
            if f.is_file():
                hash_file(f)
    else:
        hash_file(path)

def hash_file(file):
    md5 = hash.md5()
    with open(file, 'rb') as input:
        buffer = input.read(65536)
        while len(buffer) > 0:
            md5.update(buffer)
            buffer = input.read(65536)
    patch_file(file, md5.hexdigest())

def patch_file(file, checksum):
    match checksum:
        case '02d1d5867bf345af3c8c82587925e582':
            if file.name == tdb['GDT-0004C']:
                print('Known good dump of F-Zero AX (Rev C) with correct filename, nothing to do.')
                return
            print(f'Known good dump of F-Zero AX (Rev C), renaming from {file.name} to {tdb["GDT-0004C"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0004C']))
        case 'ab1e442313cc0cc2dd1f52f0407aed1a':
            if file.name == tdb['GDT-0004D']:
                print('Known good dump of F-Zero AX (Rev D) with correct filename, nothing to do.')
                return
            print(f'Known good dump of F-Zero AX (Rev D), renaming from {file.name} to {tdb["GDT-0004D"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0004D']))
        case 'd136d34eb303b32308b67f69d4c6e780':
            if file.name == tdb['GDT-0004E']:
                print('Known good dump of F-Zero AX (Rev E) with correct filename, nothing to do.')
                return
            print(f'Known good dump of F-Zero AX (Rev E), renaming from {file.name} to {tdb["GDT-0004E"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0004E']))
        case '6f6884c5dcd3e44fe0d3a42bf3b826a7':
            if file.name == tdb['GDT-0008B']:
                print('Known good dump of Gekitou Pro Yakyuu (Rev B) with correct filename, nothing to do.')
                return
            print(f'Known good dump of Gekitou Pro Yakyuu (Rev B), renaming from {file.name} to {tdb["GDT-0008B"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0008B']))
        case 'e074c698e358786013383fe36bc8fcb3':
            if file.name == tdb['GDT-0008C']:
                print('Known good dump of Gekitou Pro Yakyuu (Rev C) with correct filename, nothing to do.')
                return
            print(f'Known good dump of Gekitou Pro Yakyuu (Rev C), renaming from {file.name} to {tdb["GDT-0008C"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0008C']))
        case '3e4665b12b6abe1248d4eb2618b934c5':
            if file.name == tdb['GDT-0006A']:
                print('Known good dump of The Key Of Avalon - The Wizard Master (client, Rev A) with correct filename, nothing to do.')
                return
            print(f'Known good dump of The Key Of Avalon - The Wizard Master (client, Rev A), renaming from {file.name} to {tdb["GDT-0006A"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0006A']))
        case '127f78b732f175be610277fbc61f2d1a':
            if file.name == tdb['GDT-0006C']:
                print('Known good dump of The Key Of Avalon - The Wizard Master (client, Rev C) with correct filename, nothing to do.')
                return
            print(f'Known good dump of The Key Of Avalon - The Wizard Master (client, Rev C), renaming from {file.name} to {tdb["GDT-0006C"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0006C']))
        case '6b406cdd8d220f23336c19b6905e6c0e':
            if file.name == tdb['GDT-0006E']:
                print('Known good dump of The Key Of Avalon - The Wizard Master (client, Rev E) with correct filename, nothing to do.')
                return
            print(f'Known good dump of The Key Of Avalon - The Wizard Master (client, Rev E), renaming from {file.name} to {tdb["GDT-0006E"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0006E']))
        case '4eb0075ff475c7b024158e32a5cf2655':
            if file.name == tdb['GDT-0006F']:
                print('Known good dump of The Key Of Avalon - The Wizard Master (client, Rev F) with correct filename, nothing to do.')
                return
            print(f'Known good dump of The Key Of Avalon - The Wizard Master (client, Rev F), renaming from {file.name} to {tdb["GDT-0006F"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0006F']))
        case '9fa8c481d0629e5655ffc5436d0df7c3':
            if file.name == tdb['GDT-0006G']:
                print('Known good dump of The Key Of Avalon - The Wizard Master (client, Rev G) with correct filename, nothing to do.')
                return
            print(f'Known good dump of The Key Of Avalon - The Wizard Master (client, Rev G), renaming from {file.name} to {tdb["GDT-0006G"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0006G']))
        case 'dbacbe42a708958b51b0b59357b3711a':
            if file.name == tdb['GDT-0005A']:
                print('Known good dump of The Key Of Avalon - The Wizard Master (server, Rev A) with correct filename, nothing to do.')
                return
            print(f'Known good dump of The Key Of Avalon - The Wizard Master (server, Rev A), renaming from {file.name} to {tdb["GDT-0005A"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0005A']))
        case '46f1d6359114795aa53ddeb292187ea6':
            if file.name == tdb['GDT-0005C']:
                print('Known good dump of The Key Of Avalon - The Wizard Master (server, Rev C) with correct filename, nothing to do.')
                return
            print(f'Known good dump of The Key Of Avalon - The Wizard Master (server, Rev C), renaming from {file.name} to {tdb["GDT-0005C"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0005C']))
        case '50df6d7e611100ec90c10ed75602af6e':
            if file.name == tdb['GDT-0005E']:
                print('Known good dump of The Key Of Avalon - The Wizard Master (server, Rev E) with correct filename, nothing to do.')
                return
            print(f'Known good dump of The Key Of Avalon - The Wizard Master (server, Rev E), renaming from {file.name} to {tdb["GDT-0005E"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0005E']))
        case '6b64ec19eeed55e93091c7e707424728':
            if file.name == tdb['GDT-0005F']:
                print('Known good dump of The Key Of Avalon - The Wizard Master (server, Rev F) with correct filename, nothing to do.')
                return
            print(f'Known good dump of The Key Of Avalon - The Wizard Master (server, Rev F), renaming from {file.name} to {tdb["GDT-0005F"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0005F']))
        case '298e7766bb9aa3fbf923b9204fb0423f':
            if file.name == tdb['GDT-0005G']:
                print('Known good dump of The Key Of Avalon - The Wizard Master (server, Rev G) with correct filename, nothing to do.')
                return
            print(f'Known good dump of The Key Of Avalon - The Wizard Master (server, Rev G), renaming from {file.name} to {tdb["GDT-0005G"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0005G']))
        case '899a66d776320b211559510384ff5bd3':
            if file.name == tdb['GDT-0010A']:
                print('Known good dump of The Key Of Avalon 1.2 - Summon The New Monsters (client, Rev A) with correct filename, nothing to do.')
                return
            print(f'Known good dump of The Key Of Avalon 1.2 - Summon The New Monsters (client, Rev A), renaming from {file.name} to {tdb["GDT-0010A"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0010A']))
        case '4d5a942a2dc251806bd039e292216782':
            if file.name == tdb['GDT-0009A']:
                print('Known good dump of The Key Of Avalon 1.2 - Summon The New Monsters (server, Rev A) with correct filename, nothing to do.')
                return
            print(f'Known good dump of The Key Of Avalon 1.2 - Summon The New Monsters (server, Rev A), renaming from {file.name} to {tdb["GDT-0009A"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0009A']))
        case 'ec40384a478539fac39d1e4a175188c9':
            if file.name == tdb['GDT-0010C']:
                print('Known good dump of The Key Of Avalon 1.3 - Chaotic Sabbat (client, Rev C) with correct filename, nothing to do.')
                return
            print(f'Known good dump of The Key Of Avalon 1.3 - Chaotic Sabbat (client, Rev C), renaming from {file.name} to {tdb["GDT-0010C"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0010C']))
        case 'c5c1793a315c3232c61c796d3446a18e':
            if file.name == tdb['GDT-0009C']:
                print('Known good dump of The Key Of Avalon 1.3 - Chaotic Sabbat (server, Rev C) with correct filename, nothing to do.')
                return
            print(f'Known good dump of The Key Of Avalon 1.3 - Chaotic Sabbat (server, Rev C), renaming from {file.name} to {tdb["GDT-0009C"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0009C']))
        case 'b80ac04e7cfdf370fabaab680a4f52a5':
            if file.name == tdb['GDT-0019A']:
                print('Known good dump of The Key Of Avalon 2.5 - War of the Key (client, Rev A) with correct filename, nothing to do.')
                return
            print(f'Known good dump of The Key Of Avalon 2.5 - War of the Key (client, Rev A), renaming from {file.name} to {tdb["GDT-0019A"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0019A']))
        case '750816ed7e636fbbcc34aaaf9688bd9f':
            if file.name == tdb['GDT-0019B']:
                print('Known good dump of The Key Of Avalon 2.5 - War of the Key (client, Rev B) with correct filename, nothing to do.')
                return
            print(f'Known good dump of The Key Of Avalon 2.5 - War of the Key (client, Rev B), renaming from {file.name} to {tdb["GDT-0019B"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0019B']))
        case '6ab1732d4080d54b0ccbc73c45e726c3':
            if file.name == tdb['GDT-0018A']:
                print('Known good dump of The Key Of Avalon 2.5 - War of the Key (server, Rev A) with correct filename, nothing to do.')
                return
            print(f'Known good dump of The Key Of Avalon 2.5 - War of the Key (server, Rev A), renaming from {file.name} to {tdb["GDT-0018A"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0018A']))
        case 'be1ae078d862ae4f7e1b3f02151fce66':
            if file.name == tdb['GDT-0019B']:
                print('Known good dump of The Key Of Avalon 2.5 - War of the Key (client, Rev B) with correct filename, nothing to do.')
                return
            print(f'Known good dump of The Key Of Avalon 2.5 - War of the Key (client, Rev B), renaming from {file.name} to {tdb["GDT-0018B"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0018B']))
        case '5134088e7495d64b10747368df400d5f':
            if file.name == tdb['GDT-0011']:
                print('Known good dump of Triforce DIMM Updater (3.17) with correct filename, nothing to do.')
                return
            print(f'Known good dump of Triforce DIMM Updater (3.17), renaming from {file.name} to {tdb["GDT-0011"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0011']))
        case 'dadf78d080caa10796484afad4d4d7ce':
            if file.name == tdb['GDT-0022A']:
                print('Known good dump of Triforce Firmware Update For Compact Flash Box (4.01) with correct filename, nothing to do.')
                return
            print(f'Known good dump of Triforce Firmware Update For Compact Flash Box (4.01), renaming from {file.name} to {tdb["GDT-0022A"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0022A']))
        case 'b218ab878c6f1fbc5fa79d175db3e6f7':
            if file.name == tdb['GDT-0014']:
                print('Known good dump of Virtua Striker 4 (Asia) with correct filename, nothing to do.')
                return
            print(f'Known good dump of Virtua Striker 4 (Asia), renaming from {file.name} to {tdb["GDT-0014"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0014']))
        case '24cf61f44201747d8cf2f86d90c0309e':
            if file.name == tdb['GDT-0014B']:
                print('Known good dump of Virtua Striker 4 (Asia, Rev B) with correct filename, nothing to do.')
                return
            print(f'Known good dump of Virtua Striker 4 (Asia, Rev B), renaming from {file.name} to {tdb["GDT-0014B"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0014B']))
        case '4dafecb6de804835435551f734b21a49':
            if file.name == tdb['GDT-0015']:
                print('Known good dump of Virtua Striker 4 (Export) with correct filename, nothing to do.')
                return
            print(f'Known good dump of Virtua Striker 4 (Export), renaming from {file.name} to {tdb["GDT-0015"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0015']))
        case 'c9a1b56df120ad96f731b621d59b648a':
            if file.name == tdb['GDT-0015A']:
                print('Known good dump of Virtua Striker 4 (Export, Rev A) with correct filename, nothing to do.')
                return
            print(f'Known good dump of Virtua Striker 4 (Export, Rev A), renaming from {file.name} to {tdb["GDT-0015A"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0015A']))
        case '53a0eb3d593b3280911269d2aee2f6b1':
            if file.name == tdb['GDT-0021']:
                print('Known good dump of Virtua Striker 4 Ver.2006 (Export) with correct filename, nothing to do.')
                return
            print(f'Known good dump of Virtua Striker 4 Ver.2006 (Export), renaming from {file.name} to {tdb["GDT-0021"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0021']))
        case 'bd8e8ecbe1f8958dd8f2cc0cdf30dc5a':
            if file.name == tdb['GDT-0020B']:
                print('Known good dump of Virtua Striker 4 Ver.2006 (Japan, Rev B) with correct filename, nothing to do.')
                return
            print(f'Known good dump of Virtua Striker 4 Ver.2006 (Japan, Rev B), renaming from {file.name} to {tdb["GDT-0020B"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0020B']))
        case '76bdb7ebfa8eca19fd31374f65359a15':
            if file.name == tdb['GDT-0020D']:
                print('Known good dump of Virtua Striker 4 Ver.2006 (Japan, Rev D) with correct filename, nothing to do.')
                return
            print(f'Known good dump of Virtua Striker 4 Ver.2006 (Japan, Rev D), renaming from {file.name} to {tdb["GDT-0020D"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0020D']))
        case 'eec44d152ccd630d68f5df85293e06b3':
            if file.name == tdb['GDT-0002']:
                print('Known good dump of Virtua Striker 2002 (Export) with correct filename, nothing to do.')
                return
            print(f'Known good dump of Virtua Striker 2002 (Export), renaming from {file.name} to {tdb["GDT-0002"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0002']))
        case '4ceadb37ab23da1bd2b5fbcc92059193':
            if file.name == tdb['GDT-0001']:
                print('Known good dump of Virtua Striker 2002 (Japan) with correct filename, nothing to do.')
                return
            print(f'Known good dump of Virtua Striker 2002 (Japan), renaming from {file.name} to {tdb["GDT-0001"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0001']))
        case '97facc2db79c84ca2bd8a27ed9129c86':
            if file.name == tdb['GDT-0012']:
                print('Known good dump of Virtua Striker 2002 (Type 3) with correct filename, nothing to do.')
                return
            print(f'Known good dump of Virtua Striker 2002 (Type 3), renaming from {file.name} to {tdb["GDT-0012"]}')
            os.rename(file, Path(file.parent, tdb['GDT-0012']))
        case 'f64f4ee996c29490c5cdd352da640dbd':
            if file.name == tdb['GDT-0004D']:
                print('Known modified (DOL patch) dump of F-Zero AX (Rev D) with correct filename, patching file.')
                file_patch_inplace(file, FZeroAx.patch)
                return
            print(f'Known modified (DOL patch) dump of F-Zero AX (Rev D), patching file and from {file.name} to {tdb["GDT-0004D"]}')
            file_patch_inplace(file, FZeroAx.patch)
            os.rename(file, Path(file.parent, tdb['GDT-0004D']))
        case 'dec69ba6805a308fa486ecdb7deba86d':
            if file.name == tdb['GDT-0004D']:
                print('Known modified (DOL patch) dump of F-Zero AX (Rev D) with correct filename, patching file.')
                file_patch_inplace(file, 'F-Zero-AX_fixed.patch')
                return
            print(f'Known modified (DOL patch) dump of F-Zero AX (Rev D), patching file and from {file.name} to {tdb["GDT-0004D"]}')
            file_patch_inplace(file, 'F-Zero-AX_fixed.patch')
            os.rename(file, Path(file.parent, tdb['GDT-0004D']))
        case '236561a6fe8b6387a1f0558372d9c4ce':
            if file.name == tdb['GDT-0020D']:
                print('Known modified (DOL patch) dump of Virtua Striker 4 Ver.2006 (Japan, Rev D) with correct filename, patching file.')
                file_patch_inplace(file, vs406.patch)
                return
            print(f'Known modified (DOL patch) dump of Virtua Striker 4 Ver.2006 (Japan, Rev D), patching file and from {file.name} to {tdb["GDT-0020D"]}')
            file_patch_inplace(file, vs406.patch)
            os.rename(file, Path(file.parent, tdb['GDT-0020D']))
        case '3a28d974b96546a89c279a20c3360b04':
            if file.name == tdb['GDT-0021']:
                print('Known modified (header patch) dump of Virtua Striker 4 Ver.2006 (Export) with correct filename, patching file.')
                file_patch_inplace(file, GVS46E.patch)
                return
            print(f'Known modified (header patch) dump of Virtua Striker 4 Ver.2006 (Export), patching file and from {file.name} to {tdb["GDT-0021"]}')
            file_patch_inplace(file, GVS46E.patch)
            os.rename(file, Path(file.parent, tdb['GDT-0021']))
        case 'a8878c592abbb35c5b4d633e1cf9f179':
            if file.name == tdb['GDT-0004C']:
                print('Known modified (header patch) dump of F-Zero AX (Rev C) with correct filename, patching file.')
                file_patch_inplace(file, 'F-Zero AX (Japan) (Rev C).patch')
                return
            print(f'Known modified (header patch) dump of F-Zero AX (Rev C), patching file and from {file.name} to {tdb["GDT-0004C"]}')
            file_patch_inplace(file, 'F-Zero AX (Japan) (Rev C).patch')
        case '1632826dab98f02f87ca474345f59db1':
            if file.name == tdb['GDT-0004D']:
                print('Known modified (DOL patch) dump of F-Zero AX (Rev D) with correct filename, patching file.')
                file_patch_inplace(file, 'F-Zero AX (Japan) (Rev D).patch')
                return
            print(f'Known modified (header patch) dump of F-Zero AX (Rev D), patching file and from {file.name} to {tdb["GDT-0004D"]}')
            file_patch_inplace(file, 'F-Zero AX (Japan) (Rev D).patch')
        case '1632826dab98f02f87ca474345f59db1':
            if file.name == tdb['GDT-0004E']:
                print('Known modified (header patch) dump of F-Zero AX (Rev E) with correct filename, patching file.')
                file_patch_inplace(file, 'F-Zero AX (Japan) (Rev E).patch')
                return
            print(f'Known modified (header patch) dump of F-Zero AX (Rev E), patching file and from {file.name} to {tdb["GDT-0004E"]}')
            file_patch_inplace(file, 'F-Zero AX (Japan) (Rev E).patch')
        case '61fc061f9bf409d1e41e202d760ecfc0':
            if file.name == tdb['GDT-0008B']:
                print('Known modified (header patch) dump of Gekitou Pro Yakyuu (Rev B) with correct filename, patching file.')
                file_patch_inplace(file, 'trihdrGPY(Rev B).patch')
                return
            print(f'Known modified (header patch) dump of Gekitou Pro Yakyuu (Rev B), patching file and from {file.name} to {tdb["GDT-0008B"]}')
            file_patch_inplace(file, 'trihdrGPY(Rev B).patch')
        case '2f668e87163f8c1be1cd6d0302da6241':
            if file.name == tdb['GDT-0008C']:
                print('Known modified (header patch) dump of Gekitou Pro Yakyuu (Rev C) with correct filename, patching file.')
                file_patch_inplace(file, 'trihdrGPY(Rev C).patch')
                return
            print(f'Known modified (header patch) dump of Gekitou Pro Yakyuu (Rev C), patching file and from {file.name} to {tdb["GDT-0008C"]}')
            file_patch_inplace(file, 'trihdrGPY(Rev C).patch')
        case 'ac8eefd736b450bec30c250cfbe56882':
            if file.name == tdb['GDT-0014']:
                print('Known modified (header patch) dump of Virtua Striker 4 (Asia) with correct filename, patching file.')
                file_patch_inplace(file, 'trihdrvs4 (Asia).patch')
                return
            print(f'Known modified (header patch) dump of Virtua Striker 4 (Asia), patching file and from {file.name} to {tdb["GDT-0014"]}')
            file_patch_inplace(file, 'trihdrvs4 (Asia).patch')
        case '748678d167d9af203442eda9d3e119c9':
            if file.name == tdb['GDT-0014B']:
                print('Known modified (header patch) dump of Virtua Striker 4 (Asia, Rev B) with correct filename, patching file.')
                file_patch_inplace(file, 'trihdrvs4 (Asia, Rev B).patch')
                return
            print(f'Known modified (header patch) dump of Virtua Striker 4 (Asia, Rev B), patching file and from {file.name} to {tdb["GDT-0014B"]}')
            file_patch_inplace(file, 'trihdrvs4 (Asia, Rev B).patch')
        case '2723ef745c2ba722e4b069ffe569549a':
            if file.name == tdb['GDT-0015']:
                print('Known modified (header patch) dump of Virtua Striker 4 (Export) with correct filename, patching file.')
                file_patch_inplace(file, 'trihdrvs4 (Export).patch')
                return
            print(f'Known modified (header patch) dump of Virtua Striker 4 (Export), patching file and from {file.name} to {tdb["GDT-0015"]}')
            file_patch_inplace(file, 'trihdrvs4 (Export).patch')
        case '37dbfa1cebe6d24c59ff65f0914e30c6':
            if file.name == tdb['GDT-0015A']:
                print('Known modified (header patch) dump of Virtua Striker 4 (Export, Rev A) with correct filename, patching file.')
                file_patch_inplace(file, 'trihdrvs4 (Export, Rev A).patch')
                return
            print(f'Known modified (header patch) dump of Virtua Striker 4 (Export, Rev A), patching file and from {file.name} to {tdb["GDT-0015A"]}')
            file_patch_inplace(file, 'trihdrvs4 (Export, Rev A).patch')
        case '37dbfa1cebe6d24c59ff65f0914e30c6':
            if file.name == tdb['GDT-0021']:
                print('Known modified (header patch) dump of Virtua Striker 4 Ver.2006 (Export) with correct filename, patching file.')
                file_patch_inplace(file, 'trihdrvs4v2006 (Export).patch')
                return
            print(f'Known modified (header patch) dump of Virtua Striker 4 Ver.2006 (Export), patching file and from {file.name} to {tdb["GDT-0021"]}')
            file_patch_inplace(file, 'trihdrvs4v2006 (Export).patch')
        case '504f328b6ee8f864a6e13b9dcf4ff502':
            if file.name == tdb['GDT-0020B']:
                print('Known modified (header patch) dump of Virtua Striker 4 Ver.2006 (Japan, Rev B) with correct filename, patching file.')
                file_patch_inplace(file, 'trihdrvs4v2006 (Japan, Rev B).patch')
                return
            print(f'Known modified (header patch) dump of Virtua Striker 4 Ver.2006 (Japan, Rev B), patching file and from {file.name} to {tdb["GDT-0020B"]}')
            file_patch_inplace(file, 'trihdrvs4v2006 (Japan, Rev B).patch')
        case '6732f669b24c7b3d2cca5bb2996798e3':
            if file.name == tdb['GDT-0020D']:
                print('Known modified (header patch) dump of Virtua Striker 4 Ver.2006 (Japan, Rev D) with correct filename, patching file.')
                file_patch_inplace(file, 'trihdrvs4v2006 (Japan, Rev D).patch')
                return
            print(f'Known modified (header patch) dump of Virtua Striker 4 Ver.2006 (Japan, Rev D), patching file and from {file.name} to {tdb["GDT-0020D"]}')
            file_patch_inplace(file, 'trihdrvs4v2006 (Japan, Rev D).patch')
        case 'c3e6a83debbb605f4a9bd423f22a30a8':
            if file.name == tdb['GDT-0002']:
                print('Known modified (header patch) dump of Virtua Striker 2002 (Export) with correct filename, patching file.')
                file_patch_inplace(file, 'trihdrvsv2002 (Export).patch')
                return
            print(f'Known modified (header patch) dump of Virtua Striker 2002 (Export), patching file and from {file.name} to {tdb["GDT-0002"]}')
            file_patch_inplace(file, 'trihdrvs2002 (Export).patch')
        case 'b596e077a05a597cbba235dbe641773f':
            if file.name == tdb['GDT-0001']:
                print('Known modified (header patch) dump of Virtua Striker 2002 (Japan) with correct filename, patching file.')
                file_patch_inplace(file,'trihdrvsv2002 (Japan).patch')
                return
            print(f'Known modified (header patch) dump of Virtua Striker 2002 (Japan), patching file and from {file.name} to {tdb["GDT-0001"]}')
            file_patch_inplace(file, 'trihdrvs2002 (Japan).patch')
        case 'c238af615632568d70a1543c903774d4':
            if file.name == tdb['GDT-0012']:
                print('Known modified (header patch) dump of Virtua Striker 2002 (Type 3) with correct filename, patching file.')
                file_patch_inplace(file,'trihdrvsv2002 (Type 3).patch')
                return
            print(f'Known modified (header patch) dump of Virtua Striker 2002 (Type 3), patching file and from {file.name} to {tdb["GDT-0012"]}')
            file_patch_inplace(file, 'trihdrvs2002 (Type 3).patch')
tdb = {
    'GDT-0001': 'Virtua Striker 2002 (Japan).BIN',
    'GDT-0002': 'Virtua Striker 2002 (Export).BIN',
    'GDT-0004C': 'F-Zero AX (Rev C).BIN',
    'GDT-0004D': 'F-Zero AX (Rev D).BIN',
    'GDT-0004E': 'F-Zero AX (Rev E).BIN',
    'GDT-0005A': 'The Key Of Avalon - The Wizard Master (server, Rev A).GCM',
    'GDT-0005C': 'The Key Of Avalon - The Wizard Master (server, Rev C).GCM',
    'GDT-0005E': 'The Key Of Avalon - The Wizard Master (server, Rev E).GCM',
    'GDT-0005F': 'The Key Of Avalon - The Wizard Master (server, Rev F).GCM',
    'GDT-0005G': 'The Key Of Avalon - The Wizard Master (server, Rev G).GCM',
    'GDT-0006A': 'The Key Of Avalon - The Wizard Master (client, Rev A).GCM',
    'GDT-0006C': 'The Key Of Avalon - The Wizard Master (client, Rev C).GCM',
    'GDT-0006E': 'The Key Of Avalon - The Wizard Master (client, Rev E).GCM',
    'GDT-0006F': 'The Key Of Avalon - The Wizard Master (client, Rev F).GCM',
    'GDT-0006G': 'The Key Of Avalon - The Wizard Master (client, Rev G).GCM',
    'GDT-0008B': 'Gekitou Pro Yakyuu Mizushima Shinji All Stars vs. Pro Yakyuu (Rev B).BIN',
    'GDT-0008C': 'Gekitou Pro Yakyuu Mizushima Shinji All Stars vs. Pro Yakyuu (Rev C).BIN',
    'GDT-0009A': 'The Key Of Avalon 1.2 - Summon The New Monsters (server, Rev A).GCM',
    'GDT-0009C': 'The Key Of Avalon 1.3 - Chaotic Sabbat (server, Rev C).GCM',
    'GDT-0010A': 'The Key Of Avalon 1.2 - Summon The New Monsters (client, Rev A).GCM',
    'GDT-0010C': 'The Key Of Avalon 1.3 - Chaotic Sabbat (client, Rev C).GCM',
    'GDT-0011': 'Triforce DIMM Updater (3.17).BIN',
    'GDT-0012': 'Virtua Striker 2002 (Type 3).BIN',
    'GDT-0014': 'Virtua Striker 4 (Asia).BIN',
    'GDT-0014B': 'Virtua Striker 4 (Asia, Rev B).BIN',
    'GDT-0015': 'Virtua Striker 4 (Export).BIN',
    'GDT-0015A': 'Virtua Striker 4 (Export, Rev A).BIN',
    'GDT-0018A': 'The Key Of Avalon 2.5 - War of the Key (server, Rev A).GCM',
    'GDT-0018B': 'The Key Of Avalon 2.5 - War of the Key (server, Rev B).GCM',
    'GDT-0019A': 'The Key Of Avalon 2.5 - War of the Key (client, Rev A).GCM',
    'GDT-0019B': 'The Key Of Avalon 2.5 - War of the Key (client, Rev B).GCM',
    'GDT-0020B': 'Virtua Striker 4 Ver.2006 (Japan, Rev B).BIN',
    'GDT-0020D': 'Virtua Striker 4 Ver.2006 (Japan, Rev D).BIN',
    'GDT-0021': 'Virtua Striker 4 Ver.2006 (Export).BIN',
    'GDT-0022A': 'Triforce Firmware Update For Compact Flash Box (4.01).BIN'
}
if __name__ == '__main__':
    main()