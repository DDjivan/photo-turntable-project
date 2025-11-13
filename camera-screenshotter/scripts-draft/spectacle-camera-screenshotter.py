#!/usr/bin/env python

# chmod +x *.py

import subprocess
from os import system
from os.path import exists
from time import sleep as t_sleep

sfx_partial = "./sounds/completion-partial.wav"
sfx_success = "./sounds/completion-success.wav"

def simple_timer(seconds: int = 5, sfx: bool = True) -> bool:

    if sfx and not (exists(sfx_partial) and exists(sfx_success)):
        print("≥ 1 sound file not found!")
        sfx = False

    try:
        for y in range(1, seconds):
            print(f"{seconds - y}…")

            if sfx:
                # system(f"aplay {sfx_partial}")
                system(f"aplay {sfx_partial} > /dev/null 2>&1")
            else:
                t_sleep(1)

        print("Go!")
        # if sfx: system(f"aplay {sfx_success}")
        if sfx: system(f"aplay {sfx_success} > /dev/null 2>&1")

    except KeyboardInterrupt:
        return False

    return True

def take_screenshot_spectacle(output_file: str) -> None:
    command = [
        "spectacle",
        # "--windowundercursor",
        "--fullscreen",
        "--background",
        "--output", output_file
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Screenshot saved to: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error capturing screenshot: {e}")

    return

def take_screenshot_flameshot(output_folder: str) -> None:
    command = [
        "flameshot",
        "full",
        "--path", output_folder
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Screenshot saved in: {output_folder}")
    except subprocess.CalledProcessError as e:
        print(f"Error capturing screenshot: {e}")

    return

def take_multiple_screenshots(output_dir: str, amount: int, delay) -> None:
    for y_not in range(amount):
        path = f"{output_dir}flameshot.png"
        print(path)
        take_screenshot_flameshot(path)
        t_sleep(delay)

    return

if __name__ == "__main__":
    output_path = "./screenshots/"
    # take_screenshot(output_path)
    simple_timer(3)
    take_multiple_screenshots(output_path, 10, 0.5)

