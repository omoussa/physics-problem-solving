# Installation

## Available release

[Physics Problem Solving v1.0.0](https://github.com/omoussa/physics-problem-solving/releases/tag/v1.0.0) provides three standalone skills. Install any combination of them. The complete plugin is not included in this release.

## Download a skill

Use the individual ZIP links below, which are also linked in the release notes.

| Skill | Scope | v1.0.0 download |
| --- | --- | --- |
| `solve-1d-kinematics` | Constant-acceleration motion along one fixed spatial dimension, including vertical free fall. | [solve-1d-kinematics-v1.0.0.zip](https://github.com/omoussa/physics-problem-solving/releases/download/v1.0.0/solve-1d-kinematics-v1.0.0.zip) |
| `solve-2d-kinematics` | Constant-acceleration motion in a plane, including projectile motion. | [solve-2d-kinematics-v1.0.0.zip](https://github.com/omoussa/physics-problem-solving/releases/download/v1.0.0/solve-2d-kinematics-v1.0.0.zip) |
| `solve-newton-laws` | Translational equilibrium and dynamics, including friction, inclines, connected objects, ideal pulleys, and circular motion. | [solve-newton-laws-v1.0.0.zip](https://github.com/omoussa/physics-problem-solving/releases/download/v1.0.0/solve-newton-laws-v1.0.0.zip) |

GitHub's automatically generated **Source code** archives contain the entire repository. The links above provide the individual skill packages.

## Install in local Codex

1. Download a skill ZIP and extract it.
2. Copy the complete skill folder into one of the locations below, preserving `SKILL.md` and all supporting files.
3. Keep the installed folder name unversioned, such as `solve-1d-kinematics`. Its `SKILL.md` must sit directly inside that folder.
4. In Codex CLI or the IDE extension, select the skill with `/skills` or mention it by name: `$solve-1d-kinematics`, `$solve-2d-kinematics`, or `$solve-newton-laws`.

| Installation scope | Copy the skill folder into |
| --- | --- |
| Your user account | `~/.agents/skills/` |
| One project | `<project-root>/.agents/skills/` |

For example, a user installation should contain `~/.agents/skills/solve-1d-kinematics/SKILL.md`. The version belongs in the ZIP filename; the installed folder retains the skill's name.

### Alternative: install from GitHub

When Skill Installer is available, ask it to install the skill from its versioned repository path. For example:

```text
$skill-installer Install the skill from https://github.com/omoussa/physics-problem-solving/tree/v1.0.0/skills/solve-1d-kinematics
```

Replace `solve-1d-kinematics` with the desired skill name. The `v1.0.0` tag selects this release's files.

## environments with skill installation support

Where a standalone skill-import workflow is available, provide the complete ZIP and request installation with its instructions and supporting files preserved unchanged. Confirm that the skill appears in the environment's Skills list before use; select it with `@` where supported.

Availability varies by product and account. Copying a folder into a local Codex directory installs it in that local environment; uploading a ZIP to a chat alone does not confirm installation.

## Verify and use the skill

Try the representative problems in the [v1.0.0 tests folder](https://github.com/omoussa/physics-problem-solving/tree/v1.0.0/tests). Review the solution structure and physics, including:

- Eight numbered steps for either kinematics skill; four numbered main steps for Newton's laws.
- Explicit coordinate systems, vector notation, and unit vectors.
- Symbolic algebra before numerical substitution, followed by units and appropriate precision.

Solutions default to student-facing college-level explanations with rendered equations. For Canvas output, request an accessible Canvas-ready HTML snippet using MathJax delimiters.

## Updating an installed skill

Save any local customizations, then replace the complete installed skill folder with the folder from the newer ZIP. Use one installed copy of each skill name in your active scope, and repeat a representative problem after updating.

## Runtime requirements

- Worked solutions use the host's reasoning and equation-rendering capabilities.
- Newton's laws diagrams require Python 3 and Matplotlib in an execution-capable environment. The skill includes a fallback when diagrams cannot be rendered.
- Canvas HTML uses `\( ... \)` and `\[ ... \]` delimiters and the LMS's available math renderer. Diagrams require LMS-hosted image references or explicit placeholders.
- These workflows require no external account connection or MCP server.

## Full-plugin status

Full-plugin registration and post-installation verification remain pending. A confirmed plugin installation link and instructions will be added when available. The standalone skills can be installed independently using the methods above.


## Current status

The source repository is available. Plugin registration and post-installation verification are pending.

The individual skills are self-contained. The full plugin package has not yet been accepted by Plugin Creator or verified after installation. The initial registration attempts returned: "Plugin must include a skill, MCP server, or connected app." A portable manifest, compatibility manifest, and archive layout changes did not resolve that error.

## Install one skill in local Codex

1. Obtain this repository through your authorized GitHub access.
2. Choose a complete folder under `skills/`.
3. Copy that folder to your local Codex user skill directory, normally `~/.agents/skills/`, or to `.agents/skills/` in a project for project-scoped use. Preserve its name and all bundled files. Check an existing same-name folder before replacing it.
4. In Codex CLI or the IDE extension, select the skill through `/skills` or invoke it with `$solve-1d-kinematics`, `$solve-2d-kinematics`, or `$solve-newton-laws`.
5. Run representative prompts from this repository's `tests/` folder and review the results.

When Skill Installer is available, it can also install a skill from a repository. Specify `omoussa/physics-problem-solving` and the exact `skills/<skill-name>` path; private-repository access must already be authorized in the installation environment.

Standalone-skill support differs by product surface. Do not assume that copying a local folder installs it into ChatGPT on the web. In an environment with Skill Creator installation support, provide the complete folder and explicitly request installation. Plugin distribution is the route for a shared installable experience across supported ChatGPT surfaces.

## Complete plugin

The repository root contains `plugin.json`, the conventional `skills/` directory, and a `.codex-plugin/plugin.json` compatibility overlay. No MCP server or external account connection is required by these workflows.

Once registration succeeds, document the confirmed plugin URL and the tested installation steps here. Do not treat downloading or extracting a ZIP as proof that a host installed the plugin. Release archives are deferred until that verification succeeds.

## Runtime requirements

- Instructions and equations use the host's ordinary reasoning and math-rendering capabilities.
- Newton's laws diagrams use Python 3 and Matplotlib in an execution-capable environment. The skill documents the fallback when images cannot be rendered.
- Canvas fragments use `\( ... \)` and `\[ ... \]` delimiters and the LMS's available math renderer. Diagrams need supplied LMS-hosted image references or explicit placeholders.

## Official documentation

- [Build skills](https://learn.chatgpt.com/docs/build-skills)
- [Package your plugin](https://developers.openai.com/plugins/build/plugins)

Product installation guidance was checked on October 7, 2026.
