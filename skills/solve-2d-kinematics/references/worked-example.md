# Worked example: projectile at a specified time

Use this example to calibrate the eight-step sequence and vector table. Adapt it to the current problem rather than copying its data.

Problem: A projectile is launched with velocity (12.0 m/s)i-hat + (16.0 m/s)j-hat. With +y upward, negligible air resistance, and g = 9.80 m/s^2, find its displacement, instantaneous velocity, and speed 2.00 s after launch. Assume it remains in flight during this interval.

## 1. Identify the physics

The projectile moves in a plane with constant downward acceleration. The vector kinematic equations apply and may be resolved into horizontal and vertical components.

## 2. State the given information and requested quantities

The initial velocity components and elapsed time are given. Find the displacement vector, final instantaneous velocity vector, and speed, which is the magnitude of that velocity vector.

## 3. Identify the segment of motion

Study the interval from launch (event L) to the instant 2.00 s later (event F). Choose t_L = 0 so Delta t = t_F - t_L = 2.00 s. Both axes describe these same events.

## 4. Establish coordinates and vector notation

Use +x right and +y up; place the origin at launch. Unit vectors i-hat and j-hat point along these positive axes. Measure all directions counterclockwise from +x in [0,360) degrees.

\[
\vec v_i=(12.0\ \mathrm{m/s})\hat{\imath}+(16.0\ \mathrm{m/s})\hat{\jmath},\qquad
\vec a=(0\ \mathrm{m/s^2})\hat{\imath}-(9.80\ \mathrm{m/s^2})\hat{\jmath}.
\]
Directly from the given components,
\[
|\vec v_i|=\sqrt{(12.0)^2+(16.0)^2}\ \mathrm{m/s}=20.0\ \mathrm{m/s},\quad
\theta_i=\operatorname{atan2}(16.0,12.0)=53.1^\circ.
\]

## 5. Make the kinematic-variable table

| Kinematic variable | Vector representation | Magnitude | Direction (CCW from +x) | x-component | y-component | Status/explanation |
| --- | --- | --- | --- | --- | --- | --- |
| Displacement | \(\Delta\vec r=\Delta x\hat{\imath}+\Delta y\hat{\jmath}\) | ? | ? | ? | ? | Target unknown |
| Initial instantaneous velocity | \(\vec v_i=(12.0\hat{\imath}+16.0\hat{\jmath})\ \mathrm{m/s}\) | \(20.0\ \mathrm{m/s}\) | \(53.1^\circ\) | \(12.0\ \mathrm{m/s}\) | \(16.0\ \mathrm{m/s}\) | Components explicit; magnitude/direction calculated from givens |
| Final instantaneous velocity | \(\vec v_f=v_{fx}\hat{\imath}+v_{fy}\hat{\jmath}\) | ? | ? | ? | ? | Target vector and magnitude |
| Acceleration | \(\vec a=(0\hat{\imath}-9.80\hat{\jmath})\ \mathrm{m/s^2}\) | \(9.80\ \mathrm{m/s^2}\) | \(270^\circ\) | \(0\ \mathrm{m/s^2}\) | \(-9.80\ \mathrm{m/s^2}\) | Gravity given; components/direction follow the ideal projectile model and axes |

| Kinematic variable | Symbol | Value | Status/explanation |
| --- | --- | --- | --- |
| Time interval | \(\Delta t\) | \(2.00\ \mathrm{s}\) | Explicitly given; identical for both axes |

## 6. Select the equations

Use the displacement-time equation because initial velocity, acceleration, and elapsed time are known. Use the velocity-time equation for the final velocity. Resolve each into both axes using the same elapsed time.

## 7. Rearrange symbolically

The standard vector equations already isolate the target vectors:
\[
\Delta\vec r=\vec v_i\Delta t+\tfrac12\vec a(\Delta t)^2,\qquad
\vec v_f=\vec v_i+\vec a\Delta t.
\]
Their components are
\[
\Delta x=v_{ix}\Delta t+\tfrac12a_x(\Delta t)^2,\quad
\Delta y=v_{iy}\Delta t+\tfrac12a_y(\Delta t)^2,
\]
\[
v_{fx}=v_{ix}+a_x\Delta t,\quad v_{fy}=v_{iy}+a_y\Delta t.
\]
For either vector use magnitude sqrt(A_x^2 + A_y^2) and direction atan2(A_y,A_x), converting to the defined angular range.

## 8. Substitute, solve, and verify

\[
\Delta x=(12.0\ \mathrm{m/s})(2.00\ \mathrm{s})+\tfrac12(0\ \mathrm{m/s^2})(2.00\ \mathrm{s})^2=24.0\ \mathrm m,
\]
\[
\Delta y=(16.0\ \mathrm{m/s})(2.00\ \mathrm{s})+\tfrac12(-9.80\ \mathrm{m/s^2})(2.00\ \mathrm{s})^2=12.4\ \mathrm m.
\]
Thus
\[
\boxed{\Delta\vec r=(24.0\hat{\imath}+12.4\hat{\jmath})\ \mathrm m},\quad
|\Delta\vec r|=\sqrt{(24.0)^2+(12.4)^2}\ \mathrm m=27.0\ \mathrm m,
\]
with direction atan2(12.4,24.0) = 27.3 degrees counterclockwise from +x.

\[
v_{fx}=12.0\ \mathrm{m/s}+(0\ \mathrm{m/s^2})(2.00\ \mathrm{s})=12.0\ \mathrm{m/s},
\]
\[
v_{fy}=16.0\ \mathrm{m/s}+(-9.80\ \mathrm{m/s^2})(2.00\ \mathrm{s})=-3.60\ \mathrm{m/s}.
\]
Keep internal precision and report
\[
\boxed{\vec v_f=(12.0\hat{\imath}-3.60\hat{\jmath})\ \mathrm{m/s}},\qquad
\boxed{|\vec v_f|=\sqrt{(12.0)^2+(-3.60)^2}\ \mathrm{m/s}=12.5\ \mathrm{m/s}}.
\]
The velocity direction is atan2(-3.60,12.0) = -16.7 degrees, or 343.3 degrees counterclockwise from +x (16.7 degrees below +x).

All displacement terms have units of length and velocity terms have units of speed. The projectile is still above its launch height but is descending; these statements are compatible. Horizontal velocity remains constant because a_x = 0. Displacement and instantaneous velocity point in different directions.
