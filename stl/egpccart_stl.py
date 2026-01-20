#!/usr/bin/env python3

import argparse
import cadquery
import math
from cadquery import exporters


W, H, D = 58, 61, 20.2


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
        .box(100, 100, 11.6, centered=(True, True, False))
        .cut(
            cadquery.Workplane("XY")
            .box(W - 2, H - 3, 100, centered=(True, True, False))
            .translate((0, -0.5, 11.6 - 1.4))
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
            .cylinder(11.6, 4.5 / 2, centered=(True, True, False))
            .union(
                cadquery.Workplane("XY")
                .center(0, H / 2 - 23.5)
                .box(10, 1, 9.5, centered=(True, True, False))
            )
            .faces(">Z")
            .workplane()
            .hole(1.75, 9)
        )
        .union(
            cadquery.Workplane("XY")
            .center(0, H / 2 - 12.5)
            .box(W - 4, 1, 9.5, centered=(True, True, False))
            .union(
                cadquery.Workplane("XY")
                .center(-W / 2 + 2 + 4.9 / 2, H / 2 - 12.5)
                .box(4.9, 1, 11.6, centered=(True, True, False))
            )
            .union(
                cadquery.Workplane("XY")
                .center(W / 2 - 2 - 4.9 / 2, H / 2 - 12.5)
                .box(4.9, 1, 11.6, centered=(True, True, False))
            )
        )
        .union(
            cadquery.Workplane("XY")
            .center(-W / 2 + 2 + 4, H / 2 - 23)
            .box(8, 1, 9.5, centered=(True, True, False))
            .union(
                cadquery.Workplane("XY")
                .center(-W / 2 + 2 + 2.75, H / 2 - 23)
                .box(5.5, 1, 13, centered=(True, True, False))
            )
        )
        .union(
            cadquery.Workplane("XY")
            .center(W / 2 - 2 - 4.25, H / 2 - 25)
            .box(8.5, 1, 13, centered=(True, True, False))
        )
        .union(
            cadquery.Workplane("XY")
            .center(11.5, -H / 2 + 7.5)
            .box(1, 11, 9.5, centered=(True, True, False))
            .union(
                cadquery.Workplane("XY")
                .center(11.5, -H / 2 + 6.25)
                .box(1, 8.5, 13, centered=(True, True, False))
            )
        )
        .union(
            cadquery.Workplane("XY")
            .center(-11.5, -H / 2 + 7.5)
            .box(1, 11, 9.5, centered=(True, True, False))
            .union(
                cadquery.Workplane("XY")
                .center(-11.5, -H / 2 + 6.25)
                .box(1, 8.5, 13, centered=(True, True, False))
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
            .center(0, -6.25)
            .box(48, 22.5, 3, centered=(True, True, False))
        )
    )

    for name, obj in {"top": top, "bottom": bottom, "window": window}.items():
        file = f"egpccart-{name}.stl"
        print(f"writing to {file}")
        obj.val().exportStl(file)


if __name__ == "__main__":
    main()
