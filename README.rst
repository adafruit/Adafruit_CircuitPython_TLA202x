Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-tla202x/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/tla202x/en/latest/
    :alt: Documentation Status

.. image:: https://raw.githubusercontent.com/adafruit/Adafruit_CircuitPython_Bundle/main/badges/adafruit_discord.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_TLA202x/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_TLA202x/actions
    :alt: Build Status

.. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
    :target: https://github.com/astral-sh/ruff
    :alt: Code Style: Ruff

Library for the TI TLA202x 12-bit ADCs


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_
* `Register <https://github.com/adafruit/Adafruit_CircuitPython_Register>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_.

Installing from PyPI
=====================
On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-tla202x/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-tla202x

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-tla202x

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .venv
    source .venv/bin/activate
    pip3 install adafruit-circuitpython-tla202x

Usage Example
=============

.. code-block:: python3

    import board
    import busio
    from adafruit_tla202x import TLA2024

    i2c = busio.I2c(board.SCL, board.SDA)
    tla = TLA2024(i2c)

    for channel in range(4):
        tla.input_channel = channel
        print("Channel %d: %2f V"%(channel, tla.voltage))


Documentation
=============

API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/tla202x/en/latest/>`_.

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_TLA202x/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
