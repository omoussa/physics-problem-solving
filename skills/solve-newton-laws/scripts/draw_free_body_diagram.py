#!/usr/bin/env python3
"""Render schematic external-force diagrams from JSON, with alt text."""
from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch


def finite_number(value, field):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{field} must be a finite number.")
    value = float(value)
    if not math.isfinite(value):
        raise ValueError(f"{field} must be a finite number.")
    return value


def nonempty_string(value, field):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field} must be a nonempty string.")
    return value.strip()


def unit(angle_deg):
    angle = math.radians(angle_deg)
    return (math.cos(angle), math.sin(angle))


def plain_label(label):
    text = label.replace("$", "")
    text = re.sub(r"\\(?:vec|hat|mathrm|text)\{([^{}]*)\}", r"\1", text)
    text = text.replace("\\to", " to ").replace("\\imath", "i").replace("\\jmath", "j")
    return re.sub(r"[{}\\]", "", text).replace("_", " ").strip()


def validate_config(config):
    if not isinstance(config, dict):
        raise ValueError("The input must be a JSON object.")
    objects = config.get("objects")
    if not isinstance(objects, list) or not objects:
        raise ValueError("objects must be a nonempty list.")
    if "title" in config:
        nonempty_string(config["title"], "title")
    for i, obj in enumerate(objects):
        prefix = f"objects[{i}]"
        if not isinstance(obj, dict):
            raise ValueError(f"{prefix} must be an object.")
        nonempty_string(obj.get("object_label"), f"{prefix}.object_label")
        forces = obj.get("forces")
        if not isinstance(forces, list):
            raise ValueError(f"{prefix}.forces must be a list.")
        for j, force in enumerate(forces):
            name = f"{prefix}.forces[{j}]"
            if not isinstance(force, dict):
                raise ValueError(f"{name} must be an object.")
            nonempty_string(force.get("label"), f"{name}.label")
            finite_number(force.get("angle_deg"), f"{name}.angle_deg")
            if "description" in force:
                nonempty_string(force["description"], f"{name}.description")
            offset = force.get("label_offset", [0, 0])
            if not isinstance(offset, (list, tuple)) or len(offset) != 2:
                raise ValueError(f"{name}.label_offset must contain two numbers.")
            for n in offset:
                finite_number(n, f"{name}.label_offset")
        if "axes" in obj:
            axes = obj["axes"]
            if not isinstance(axes, dict):
                raise ValueError(f"{prefix}.axes must be an object.")
            x_angle = finite_number(axes.get("x_angle_deg", 0), f"{prefix}.axes.x_angle_deg")
            y_angle = finite_number(axes.get("y_angle_deg", x_angle + 90), f"{prefix}.axes.y_angle_deg")
            if not math.isclose((y_angle - x_angle) % 180, 90, abs_tol=1e-7):
                raise ValueError(f"{prefix}.axes must be perpendicular.")
            for key in ("x_label", "y_label"):
                if key in axes:
                    nonempty_string(axes[key], f"{prefix}.axes.{key}")
    return config


def angle_difference(a, b):
    return abs((a - b + 180) % 360 - 180)


def arrow(ax, start, end, *, force=True):
    patch = FancyArrowPatch(
        start, end, arrowstyle="-|>", mutation_scale=18 if force else 13,
        linewidth=2.2 if force else 1.2,
        color="#111111" if force else "#555555",
        linestyle="-" if force else "--", zorder=3,
        shrinkA=0, shrinkB=0,
    )
    ax.add_patch(patch)


def draw_forces(ax, obj):
    ax.set_aspect("equal")
    ax.set_xlim(-1.85, 1.85)
    ax.set_ylim(-1.85, 1.85)
    ax.axis("off")
    ax.set_title(obj["object_label"], fontsize=15, fontweight="bold", pad=14)
    ax.add_patch(Circle((0, 0), radius=0.14, facecolor="#eeeeee",
                        edgecolor="#111111", linewidth=1.3, zorder=4))
    forces = obj["forces"]
    for index, force in enumerate(forces):
        angle = force["angle_deg"] % 360
        ux, uy = unit(angle)
        nx, ny = -uy, ux
        peers = [
            j for j, other in enumerate(forces)
            if angle_difference(angle, other["angle_deg"]) < 8
        ]
        # Separate nearly parallel force arrows while retaining their attachment.
        rank = peers.index(index)
        spread = 0 if len(peers) == 1 else (rank / (len(peers) - 1) - 0.5) * 0.18
        start = (0.06 * ux + spread * nx, 0.06 * uy + spread * ny)
        end = (1.18 * ux + spread * nx, 1.18 * uy + spread * ny)
        arrow(ax, start, end)
        offset = force.get("label_offset", [0, 0])
        label_spread = spread * 2.5
        position = (
            1.40 * ux + label_spread * nx + offset[0],
            1.40 * uy + label_spread * ny + offset[1],
        )
        ax.text(*position, force["label"], fontsize=15, ha="center", va="center",
                color="#111111", zorder=5, clip_on=False)
    if not forces:
        ax.text(0, -0.55, "No external forces\nin this model",
                fontsize=11, ha="center", va="top", color="#333333")
    ax.text(0.5, -0.03, "Isolated object", transform=ax.transAxes,
            fontsize=10, ha="center", color="#444444")


def draw_axes(ax, axes):
    ax.set_aspect("equal")
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.axis("off")
    ax.set_title("Coordinates", fontsize=10, pad=10, color="#444444")
    x_angle = axes.get("x_angle_deg", 0)
    y_angle = axes.get("y_angle_deg", x_angle + 90)
    for angle, label in (
        (x_angle, axes.get("x_label", "$+x$")),
        (y_angle, axes.get("y_label", "$+y$")),
    ):
        ux, uy = unit(angle)
        arrow(ax, (0, 0), (0.63 * ux, 0.63 * uy), force=False)
        ax.text(0.86 * ux, 0.86 * uy, label, fontsize=12,
                ha="center", va="center", color="#444444", clip_on=False)


def alt_text(config):
    parts = []
    if config.get("title"):
        parts.append(config["title"] + ".")
    for obj in config["objects"]:
        parts.append(f"Free-body diagram for {obj['object_label']}.")
        if not obj["forces"]:
            parts.append("No external forces are included in this model.")
        for force in obj["forces"]:
            description = force.get("description", plain_label(force["label"]))
            angle = force["angle_deg"] % 360
            parts.append(
                f"{description}; arrow at {angle:g} degrees counterclockwise from page-right."
            )
        if "axes" in obj:
            axes = obj["axes"]
            x_angle = axes.get("x_angle_deg", 0) % 360
            y_angle = axes.get("y_angle_deg", x_angle + 90) % 360
            parts.append(
                f"Separate coordinate guides: {plain_label(axes.get('x_label', '+x'))} "
                f"at {x_angle:g} degrees and {plain_label(axes.get('y_label', '+y'))} "
                f"at {y_angle:g} degrees counterclockwise from page-right."
            )
    parts.append("Force arrows are schematic; their lengths do not encode magnitudes.")
    return " ".join(parts)


def render(config, output, dpi=180):
    validate_config(config)
    output = Path(output)
    if output.suffix.lower() not in {".png", ".svg", ".pdf"}:
        raise ValueError("The output extension must be .png, .svg, or .pdf.")
    if isinstance(dpi, bool) or not isinstance(dpi, int) or dpi <= 0:
        raise ValueError("dpi must be a positive integer.")
    objects = config["objects"]
    columns = min(2, len(objects))
    rows = math.ceil(len(objects) / columns)
    fig = plt.figure(figsize=(6.1 * columns, 4.9 * rows), facecolor="white")
    grid = fig.add_gridspec(rows, columns, wspace=0.25, hspace=0.35)
    for index, obj in enumerate(objects):
        row, col = divmod(index, columns)
        if "axes" in obj:
            panel = grid[row, col].subgridspec(1, 2, width_ratios=[4, 1], wspace=0.24)
            body_ax = fig.add_subplot(panel[0, 0])
            draw_axes(fig.add_subplot(panel[0, 1]), obj["axes"])
        else:
            body_ax = fig.add_subplot(grid[row, col])
        draw_forces(body_ax, obj)
    if config.get("title"):
        fig.suptitle(config["title"], fontsize=17, fontweight="bold", y=0.97)
    fig.text(0.5, 0.025, "Force arrows are schematic; lengths do not encode magnitudes.",
             fontsize=10, ha="center", color="#444444")
    fig.subplots_adjust(left=0.055, right=0.965, top=0.85 if config.get("title") else 0.90,
                        bottom=0.12)
    output.parent.mkdir(parents=True, exist_ok=True)
    try:
        fig.savefig(output, dpi=dpi, bbox_inches="tight", facecolor="white")
    finally:
        plt.close(fig)
    alt_path = output.with_suffix(".alt.txt")
    alt_path.write_text(alt_text(config) + "\n", encoding="utf-8")
    return output, alt_path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="JSON force configuration")
    parser.add_argument("--output", required=True, type=Path, help="PNG, SVG, or PDF output")
    parser.add_argument("--dpi", type=int, default=180)
    args = parser.parse_args()
    try:
        with args.input.open(encoding="utf-8") as stream:
            config = json.load(stream)
        output, alt_path = render(config, args.output, args.dpi)
    except (OSError, ValueError, TypeError) as exc:
        parser.error(str(exc))
    print(f"Diagram: {output.resolve()}")
    print(f"Alt text: {alt_path.resolve()}")


if __name__ == "__main__":
    main()
