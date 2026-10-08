# Physics Problem Solving

College-level, student-facing physics solution skills by O. Moussa. Install a single skill or use the complete plugin when its installation has been verified.

**Status:** Current release ([v1.0.0](https://github.com/omoussa/physics-problem-solving/releases)) includes the individual skills listed below only. Plugin registration and post-installation behavior are pending verification.

## Included skills

| Skill | Scope | Required solution structure |
| --- | --- | --- |
| [solve-1d-kinematics](skills/solve-1d-kinematics/SKILL.md) | Constant-acceleration motion along one fixed axis, including vertical free fall and individual motion segments | Eight steps with a five-variable table |
| [solve-2d-kinematics](skills/solve-2d-kinematics/SKILL.md) | Constant-acceleration motion in a plane, including projectiles and intervals with acceleration along both axes | Eight steps with magnitude, direction, and component columns |
| [solve-newton-laws](skills/solve-newton-laws/SKILL.md) | Translational equilibrium and dynamics, friction, ideal connected objects, and circular motion | Four steps with labeled free-body diagrams |

Each skill retains its existing scope, instructions, supporting references, and interface metadata. The Newton's laws skill includes its Python force-diagram renderer.

## Solution conventions

Solutions default to rendered equations in chat, explicit coordinates and unit vectors, signed components, symbolic algebra before numerical substitution, units, appropriate precision, and physical checks. Essential missing information is clarified rather than invented. Accessible Canvas HTML with MathJax delimiters is available on request.

The full-solution skills exclude hints-only tutoring and problem generation. Constant-acceleration kinematics requires a constant acceleration vector throughout the chosen interval. The Newton's laws skill retains its separate force-analysis scope and does not assume constant acceleration automatically.

## Installation and use

See [installation instructions](docs/installation.md) for individual skills and the plugin's current status. Keep a skill's whole directory together when copying or installing it.

Example request: "Solve this problem step by step using solve-2d-kinematics."

Example format request: "Use solve-newton-laws and provide an accessible Canvas HTML snippet with MathJax delimiters."

## Verification and contributions

The [test index](tests/README.md) links to representative prompts, expected results, and review criteria. These are acceptance materials, not claims that post-install model evaluation has passed. The original skills were preserved byte-for-byte and the Newton's laws renderer passed a smoke test during package preparation.

See [contributing](docs/contributing.md) and [changelog](CHANGELOG.md). The repository uses the [MIT license](LICENSE).
