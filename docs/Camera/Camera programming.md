
# Camera programming 

## What we need 

Something to take pictures of the real world. Two parts: 

Hardware: 

- One or multiple cameras? More is better for testing. 
- Resolution: what target? 
- Stability: test by taking pictures on worst case scenarios. 
- Output: what format? 
- Settings: aperture, exposure… are they controllable? 
- Connection: integrated, USB cable… 

Software: 

- A program that can communicate with cameras 
- Platform: Web, Android, iOS, Linux, Windows? 
- What are the different limitations? 
- What exists already? 
- How to connect it to the rest of the project? 

## First ideas 

### Programming framework 

What framework? What programming language(s) or which IDE (Integrated Development Environment)? 

| Framework    | Godot Engine                                    | Android Studio            | Web Development           |
| ------------ | ----------------------------------------------- | ------------------------- | ------------------------- |
| Available on | Linux<br>Windows<br>macOS                       | Linux<br>Windows<br>macOS | Any                       |
| Open         | Yes                                             | No                        | Yes                       |
| Export to    | Web app <br>Android <br>iOS<br>Linux<br>Windows | Android                   | Web app                   |
| Camera       | Web app <br>Android <br>iOS<br>Linux            | Android                   | Web app                   |
| Language     | GDScript<br>or<br>C#                            | Kotlin<br>C++<br>Java     | JavaScript<br>HTML<br>CSS |

## Devices to test on 

[Djivan](../People/VARTANIAN%20Djivan.md): I have a laptop running Linux and a smartphone running iOS. I managed to get a webcam output on linux using Godot. I need to make the project more modular, and then try to export as an IPA file so that I can sideload it on my phone. Smartphones running Android should be the next target, but I don't have any. 

---
## Web app  

[Djivan](../People/VARTANIAN%20Djivan.md): Let's use VDO Ninja 

> VDO is the loose phonetic spelling of the world _video_. "VeeDeeOh". It is not an abbreviation.
> 
> [Source](https://docs.vdo.ninja/help/what-does-vdo-stand-for) 

- Code repository: https://github.com/steveseguin/vdo.ninja 
- Documentation: https://docs.vdo.ninja/ 

It's an amazing web application with "Smartphone wireless webcam capabilities". 

- ==**Web service URL:** https://vdo.ninja/     ==
- Backup web instance: https://backup.vdo.ninja/ 
- Android app:  [Google Play Store](https://play.google.com/store/apps/details?id=flutter.vdo.ninja) 
- iOS app: [Apple App Store](https://apps.apple.com/us/app/vdo-ninja/id1607609685) 

**⚠️ Note:** the smartphone applications do not offer "4K video options" (according to the app), so it is best to use the web instances. 

Here is how to use it: [VDO Ninja Tutorial](VDO%20Ninja%20Tutorial.md). 





