#!/usr/bin/env bash
flask-sqlacodegen mysql://test:123456789@192.168.5.90:3306/ordering_system --flask > models.py
