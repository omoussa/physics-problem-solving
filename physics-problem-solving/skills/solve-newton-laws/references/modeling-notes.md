# Modeling notes for Newton's laws

Read the relevant section when the problem involves friction, changing contact, linked objects, circular motion, or an ambiguity about equilibrium. Use the worked example to calibrate the four-step solution, not to substitute its data for the current problem.

## Contents

- Equilibrium and coordinate choices
- Friction and contact
- Connected objects and ideal pulleys
- Circular motion
- Worked example: pulling a crate at an angle

## Equilibrium and coordinate choices

Treat all equilibrium statements here as translational. A body remains at rest or moves with a constant velocity vector only when its acceleration is zero. A turning point gives zero instantaneous velocity, not generally zero acceleration. At the top of a projectile trajectory, the vertical velocity is zero while gravitational acceleration persists. Motion at constant speed around a curve also has acceleration.

Choose ground/laboratory axes when that frame is appropriately inertial. Do not apply the simple equation sum F = ma in an accelerating elevator's frame without accounting for the frame acceleration; use an approximately inertial ground frame and the elevator/object acceleration instead. A coordinate origin need not be specified when only force vectors and acceleration are involved.

For a straight incline at angle alpha above horizontal, with +x up the incline and +y perpendicular outward, weight is
\[
\vec W=-mg\sin\alpha\,\hat{\imath}
-mg\cos\alpha\,\hat{\jmath}.
\]
The normal force is \(N\hat{\jmath}\). Establish any friction or applied-force signs from the scenario. Do not assume every object's axes must have the same physical orientation; define each basis and link signed components carefully.

## Friction and contact

Use \(f_s\) and \(f_k\) as NONNEGATIVE force magnitudes; apply direction through their signed components. A negative solved signed static-friction component means the required direction is opposite the provisional positive direction, not that the magnitude is negative.

For a proposed no-slip state:

- Determine the normal force from the force balance or normal acceleration.
- Solve for the friction required to keep the contacting surfaces from slipping.
- Verify \(N\ge0\) and \(|F_{s,\mathrm{tangent}}|\le\mu_sN\).
- Use equality only for the limiting static condition explicitly sought or physically established.

If the required friction exceeds the bound, the no-slip assumption fails. To calculate sliding acceleration, use the specified kinetic coefficient and the direction of relative sliding. Do not replace an unspecified kinetic coefficient with the static coefficient.

Static friction can act in the direction of an object's acceleration, such as a package accelerating without slipping on a conveyor belt. It opposes the slipping tendency relative to the belt, not necessarily the package's velocity relative to the ground. If several simultaneous frictional contacts leave forces underdetermined, identify that fact instead of imposing equality at every contact.

A normal force is a contact interaction and cannot pull the object into the surface. \(N<0\) invalidates a maintained-contact model. \(N=0\) can mark the boundary of losing contact; examine geometry and the subsequent motion. If contact is lost, remove the normal and contact-friction forces and rebuild the equations.

For a crate pulled on a horizontal floor by a force P at angle beta above horizontal, maintained contact with \(a_y=0\) gives
\[
N+P\sin\beta-mg=0,\qquad N=mg-P\sin\beta.
\]
Pushing at an angle below horizontal instead increases the normal force. An incline alone with no other perpendicular forces and \(a_y=0\) yields \(N=mg\cos\alpha\); this is a derived result, not a universal rule.

## Connected objects and ideal pulleys

Name the objects and provide separate diagrams. A force exerted by B on A and its reaction exerted by A on B obey
\[
\vec F_{B\to A}=-\vec F_{A\to B}.
\]
They act on different bodies. Their global vectors are opposite; if separate local axes point in different directions, scalar component signs need not look opposite.

For a single massless inextensible taut rope over a fixed massless frictionless pulley, the tension magnitude is common and the linked acceleration magnitudes are equal. Choose local positive directions consistent with one proposed motion and explicitly derive the signed relation from fixed rope length. Do not assume that two different ropes have the same tension.

For a standard fixed-pulley Atwood machine with the right mass provisionally moving down, choosing +down for the right mass and +up for the left mass gives
\[
m_Rg-T=m_Ra,\qquad T-m_Lg=m_La.
\]
These are two local bases linked by the rope. A negative solved a reverses the proposed motion/acceleration directions.

For a movable pulley, start from the total rope-length relation. If two rope segments support the moving pulley, the load displacement can change two segment lengths; derive the appropriate displacement, velocity, and acceleration factors instead of asserting equal magnitudes.

When using a combined-system equation, include the correct total mass and the acceleration relation of its members. Do not write a single total-mass times acceleration expression for arbitrary members with different accelerations. A massive pulley can create unequal rope tensions and generally needs a torque equation; identify that extension as outside this translational skill.

## Circular motion

Use the diagram at a clearly named position and instant. Define inward radial \(\hat r\) and tangential \(\hat t\), with the tangential direction tied to the chosen direction of travel. For nonzero speed and +r inward:
\[
\vec a=\frac{v^2}{r}\hat r+\frac{dv}{dt}\hat t,\qquad
\sum F_r=m\frac{v^2}{r},\qquad
\sum F_t=m\frac{dv}{dt}.
\]
With +r outward, the radial component is \(-v^2/r\). State the convention. These are local components of the acceleration in an inertial frame, not a claim that the local basis is fixed throughout the orbit.

At constant speed the tangential acceleration is zero; radial acceleration remains. "Centripetal force" names the NET inward component of the real forces, not an additional force to draw. Do not add a centrifugal force in an inertial-frame free-body diagram.

At the top of an ideal vertical loop, inward is downward. If both weight and track normal force point inward, then
\[
mg+N=m\frac{v^2}{r}.
\]
Check \(N\ge0\). For a string the analogous check is \(T\ge0\). Do not assume the same force directions at the bottom, side, or a different contact geometry. Obtain a changing speed from supplied information or explicitly needed supplementary physics, rather than assuming uniform circular motion.

## Worked example: pulling a crate at an angle

Prompt: A 10.0 kg crate slides to the right on a horizontal floor. A 40.0 N pull acts 30.0 degrees above horizontal, and the kinetic friction coefficient is 0.200. Find the crate's acceleration. Ignore air resistance.

### 1. Identify the object and draw its free-body diagram

Object: the crate. Target: its acceleration vector. The floor is stationary, so the crate slides right relative to it. Use near-Earth \(g=9.80\,\mathrm{m/s^2}\) and check maintained contact.

Draw four actual force arrows: Earth's weight downward, floor normal upward, applied pull up/right at 30.0 degrees, and floor kinetic friction left. Do not add acceleration to this diagram.

### 2. Choose coordinates, express the force vectors, and sum them

Choose +x right and +y upward in the ground frame:
\[
\vec W=-mg\hat{\jmath},\quad
\vec N=N\hat{\jmath},\quad
\vec P=P\cos\beta\,\hat{\imath}+P\sin\beta\,\hat{\jmath},\quad
\vec f_k=-\mu_kN\hat{\imath}.
\]
\[
\vec F_{\mathrm{net}}
=(P\cos\beta-\mu_kN)\hat{\imath}
+(N+P\sin\beta-mg)\hat{\jmath}.
\]
A force table is useful here but need not duplicate every explanatory sentence.

### 3. Justify the acceleration and apply Newton's laws in components

For maintained contact on the horizontal floor, \(a_y=0\). The horizontal acceleration is unknown; do not call the crate fully in equilibrium:
\[
\vec a=a_x\hat{\imath}+0\hat{\jmath},\qquad
\sum\vec F=m\vec a,
\]
\[
P\cos\beta-\mu_kN=ma_x,\qquad
N+P\sin\beta-mg=0.
\]

### 4. Solve the component equations and verify the result

First isolate the unknowns symbolically:
\[
N=mg-P\sin\beta,\qquad
a_x=\frac{P\cos\beta-\mu_k(mg-P\sin\beta)}{m}.
\]
Then substitute with units:
\[
N=(10.0\,\mathrm{kg})(9.80\,\mathrm{m/s^2})
-(40.0\,\mathrm N)\sin30.0^\circ=78.0\,\mathrm N,
\]
\[
a_x=
\frac{(40.0\,\mathrm N)\cos30.0^\circ
-(0.200)(78.0\,\mathrm N)}
{10.0\,\mathrm{kg}}
=1.9041\ldots\,\mathrm{m/s^2}.
\]
Report
\[
\boxed{\vec a=(1.90\,\mathrm{m/s^2})\hat{\imath}}.
\]
The acceleration is to the right. Contact is feasible because \(N>0\); the floor friction is \(15.6\,\mathrm N\), less than the \(34.6\,\mathrm N\) horizontal pull. The horizontal net force is positive, and force divided by mass has acceleration units.
