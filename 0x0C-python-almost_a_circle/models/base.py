#!/usr/bin/python3
"""This is a Python package base file"""
import json
import os
import csv
import turtle
import random


class Base:
    """This is the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string.

        Args:
            list_dictionaries: A list of dictionaries to be converted.
        Returns:
            A JSON string representation of the list of dictionaries.
        """
        return json.dumps(list_dictionaries) if list_dictionaries else "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of objects to a JSON file.

        Args:
            cls: The class of the objects.
            list_objs: A list of objects to be saved.
        """
        file_name = f"{cls.__name__}.json"
        with open(file_name, "w", encoding="utf-8") as f:
            if list_objs:
                my_Objlist = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(my_Objlist))
            else:
                f.write("[]")

    @staticmethod
    def from_json_string(json_string):
        """This function returns list of JSON string representations"""
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """This function returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            new_obj = cls(1, 1)
        else:
            new_obj = cls(1)
        new_obj.update(**dictionary)
        return new_obj

    @classmethod
    def load_from_file(cls):
        """
        Loads objects from a JSON file and returns
        a list of instantiated objects.

        Returns:
            A list of instantiated objects loaded from the JSON file.
        """
        file_name = f"{cls.__name__}.json"
        if os.path.exists(file_name):
            with open(file_name, "r", encoding="utf-8") as f:
                json_data = f.read()
                return [
                    cls.create(**obj) for obj
                    in cls.from_json_string(json_data)
                ]
        else:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Saves a list of objects to a CSV file.

        Args:
            cls: The class of the objects.
            list_objs: A list of objects to be saved.
        """

        file_name = f"{cls.__name__}.csv"
        with open(file_name, "w") as new_file:
            if list_objs:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                my_Objlist = [obj.to_dictionary() for obj in list_objs]
                csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)

                for line in my_Objlist:
                    csv_writer.writerow(line)
            else:
                new_file.write("[]")

    @classmethod
    def load_from_file_csv(cls):
        """
        Loads objects from a CSV file and returns
        a list of instantiated objects.

        Returns:
            A list of instantiated objects loaded from the CSV file.
        """

        file_name = f"{cls.__name__}.csv"
        if os.path.exists(file_name):
            with open(file_name, "r") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                csv_reader = csv.DictReader(csvfile, fieldnames=fieldnames)
                new_obj = [
                    dict([k, int(v)] for k, v in dic.items())
                    for dic in csv_reader
                ]
                return [cls.create(**obj) for obj in new_obj]
        else:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draws rectangles and squares using the turtle graphics module.

        Args:
            list_rectangles (list): A list of Rectangle objects.
            list_squares (list): A list of Square objects.

        Returns:
            None
        """
        wn = turtle.Screen()
        wn.colormode(255)
        wn.bgcolor(51, 65, 85)
        wn.title("Turtle")
        wn.setup(width=0.9, height=0.8)

        skk = turtle.Turtle()
        skk.penup()
        skk.width(8)
        for rect in list_rectangles + list_squares:
            r = random.randint(0, 255)
            b = random.randint(0, 255)
            g = random.randint(0, 255)
            skk.pencolor(r, g, b)
            skk.goto(rect.x, rect.y)
            skk.pendown()
            for _ in range(4):
                skk.forward(rect.width)
                skk.right(90)
                skk.forward(rect.height)
            skk.hideturtle()
            skk.penup()

        turtle.exitonclick()
