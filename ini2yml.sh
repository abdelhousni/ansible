#!/bin/bash
find . name inventory -exec ansible-inventory -i {} --list --yaml --output inventory.yml
