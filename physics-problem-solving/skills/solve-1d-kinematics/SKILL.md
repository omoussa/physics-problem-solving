---
name: solve-1d-kinematics
description: Provide full worked solutions to uniformly accelerated motion along one fixed spatial dimension in the professor's preferred eight-step format, with explicit motion intervals, vector notation and unit vectors, a kinematic-variable table, symbolic algebra, and substitution with units. Use for requests for complete solutions to constant-acceleration 1D problems, including vertical free fall and individual constant-acceleration segments. Do not trigger for hints-only tutoring, problem generation, variable-acceleration calculus, or general two-dimensional projectile motion.
---

# Solve 1D Kinematics

Provide a complete college-level worked solution. Follow the eight numbered steps below in order. Keep explanations concise but make signs, interval boundaries, equation selection, and algebra explicit. Do not replace the solution with hints or add a rubric, diagram, or problem bank unless requested.

## Check applicability

- Verify that the chosen segment follows a fixed straight axis with constant acceleration, including zero acceleration as a limiting case. Do not infer constant acceleration from two endpoint velocities alone.
- For multiple objects or segments, label them and apply the method separately to each applicable interval. Connect boundary positions, velocities, and times only when physically justified. Do not carry constant acceleration across a change in acceleration.
- If the supplied problem is outside scope, explain why this method does not apply. If essential data are missing or inconsistent, identify that limitation rather than inventing data or forcing a numerical answer. Provide a symbolic result when possible.
- Use the problem's constants and assumptions. For Earth free fall when gravity is unspecified, state the default assumption of negligible air resistance and g = 9.80 m/s^2 near Earth's surface. Do not use this value for another celestial body.

## Required solution sequence

### 1. Identify the physics

State that the motion is along a straight line with constant acceleration during the interval under study, so the constant-acceleration kinematic equations apply. Tie the statement to the actual problem.

### 2. State the given information and requested quantity

Briefly summarize what is given and what must be found. Explicitly identify a requested magnitude: speed is the magnitude of instantaneous velocity; acceleration magnitude is the magnitude of the acceleration vector; displacement magnitude is the magnitude of the displacement vector. Do not call distance traveled a displacement magnitude without first checking for reversal.

### 3. Identify the segment of motion

Name the initial and final physical events, not merely "initial" and "final." Define t_i, t_f, and Delta t = t_f - t_i as needed. Use event labels consistently. Do not confuse a clock reading with elapsed time or assume the object begins at rest at the beginning of an arbitrarily selected interval.

### 4. Establish coordinates and vector notation

State the axis and its positive direction; define the position origin when needed. Preserve supplied coordinates. Ordinarily use x and i-hat for horizontal motion, y and j-hat for vertical motion. Choose a convenient origin and time zero only when unspecified, and identify these as choices rather than givens.

Write displacement, initial and final instantaneous velocities, and acceleration as vectors with explicit unit-vector representations. For x motion use:

\[
\Delta\vec r=\Delta x\,\hat{\imath},\qquad
\vec v_i=v_{ix}\hat{\imath},\qquad
\vec v_f=v_{fx}\hat{\imath},\qquad
\vec a=a_x\hat{\imath}.
\]

Use signed scalar components in component equations. Do not give time, components, or magnitudes vector arrows. Retain vector notation in the table, the initial vector equations where available, and vector results; do not let component algebra erase the distinction between a component and its vector.

### 5. Make the kinematic-variable table

Include these five core rows in this order: displacement, initial instantaneous velocity, final instantaneous velocity, acceleration, and time interval. Use columns **Kinematic variable | Symbol | Value | Status/explanation**. Use vector symbols for the first four rows and Delta t for the last. Supply units and unit vectors for known vector values.

Classify information as explicitly given, implicitly given, target unknown, or other unknown, adding a brief explanation. Explain each implicit value: "starts from rest," "stops," or "at a vertical turning point" can imply zero instantaneous velocity at the relevant event. Zero velocity does not imply zero acceleration. Distinguish assumptions, coordinate choices, and values calculated from explicit data from actual implicit givens. If a magnitude is given but direction is unresolved, record the magnitude and the unresolved component sign; do not silently invent direction. Mark unknown values with ?, distinguishing the target (including a target magnitude of that vector) from an unnecessary or intermediate unknown. Do not fill the table retroactively with answers.

### 6. Select the equation

Identify the needed equation based on the table and briefly explain which knowns it connects to the target and which unnecessary unknown it avoids. Use multiple equations only when needed. Prefer the direct constant-acceleration method over unrelated force, energy, or calculus approaches.

### 7. Rearrange symbolically

Start with a common form of the selected equation. Show the vector form where available, then the corresponding component equation with the same axis convention. Isolate the requested variable algebraically before inserting numerical values. Do not divide by a vector. Use component squares or dot products, never ambiguous vector squares.

Use these common forms as appropriate:

\[
\vec v_f=\vec v_i+\vec a\Delta t,\qquad
\Delta\vec r=\vec v_i\Delta t+\tfrac12\vec a(\Delta t)^2,
\]
\[
\Delta\vec r=\tfrac12(\vec v_i+\vec v_f)\Delta t,\qquad
\Delta\vec r=\vec v_f\Delta t-\tfrac12\vec a(\Delta t)^2.
\]

For the time-independent equation, use the unambiguous scalar form
\[
v_{fx}^{2}=v_{ix}^{2}+2a_x\Delta x.
\]
If a vector-based common form is useful, use
\[
\vec v_f\cdot\vec v_f=\vec v_i\cdot\vec v_i+2\vec a\cdot\Delta\vec r.
\]

For square roots or quadratics, retain candidate roots until the event and direction conditions select them. Positive elapsed time is necessary but may not uniquely identify an event. A negative clock time is not automatically invalid. Check degeneracies before dividing by a quantity that may vanish.

### 8. Substitute, solve, and verify

Substitute numerical values together with units, including signed components. Show enough arithmetic and unit simplification to follow the calculation. Keep unrounded intermediate values; round the final answer using the precision of measured givens and appropriate significant-figure or decimal-place rules. Do not let exact definitions or exact zeros limit precision. If precision is unclear, state a reasonable rounding choice.

Reconstruct vector answers using the correct unit vector. For a requested magnitude, explicitly take the magnitude after finding the vector or component, and report a nonnegative scalar with units. Box or otherwise clearly identify the requested final answer and explain its physical meaning or direction where applicable.

Finish with a short check of dimensions, signs, and physical plausibility, within this step. Check a turning time against the interval before equating distance with displacement magnitude. If direction reverses and distance is requested, split at the turning event and sum the magnitudes of the segment displacements. Explain that slowing down depends on velocity and acceleration having opposite signs, not on acceleration being negative alone. Do not assign a direction to a zero vector.

## Output conventions

- Default to a readable solution in chat with numbered steps, a Markdown table, and rendered LaTeX. Follow an explicitly requested output format instead.
- For Canvas HTML, use semantic headings, a table caption, scoped column and row headers, accessible contrast, and LaTeX within \( ... \) and \[ ... \] delimiters. Do not assume pasted delimiters automatically enable MathJax in Canvas or inject an external script into a Canvas fragment. Explain rendering requirements if relevant to the request.
- For multiple parts using the same interval, share steps 1–5 when clear and label steps 6–8 for each part. For a changed interval, explicitly identify the new events and supply its table.
- Read [references/worked-example.md](references/worked-example.md) when calibrating the level of detail or checking how vector notation carries through component algebra. Treat the example as an illustration, not a substitute for the current problem's data.
