---
title: "Systemctl basic usage"
date: 2021-06-03T00:05:11-05:00
draft: false
summary: |
    Introduction to the usage of `systemctl` to manage services under
    linux systems that uses `systemd`.
---

If your linux system uses `systemd` then you can take advantage of `systemctl` command to manage services.

Management of services is pretty straighforward, take a look on below commands

```bash
systemctl start <service_name>
systemctl stop <service_name>
systemctl status <service_name>
```

Commands are pretty self-descriptive. Now, if a service refuses to stop gracefully, you can force it with `kill` subcommand

```bash
systemctl kill <service_name>
```


## Restart and reload

After updating a configuration file we must either `restart` or `reload` the service, that causes the service to re-read the configuration file and apply changes. Take a look on below examples

```bash
systemctl restart sshd
systemctl reload sshd
```

Now, what's the difference between `restart` and `reload`?

`restart` will shut down service entirely and then start it again, whereas `reload` will re-read its configuration but keep the same process running.


## Enable and disable

If you want a service starts automatically during system boot, then you can `enable` it:

```bash
systemctl enable httpd
```

On the contrary, if you want service does not starts automatically, then use `disable`

```bash
systemctl disable httpd
```

Also you can check if a service is enabled with `is-enabled` subcommand

```bash
systemctl is-enabled httpd
```

## Override unit files

Units are the main *objects* that systemd manages, the *unit files* indicates to systemd how to manage a specific *unit*.

By default those files are placed at `/lib/systemd/system` however, you should **NOT** edit files here, instead, use `/etc/systemd/system` which take precedence over the `/lib` path and put there a copy of the unit file that you want to modify.

Alternatively If you want to modify only specific parts of a unit file you can create *snippets* within a subdirectory named after the unit file with a `.d` appended on the end, for a service named `httpd` we could create a directory `/etc/systemd/system/httpd.service.d/` and inside that directory, a file ending with `.conf` (e.g. `override.conf`). 

Fortunately there is a command to do this automatically for you and it is `systemctl edit <service>`. Let's say we want to change the user and group that runs the service `plexmediaserver` to username `ubuntu` and groupname `admins`, then we use the command

```bash
systemctl edit plexmediaserver
```

that will launch our default editor and will allow us to override parts of the unit file, so we can enter below config

```ini
[Service]
User=ubuntu
Group=admins
```

After saving the file we can restart the service and our changes will take effect.
