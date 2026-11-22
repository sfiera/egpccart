#!/usr/bin/env python3

import argparse
import cadquery
import math
from cadquery import exporters

W, H, D = 58, 61, 20.2
TOP = 8.6
BOT = 11.6
PCB = 1.7
EXT = 1.4


def main():
    top = (
        cadquery.Workplane("XY")
        .box(100, 100, 8.6, centered=(True, True, False))
        .union(
            cadquery.Workplane("XY")
            .box(W - 2, H - 3, 1.5, centered=(True, True, False))
            .translate((0, -0.5, 8.6))
        )
        .cut(
            cadquery.Workplane("XY")
            .box(W - 4, H, 100, centered=(True, True, False))
            .translate((0, 2, 2))
        )
        .union(
            cadquery.Workplane("XY")
            .center(0, H / 2 - 23.5)
            .cylinder(8.5, 7.7 / 2, centered=(True, True, False))
            .faces(">Z")
            .workplane()
            .hole(2.8, 3)
        )
        .cut(
            cadquery.Workplane("XY")
            .center(0, H / 2 - 23.5)
            .cylinder(6.9, 5.0 / 2, centered=(True, True, False))
        )
        .union(
            cadquery.Workplane("XY")
            .center(0, H / 2 - 12.5)
            .box(W - 4, 1, 8.5, centered=(True, True, False))
        )
        .union(
            cadquery.Workplane("XY")
            .center(13.5, -H / 2 + 7.5)
            .box(1, 11, TOP, centered=(True, True, False))
        )
        .union(
            cadquery.Workplane("XY")
            .center(-13.5, -H / 2 + 7.5)
            .box(1, 11, TOP, centered=(True, True, False))
        )
        .cut(
            cadquery.Workplane("XY")
            .center(0, H / 2 - 32 / 2 - 9.5)
            .box(49, 32, 0.2, centered=(True, True, False))
            .cut(
                cadquery.Workplane("XY")
                .center(0, H / 2 - 32 / 2 - 9.5)
                .box(48, 31, 0.2, centered=(True, True, False))
            )
        )
        .intersect(
            cadquery.Workplane("XY").rect(W, H).extrude(D).edges(">Y").chamfer(1)
        )
    )

    bottom = (
        cadquery.Workplane("XY")
        .box(100, 100, BOT, centered=(True, True, False))
        .cut(
            cadquery.Workplane("XY")
            .box(W - 2, H - 3, 100, centered=(True, True, False))
            .translate((0, -0.5, BOT - 1.4))
        )
        .cut(
            cadquery.Workplane("XY")
            .box(W - 4, H, 100, centered=(True, True, False))
            .edges("|Y")
            .chamfer(1.5)
            .translate((0, 2, 2))
        )
        .union(
            cadquery.Workplane("XY")
            .center(0, H / 2 - 23.5)
            .cylinder(BOT, 4.8 / 2, centered=(True, True, False))
            .union(
                cadquery.Workplane("XY")
                .center(0, H / 2 - 23.5)
                .box(10, 1, BOT - PCB, centered=(True, True, False))
            )
            .faces(">Z")
            .workplane()
            .hole(1.75, 9)
        )
        .union(
            cadquery.Workplane("XY")
            .center(0, H / 2 - 12.5)
            .box(W - 4, 1, BOT - PCB, centered=(True, True, False))
            .union(
                cadquery.Workplane("XY")
                .center(-W / 2 + 2 + 5.5 / 2, H / 2 - 12.5)
                .box(5.5, 1, BOT, centered=(True, True, False))
            )
            .union(
                cadquery.Workplane("XY")
                .center(W / 2 - 2 - 5.5 / 2, H / 2 - 12.5)
                .box(5.5, 1, BOT, centered=(True, True, False))
            )
        )
        .union(
            cadquery.Workplane("XY")
            .center(-W / 2 + 2 + 4, H / 2 - 23)
            .box(8, 1, BOT - PCB, centered=(True, True, False))
            .union(
                cadquery.Workplane("XY")
                .center(-W / 2 + 2 + 2.75, H / 2 - 23)
                .box(5.5, 1, BOT + EXT, centered=(True, True, False))
            )
        )
        .union(
            cadquery.Workplane("XY")
            .center(W / 2 - 2 - 4.25, H / 2 - 25)
            .box(8.5, 1, BOT + EXT, centered=(True, True, False))
        )
        .union(
            cadquery.Workplane("XY")
            .center(11.5, -H / 2 + 7.5)
            .box(1, 11, BOT - PCB, centered=(True, True, False))
            .union(
                cadquery.Workplane("XY")
                .center(11.5, -H / 2 + 6.5)
                .box(1, 9.0, BOT + EXT, centered=(True, True, False))
            )
        )
        .union(
            cadquery.Workplane("XY")
            .center(-11.5, -H / 2 + 7.5)
            .box(1, 11, BOT - PCB, centered=(True, True, False))
            .union(
                cadquery.Workplane("XY")
                .center(-11.5, -H / 2 + 6.5)
                .box(1, 9.0, BOT + EXT, centered=(True, True, False))
            )
        )
        .intersect(
            cadquery.Workplane("XY")
            .rect(W, H)
            .extrude(D)
            .edges("|Y")
            .edges("<Z")
            .chamfer(4)
            .edges(">Y")
            .chamfer(1)
        )
    )

    window = (
        cadquery.Workplane("XY")
        .union(bottom)
        .cut(
            cadquery.Workplane("XY")
            .center(0, -6.5)
            .box(48, 22, 3, centered=(True, True, False))
        )
    )

    for name, obj in {"top": top, "bottom": bottom, "window": window}.items():
        file = f"egpccart-{name}.stl"
        print(f"writing to {file}")
        obj.val().exportStl(file)


if __name__ == "__main__":
    main()
