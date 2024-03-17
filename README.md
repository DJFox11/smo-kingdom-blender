# smo-kingdom-blender
A Blender plugin that contains a utility for importing kingdoms from Super Mario Odyssey.

## Key Features
- Decompress `.szs` and import Super Mario Odyssey's models, textures, and materials.
    - Model Files: `.bfmdl`
    - Material Files: `.bfmat`
    - Texture Files: `.bftex`
- Decompress and read `.szs` files containing information regarding a selected kingdom:
    - Binary YAML File: `.byml`

## Installation
See the [Blender Wiki](https://docs.blender.org/manual/en/latest/editors/preferences/addons.html) for instructons.

1. Selct a version.
    - For the latest version, click the green `Code` button and select `Download ZIP`.
    - To download a specific version, check the [Releases](https://www.youtube.com/watch?v=dQw4w9WgXcQ) page.

2. Install the .ZIP in Blender under `Edit > Preferences > Addons > Install.`
3. Make sure the addon is enabled by searching `Super Mario Odyssey Kingdom Importer` if not already enabled.
4. After installing and enabling the addon in Blender, in the 3D Viewport open the Sidebar by pressing the `N` key, a new `Kingdom Importer` tab should appear. **If the addon panel doesn't appear, make sure you are in Object Mode.**

## System Reqirements
This addon supports 64-bit versions of Blender 4.0 or later for Windows, macOS, and Linux. Machines running Apple silicon are also supported. *(Requires further tesing.)* If your computer does run a supported version of Blender and are running into problems, please make an issue in [Issues](https://www.youtube.com/watch?v=dQw4w9WgXcQ).

## Uninstall/Updating
To remove the addon, hit the `Remove` button to uninstall. Then you can install the newest avaliable version.

## Special Thanks
masbmf03 / szs_decompress: Gives the addon the ability to decompress the game's `.szs` files containg the models, textures, and materials.\
https://github.com/masbmf03/szs_compress

MonsterDruide1 / OdysseyDecomp: A very useful tool for managing the game's StageData files.\
https://github.com/MonsterDruide1/OdysseyDecomp

RenaKunisaki / bfres-importer: A tool used for importing .`bfres` files, with support for models, textures, and materials.\
https://github.com/RenaKunisaki/bfres_importer
