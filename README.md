# re**sh**act

WIP

re**sh**act is a command-line tool used to redact secrets in shell history. I realized that if someone got ahold of my shell history that they could do a lot of damage; and I don't want to delete my shell history files because I use autocomplete religiously. So I made re**sh**act, which is some kind of shitty portmanteau of redact and shell. It works on both Linux & macOS and supports all the popular shells like `bash`, `zsh`, and `fish`. You run it, choose which secrets you want to redact, and continue hacking with less stress.

Install:
```
$ pip install reshact --user
```

Usage:
```
$ reshact

```
