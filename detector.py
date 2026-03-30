from langdetect import detect, DetectorFactory

# Make results more consistent
DetectorFactory.seed = 0

def detect_language(text):
    try:
        if not text or not isinstance(text, str):
            return "unknown"
        return detect(text)
    except:
        return "unknown"