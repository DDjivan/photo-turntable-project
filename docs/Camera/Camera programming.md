
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












