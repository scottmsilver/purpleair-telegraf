# purpleair-telegraf
purple-air scripts for outputting telegraf metrics (in the line protocol format)

# Want to connect your Purple Air to influx/grafana/etc?

This script can be used with telegraf to gather data from your purple air. It outputs
in the line protocol format. Then you can use telegraf to redirect the output wherever you like

# Docker use (recommended)

We will use a command like this, you need to find out your purplie air id in the XXX below.

```
docker run scottmsilver/purple-air:1.0 python3 json-to-influx-telegraf.py  http://purpleair-XXX/json?live=true
```

NB: your telegraf user must be part of the docker group. Sometimes it's called telegraf other times telegraf_

# Manually

```
pip install --no-cache-dir -r requirements.txt
python3 json-to-influx-telegraf.py http://purpleair-XXXX.localdomain/json?live=true
```

# Add to /etc/telegraf/telegraf.conf the following:

```
[[inputs.exec]]
   ## Commands array
   commands = [
     # Make sure to update where your script is and that is executable
     # The second argument is the URL to your purpleair. I use mine locally
     # But I think you can use the purpleair website URL (note that the JSON parser will need to be modified a touch)
     "docker run scottmsilver/purple-air:1.0 python3 json-to-influx-telegraf.py  http://purpleair-XXX/json?live=true"
   ]

   ## Timeout for each command to complete.
   timeout = "10s"
   interval = "1m"

   data_format = "influx"
```

test it

```
telegraf --test
```

restart telegraf

```
systemctl restart telegraf
```
