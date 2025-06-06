<h1 align="center">
 Yurt
</h1>

This repository is a collection of curated or created assets by creative commons and other open source license families mainly for testing or modeling web-, game-design and graphics programming. This repository is extensively sampled from Khronos Groups' [glTF-Sample-Assets repository](https://github.com/KhronosGroup/glTF-Sample-Assets/tree/main).

<p align="center">
    <img src="scenes/outliner-testscene/ss-cycles.png" />
    <br>
    <sub><i> Outliner Test Scene</i></sub>
</p>

__What is yurt?__  
Yurt is a portable tent used by various nomadic cultures. Built with minimal materials and tools, it offers a cozy and functional dwelling for its inhabitants. Beyond its practicality, the yurt symbolizes community, openness, and resilience—serving as a steadfast shelter and a place to create a home, even in the most challenging natural environments. It is aimed to provide set of tools for you to start your journey on creative wilderness.

In modern Turkish it means homeland and/or dormitory, also it is the given name of 'mobile depot' in the virtual realm of EvE Online.


# Asset Metadata Structure
Every asset in this repository aimed to contain metadata file in json format to provide collected information about the asset.  

For complex assets like models and scenes `metadata.json` file stands within the same directory with the asset.

For simpler assets who do not have their own directory like simple textures, metadata files are held in `metadata` directory within the same parent folder as the same name with the asset.

```json
{
    "name": "",
    "description" : "",
    "version" : 1,  
    "type": "",
    "formats": [""],
    "accessDate" : "",
    "screenshot" : "",
    "paths" : [
        ""
    ],
    "tags" : [],
    "legal" : [
        {
            "authors" : [
                ""
            ],
            "owner" : "",
            "source": "",
            "publishDate" : "",
            "license" : "",
            "licenceURLs" : [
                ""
            ],
            "what" : ""
        }
    ],
    "modifications": [
        {
            "author": "",
            "description": ""
        }
    ],
    "template": 5
}
```

# Asset Naming Conventions

__Rules for Consistent Naming__  
1. Naming is lowercase, underscore (_) character used instead of white space for multiple words.
2. Various data types are separated by dash(-) character within the naming.   
    ex. name_of_asset-name_of_author
3. On the template variables stated within braces <> while optional data marked encapsulated with square braces [].
4. To handle naming collision, if the name exists in the previos list new item gets an incremental positive integer next to its name.   
    Ex. name_of_asset01

You can inspect the example below to understand naming structure.

### 1. Textures  

_Template_
```html
<name_of_the_texture>-<detail_of_the_texture>-<resolution>
```

_Example_
```bash
parallax_test-displacement-512
gamma_test-srgb-2k
```

### 2. Models
_Directory Template_
```html
<name_of_the_model>-[by_<name_of_the_authors>]-<source>
```
_Example_
```bash
kokorec-by_berk_gedik-sketchfab-obj
lantern-polyhaven (author is unknown)
lantern (bare minimum)
```

### 3. Scenes
_Directory Template_
```html
<name_of_the_scene>-[by_<name_of_the_authors>]-[<source>]
```
_Example_
```bash
sponza
```

# Folder Structure
```plaintext
:root:
├── models/                     3d single object models
├── scenes/                     3d scenes with multiple objects, animations, lighting ...
│
├── textures-alpha/             2d alpha brushes, textures
├── textures-cubemaps/          2d six piece cubemap textures
├── textures-hdri/              2d high dynamic range lighting textures
├── textures-pbr/               2d pbr textures with various maps such as normal, roughness etc.
└── textures-simple/            2d single textures
```

# Curated Sources

| Desc | Name| Last Access Date|
| :-- | :-- | :--: |
| glTF Format 3D Assets | [Khronos Group glTF-Sample Assets repository](https://github.com/KhronosGroup/glTF-Sample-Assets/tree/main) | 2025-01-09
| Images | [Pexels](https://www.pexels.com/) | 2025-01-09
| Images | [Unsplash](https://unsplash.com/s/photos/cc0) | 2025-01-09
| Madjin CC0 Repository | [awesome-cc0](https://github.com/madjin/awesome-cc0) | 2025-01-09
| Textures, Models, HDRIs | [AmbientCG](https://ambientcg.com/) | 2025-01-09
| Textures, Models, HDRIs | [Polyhaven](https://polyhaven.com/) | 2025-01-09
| Scenes, Models | [Intel GPU Research Samples](https://www.intel.com/content/www/us/en/developer/topic-technology/graphics-research/samples.html) | 2025-01-11
| Scene          | [Amazon Lumberyard Bistro (NVIDIA ORCA Collection)](https://developer.nvidia.com/orca/amazon-lumberyard-bistro) | 2025-01-19
| Scenes, Models | [Morgan McGuire, Computer Graphics Archive](https://casual-effects.com/data/) | 2025-01-19
| Models, Datasets | [Wolfram Data Repository](https://datarepository.wolframcloud.com/) | 2025-01-19
| Scenes, Models | [Blender Demo Files](https://www.blender.org/download/demo-files/) | 2025-01-28
| Models, Textures ... | [PBRPX](https://library.pbrpx.com/asset?category=995) | 2025-02-11 