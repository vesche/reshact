re**sh**act is a command-line tool used to redact secrets in shell history.

```
[vesche@t480 reshact]$ python reshact.py
Processing /home/vesche/.bash_history ...
Processing /home/vesche/.local/share/fish/fish_history ...
Processing /home/vesche/.python_history ...
Processing /home/vesche/.zsh_history ...
4 secret(s) found in /home/vesche/.local/share/fish/fish_history
reshact all (y/n)? y
6 secret(s) found in /home/vesche/.python_history
reshact all (y/n)? y
```

