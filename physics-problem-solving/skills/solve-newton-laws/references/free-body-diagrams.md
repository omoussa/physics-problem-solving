# Typeset free-body diagrams

Use the bundled script to draw exact, labeled force arrows. It uses Python 3 and Matplotlib; it does not solve the physics. Determine the object, all external forces, their directions, and chosen axes before preparing the input.

## Run the renderer

~~~bash
python3 /absolute/path/to/solve-newton-laws/scripts/draw_free_body_diagram.py \
  --input /absolute/path/to/forces.json \
  --output /absolute/path/to/free_body_diagram.png
~~~

Resolve the script path relative to the installed skill's actual directory; its folder may have changed after installation. PNG is suitable for rendered chat and HTML. SVG and PDF output are also supported. The script also writes a same-basename .alt.txt file.

Write temporary input and preview images to scratch. Treat those as intermediates when they support a chat solution. If the user requests a downloadable artifact, use the applicable Library workflow to save that deliverable. Embed the PNG in chat using Markdown image syntax with an absolute sandbox target. For Canvas HTML, use a supplied LMS-hosted image URL or a clearly identified placeholder and the descriptive alt text. Do not use a local filesystem URL as if it were a Canvas image URL.

## Input schema

~~~json
{
  "title": "Free-body diagram",
  "objects": [
    {
      "object_label": "Crate",
      "axes": {
        "x_angle_deg": 0,
        "y_angle_deg": 90,
        "x_label": "$+x$",
        "y_label": "$+y$"
      },
      "forces": [
        {
          "label": "$\\vec W$",
          "description": "Weight exerted by Earth, vertically downward",
          "angle_deg": 270
        },
        {
          "label": "$\\vec N$",
          "description": "Normal force exerted by the floor, vertically upward",
          "angle_deg": 90
        },
        {
          "label": "$\\vec P$",
          "description": "Applied pull, 30 degrees above page-right",
          "angle_deg": 30
        },
        {
          "label": "$\\vec f_k$",
          "description": "Kinetic friction exerted by the floor, leftward",
          "angle_deg": 180,
          "label_offset": [0, -0.08]
        }
      ]
    }
  ]
}
~~~

- Supply one object entry for each required diagram. The renderer arranges multiple objects in separate labeled panels.
- Define all angles in degrees counterclockwise from page-right in the drawing, independently of the analysis axes. Thus page-up is 90 degrees, page-left is 180 degrees, and page-down is 270 degrees.
- For an incline rising to the right at alpha degrees, weight remains page-down (270 degrees), normal points at alpha + 90 degrees, and up-slope tension points at alpha degrees. Set the coordinate x-angle to alpha. Do not mistakenly use analysis-frame force angles as page angles.
- Axes are optional. When supplied, y defaults to x + 90 degrees; an explicitly supplied y-angle must be perpendicular to x. Either handedness is allowed so an inward radial basis can be paired with a chosen tangential direction. Set radial/tangential labels when relevant.
- Labels support Matplotlib mathtext inside dollar signs. Use concise vector labels; identify the force-producing agents in the prose, table, and descriptions.
- Supply a meaningful description for each force to improve image alt text.
- Optional label_offset is [horizontal, vertical] in schematic plot units, added to the automatic label position. Use it to correct crowding after visual inspection.
- Force arrows have equal schematic lengths, which do not encode magnitudes. Parallel arrows may have slightly displaced tails to remain visible; they still attach to the isolated object.
- Do not put acceleration, velocity, a net-force arrow, or a fictitious additional centripetal force in the forces list. This renderer produces a free-body diagram, not a kinematics sketch.
- Do not use the script to assert an unknown direction as given. Label a provisional direction in the surrounding explanation, and revise the diagram if the solved direction is opposite.

## Verify the image

Render and inspect the resulting image at readable size. Check every force against the modeled external interactions, every arrow angle against the physical geometry, the coordinate directions, label collisions or clipping, and clear separation of coordinate guides from forces.

Correct the input or label offsets and rerender when needed. The automatically generated alt text describes the page angles but does not establish the physical correctness of the model.
