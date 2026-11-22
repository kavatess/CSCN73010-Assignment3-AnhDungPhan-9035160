"""Command-line interface: python -m unitconv 10 km mi"""

import argparse
import sys

from unitconv.converter import convert


def build_parser():
    parser = argparse.ArgumentParser(prog="unitconv", description="Convert units.")
    parser.add_argument("value", type=float, help="numeric value to convert")
    parser.add_argument("from_unit", help="source unit, e.g. km, lb, C")
    parser.add_argument("to_unit", help="target unit, e.g. mi, kg, F")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        result = convert(args.value, args.from_unit, args.to_unit)
    except ValueError as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 1
    print("%g %s = %.6g %s" % (args.value, args.from_unit, result, args.to_unit))
    return 0


if __name__ == "__main__":
    sys.exit(main())
