Getting started
~~~~~~~~~~~~~~~

In order to enable REST in NSO, REST must be enabled in ncs.conf.
The web server configuration for REST is shared with the WebUI's config.
However, the WebUI does not have to be enabled for REST to work.

Here's a minimal example of what is needed in the conf file:

.. sourcecode:: xml

    <rest>
        <enabled>true</enabled>
    </rest>
    <webui>
        <enabled>false</enabled>
        <transport>
            <tcp>
                <enabled>true</enabled>
                <ip>0.0.0.0</ip>
                <port>8080</port>
            </tcp>
        </transport>
    </webui>