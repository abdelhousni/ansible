# Journald


This role provides an easy way to configure the systemd-journald logging
service.

## Requirements

None

## Role Variables

The role allows system administrator to configure basic systemd-journald
settings, through the following set of variables which form the role's public
API.

- `journald_persistent` - boolean variable which governs where journald stores
  log file. When set to `true` the logs will be stored on disk in
  `/var/log/journal/`. Defaults to `false`, i.e. `volatile` journal storage.

**NOTE**: The following settings apply to both `persistent` and `volatile` modes
unless otherwise indicated.

- `journald_max_disk_size` - integer variable, in megabytes, that governs how
  much disk space can journal files occupy before some of them are deleted. No
  implicit value is configured by the role, hence default sizing calculation
  described in `man 5 journald.conf` applies.

- `journald_max_files` - integer variable that governs how many journal files
  can be kept at maximum while respecting max disk size settings for journal. No
  implicit value is configured by default.

- `journald_max_file_size` - integer variable, in megabytes, describes the
 maximum size of single journal file. No implicit configuration is set up by the
 role.

- `journald_per_user` - boolean variable, allows to configure whether journald
  should keep log data separate for each user, e.g. allowing unprivileged users
  to read system log from their own user services. Defaults to `true`. Note that
  per user journal files are available only when `journald_persistent: true`.

- `journald_compression` - boolean variable instructs journald to apply
  compression to journald data objects that are bigger than default 512 bytes.
  Defaults to `true`.

- `journald_sync_interval` - integer variable, in minutes, configures the time
  span after which journald synchronizes the currently used journal file to
  disk. By default role doesn't alter currently used value.  This setting is
  only applicable for `journald_persistent: true`.  You will get a warning if
  set otherwise.

- `journald_forward_to_syslog` - boolean variable, control whether log messages
  received by the journal daemon shall be forwarded to a traditional syslog
  daemon. Defaults to `false`.

## Example Playbook

```yaml
- hosts: all
  vars:
    journald_persistent: true
    journald_max_disk_size: 2048
    journald_per_user: true
    journald_sync_interval: 1
  roles:
    - redhat.rhel_system_roles.journald
```

## rpm-ostree

See README-ostree.md

## License

MIT

## Author Information

Michal Sekletar