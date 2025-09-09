#!/usr/bin/env python3
import sys, yaml, jsonschema

with open("schema/registry.schema.yml") as f:
    schema = yaml.safe_load(f)
with open("registry.yml") as f:
    data = yaml.safe_load(f)

jsonschema.validate(instance=data, schema=schema)
print("✅ registry.yml is valid.")
