Building the Documentation
##########################

Using tox
*********

The `tox` tools allows for a one-line solution to building documentation
(two lines if you count installing `tox`).

0. If you are not in a virtual environment, it is highly recommended to create
   and activate one before doing any work in Python.

   .. code-block:: bash

      # Create the virtual environment in the "venv" directory
      python -m venv venv

      # Activate the virtual environment
      source venv/bin/activate

1. Install `tox` using `pip`

   .. code-block:: bash

      pip install tox

2. Build the documentation

   .. code-block:: bash

      tox -e docs

Viewing the Documentation
*************************

Once the documentation is built, you can view it in a web browser by opening
the various HTML files under `docs/build/html`, or host the website locally
on your system using Python by navigating into `docs/build/html` and running
the following command in a terminal:

.. code-block::

   python -m http.server

If the command succeeded, you can visit `http://0.0.0.0:8000` in a web browser
to view the documentation website.
