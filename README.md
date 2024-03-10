# AirBnB Clone CLI

Command line interpreter for AirBnB clone.

## Overview

This is a simple CLI program that allows you to manage a collection of objects and store them in a JSON file.

## Commands

Available commands:

- `create <class_name>`: Creates a new instance of the specified class.
- `show <class_name> <id>`: Displays information about the instance with the specified ID.
- `destroy <class_name> <id>`: Deletes the instance with the specified ID.
- `all [class_name]`: Displays information about all instances, or all instances of a specific class if provided.
- `update <class_name> <id> <attribute_name> <attribute_value>`: Updates the attribute of the specified instance with the given value.
- `count <class_name>`: Counts the number of instances of the specified class.

or:

`<class_name>` with:

- `.show(<id>)`
- `.all()`
- `.destroy(<id>)`
- `.update(<id>, <attribute_name>, <attribute_value>)` | `update(<id>, <dictionary representation>)`
- `.count()`

## Classes

Available classes:

- `User` has the following attributes: `first_name`, `last_name`, `email`, `password`
- `Place` has the following attributes: `city_id`, `user_id`, `name`, `description`, `number_rooms`, `number_bathrooms`, `max_guest`, `price_by_night`, `latitude`, `longitude`, `amenity_ids`
- `State` has the following attributes: `name`
- `City` has the following attributes: `state_id`, `name`
- `Amenity` has the following attributes: `name`
- `Review` has the following attributes: `place_id`, `user_id`, `text`
