# rehau-homeassistant

shows how to use a rehau air sensor with homeassistant

* see https://www.home-assistant.io/ for further details about Home Assistant
* for testing Home Assistant has been installed in a Python virtual environment on a rasbperry pi 3- see https://www.home-assistant.io/docs/installation/virtualenv/ for further instructions
* to read out values from the command line airsensor.c was used (see usb-sensors-linux).
* the following udev rule was added to call the querySensor.sh script (/etc/udev/rules.d/test.rules): ACTION=="add", ATTRS{idVendor}=="03eb", ATTR{idProduct}=="2013" RUN+="/home/pi/querySensor.sh"
* the script calls the python script querySensor.py which calls every 60 seconds the ./airsensor -o -v to get the VOC value.
* MQTT is used to pass the value to home assistant
* see configuration.yaml to see how Home Assistant must be configured (.homeassistant/configuration.yaml)

# further information

* Ein kleiner Nachteil dieses Sensors ist, dass er sich beim Einstecken in die USB-Buchse (oder beim Einschalten des RasPi) neu kalibiriert, d. h. es wird dann selbst schlechte Luft als "gut" angezeigt. Das kann man nur umgehen, indem man den Sensor bei sauberer Luft fest kalibriert. Das geht leider nur mit dem von REHAU herunterladbaren Windows-Tool. Sie starten diese REHAU-Software ( https://www.rehau.com/de-de/privatkunden/raumluftsensor/-/1560976) und doppelklicken bei gedrückter STRG(CTRL)-Taste auf das REHAU-Logo. Nun erscheint ein Menü, bei dem Sie "edit knobs" auswählen. Dort ändern Sie den letzten Punkt in "ui16StartupBits=0" ab. 

see http://www.netzmafia.de/skripten/hardware/RasPi/Projekt-Raumluftsensor/index.html for further details...