---
name: solve-2d-kinematics
description: Provide full worked solutions to constant-acceleration motion in a plane in the professor's preferred eight-step format. Use a vector table with magnitude, direction, x and y components, explicit motion intervals, unit vectors, symbolic algebra, and substitution with units. Use for complete solutions to 2D kinematics, projectile motion, and planar motion with constant acceleration in both axes, including individual constant-acceleration intervals. Do not trigger for hints-only tutoring, problem generation, variable-acceleration motion, or ordinary 1D problems better handled by solve-1d-kinematics.
---

# Solve 2D Kinematics

Provide a complete college-level worked solution. Follow the eight numbered steps below in order. Keep explanations concise but make signs, interval boundaries, equation selection, and algebra explicit. Do not replace the solution with hints or add a rubric, diagram, or problem bank unless requested.

## Check applicability

- Verify that motion lies in a plane and the acceleration VECTOR is constant during the interval, including zero acceleration as a limiting case. Constant acceleration magnitude alone is insufficient if its direction changes. The path may curve; do not describe general 2D motion as motion along a straight line. Do not infer constant acceleration from endpoint velocities alone.
- For multiple objects or segments, label them and apply the method separately to each applicable interval. Connect boundary positions, velocities, and times only when physically justified. Do not carry constant acceleration across a change in acceleration.
- If the supplied problem is outside scope, explain why this method does not apply. If essential data are missing or inconsistent, identify that limitation rather than inventing data or forcing a numerical answer. Provide a symbolic result when possible.
- Use the problem's constants and assumptions. For Earth free fall when gravity is unspecified, state the default assumption of negligible air resistance and g = 9.80 m/s^2 near Earth's surface. Do not use this value for another celestial body.

## Required solution sequence

### 1. Identify the physics

State that motion occurs in a plane with a constant acceleration vector during the interval under study, so the vector kinematic equations apply and can be resolved along two fixed perpendicular axes. Tie the statement to the actual problem.

### 2. State the given information and requested quantity

Briefly summarize what is given and what must be found. Explicitly identify a requested magnitude: speed is the magnitude of instantaneous velocity; acceleration magnitude is the magnitude of the acceleration vector; displacement magnitude is the magnitude of the displacement vector. Distinguish distance traveled along the path, displacement magnitude, and horizontal range. They are generally different in 2D motion.

### 3. Identify the segment of motion

Name the initial and final physical events, not merely "initial" and "final." Define t_i, t_f, and Delta t = t_f - t_i as needed. Use event labels consistently. Do not confuse a clock reading with elapsed time or assume the object begins at rest at the beginning of an arbitrarily selected interval.

### 4. Establish coordinates and vector notation

State the fixed perpendicular x- and y-axes and their positive directions; define the position origin when needed. Preserve supplied coordinates. Ordinarily choose +x right/east and +y upward/north, with unit vectors \(\hat{\imath}\) and \(\hat{\jmath}\). State which physical directions apply. Identify a chosen origin and time zero as choices rather than givens.

Write every vector in component form:
\[
\Delta\vec r=\Delta x\hat{\imath}+\Delta y\hat{\jmath},\quad
\vec v_i=v_{ix}\hat{\imath}+v_{iy}\hat{\jmath},\quad
\vec v_f=v_{fx}\hat{\imath}+v_{fy}\hat{\jmath},\quad
\vec a=a_x\hat{\imath}+a_y\hat{\jmath}.
\]

Use signed scalar components in component equations. Do not give time, components, or magnitudes vector arrows. Define the direction convention: by default measure angles counterclockwise from +x, normalized to [0,360) degrees. Preserve given bearings or reference axes and explicitly convert before resolving components.

For any nonzero vector \(\vec A=A_x\hat{\imath}+A_y\hat{\jmath}\), use
\[
|\vec A|=\sqrt{A_x^2+A_y^2},\quad
\theta_A=\operatorname{atan2}(A_y,A_x),\quad
A_x=|\vec A|\cos\theta_A,\quad A_y=|\vec A|\sin\theta_A.
\]
Use the defined angle reference for the sine/cosine relations; convert atan2 output to degrees and the stated range. Never use an uncorrected arctangent ratio that loses the quadrant. Mark the direction of a zero vector as undefined; axis-aligned nonzero vectors have well-defined directions.

### 5. Make the kinematic-variable table

Create four vector rows in this order: displacement, initial instantaneous velocity, final instantaneous velocity, and acceleration. Use exactly these columns:

| Kinematic variable | Vector representation | Magnitude | Direction | x-component | y-component | Status/explanation |
| --- | --- | --- | --- | --- | --- | --- |
| Displacement | \(\Delta\vec r=\Delta x\hat{\imath}+\Delta y\hat{\jmath}\) | known value or ? | known value or ? | known value or ? | known value or ? | classify each known/unknown as needed |
| Initial instantaneous velocity | \(\vec v_i=v_{ix}\hat{\imath}+v_{iy}\hat{\jmath}\) | value or ? | value or ? | value or ? | value or ? | status and explanation |
| Final instantaneous velocity | \(\vec v_f=v_{fx}\hat{\imath}+v_{fy}\hat{\jmath}\) | value or ? | value or ? | value or ? | value or ? | status and explanation |
| Acceleration | \(\vec a=a_x\hat{\imath}+a_y\hat{\jmath}\) | value or ? | value or ? | value or ? | value or ? | status and explanation |

Substitute known components into the vector-representation cells and retain symbols for unknown components. Include units with all numerical quantities and an explicit reference for each direction. In a zero-vector row, use magnitude 0, components 0, and direction "undefined (zero vector)."

Immediately below the vector table, include the fifth kinematic variable in a small scalar table: **Kinematic variable | Symbol | Value | Status/explanation**, with one row for **Time interval | Delta t | value with units or ? | status**. State that this is the SAME elapsed time in both component equations; do not assign a magnitude, direction, or x/y components to time.

Classify information as explicitly given, implicitly given, calculated from givens, target unknown, or other unknown. Label assumptions and coordinate choices separately. Explain implicit values: horizontal launch means v_iy = 0, not v_ix = 0; a projectile's apex means v_y = 0, not generally zero velocity; no horizontal force in ideal projectile motion means a_x = 0. "Starts from rest" or "comes to rest" means BOTH velocity components vanish. Zero velocity does not imply zero acceleration.

If the known magnitude or direction is insufficient to determine components, retain the known information and mark unresolved cells with ?. Partial vector information is allowed. Do not fill the initial table retroactively with answers. Do not solve unneeded target quantities just to fill cells; direct decomposition or recombination of given vector data may be shown and labeled calculated from givens.

### 6. Select the equation

Identify the needed equation based on the table and briefly explain which knowns it connects to the target and which unnecessary unknown it avoids. Resolve equations into x and y components and explain how the common elapsed time connects them. For ideal projectile motion with +y upward, use a_x = 0 and a_y = -g; allow both components to be nonzero for general planar motion. Use multiple equations only when needed. Prefer the direct constant-acceleration method over unrelated force, energy, or calculus approaches.

### 7. Rearrange symbolically

Start with a common form of the selected equation. Show the vector form where available, then the relevant x- and y-component equations with the same axis convention and the same Delta t. Isolate the requested variable algebraically before inserting numerical values. Do not divide by a vector. Use component squares or dot products, never ambiguous vector squares.

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
v_{fx}^{2}=v_{ix}^{2}+2a_x\Delta x,\qquad
v_{fy}^{2}=v_{iy}^{2}+2a_y\Delta y.
\]
If a vector-based common form is useful, use
\[
\vec v_f\cdot\vec v_f=\vec v_i\cdot\vec v_i+2\vec a\cdot\Delta\vec r.
\]

Do not replace the dot product by |a||Delta r| unless the vectors are parallel and point the same way. The time-independent scalar relation alone does not determine the final velocity direction. Avoid memorized range/time formulas unless their assumptions (such as equal launch and landing height) are established; derive from component equations instead.

For square roots or quadratics, retain candidate roots until the event and direction conditions select them. Positive elapsed time is necessary but may not uniquely identify an event. A negative clock time is not automatically invalid. Check degeneracies before dividing by a quantity that may vanish.

### 8. Substitute, solve, and verify

Substitute numerical values together with units, including signed components. Show enough arithmetic and unit simplification to follow the calculation. Keep unrounded intermediate values; round the final answer using the precision of measured givens and appropriate significant-figure or decimal-place rules. Do not let exact definitions or exact zeros limit precision. If precision is unclear, state a reasonable rounding choice.

Reconstruct vector answers as A_x i-hat + A_y j-hat. For a requested magnitude, explicitly use sqrt(A_x^2 + A_y^2) and report a nonnegative scalar with units. For direction, use atan2 and verify the quadrant. Report magnitude and direction when needed to fully describe a requested vector; do not confuse the direction of displacement with the direction of instantaneous velocity. Box or otherwise clearly identify the requested final answer and explain its physical meaning or direction where applicable.

Finish with a short check of dimensions, signs, event conditions, and physical plausibility, within this step. Verify both coordinates correspond to the same elapsed time and that an impact or crossing root satisfies the stated direction of travel. A projectile can have nonzero horizontal velocity at its apex. Do not assume a parabola when the initial velocity is parallel to acceleration or acceleration is zero.

Use the sign of \(\vec v\cdot\vec a\) to distinguish increasing from decreasing speed at nonzero velocity; the sign of one acceleration component alone is insufficient. Do not assign a direction to a zero vector.

If total distance along a curved path is explicitly requested, do not equate it to displacement magnitude or sum the magnitudes of a few finite displacements. Explain that arc length requires
\[
s=\int_{t_i}^{t_f}\sqrt{[v_{ix}+a_x(t-t_i)]^2+[v_{iy}+a_y(t-t_i)]^2}\,dt.
\]
Evaluate analytically or numerically as appropriate, keeping the eight-step setup. This is an extension for a requested distance in constant-acceleration motion, not permission to apply constant-acceleration equations to variable acceleration. For a genuinely straight path with reversal, split at the turning event and sum displacement magnitudes.

## Output conventions

- Default to a readable solution in chat with numbered steps, a Markdown table, and rendered LaTeX. Follow an explicitly requested output format instead.
- For Canvas HTML, use semantic headings, a table caption, scoped column and row headers, accessible contrast, and LaTeX within \( ... \) and \[ ... \] delimiters. Do not assume pasted delimiters automatically enable MathJax in Canvas or inject an external script into a Canvas fragment. Explain rendering requirements if relevant to the request.
- For multiple parts using the same interval, share steps 1–5 when clear and label steps 6–8 for each part. For a changed interval, explicitly identify the new events and supply its table.
- Read [references/worked-example.md](references/worked-example.md) when calibrating the level of detail or checking how vector notation carries through component algebra. Treat the example as an illustration, not a substitute for the current problem's data.
