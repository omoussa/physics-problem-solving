# Acceptance problems: solve-2d-kinematics

These are review prompts with numerical or behavioral oracles, not records of post-install model execution. For full solutions verify symbolic algebra before substitution, units throughout, reasonable precision, explicit coordinates and unit vectors, and final dimensional/physical checks.


## 2D: horizontal launch
Prompt: A ball is launched horizontally at 12.0 m/s from a ledge 20.0 m above level ground. Neglect air resistance and use g = 9.80 m/s². Find the time to impact, horizontal range, and velocity just before impact.
Expected skill: solve-2d-kinematics. With +x along launch and +y upward, t = 2.02 s, range = 24.2 m, v = (12.0 i-hat - 19.8 j-hat) m/s. Speed 23.2 m/s; direction 58.8° below horizontal.
Review: eight steps, vector table with magnitude/direction/x/y components, common elapsed time, nonzero horizontal velocity at impact; no equal-height range formula.

## 2D: nonzero acceleration in both axes
Prompt: A particle has initial velocity (3.00 i-hat + 4.00 j-hat) m/s and constant acceleration (2.00 i-hat - 1.00 j-hat) m/s². Find its displacement and velocity after 2.00 s.
Expected skill: solve-2d-kinematics. Displacement (10.0 i-hat + 6.00 j-hat) m; velocity (7.00 i-hat + 2.00 j-hat) m/s.
Review: do not assume gravity or zero horizontal acceleration; define supplied axes and preserve vector notation.

