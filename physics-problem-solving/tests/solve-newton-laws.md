# Acceptance problems: solve-newton-laws

These are review prompts with numerical or behavioral oracles, not records of post-install model execution. For full solutions verify symbolic algebra before substitution, units throughout, reasonable precision, explicit coordinates and unit vectors, and final dimensional/physical checks.


## Newton laws: kinetic friction and incline
Prompt: A 5.00 kg block slides down a fixed incline at 30.0° above horizontal. The coefficient of kinetic friction is 0.200. Find the block's acceleration. Use g = 9.80 m/s² and neglect air resistance.
Expected skill: solve-newton-laws. With +x down slope and +y perpendicular outward, N = mg cos(theta) = 42.4 N, f_k = 8.49 N, a = g(sin(theta) - mu_k cos(theta)) = +3.20 i-hat m/s².
Review: exactly four main steps; labeled isolated-object diagram with weight downward, normal perpendicular outward, kinetic friction up slope. Do not add a separate net-force or acceleration arrow to that diagram. Show component equations and justify a_y = 0.

## Newton laws: static friction check
Prompt: A 10.0 kg crate rests on a horizontal floor. A horizontal force of 20.0 N pushes it right. The coefficient of static friction is 0.300. Determine whether it can remain at rest and find the static friction. Use g = 9.80 m/s².
Expected skill: solve-newton-laws. N = 98.0 N; maximum available static friction 29.4 N. Rest is possible with f_s = 20.0 N leftward and a = 0.
Review: determine required friction and check its bound; do not automatically use f_s = mu_s N. The diagram has weight, normal, applied force, and static friction on the crate.

