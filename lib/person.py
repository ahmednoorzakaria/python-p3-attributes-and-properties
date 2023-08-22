#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name, job):
        self._name = None
        self._job = None
        self.name = name 
        self.job = job

    def name(self):
        return self._name

    def name(self, name):
        if isinstance(name, str) and len(name) <= 25:
            self._name = name.title()
        else:
            print("Name must be a string under 25 characters.")

    def job(self):
        return self._job

    def job(self, job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in the list of approved jobs.")