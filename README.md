<h1 align="center">
 Yurt
</h1>

This repository is a collection of curated or created assets by creative commons and other open source license families mainly for testing or modeling web-, game-design and graphics programming. This repository is extensively sampled from Khronos Groups' [glTF-Sample-Assets repository](https://github.com/KhronosGroup/glTF-Sample-Assets/tree/main).

__What is yurt?__  
Yurt is a portable tent used by various nomadic cultures. Built with minimal materials and tools, it offers a cozy and functional dwelling for its inhabitants. Beyond its practicality, the yurt symbolizes community, openness, and resilience—serving as a steadfast shelter and a place to create a home, even in the most challenging natural environments. It is aimed to provide set of tools for you to start your journey on creative wilderness.

In modern Turkish it means student dormitory, also it is the name of mobile depot in the virtual realm of EvE Online.



<p align="center">
    <img alt="'Yurt' Mobile Depot (Eve Online)" src="https://wiki.eveuniversity.org/images/c/c4/Mobile_Depot_image.jpg" />
        <br>
    <sub><i>'Yurt' Mobile Depot (Eve Online)</i></sub>
</p>

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
    "format": "",
    "accessDate" : "",
    "screenshot" : "",
    "path" : "",
    "tags" : [],
    "legal" : [
        {
            "author" : "",
            "owner" : "",
            "source": "",
            "publishDate" : "",
            "license" : "",
            "licenceURL" : "",
            "what" : ""
        }
    ],
    "modifications": [
        {
            "name": "",
            "author": "",
            "description": ""
        }
    ],
    "template": 1
}
```

# Asset Naming Conventions

__Rules for Consistent Naming__  
1. Naming is lowercase, dash(-) character used instead of white space for multiple words.
2. Various data types are separated by underscore (_) character within the naming.   
    ex. name-of-asset_name-of-author
3. On the template variables stated within braces <> while optional data marked encapsulated with square braces [].
4. To handle naming collision, if the name exists in the previos list new item gets an incremental positive integer next to its name.   
    Ex. name-of-asset1

Please inspect the names below to understand consistent naming structure.

### 1. Textures  

_Template_
```html
<name-of-the-texture>_<detail-of-the-texture>_<resolution>
```

_Example_
```bash
parallax-test_displacement_512
gamma-test_srgb_2k
```

### 2. Models
_Directory Template_
```html
<name-of-the-model>_[by-<name-of-the-authors>]_<source>_<format>
```
_Example_
```bash
kokorec_by-berk-gedik_sketchfab_obj
lantern_polyhaven (author is unknown)
```

### 3. Scenes

```html
not yet implemented
```


# Folder Structure

```html
not yet implemented
```

# Other Similar Sources
I also collect various quality sources with Creative Commons license family.

| Desc | Name| Last Access Date|
| :-- | :-- | :--: |
| glTF Format 3D Assets | [Khronos Group glTF-Sample Assets repository](https://github.com/KhronosGroup/glTF-Sample-Assets/tree/main) | 2025-01-09
| Images | [Pexels](https://www.pexels.com/) | 2025-01-09
| Images | [Unsplash](https://unsplash.com/s/photos/cc0) | 2025-01-09
| Madjin CC0 Repository | [awesome-cc0](https://github.com/madjin/awesome-cc0) | 2025-01-09
| Textures, Models, HDRIs | [AmbientCG](https://ambientcg.com/) | 2025-01-09
| Textures, Models, HDRIs | [Polyhaven](https://polyhaven.com/) | 2025-01-09
| Scenes, Models | [Intel GPU Research Samples](https://www.intel.com/content/www/us/en/developer/topic-technology/graphics-research/samples.html) | 2025-01-11