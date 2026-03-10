import hashlib, re
class PrivacySynthesizer:
  def pseudonymize(self, t):
    return re.sub(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", lambda m: hashlib.sha256(m.group(0).encode()).hexdigest()[:10], t, flags=re.I)