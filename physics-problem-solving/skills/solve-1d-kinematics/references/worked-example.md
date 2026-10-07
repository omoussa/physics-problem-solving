# Worked example: stopping vehicle

Use this example to calibrate structure and explanatory detail. Adapt the language to the actual problem.

Problem: A vehicle traveling east at 18.0 m/s brakes with constant acceleration and stops in 6.00 s. Find the magnitude of its acceleration.

## 1. Identify the physics

The vehicle moves along a straight line with constant acceleration during braking, so the constant-acceleration kinematic equations apply.

## 2. State the given information and requested quantity

The initial velocity is 18.0 m/s east, the final velocity is zero, and the braking interval is 6.00 s. We seek \(|\vec a|\), the magnitude of the acceleration vector.

## 3. Identify the segment of motion

Study the interval from the instant braking begins to the instant the vehicle first comes to rest. Set \(t_i=0\) at the start of braking, so \(\Delta t=t_f-t_i=6.00\ \mathrm{s}\).

## 4. Establish coordinates and vector notation

Choose the x-axis along the road with east positive and \(\hat{\imath}\) pointing east. Set the origin at the braking position. Thus \(\vec v_i=(+18.0\ \mathrm{m/s})\hat{\imath}\), \(\vec v_f=(0\ \mathrm{m/s})\hat{\imath}\), and \(\vec a=a_x\hat{\imath}\).

## 5. Make the kinematic-variable table

| Kinematic variable | Symbol | Value | Status/explanation |
| --- | --- | --- | --- |
| Displacement | \(\Delta\vec r\) | ? | Other unknown; not needed |
| Initial instantaneous velocity | \(\vec v_i\) | \((+18.0\ \mathrm{m/s})\hat{\imath}\) | Explicitly given; east is positive |
| Final instantaneous velocity | \(\vec v_f\) | \((0\ \mathrm{m/s})\hat{\imath}\) | Implicitly given by "stops" |
| Acceleration | \(\vec a\) | ? | Target unknown; requested answer is its magnitude |
| Time interval | \(\Delta t\) | \(6.00\ \mathrm{s}\) | Explicitly given |

## 6. Select the equation

Use \(\vec v_f=\vec v_i+\vec a\Delta t\), which relates acceleration to the known velocities and elapsed time without requiring displacement.

## 7. Rearrange symbolically

\[
\vec v_f=\vec v_i+\vec a\Delta t
\quad\Longrightarrow\quad
\vec a=\frac{\vec v_f-\vec v_i}{\Delta t}.
\]
For the x-component,
\[
v_{fx}=v_{ix}+a_x\Delta t
\quad\Longrightarrow\quad
a_x=\frac{v_{fx}-v_{ix}}{\Delta t}.
\]

## 8. Substitute, solve, and verify

\[
a_x=\frac{0\ \mathrm{m/s}-(+18.0\ \mathrm{m/s})}{6.00\ \mathrm{s}}
=-3.00\ \mathrm{m/s^2}.
\]
Therefore,
\[
\vec a=(-3.00\ \mathrm{m/s^2})\hat{\imath},\qquad
\boxed{|\vec a|=|a_x|=3.00\ \mathrm{m/s^2}}.
\]
The acceleration points west, opposite the eastward velocity while the vehicle is braking. Its magnitude is positive. The units are \((\mathrm{m/s})/\mathrm{s}=\mathrm{m/s^2}\), and \(18.0+(-3.00)(6.00)=0\) confirms the stated final velocity.
