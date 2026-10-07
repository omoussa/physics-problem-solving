# Acceptance problems: behavior-and-format

These are review prompts with numerical or behavioral oracles, not records of post-install model execution. For full solutions verify symbolic algebra before substitution, units throughout, reasonable precision, explicit coordinates and unit vectors, and final dimensional/physical checks.


## Clarification
Prompt: A block is pulled along a horizontal surface by a 30.0 N force. Find its acceleration.
Expected behavior: Newton laws setup or symbolic relation is useful, but no unique numerical answer is possible. Ask for the mass and friction information/assumption. Do not assume a frictionless surface or invent mass.

## Scope
Prompt: A particle moves in a circle at constant speed. Use the constant-acceleration 2D equations to find its position after one quarter orbit.
Expected behavior: explain that the acceleration vector changes direction, so solve-2d-kinematics does not apply across the orbit. Circular-motion force analysis belongs to solve-newton-laws when relevant; constant speed is not zero acceleration.

## Canvas output
Repeat the horizontal-launch and incline prompts asking for Canvas-ready HTML snippets with MathJax delimiters.
Review: same required physics and step structure, semantic headings, table captions, scoped row/column headers, \( ... \) and \[ ... \] math, diagram alt text and a supplied LMS URL or explicit image placeholder, no injected external scripts.
