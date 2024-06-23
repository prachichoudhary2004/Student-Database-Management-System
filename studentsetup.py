from cx_Freeze import*
import sys


includefiles =["iitp logo.ico"]
excludes = []
packages = []
base = None
if sys.platform == "win32":
    base = "win32GUI"

shorcut_table =[
    ("DesktopShortcut", #Shortcut
     "DesktopFolder", #Directory_
     "studentmanagementsystem", #Name
     "TARGETDIR", #component_
     "[TARGETDIR]\studentmanagementsystem.exe", #Target
     None, #Arguments
     None, #Description
     None, #Hotkey
     None, #Icon
     None, #IconIndex
     None, #Showcmd
     "TARGETDIR", #WkDir

    )
]

msi_data = {"shortcut": shorcut_table}

bdist_msi_option = {"data": msi_data}
setup()(
    version='0.1',
    description='Student management system Devloped By Team 54',
    
    author="Team 54",
    name='Project',
    options={'build_exe': {'include_files':includefiles},'bdist_msi':bdist_msi_option},
    executables=[
        Executable(
            script="studentmanagementsystem.py",
            base=base,
            icon='iitp logo.ico',
            
        )
    ]


)
