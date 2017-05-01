# Barebones Plugin Framework

## Services
Plugins are accessed via a service that provides methods for the plugins to call.
The base implementation has `send` to send info to the service and `error` to send error info to the service.
These are currently implemented with calls to `logging.Logger`.

## Plugins
* Must have:
 * `load` function that takes the service and configuration at the module level.
 * `__call__(*args,**kwargs)` method in the Plugin subclass

## Usage
See the example directory.
