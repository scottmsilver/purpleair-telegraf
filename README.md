# purpleair-telegraf
purple-air scripts for outputting telegraf metrics (in the line protocol format)

Want to connect your Purple Air to influx/grafana/etc?

This script can be used with telegraf to gather data from your purple air. It outputs
in the line protocol format. Then you can use telegraf to redirect the output wherever you like

Add this to your telegraf config (be sure to update the 

```
# # Read metrics from one or more commands that can output to stdout (I am outputing to influx here)

[[inputs.exec]]
   ## Commands array
   commands = [
     # Make sure to update where your script is and that is executable
     # The second argument is the URL to your purpleair. I use mine locally
     # But I think you can use the purpleair website URL (note that the JSON parser will need to be modified a touch)
     "/PATH/TO/json-to-influx-telegraf.py http://purpleair-XXXX.localdomain/json?live=true"
   ]

   ## Timeout for each command to complete.
   timeout = "10s"
   interval = "1m"

   data_format = "influx"
```

And configure telegraf as you normally do to send to wherever.
