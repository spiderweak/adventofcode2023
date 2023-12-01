# AdventOfCode2023

Hi, welcome to my Advent of Code 2023 repository.

I'll probably pickup another language and do this year's advent of code with two languages.

The first language I'll use is Python, despite having practiced it for years, I still find myself lacking, especially regarding code quality, documentation, and best practice. I'll work on the Python code in three steps:
- First is providing a quick and dirty solution to the problem, in order to perform better in the rankings (either the public rankings (but I'm not confident about it) or the private one that I use with my friend (on which I'm cheating a bit because I can start working on it at midnight and I don't have to wake up early to solve it at 6am (UTC+1, Paris), which becomes a liability if I can't solve it under an hour because then I'll need to go to sleep because I usually need to wake up the next day to go to work))
- Second will be refining the code, add in commentary, error handling, logging, and everything possible to make some code as clean as possible (I probably stick to single file solution at first because making complex classes to tackle really simple problem seem a bit overkill, but later on, on more difficult problems, having a proper code structure will also matter 
- Finally, I created a custom GPT : https://chat.openai.com/g/g-7Hxprh2tg-adventofcoach that serves as coach for the event. The GPT is tasked with providing feedback on code quality, documentation, error handling, logging, and provide alternative or more efficient code, it is not provided the problem but instead tasked with hitting me when I'm coding badly, because coding is not telling the computer what to do, it's telling another developper what you want the computer to do.

The other language is not defined yet, because I'll probably not play with it in the first day but probably after the first week of the event (a bit overworked for now) but it will probably be some functional programming using either Elixir or OCamL, or some Rust (because for some reasons most of my friends decided that this would be a Rusty year).

## Getting started

This is not really a Getting Started with my code, but rather to present how I am getting started with my Python code.

As I don't want to lose too much time on file structure but still want to have some quick clean code on my first solution, I developed a skeleton solution under Python/skel/main.py

This skeleton solution has some input argument parsing, raises notImplementedErrors on non implemented part_one or part_two functions (error that are then catched in the main() part of the program so that the program does not crash encountering them, especially considering the way the problems are provided). There is also a quick and dirty way to parse the input file line by line, because it'is usually what we're asked to do in the firsts few puzzles, the functions are not used for now but I keep them on hand in the (most likely) case I'll need them quickly to lose less time during the firsts days.

## Licensing

Pretty much all my code is usually under CC BY-NC-SA

## Contributing

No need to contribute, especially considering this repo is just mirroring my private GitLab server's repository.

## Acknowledgement

I'll probably put some links around here to the repositories that my friends are using.
