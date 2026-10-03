"""PowerWash Desktop — A local helper for PowerWash Simulator job folders, wash notes, and clean photos."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='powerwash_desktop',
        description='A local helper for PowerWash Simulator job folders, wash notes, and clean photos.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('PowerWash Desktop')
    print('Keep the job list on disk before a DLC lot.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
