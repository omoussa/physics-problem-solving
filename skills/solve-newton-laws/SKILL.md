---
name: solve-newton-laws
description: Provide complete college-level solutions to Newton's laws problems in the professor's four-step format, with explicit object identification, typeset free-body diagrams, force vectors and components, justified equilibrium or acceleration, symbolic algebra, substitution with units, and verification. Use for translational equilibrium and dynamics in one or two dimensions, inclines, static and kinetic friction, connected objects and ideal pulleys, and circular motion. Default to rendered equations in chat and honor requests for Canvas HTML with MathJax or other formats. Do not trigger for hints-only tutoring, problem generation, pure kinematics, rotational dynamics requiring torque, variable-mass systems, or advanced differential-equation solutions.
---

# Solve Newton's Laws

Provide a complete student-facing solution using exactly the four numbered main steps below, with descriptive substeps as needed. Explain the physical reasoning before the algebra. Keep vector notation, force-producing agents, signs, and assumptions explicit. Do not add a rubric or problem bank unless requested.

## Establish applicability and assumptions

- Use an inertial reference frame and constant object mass for the standard equation of motion. Include one- and two-dimensional translational equilibrium, straight-line acceleration, inclined surfaces, friction, connected objects and pulleys, and circular motion at a specified instant.
- Do not assume constant acceleration merely because Newton's second law applies. For variable forces, solve an instantaneous acceleration or force relation when the information permits; identify any differential-equation work outside this skill's scope. Use the appropriate kinematics skill only when needed and its constant-acceleration assumptions are justified.
- Treat a supplied idealization as given. State necessary additional modeling assumptions explicitly, such as negligible air resistance, a massless inextensible taut rope, or a massless frictionless pulley. Do not silently idealize a problem that specifies otherwise.
- Use supplied constants. For near-Earth gravity when unspecified, state g = 9.80 m/s^2; do not use it for another celestial body. Distinguish mass from weight and givens from assumptions.
- If data or geometry are missing, contradictory, or insufficient, identify what cannot be determined and give a symbolic result when possible. Ask only for information necessary to resolve the problem; never invent a numerical value or force direction.
- Read [references/modeling-notes.md](references/modeling-notes.md) for friction, contact, rope constraints, circular motion, or an example of the expected algebra and units.

## 1. Identify the object and draw its free-body diagram

**Object and target.** Name the specific object on which the desired force acts or whose acceleration is requested. Briefly state the givens and target. Explicitly distinguish a requested vector from its magnitude, a signed component, or a direction. Identify the instant or motion interval relevant to the force model.

**External interactions.** Identify every relevant external force by its agent and recipient: force exerted by agent A on object B. Use labels such as weight, normal force, tension, friction, and applied force only when the corresponding interaction exists. Do not invent a force simply because the object moves.

**Free-body diagram.** Draw the object in isolation as a point or simple body, with labeled arrows for all external forces acting ON it. Use the bundled renderer following [references/free-body-diagrams.md](references/free-body-diagrams.md), or another exact plotting/vector method suited to the requested format. Deliver the diagram in this step; it may include the axes explained in step 2.

- Preserve physical arrow directions independently of later algebraic signs. If a force direction is genuinely unknown, state a provisional direction and interpret the solved sign.
- Do not add velocity, acceleration, a separate net-force arrow, or a separate "centripetal force" to the force diagram. Show kinematic arrows in a separate sketch if useful.
- If a component diagram is useful, distinguish dashed components from the original force and explain that they represent that same force; never count both in the force sum.
- Show coordinate guides separately from force arrows. State when arrow lengths are schematic. Supply a concise description or alt text naming the object, forces, and physical directions.
- Keep action-reaction partners on different objects' diagrams. Write Newton's third law with agent/recipient labels when relevant; those partners do not cancel in a single object's net force.

**Multiple objects.** Draw a separate free-body diagram and write equations for each object needed to determine the target. A combined-system diagram may supplement these when it simplifies the calculation. Internal forces cancel only inside the chosen combined boundary; keep all forces external to that boundary. Label each diagram clearly.

## 2. Choose coordinates, express the force vectors, and sum them

**Coordinates.** State the inertial frame, perpendicular axes, positive physical directions, and unit vectors. Prefer an axis along the expected acceleration or parallel to the surface/direction of actual or impending motion when useful. Do not infer acceleration direction from velocity direction. If acceleration direction is unknown, choose convenient axes and let the component signs establish it.

Use x and y with \(\hat{\imath}\) and \(\hat{\jmath}\) for Cartesian axes. Define any rotated axes clearly; for an incline, x can be along the slope and y perpendicular outward. For circular motion, use radial/tangential axes at the stated instant and define inward/outward explicitly. Do not treat rotating radial/tangential unit vectors as globally fixed.

**Force vectors.** Express each actual force in the SAME chosen coordinate system:
\[
\vec F_k=F_{kx}\hat{\imath}+F_{ky}\hat{\jmath}.
\]
Use signed scalar components; do not put vector arrows on components, magnitudes, mass, or time. Define angle references before applying trigonometry. If \(\theta_k\) is measured counterclockwise from +x,
\[
F_{kx}=|\vec F_k|\cos\theta_k,\qquad
F_{ky}=|\vec F_k|\sin\theta_k.
\]
Retain unknown quantities symbolically. Establish any sign from geometry or a stated provisional direction.

**Optional force table.** Include a table when several forces, rotated axes, or unresolved components make it helpful. Use columns:
Force (agent on object) | Vector representation | Magnitude | Direction/reference | x-component | y-component.
Adapt x/y column names for radial/tangential axes. Include units, identify unknowns and any provisional directions, and distinguish given values from assumptions or calculated decompositions. Do not fill the initial table retroactively with final answers. A zero vector has undefined direction.

**Net force.** Write the vector sum explicitly, grouping all components along each axis:
\[
\vec F_{\mathrm{net}}=\sum_k\vec F_k
=\left(\sum_k F_{kx}\right)\hat{\imath}
+\left(\sum_k F_{ky}\right)\hat{\jmath}.
\]
Show the actual problem's force terms in each grouped sum. Do not replace the force model with an unexplained memorized acceleration formula.

## 3. Justify the acceleration and apply Newton's laws in components

**Equilibrium decision.** Use the scenario to decide which acceleration components vanish and explain why. Translational equilibrium means \(\vec a=\vec 0\), so the velocity vector is constant, including remaining at rest. Being momentarily at rest does not imply equilibrium. Constant speed along a curved path does not imply zero acceleration. Do not claim rotational equilibrium from zero net force alone.

If translational equilibrium is established, write
\[
\sum_k\vec F_k=\vec 0,\qquad
\sum_k F_{kx}=0,\qquad
\sum_k F_{ky}=0.
\]
Explain that a zero vector has zero components.

**Accelerating object.** Write the acceleration vector in the same basis, including unknown components:
\[
\vec a=a_x\hat{\imath}+a_y\hat{\jmath}.
\]
Then apply Newton's second law BEFORE separating components:
\[
\sum_k\vec F_k=m\vec a,
\]
\[
\left(\sum_k F_{kx}\right)\hat{\imath}
+\left(\sum_k F_{ky}\right)\hat{\jmath}
=ma_x\hat{\imath}+ma_y\hat{\jmath},
\]
\[
\sum_k F_{kx}=ma_x,\qquad
\sum_k F_{ky}=ma_y.
\]
An object can accelerate along one axis while the other component is zero. Zero net force along one axis is not full equilibrium.

**Force models and constraints.** Add only the relations justified by this problem.

- Determine normal forces from the perpendicular component equation; do not automatically set N = mg.
- For static friction, use \(0\le f_s\le\mu_sN\); determine the friction required by the no-slip equations and check the bound. Use \(f_s=\mu_sN\) only at the limiting condition of impending slipping.
- For kinetic friction, use \(f_k=\mu_kN\) and oppose sliding relative to the contacting surface. Static friction opposes the relative slipping tendency. Friction need not oppose acceleration or absolute velocity.
- A surface's normal force and a rope's tension cannot be negative in these models. If a solution gives an impossible sign, reconsider contact, slackness, the assumed motion, or data consistency.
- For connected objects, relate signed accelerations using the rope geometry. Equal acceleration magnitudes require the applicable ideal-rope constraint; movable pulleys can introduce factors. Equal tension along a single rope requires the applicable ideal massless rope/pulley assumptions.
- For circular motion with +r inward, use \(\vec a=(v^2/r)\hat r+(dv/dt)\hat t\) and write radial and tangential component equations. At constant speed, only the tangential acceleration vanishes. The inward net force is produced by the real forces already shown.

## 4. Solve the component equations and verify the result

**Symbolic solution.** Identify the unknowns and solve the necessary component equations together with the force laws and constraints. Show the target isolated algebraically before numerical substitution. For connected objects, display the coupled equations and how shared unknowns are eliminated. Do not divide by a vector. Check before dividing by a quantity that could vanish.

**Units and arithmetic.** Substitute numerical values with units and signed components. Show enough arithmetic and unit cancellation to follow the result. Keep unrounded intermediate values and round final results appropriately to the measured givens. Exact definitions, exact zeros, and idealized geometric factors do not limit significant figures. State a reasonable rounding choice if the input precision is ambiguous.

**Report the requested quantity.** Reconstruct a vector answer with the defined unit vectors. For a requested magnitude, explicitly evaluate
\[
|\vec A|=\sqrt{A_x^2+A_y^2}
\]
and report a nonnegative scalar with units. For a direction, use a quadrant-aware angle such as atan2 and state its physical reference; do not assign a direction to a zero vector. Interpret a negative component relative to the chosen positive axis. Clearly identify the final answer and its physical meaning.

**Verify.** Check dimensions, component signs, physical plausibility, and the assumed friction/contact/rope conditions. Check the derived normal force and required static friction before accepting a no-slip solution. If the assumed branch fails and the data permit another branch, solve the physically consistent branch; otherwise explain the limitation. Briefly substitute back into the governing equations when it resolves an important uncertainty.

## Output conventions

- Default to four numbered steps, rendered LaTeX equations in chat, and the labeled free-body diagram. Use the force table only when it improves clarity.
- Honor any explicitly requested format, including Canvas-ready HTML snippets with MathJax delimiters. Keep the same physics, step order, diagrams, and reasoning.
- For HTML snippets, use semantic headings, accessible image alt text, a table caption, scoped row/column headers, sufficient contrast, and math within \( ... \) and \[ ... \]. Do not inject external scripts into Canvas snippets or assume pasted delimiters alone enable rendering. Use supplied LMS image references; identify an image placeholder if no Canvas-hosted image is available.
- For multipart questions sharing one object, coordinates, and force model, share steps 1-3 and label the step-4 calculations by part. For a changed contact state, interval, or object, explicitly revise the relevant diagram and equations.
- Use exact plotting/vector tools for force diagrams rather than generative image tools. If images are technically unavailable, explain the limitation and provide a precise textual diagram description rather than pretending to have drawn one.
