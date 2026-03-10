from .inspectors import SafetyInspector
class SentryProxy:
  def __init__(self): self.inspector = SafetyInspector()
  def inspect(self, dest, data, proto):
    if self.inspector.contains_sensitive_info(data) and proto != "https":
      return "BLOCKED"
    return "CLEARED"