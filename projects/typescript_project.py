from dataclasses import dataclass, field

from projects.project import Project, ProjectDirectory, ProjectFile


@dataclass
class TypescriptProject(Project):
    id: str = "typescript"
    directories: list[ProjectDirectory] = field(
        default_factory=lambda: [
            ProjectDirectory(
                "",
                [
                    # TODO: Get project name and put into package.json
                    ProjectFile(
                        "package.json",
                        """{
    "name": "my-project",
    "version": "1.0.0",
    "main": "dist/index.js",
    "scripts": {
    "build": "tsc",
    "start": "node dist/index.js",
    "dev": "tsc --watch"
    },
    "devDependencies": {
    "typescript": "^5.0.0"
    }
}""",
                    ),
                    ProjectFile(
                        "tsconfig.json",
                        """{
    "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true
    }
}""",
                    ),
                    ProjectFile(
                        ".gitignore",
                        """node_modules/
dist/
build/
*.js
*.d.ts
.env""",
                    ),
                    ProjectFile("README.md", "# Typescript Project"),
                ],
            ),
            ProjectDirectory("src", [ProjectFile("index.ts", "")]),
            ProjectDirectory("dist", []),
            ProjectDirectory("node_modules", []),
        ]
    )
