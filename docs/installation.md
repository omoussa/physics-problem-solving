# Installation

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
