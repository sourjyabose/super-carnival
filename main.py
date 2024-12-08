from flask import Flask
from initial import Initial
from tmphndlr import Template_Handler
fl = Flask(__name__)
Template_Handler(fl);
Initial(fl)