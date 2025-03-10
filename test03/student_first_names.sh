#!/bin/dash

#! /usr/bin/env dash

cut -d'|' -f2,3 | sort -u -t'|' -k1,1 | cut -d'|' -f2 | cut -d',' -f2 | cut -d' ' -f2 | sort