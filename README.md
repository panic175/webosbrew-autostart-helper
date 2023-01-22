# WebOS Brew Autostart Helper for Home Assistant

## Installation

1. Add this repo as custom repo to HACS
2. Search and install this in HACS
3. Add this to your configuration.yaml

```yaml
webosbrew_autostart_helper:
```

4. Restart
5. Add an automation like this

```yaml
alias: WebOS Brew Autostart
description: ""
trigger:
  - platform: device
    device_id: 3b3 # This will be different for you. I used graphical editor to figure this out
    domain: media_player
    entity_id: media_player.lg_webos_smart_tv
    type: turned_on
condition: []
action:
  - service: webosbrew_autostart_helper.webosbrew_autostart_helper
    data:
      tv_ip: 127.0.0.1 # Enter your TV IP address here
mode: single
```
