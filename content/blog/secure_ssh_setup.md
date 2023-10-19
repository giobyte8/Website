---
title: "Secure sshd setup"
date: 2023-10-18T22:04:11-05:00
draft: false
summary: |
    Guide to configure `ssh` daemon in a secure way by disabling root login
    and password login from external networks.
---

Exposing a ssh server to the external world is dangerous since the server
will receive a lot of login attempts from attackers.

A more secure approach is to expose it with following configs:

1. [Disable root ssh login](#disable-root-ssh-login)
2. [Disable password login from external networks](#disable-password-login-from-external-networks)
3. [Allow password login from internal network](#allow-password-login-from-internal-network)
4. [Monitor auth activity](#monitor-auth-activity)

## Disable root ssh login

> **WARN:** Make sure you can login with a regular user before disabling root login

Set `PermitRootLogin` to `no` in `/etc/ssh/sshd_config` file within your server

```bash
sudo vim /etc/ssh/sshd_config

# Disable root login:
...
PermitRootLogin no
...
```

Then reload ssh config
```bash
sudo systemctl reload ssh
```

## Disable password login from external networks

This method consists in using *ssh keys* for login instead of password. For
that we'll need to put client machines *ssh public key* into
server's `~/.ssh/authorized_keys` file so that clients can authenticate
using their *shh private key*

Your client machine may already have existing keys at `~/.ssh/` dir, keys
files usually start with `id_` prefix. You can use existing keys or create
a new one (with different name).

1. Generate ssh keys using `ssh-keygen` (if not previous key exists or
   custom key is desired)
   ```bash
   # Run below command and follow on screen instructions
   ssh-keygen

   # Alternatively specify a custom file name if other key already exists
   ssh-keygen -f <custom_key_name>
   ```
2. Add your public key to the server's `~/.ssh/authorized_keys` file
   ```bash
   # 'ssh-copy-id' can automate this step
   ssh-copy-id username@server.ip

   # Alternatively if using a custom key file, indicate the identity
   ssh-copy-id -i <custom_key_name> username@server.ip
   ```
3. Test ssh key auth to verify it works from your client machine
   ```bash
   # It should login without asking for user password
   ssh username@server.ip
   ```
4. Disable password login
   > **WARN:** Make sure ssh key login works before disabling password login

   Set `PasswordAuthentication` to `no` in server's `/etc/ssh/sshd_config` file
    ```bash
    sudo vim /etc/ssh/sshd_config

    # Disable password login:
    ...
    PasswordAuthentication no
    ...
    ```

    Then reload ssh config
    ```bash
    sudo systemctl reload ssh
    ```

Repeat steps for each one of your client machines

## Allow password login from internal network
As a fallback option you may want to enable password login from internal
network only in case you lost your client machine or keys.

SSH allows to override config params using `MATCH` expressions. Add a
block like below at end of `/etc/ssh/sshd_config`.

```shell
# Settings that override the global settings for matching IP addresses only
Match address 192.0.2.0/24
    PasswordAuthentication yes
```
> Use your own home network(s) addresses

Then reload ssh config
```bash
sudo systemctl reload ssh
```

## Monitor auth activity
Use following commands to view system authentication activity

- `sudo last` Shows all successful logins and sessions length
- `sudo lastb` Shows all failed attemps and the source IP
- `cat /var/log/auth.log` Shows detailed authentication info

## References

- [Ask Ubuntu: Allow ssh auth from certain IPs only](https://askubuntu.com/a/101672/618140)
- [Digial ocean: How to setup SSH Key-Based auth](https://www.digitalocean.com/community/tutorials/how-to-configure-ssh-key-based-authentication-on-a-linux-server#step-4-disabling-password-authentication-on-your-server)

