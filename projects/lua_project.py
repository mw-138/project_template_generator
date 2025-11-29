from dataclasses import dataclass, field

from projects.project import Project, ProjectDirectory, ProjectFile


@dataclass
class LuaProject(Project):
    id: str = "lua"
    directories: list[ProjectDirectory] = field(
        default_factory=lambda: [
            ProjectDirectory(
                "",
                [
                    ProjectFile("main.lua", ""),
                    ProjectFile(
                        ".gitignore",
                        """# Compiled Lua sources
luac.out
*.luac

# LuaRocks
*.rock
*.src.rock
/lua_modules
/lib/luarocks/rocks-5.*/

# LÖVE (Love2D)
*.love

# Object files
*.o
*.os
*.ko
*.obj
*.elf

# Precompiled Headers
*.gch
*.pch

# Libraries
*.lib
*.a
*.la
*.lo
*.def
*.exp

# Shared objects (inc. Windows DLLs)
*.dll
*.so
*.so.*
*.dylib

# Executables
*.exe
*.out
*.app
*.i*86
*.x86_64
*.hex

# Debug files
*.dSYM/
*.su
*.idb
*.pdb

# Kernel Module Compile Results
*.mod*
*.cmd
.tmp_versions/
modules.order
Module.symvers
Mkfile.old
dkms.conf

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# OS
Thumbs.db

# Project specific
*.log""",
                    ),
                    ProjectFile("README.md", "# Lua Project"),
                ],
            ),
        ]
    )
