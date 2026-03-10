import re
from presidio_analyzer import AnalyzerEngine
class SafetyInspector:
  def __init__(self):
    self.analyzer = AnalyzerEngine()
  def contains_sensitive_info(self, text):
    return len(self.analyzer.analyze(text=text, entities=[], language="en")) > 0